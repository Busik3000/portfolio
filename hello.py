from flask import Flask, render_template,request, redirect
app = Flask(__name__)
import csv

@app.route('/<page_name>')
def pages(page_name):
    return render_template(page_name)

@app.route('/')
def index():
    return render_template('index.html')

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         database.write(f'{email}, {subject}, {message}\n')

def write_to_csv_file(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_to_csv_file(data)
            return redirect('/thanks.html')
        except:
            return 'Saving to database failed'
    else:
        return 'Something went wrong :('


app.run(debug=True)

