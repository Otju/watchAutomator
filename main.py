from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

showUrl = "steinsgate.1rx"
episodeUrl = "ep-23"
url = "https://9anime.to/watch/"+ showUrl + "/" + episodeUrl

options = Options()
options.add_argument("user-data-dir=C:\\Users\\ottoj\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get(url)
time.sleep(5)

action = ActionChains(driver)
videoPlayer = driver.find_element_by_id('player')
action.double_click(videoPlayer).perform()

