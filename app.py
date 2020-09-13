from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def default():
    return render_template('index.html')

@app.route('/<string:page_name>')
def navigate(page_name):
    return render_template(page_name)

@app.route('/submitform', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            form_data = request.form.to_dict()
            write_to_csv(form_data)
            return redirect("/formsubmission.html")
        except:
            return "Did Not Add to Database"
    else:
        return "Failure"

def write_to_file(form_data):
    with open("database.txt", mode='a') as database:
        email = form_data["email"]
        subject = form_data["subject"]
        message = form_data["email_message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(form_data):
    with open("database.csv", newline='', mode='a') as database_csv:
        email = form_data["email"]
        subject = form_data["subject"]
        message = form_data["email_message"]
        csv_writer = csv.writer(database_csv, delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

if __name__ == '__main__':
    app.run()
