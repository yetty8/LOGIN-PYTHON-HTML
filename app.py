from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Dummy user data
users = {
    "user1": "password1",
    "user2": "password2"
}

def authenticate_user(username, password):
    return users.get(username) == password

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('welcome', username=username))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash("Username already exists. Please choose another.", "error")
        else:
            users[username] = password
            flash(f"Account created for {username}!", "success")
            return redirect(url_for('home'))
    
    return render_template('create_account.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username', 'Guest')
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)