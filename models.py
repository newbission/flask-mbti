from db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    selects = db.relationship("Selects", back_populates="users")


class Types(db.Model):
    __tablename__ = "types"

    code = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(2), unique=True, nullable=False)

    questions = db.relationship("Questions", back_populates="types", lazy="dynamci")


class Questions(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_code = db.Column(db.Integer, db.ForeignKey("types.code"), nullable=False)
    title = db.Column(db.Text, nullable=True)
    q1 = db.Column(db.Text, nullable=False)
    q2 = db.Column(db.Text, nullable=False)

    types = db.relationship("Types", back_populates="questions")
    current_questions = db.relationship("CurrentQuestions", back_populates="questions")
    selects = db.relationship("Selects", back_populates="questions")


class CurrentQuestions(db.Model):
    __tablename__ = "current_questions"

    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), primary_key=True)

    questions = db.relationship("Questions", back_populates="current_questions")


class MbtiList(db.Model):
    __tablename__ = "mbti_list"

    code = db.Column(db.Integer, autoincrement=True, primary_key=True)
    mbti = db.Column(db.String(4), nullable=False)

    results = db.relationship("Reults", back_populates="mbtis")

class Selects(db.Model):
    __tablename__ = "selects"

    num = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    round = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    answer = db.Column(db.String(1), nullable=False)

    questions = db.relationship("Questions", back_populates="selects")
    users = db.relationship("User", back_populates="selects")

class Results(db.Model):
    __tablename__ = "results"

    num = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    round = db.Column(db.Integer, nullable=False)
    mbti_code = db.Column(db.Integer, db.ForeignKey("mbti_list.code"), nullable=False)

    mbtis = db.relationship("MbtiList", back_populates="results")