from flask import Flask, render_template,request, send_from_directory,abort, redirect, url_for
import random, string
import flask
from tinydb import TinyDB, Query,where
import sys
import os
import json


db = TinyDB('db.json')
User = Query()
table = db.table('comment')






app = Flask(__name__,
            static_url_path='',
            static_folder='./static',
            template_folder='./templates')
app.config['SECRET_KEY'] = 'mysecret'


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))



@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route("/addcomment", methods=['GET', 'POST'])
def addcomment ():
    if request.method == 'GET':
        comment_data = str(request.args.get("comment_data"))
        user_name = str (request.args.get("user_name"))
        like = request.args.get("like")
    else:
        comment_data = str(request.form["comment_data"])
        user_name = str(request.form["user_name"])
        like = request.form["like"]
    id_comment = randomword(20)
    print(like)
    send = {'comment':comment_data,'id_comment':id_comment,"user_name" : user_name,'like':like}
    try:
        table.insert(send)
        update_status=True
    except:
        update_status=False
    print(table.all())
    if update_status:
        return flask.jsonify({'data':table.all(),'status':"update finish",'status-b':True})



@app.route("/readcomment", methods=['GET', 'POST'])
def readcomment():
    return flask.jsonify({"data":table.all()})




@app.route("/setlike/<comment_id>/<numberlike>", methods=['GET', 'POST'])
def setlike(comment_id,numberlike):
    numberlike = int(numberlike);
    temp = table.search(where("id_comment") == comment_id)[0]
    print(temp)
    table.upsert({"comment":temp['comment'],'id_comment':temp['id_comment'],'user_name':temp['user_name'],'like':int(temp['like']) + numberlike},where("id_comment") == comment_id)
    return flask.jsonify(temp)



@app.route("/getbesstcomment", methods=['GET', 'POST'])
def getbesstcomment():
    data = table.all()
    temp = []
    for row in data:
        temp.append(row["like"])
    number = temp.index(max(temp))
    send_data = data[number]
    return flask.jsonify(send_data)


if __name__ == '__main__':
    app.run(debug=True)
    os.execv(__file__, sys.argv)
