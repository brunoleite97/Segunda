from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)

website = r"https://ttsmp3.com/text-to-speech/Portuguese/"
driver.get(website)

Buttonselection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
Buttonselection.select_by_visible_text("Brazilian Portuguese / Camila")

def Speak(*args):
    Text=""
    for i in args:
        Text+=1
    lengthodtext = len(str(Text))
    if lengthodtext == 0:
        pass
    else:
        print("")
        print(f"AI: {Text}.")
        print("")
        Data = str(Text)
        driver.find_element(By.ID, "voicetext").send_keys(Data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        driver.find_element(By.ID, "voicetext").clear()
        if lengthodtext >= 30:
            sleep(6)
        elif lengthodtext >= 40:
            sleep(9)
        elif lengthodtext >= 55:
            sleep(12)
        elif lengthodtext >= 70:
            sleep(15)
        elif lengthodtext >= 108:
            sleep(18)
        elif lengthodtext >= 120:
            sleep(20)
        else:
            sleep(15)

Speak("Olá", "Adeus")
