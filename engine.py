from flaskwash import app, db, admin

if __name__ == "__main__":
    db.create_all()
    app.debug =True
    app.run(host='127.0.0.1', port=5000)
