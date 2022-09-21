from flask import Flask
from flask import render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/live')
def live():
	return render_template('live.html', title='Контакты')

link = "http://127.0.0.1:5000/"
browser = webdriver.Chrome()
browser.get(link)




