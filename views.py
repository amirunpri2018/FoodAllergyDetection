from flask import Flask, render_template, redirect, request, g, session, url_for, flash
import model
import forms

app = Flask(__name__)
app.config.from_object('config')

@app.route("/", methods=['GET', 'POST'])
def index():
	form = forms.LoginForm(request.form)
	if request.method == 'POST' and not form.validate():
		flash ('All fields are required. Please try again.')
		return redirect(url_for("index"))

	elif request.method == 'POST' and form.validate():
		email = form.email.data
		password = form.password.data

		user = model.session.query(model.User).filter_by(email=email).first()
		if not user:
			flash("Incorrect username or password. Please try again.")
			return redirect(url_for("index"))

		session['user_email'] = email
		username = user.username
		return redirect(url_for("#", username=username))
	return render_template("index.html", form=form)

@app.route("/user/<username>")
def userpage(username):
	  return render_template("userpage.html")

if __name__ == "__main__":
	app.run(debug=True)
