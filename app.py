from flask import Flask, render_template, request, redirect
import MySQLdb
import my_sql
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_k')
def form_k():
    return render_template('form_k.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    Name = request.form['name']
    Email = request.form['email']
    Number = request.form['Number']
    PinCode = request.form['PinCode']
    Category = request.form['Category']
    State = request.form['State']
    City = request.form['City']
    Address = request.form['Address']

    # Create a cursor
    # cursor = mydb.cursor()

    # Execute SQL query to insert data
    my_sql.my_cursor.execute("INSERT INTO Form_Details.form (Name, Email, Number, PinCode, Category, State, City, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Name, Email, Number, PinCode, Category, State, City, Address))
    # Commit to the database
    my_sql.mydb.commit()
    # Redirect to a thank you page or back to the form
    return redirect('/ThankYou')

@app.route('/ThankYou')
def ThankYou():
    return render_template('ThankYou.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Products')
def Products():
    return render_template('products_parag_web_H.html')

@app.route('/Services')
def Services():
    return render_template('Services_parag_web_H.html')


@app.route('/contact')
def contact():
    return render_template('Contact_parag_web.html')


@app.route('/Blog')
def Blog():
    return render_template('Blog_parag_web.html')


@app.route('/Testimonial')
def Testimonial():
    return render_template('Testimonial_parag_web_H.html')


@app.route('/about')
def about():
    return render_template('About_parag_web.html')


if __name__ == "__main__":
    app.run(debug=True)



