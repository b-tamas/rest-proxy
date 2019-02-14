from flask import Flask
app = Flask(__name__)
import json
import sys
from time import sleep
from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import argparse
import queue


@app.route("/getsizeofq", methods=['GET'])
def get_size_req_q():
    return("size: " + str(q.qsize()))

@app.route("/getnext", methods=['GET'])
def get_next_from_req_q():
    return(str(q.get()))
    #curl -sb -H "Accept: application/json"  http://localhost:8888/getnext



@app.route("/post", methods=['POST'])
def put_req_q():
    print("request: " +str(request.data))
    q.put(request.data)
    print("size: " + str(q.qsize()))
    return "Done"

    #curl -d "{my json data}" -X POST http://localhost:8888/post
    #curl -d "{my json data1}" -X POST http://localhost:8888/post



if __name__ == "__main__":
    print("Rest-simulator")
    
    
    q = queue.Queue()
    
    q.put(1)
    q.put(2)
    
    app.run(port=8888)
