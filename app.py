from model.Users import db, app
from controllers.Users import User
from flask import Flask, request, render_template


# app = Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        if request.form['username'] == "admin" and request.form["password"] == "admin":
            return render_template("admin/main.html")
        elif request.form['username'] == "user" and request.form["password"] == "user":
            return render_template("user/base.html")
    else:
        return render_template("login.html")

@app.route("/logoff", methods=["GET"])
def logoff():
    return render_template("login.html")


@app.route("/admin/users", methods=["GET"])
def user():
    usuarios = User()
    usuarios = usuarios.findAll()
    return render_template("admin/userList.html", usuarios=usuarios)

@app.route("/admin/user/new", methods=["GET", "POST"])
def new_user():
    if request.method == 'POST':
        usuario = User()
        usuario = usuario.insertUser(request.form)
        return render_template("admin/userCadastro.html")
    else:
        return render_template("admin/userCadastro.html")

@app.route("/admin/user/<id>", methods=["GET", "POST"])
def edit_user(id):
    if request.method == 'POST':
        return "Editando usuario" 
    else:
        usuario = User()
        usuario = usuario.findOne(id)
        return render_template("admin/userList.html", usuario=usuario)


@app.route("/admin/user/<id>/remove")
def delete_user(id):
    usuario = User()
    usuario = usuario.removeUser(id)
    return "Usuario Deletado com sucesso"


if __name__ == "__main__":
    app.run(debug=True)


