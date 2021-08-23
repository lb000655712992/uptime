from flask import render_template
import config

connex_app = config.connex_app
connex_app.add_api("swagger.yml")


@connex_app.route("/")
def home():
    return render_template("home.html")


@connex_app.route("/email")
def email():
    return render_template("email.html")


@connex_app.route("/data")
def data():
    return render_template("data.html")


@connex_app.route("/config")
def config():
    return render_template("config.html")


@connex_app.route("/data_create")
def data_create():
    return render_template("/data_create.html")


@connex_app.route("/email_create")
def eMail_create():
    return render_template("/email_create.html")


@connex_app.route("/data_edit")
def data_edit():
    return render_template("/data_edit.html")


if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)
