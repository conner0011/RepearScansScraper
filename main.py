from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def getComic():
    driver = webdriver.Chrome()
    driver.get("https://reaperscans.com/latest-comic/")
    wait = WebDriverWait(driver, 10)

    latestComic = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"loop-content\"]/div[1]/div/div[1]/div/div[2]")))
    chapTitle = latestComic.find_element_by_xpath("//*[@id=\"loop-content\"]/div[1]/div/div[1]/div/div[2]/div[1]/h3/a").text
    chapNum = latestComic.find_element_by_xpath("//*[@id=\"loop-content\"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/span[1]/a").text
    chapLink = latestComic.find_element_by_xpath("//*[@id=\"loop-content\"]/div[1]/div/div[1]/div/div[2]/div[1]/h3/a").get_attribute("href")
    driver.quit()
    return chapTitle, chapNum, chapLink

def loop():
    with open("currentComic.txt", "r") as f:
        currentComic = f.read()
    if currentComic == "":
        chapTitle, chapNum, chapLink = getComic()
        with open("currentComic.txt", "w") as f:
            f.write(chapTitle)
        print("New comic! " + chapTitle + " " + chapNum)
    else:
        chapTitle, chapNum, chapLink = getComic()
        if chapTitle != currentComic:
            with open("currentComic.txt", "w") as f:
                f.write(chapTitle)
            print("New comic: " + chapTitle + " " + chapNum + " " + chapLink)
        else:
            print("No new comic")
    sleep(300)
    loop()

loop()