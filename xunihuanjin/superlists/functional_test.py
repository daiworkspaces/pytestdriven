from selenium import webdriver

browser = webdriver.Chrome('/Users/chaomingdai/Documents/pytestdriven/xunihuanjin/webdriver/chromedriver')
browser.get('http://127.0.0.1:8000/')
assert 'Djangofff' in browser.title
