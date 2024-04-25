from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/landing", methods=['GET', 'POST'])
def landing_site():
    return render_template('landing_page.html')

if __name__ == '__main__':
    app.run(debug=True)