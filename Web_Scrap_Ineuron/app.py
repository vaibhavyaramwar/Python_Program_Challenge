from flask import Flask,render_template,request,jsonify
from flask_cors import cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)




if __name__ == "__main__":
    app.run()