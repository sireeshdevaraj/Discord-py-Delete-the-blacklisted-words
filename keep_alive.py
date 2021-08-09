from flask import Flask
from threading import Thread 

app = Flask('')

@app.route('/')
def home():
  return 'bot will be perm online if u paste the above link in uptime robot monitor'

def run():
  app.run(host='0.0.0.0',port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()