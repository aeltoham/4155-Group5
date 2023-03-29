# importing flask
from flask import Flask, render_template

# importing pandas module
import pandas as pd

app = Flask(__name__)
# Source: https://www.geeksforgeeks.org/convert-csv-to-html-table-using-python-pandas-and-flask-framework/?ref=rp

#reading csv file data
#Change file path to your local machine
data = pd.read_csv('./static/source/UNCCFaculty.csv')

# route to html page - "table"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    # converting csv to html
    
    return render_template('table.html', tables=[data.to_html(classes='table')], titles=[''])


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))

#print(df)
#df.to_html("Table.htm")
#html_file = df.to_html()
