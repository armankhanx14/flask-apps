from app import db, Users



db.drop_all()   ##deletes db
db.create_all()  ## creates db

user_1 = Users(first_name="Arman", Last_name="Khan")
db.session.add(user_1)
db.session.commit()