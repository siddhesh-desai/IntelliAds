import sqlite3
import os
from flask import Flask, render_template, request, redirect
from openai_functions import *
from bard_functions import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        cust_name = request.form['customerName']
        cust_desc = request.form['customerInterests']
        product_name = request.form['productName']
        product_desc = request.form['productDetails']

        ans = answer_prompt_bard(create_prompt_from_description(product_name=product_name, product_desc=product_desc, customer_name=cust_name, customer_interests=cust_desc))
        return render_template('ad_display.html', advert=ans)


    return render_template('ad_generation_form.html')
    # return "<p>Hello, World!</p>"

@app.route("/a", methods=['GET', 'POST'])
def bulk_send():
    return render_template('upload_csv.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return "No selected file"

    # Save the file to the upload folder
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return "File successfully uploaded and saved at " + filename

    return render_template()



@app.route('/customers')
def display_table():
    connection = sqlite3.connect('demo.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM da')
    data = cursor.fetchall()
    print(data)
    connection.close()

    return render_template('customer_table.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
