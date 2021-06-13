from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import json
import os
import time
import atexit
from pynput.keyboard import Key,Controller

def relativePath(path):
  dirname = os.path.dirname(__file__)
  return os.path.join(dirname, path.replace("/", "\\"))

profile = webdriver.FirefoxProfile() 
firefox_dev_binary = FirefoxBinary(r'C:\Program Files\Firefox Developer Edition\firefox.exe')
driver = webdriver.Firefox(firefox_binary=firefox_dev_binary, executable_path='webdriver/geckodriver.exe')
driver.install_addon(relativePath("webdriver/extensions/ublock_origin-1.35.2-an+fx.xpi"))
driver.install_addon(relativePath("webdriver/extensions/https_everywhere-2021.4.15-an+fx.xpi"))
driver.get("https://9anime.to/watch/steinsgate.1rx/ep-23")#"https://9anime.to/"
#driver.fullscreen_window()

def disable_fullscreen():
  action = ActionChains(driver)
  action.send_keys(Keys.ESCAPE).perform()

def enable_fullscreen():
  action = ActionChains(driver)
  videoPlayer = driver.find_element_by_id('player')
  action.double_click(videoPlayer).perform()

def search(searchString):
  url = "https://9anime.to/filter?language%5B%5D=subbed&keyword=" + searchString
  driver.get(url)

def getPosters():
  return driver.find_elements_by_class_name("poster")

def selectPoster(number):
  items = getPosters()
  item = items[number-1]
  item.click()

def togglePause():
  videoPlayer = driver.find_element_by_id('player')
  videoPlayer.click()

def getEpisodes():
  episodes = driver.find_element_by_id("episodes")
  return episodes.find_elements_by_tag_name("li")

def selectEpisode(number):
  items = getEpisodes()
  item = items[number-1]
  item.click()


def save(name):
  if(not name):
    name = "default"
  url = driver.current_url
  jsonFile = open("data.json", mode="r")
  savedShows = json.load(jsonFile)
  jsonFile.close()
  savedShows.update({name: url})
  jsonFile = open('data.json', mode='w')
  json.dump(savedShows, jsonFile)
  jsonFile.close()

def delete(name):
  jsonFile = open("data.json", mode="r")
  savedShows = json.load(jsonFile)
  jsonFile.close()
  savedShows.pop(name, None)
  jsonFile = open('data.json', mode='w')
  json.dump(savedShows, jsonFile)
  jsonFile.close()

def continue_show(name):
  if(not name):
    name = "default"
  with open('data.json') as file:
    savedShows = json.load(file)
    url = savedShows[name]
    driver.get(url)

def selectEpisode(number):
  episodes = driver.find_element_by_id("episodes")
  items = episodes.find_elements_by_tag_name("li")
  item = items[number-1]
  item.click()

def refresh():
  driver.refresh()

def scrollDown():
  driver.execute_script("window.scrollTo(0, window.scrollY + 500)") 

def scrollUp():
  driver.execute_script("window.scrollTo(0, window.scrollY - 500)") 


def exit_handler():
    print('Closing...')
    driver.close()

def next():
  disable_fullscreen()
  time.sleep(1)
  item = driver.find_element_by_class_name("next")
  item.click()

def prev():
  disable_fullscreen()
  time.sleep(1)
  item = driver.find_element_by_class_name("prev")
  item.click()

def volumeDown():
    keyboard = Controller()
    keyboard.press(Key.media_volume_down)

def volumeUp():
    keyboard = Controller()
    keyboard.press(Key.media_volume_up)

def skipTime(amount, isBackward):
    dividedByFive = int(round(int(amount)/5))
    for x in range(dividedByFive):
      if(isBackward):
        driver.find_element_by_tag_name("body").send_keys(Keys.LEFT)
      else:
        driver.find_element_by_tag_name("body").send_keys(Keys.RIGHT)

def forward(amount):
  skipTime(amount, False)

def backward(amount):
  skipTime(amount, True)

isHidden = False

def hide():
    global isHidden
    if isHidden:
      driver.execute_script("document.getElementById('body').style.display = 'block';")
      isHidden=False
    else:
      driver.execute_script("document.getElementById('body').style.display = 'none';")
      isHidden=True

atexit.register(exit_handler)