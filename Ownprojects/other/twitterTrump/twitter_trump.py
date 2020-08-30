from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://twitter.com/realDonaldTrump/status/1292181029541879812")

# driver.execute_script("console.log(document.getElementsByClassName('css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').length);")

# driver.execute_script("function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;};");

# driver.execute_script("function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}; getElementByXpath('//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[1]/div/span[1]').innerHTML = '200';");

# driver.execute_script("function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}; console.log(getElementByXpath('//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[1]/div/span[1]').innerHTML);");

driver.execute_script('console.log(document.querySelector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-156q2ks > div > span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0").innerHTML)')
