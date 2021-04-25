from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Test(db.Model):
    print(None)
