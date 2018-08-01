from flask import Blueprint, render_template
from admin_required import admin_required


from flask_login import LoginManager, login_required, login_user, logout_user


quiz = Blueprint('quiz', __name__)

@quiz.route("/admin/quiz", methods=["GET"])
@login_required
def list_quiz():
    return render_template("admin/quiz/quizList.html")

@quiz.route("/admin/quiz/new", methods=["GET"])
@login_required
def new_quiz():
    return render_template("admin/quiz/quizNew.html")


@quiz.route("/admin/quiz/id/edit", methods=["POST"])
@login_required
def edit_quiz(id):
    return "edit quiz"

@quiz.route("/admin/quiz/id/remove")
@login_required
def remove_quiz(id):
    return " delete quiz"


if __name__ == "__main__":
    app.run(debug=True)