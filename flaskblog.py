from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# secret key to protect modefying cookies, ...
app.config['SECRET_KEY'] = '45abf140032ed87b92351aa9399b2751'

posts = [
    {
     'author': 'Sina Schriewer',
     'title': 'Blog Post 1',
     'content': 'First Post content'
    },
     {
     'author': 'Bjoern Schriewer',
     'title': 'Bjoerns Blog',
     'content': 'Best Post ever'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Huhuuhiii!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
