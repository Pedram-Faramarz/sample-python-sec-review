from flask import Flask, request, session, redirect, url_for, render_template_string
from auth import register_user, login_user

app = Flask(__name__)
app.secret_key = 'dev-secret-key'  

@app.route('/')
def index():
    if 'user' in session:
        return f'Logged in as {session["user"]}'
    return 'You are not logged in'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
      
        register_user(username, password)
        return redirect(url_for('index'))
    return render_template_string('''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Register">
        </form>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            session['user'] = username  
            return redirect(url_for('index'))
        return 'Login failed'
    return render_template_string('''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
