from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='!', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@ app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'hurrey its submitted'
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    app.run(debug=True)
