import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify, request

app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

"""
#adding first data
doc_ref = db.collection('employee').document('empdoc')

doc_ref.set({

    'name':'Parwiz',
    'lname':'Forogh',
    'age':24


})
"""
courses = [
    {
        'name': "Sahe Khan",
        'age': "24",
        'color': "black",
        'phone': "1212",
    },
    {
        'name': "Sabir Khan",
        'age': "36",
        'color': "black",
        'phone': "3212",
    },
    {
        'name': "Mahmud Khan",
        'age': "44",
        'color': "black",
        'phone': "5454",
    },
]

# Reading the data


product_ref = db.collection('employee')
"""
docs = emp_ref.stream()

for doc in docs:
    pro = doc.to_dict()
    print(pro)
"""


# print('{} => {} '.format(doc.id, doc.to_dict()))


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route('/course', methods=['GET'])
def get():
    product_list = [doc.to_dict() for doc in product_ref.stream()]
    return jsonify(product_list), 200


# return jsonify({'Courses:' : pro})

print(courses)
if __name__ == '__main__':
    app.run(debug=True)
