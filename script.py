from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo

application = Flask(__name__, static_url_path='')
application.config["MONGO_URI"] = "mongodb://localhost:27017/shaheela"
mongo = PyMongo(application)

books = [
    {
        'name': 'Green egges and hams',
        'price': '$3.67',
        'isbn': 78900765478
    },
    {
        'name': 'The cat in the hat',
        'price': '$9.67',
        'isbn': 98765465544
    }
]

@application.route('/')
def home_page():
    return render_template('home.html')

@application.route('/forms/')
def form_page():
    return render_template('form.html')

@application.route('/about/')
def about_page():
    online_users = mongo.db.first.find({})
    return render_template('about.html', online_users=online_users)

@application.route('/input_data', methods=['POST'])
def input_data():
    fname = request.form['firstName']
    phone = request.form['phone']
    image = request.form['image']
    mongo.db.first.insert({"fname":fname, "phone":phone, "image":image})
    online_users = mongo.db.first.find({})
    return render_template('about.html', online_users=online_users)

@application.route('/update_data', methods=['POST'])
def update_data():
    oldData = request.form['old_phone']
    phone = request.form['phone']
    fname = request.form['firstName']
    mongo.db.first.update({"phone":oldData},{"$set":{"fname":fname,"phone":phone}}, upsert=False)
    online_users = mongo.db.first.find({})
    return render_template('about.html', online_users=online_users)

@application.route('/delete/<phone>')
def delete(phone=None):
    if phone != None:
        mongo.db.first.remove({"phone": phone,})
        online_users = mongo.db.first.find({})
        return render_template('about.html', online_users=online_users)

if __name__ == "__main__":
    application.run(host='0.0.0.0')