from flask import Flask, render_template
import browser
import json
from flask import jsonify

app = Flask(__name__, static_url_path='', static_folder="frontend/build", template_folder="frontend/build")

def formatName(name):
    return name.replace("+", " ")

def sendJson(json):
    response = jsonify(json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
def preact():
    return render_template('index.html')

@app.route('/search/<searchString>', methods=['POST'])
def search(searchString):
    browser.search(searchString)
    return ""

@app.route('/select/<type>/<number>', methods=['POST'])
def select(type, number):
    selectedNumber = int(number)
    if(type=="show"):
        browser.selectPoster(selectedNumber)
    if(type=="episode"):
        browser.selectEpisode(selectedNumber)
    return ""

@app.route('/save/<name>', methods=['POST'])    
def save(name):
    browser.save(formatName(name))
    return ""

@app.route('/delete/<name>', methods=['POST'])    
def delete(name):
    browser.delete(formatName(name))
    return ""

@app.route('/continue/<name>', methods=['POST'])    
def continueShow(name):
    browser.continue_show(formatName(name))
    return ""

@app.route('/pause', methods=['POST'])    
def pause():
    browser.togglePause()
    return ""

@app.route('/fullscreen', methods=['POST'])    
def fullscreen():
    browser.enable_fullscreen()
    return ""

@app.route('/refresh', methods=['POST'])    
def refresh():
    browser.refresh()
    return ""

@app.route('/scrollup', methods=['POST'])    
def scrollup():
    browser.scrollUp()
    return ""

@app.route('/scrolldown', methods=['POST'])    
def scrollDown():
    browser.scrollDown()
    return ""

@app.route('/save', methods=['GET'])    
def getSaved():
    jsonFile = open("data.json", mode="r")
    savedShows = json.load(jsonFile)
    return sendJson(savedShows)

@app.route('/episode', methods=['GET'])    
def getEpisodes():
    episodes = browser.getEpisodes()
    count = len(episodes)
    return sendJson({"count": count})

@app.route('/show', methods=['GET'])    
def getShows():
    shows = browser.getPosters()
    count = len(shows)
    return sendJson({"count": count})

@app.route('/next', methods=['POST'])    
def next():
    browser.next()
    return ""

@app.route('/prev', methods=['POST'])    
def prev():
    browser.prev()
    return ""

@app.route('/volumeup', methods=['POST'])    
def volumeup():
    browser.volumeUp()
    return ""

@app.route('/volumedown', methods=['POST'])    
def volumedown():
    browser.volumeDown()
    return ""

@app.route('/hide', methods=['POST'])    
def hide():
    browser.hide()
    return ""

@app.route('/forward/<duration>', methods=['POST'])    
def forward(duration):
    browser.forward(duration)
    return ""

@app.route('/backward/<duration>', methods=['POST'])    
def backward(duration):
    browser.backward(duration)
    return ""


