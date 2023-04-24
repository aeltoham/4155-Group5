# importing flask
from flask import Flask,  render_template, abort, flash, redirect, url_for

# importing pandas module
import pandas as pd

app = Flask(__name__)
# Source: https://www.geeksforgeeks.org/convert-csv-to-html-table-using-python-pandas-and-flask-framework/?ref=rp
app.secret_key = 'secretKey'
# reading csv file data
# Change file path to your local machine
data = pd.read_csv('./static/source/UNCCFaculty.csv')

# route to html page - "table"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact', methods = ['POST'])
def contactIndex():
    flash('Your message was received!', 'info')
    return redirect(url_for('index'))


@app.route('/table')
def table():
    # converting csv to html
    return render_template('table.html', tables=[data.to_html(columns=['MMS ID (System Identifier)', 'ISBN', 'Author or Editor','Title','Publisher','Physical Description','Topical Subjects'],classes='table dataTable table-striped table-bordered table-sm ',na_rep = 'N/A', table_id='dataTable')], titles=[''])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", error=e)


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))

# print(df)
# df.to_html("Table.htm")
#html_file = df.to_html()
