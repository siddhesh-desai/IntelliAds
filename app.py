import sqlite3
from csv_functions import *
import os
from flask import Flask, render_template, request, redirect
# from openai_functions import *
# from bard_functions import *
# from whatsapp_messages import send_whatsapp_message
from whatsapp_messages import send_whatsapp_message

app = Flask(__name__)


@app.route("/landing", methods=['GET', 'POST'])
def landing_site():
    return render_template('landing_page.html')

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':

        cust_name = request.form['customerName']
        cust_desc = request.form['customerInterests']
        product_name = request.form['productName']
        product_desc = request.form['productDetails']
        # cust_mobile = request.form['custMobile']

        ans = answer_prompt_bard(create_prompt_from_description(product_name=product_name, product_desc=product_desc, customer_name=cust_name, customer_interests=cust_desc))
        return render_template('ad_display.html', advert=ans)

        # if 'button1' in request.form:
        #     send_whatsapp_message(cust_mobile, ans)


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
    product_name = request.form['productName']
    product_desc = request.form['productDetails']
    print(product_name,product_desc)

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return "No selected file"

    # Save the file to the upload folder
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        create_ad_for_all(product_name,product_desc)
        return redirect("/customers")
        # return "File successfully uploaded and saved at " + filename





@app.route('/customers', methods=['GET', 'POST'])
def display_table():
    connection = sqlite3.connect('demo.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM da')
    data = cursor.fetchall()
    print(data)
    connection.close()
    if request.method == 'POST':
        for i in data:
            send_whatsapp_message("+" + str(i[4]), i[9])

    # connection = sqlite3.connect('demo.db')
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM da')
    # data = cursor.fetchall()
    # print(data)
    # connection.close()

    # return redirect("/deliver")
    return render_template('customer_table.html', data=data)




@app.route('/deliver')
def deliver():
    connection = sqlite3.connect('demo.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM da')
    data = cursor.fetchall()
    print(data)
    connection.close()

    # for i in data:
    #     send_whatsapp_message(i[4],i[9])
    return "Success"
    # return render_template('customer_table.html', data=data)

@app.route('/ss')
def deliverr():
    send_whatsapp_message("+919370554548","HHHHHH")
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)

