from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json

options = Options()
options.add_argument("user-data-dir=C:\\Users\\ottoj\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://9anime.to/")

def disable_fullscreen():
  action = ActionChains(driver)
  action.send_keys(Keys.ESCAPE).perform()

def enable_fullscreen():
  action = ActionChains(driver)
  videoPlayer = driver.find_element_by_id('player')
  action.double_click(videoPlayer).perform()

def search(searhStrings):
  searchString = "+".join(searhStrings)
  url = "https://9anime.to/filter?language%5B%5D=subbed&keyword=" + searchString
  driver.get(url)

def selectPoster(number):
  items = driver.find_elements_by_class_name("poster")
  item = items[number-1]
  item.click()

def togglePause():
  videoPlayer = driver.find_element_by_id('player')
  videoPlayer.click()

def selectEpisode(number):
  episodes = driver.find_element_by_id("episodes")
  items = episodes.find_elements_by_tag_name("li")
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
