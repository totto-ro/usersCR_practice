# endpoints related to the users

from flask import render_template, redirect, request
from users_app import app
from users_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "index.html", users=users )

@app.route( "/users/new", methods=['GET'] )
def displayAddNewUser():
    return render_template("new_users.html")

@app.route( "/users/createNewUser", methods=['GET'] )
def creteNewUser():
    return redirect("/users/new")

@app.route( "/users/add", methods=['POST'] )
def addNewInfo():
    print(request.form)
    User.add_data(request.form)
    return redirect("/users")
    






