from app import db, app

app.app_context().push()
db.create_all()