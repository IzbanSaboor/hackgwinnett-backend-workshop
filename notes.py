'''
intro:
- discuss what backend is
- talk about flask, its uses, compare to node and django
- explain what an api is
- explain how rest apis evolved from socket connections
- "in this workshop, we are going to be making a simple rest api using flask
'''

'''
setup:
- you are welcome to follow along or just watch
- if you want to follow along, you can open up a replit project -> click on the package manager (box) -> search for flask -> click the plus
- if you are using a native encvironment on your own machine, you can install flask with 'pip install Flask'
- ^^ explain what pip is and explain that python is required for native setups
'''

'''
NOTES:
- To run the client on replit, navigate to 'shell' -> 'python client.py'
- link: https://replit.com/@hershyz/HackGwinnett-Backend-Workshop#main.py
'''




# init: explain modules, what this below code does, etc
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
  return "hello flask!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))





# get requests: explain server vs client, api endpoints, get requests

# -- main.py (server)
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
  return "hello flask!"

@app.route("/get_endpoint", methods=["GET"])
def get_endpoint():
  return "hello client!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))

# -- client.py
import requests

r = requests.get("https://HackGwinnett-Backend-Workshop.hershyz.repl.co/get_endpoint")
print(r.text)





# payloads: explain what json is (parameterized generic data), explain how we can send json to apis, and how apis can parse it

# --main.py (server)
from flask import Flask, request # MAKE SURE TO INCLUDE REQUEST IMPORT AND EXPLAIN IT
import random

app = Flask(__name__)

@app.route("/")
def home():
  return "hello flask!"

@app.route("/get_greeting", methods=["GET"])
def get_greeting():
  data = request.get_json()
  name = data['name']
  return "hello " + name + "!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))

# --client.py
import requests

payload = {
  "name": "bob"
}

r = requests.get("https://HackGwinnett-Backend-Workshop.hershyz.repl.co/get_greeting", json=payload)
print(r.text)





# post requests: explain what post requests are (distinguished from get requests)
'''
- let's say I wanted to make a web application where users can enter their names and then find the names of others
- for adding the names to the server, I'm going to use something called a post request
- a post request is another type of http request, just like get requests, but the parameters sent through the post request can't be seen by the url
- post requests are more secure for the transfer of data and typically used when adding values from a client
'''

# --main.py (server)
from flask import Flask, request
import random

app = Flask(__name__)

fnames = []
lnames = []

@app.route("/")
def home():
  return "hello flask!"

@app.route("/put_name", methods=["POST"])
def put_name():
  data = request.get_json()
  fname = data['fname']
  lname = data['lname']
  fnames.append(fname)
  lnames.append(lname)
  return "added " + str(fname) + ", " + str(lname)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))

# --client.py
import requests

payload = {
  "fname": "john",
  "lname": "doe"
}

r = requests.post("https://HackGwinnett-Backend-Workshop.hershyz.repl.co/put_name", json=payload)
print(r.text)




# get request iterating through our arrays

# -- main.py (server)
from flask import Flask, request
import random

app = Flask(__name__)

fnames = []
lnames = []

@app.route("/")
def home():
  return "hello flask!"

@app.route("/put_name", methods=["POST"])
def put_name():
  data = request.get_json()
  fname = data['fname']
  lname = data['lname']
  fnames.append(fname)
  lnames.append(lname)
  return "added " + str(fname) + ", " + str(lname)

@app.route("/get_last_name", methods=["GET"])
def get_last_name():
  data = request.get_json()
  fname = str(data['fname'])
  for i in range(0, len(fnames)):
    if fnames[i] == fname:
      return lnames[i]
  return "could not find user!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))

# client.py (adding users, post)
import requests

payload = {
  "fname": "john",
  "lname": "doe"
}

r = requests.post("https://HackGwinnett-Backend-Workshop.hershyz.repl.co/put_name", json=payload)
print(r.text)

# client.py (getting users, get)
import requests

payload = {
  "fname": "john",
}

r = requests.get("https://HackGwinnett-Backend-Workshop.hershyz.repl.co/get_last_name", json=payload)
print(r.text)