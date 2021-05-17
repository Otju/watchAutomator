from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\ottoj\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://9anime.to/filter?language%5B%5D=subbed&keyword=Cowboy+Bebop")

def disable_fullscreen():
  action = ActionChains(driver)
  action.send_keys(Keys.ESCAPE).perform()

def enable_fullscreen():
  action = ActionChains(driver)
  videoPlayer = driver.find_element_by_id('player')
  action.double_click(videoPlayer).perform()

def watch():
  showUrl = "steinsgate.1rx"
  episodeUrl = "ep-23"
  url = "https://9anime.to/watch/"+ showUrl + "/" + episodeUrl
  driver.get(url)
  time.sleep(5)

def search(searhStrings):
  searchString = "+".join(searhStrings)
  url = "https://9anime.to/filter?language%5B%5D=subbed&keyword=" + searchString
  driver.get(url)

def selectPoster(number):
  items = driver.find_elements_by_class_name("poster")
  item = items[number-1]
  item.click()

def selectEpisode(number):
  episodes = driver.find_element_by_id("episodes")
  items = episodes.find_elements_by_tag_name("li")
  item = items[number-1]
  item.click()

