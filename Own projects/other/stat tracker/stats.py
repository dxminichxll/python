from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")


game = int(input("Enter which game you want to search stats for (1=fortnite, 2=rainbow)"))

if game == 2:
    gameName = "Rainbow Six Siege"
else:
    gameName = "Fortnite"
username = input("Enter {} username:".format(gameName))

print("processing...\n")

driver = webdriver.Chrome(options=chrome_options)


if game == 2:

    driver.get("https://r6.tracker.network/")

    name_box = driver.find_element_by_xpath('//*[@id="hp-search"]/form/input[1]')
    name_box.send_keys(username)

    search_button = driver.find_element_by_xpath('//*[@id="hp-search"]/form/button')
    search_button.click()

    # time.sleep(2)
    new_url = driver.current_url
    driver.get(new_url)

    wins = driver.find_element_by_xpath('//*[@id="profile"]/div[3]/div[1]/div[1]/div[3]/div/div[1]/div[2]')
    win_percent = driver.find_element_by_xpath('//*[@id="profile"]/div[3]/div[1]/div[1]/div[3]/div/div[2]/div[2]')
    kills = driver.find_element_by_xpath('//*[@id="profile"]/div[3]/div[1]/div[1]/div[3]/div/div[3]/div[2]')
    kd = driver.find_element_by_xpath('//*[@id="profile"]/div[3]/div[1]/div[1]/div[3]/div/div[4]/div[2]')
    matches = driver.find_element_by_xpath('//*[@id="profile"]/div[3]/div[1]/div[1]/div[1]/div')

    print("Name: {}".format(username))
    print("Wins: {}".format(wins.text))
    print("Win %: {}".format(win_percent.text))
    print("Kills: {}".format(kills.text))
    print("K/D: {}".format(kd.text))
    print(matches.text)


else:

    driver.get("https://fortnitetracker.com/")

    name_box = driver.find_element_by_xpath('//*[@id="hp-search"]/form/input')
    name_box.send_keys(username)

    search_button = driver.find_element_by_xpath('//*[@id="hp-search"]/form/button')
    search_button.click()

    new_url = driver.current_url
    driver.get(new_url)

    wins = driver.find_element_by_xpath('//*[@id="profile"]/div[4]/div/div[3]/div/div[1]/div[2]/div')
    win_percent = driver.find_element_by_xpath('//*[@id="profile"]/div[4]/div/div[3]/div/div[2]/div[2]/div')
    kills = driver.find_element_by_xpath('//*[@id="profile"]/div[4]/div/div[3]/div/div[3]/div[2]/div')
    kd = driver.find_element_by_xpath('//*[@id="profile"]/div[4]/div/div[3]/div/div[4]/div[2]/div')
    matches = driver.find_element_by_xpath('//*[@id="profile"]/div[4]/div/div[1]/div')

    with open("stats.txt", 'w') as stats:
        print("Name: {}".format(username), file=stats)
        print("Wins: {}".format(wins.text), file=stats)
        print("Win %: {}".format(win_percent.text), file=stats)
        print("Kills: {}".format(kills.text), file=stats)
        print("K/D: {}".format(kd.text), file=stats)
        print("\n", file=stats)
    print("Stats saved to stats.txt")
