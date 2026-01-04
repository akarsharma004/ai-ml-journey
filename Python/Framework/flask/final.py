from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# HOME ROUTE: Displays the input form
@app.route('/')
def index():
    return render_template('form.html')

# SUBMIT ROUTE: Processes the "Data Source"
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Grabbing the score from the form
        score = int(request.form['score'])
        # Redirecting dynamically using url_for and a Variable Rule
        return redirect(url_for('display_results', score_val=score))

# DYNAMIC VARIABLE RULE ROUTE: Captures the score from the URL
@app.route('/results/<int:score_val>')
def display_results(score_val):
    # Logic: Pass or Fail
    status = "PASSED" if score_val >= 50 else "FAILED"
    
    # Simulating a Data Source (Dictionary) to pass to Jinja2
    exp = {
        "Student Score": score_val,
        "Final Status": status,
        "Minimum Required": 50
    }
    return render_template('result.html', results=exp)

if __name__ == '__main__':
    app.run(debug=True)