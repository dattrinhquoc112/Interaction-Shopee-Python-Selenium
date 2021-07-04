import PySimpleGUI as sg
import csv
from interaction import interactionLogin, interactionProduct

from webdriver_manager.chrome import ChromeDriverManager
import time
from seleniumwire import webdriver
from MacAddress import changeCurrentMac, getCurrentMac

layout = [
        [sg.Text("USERNAME")],
        [sg.InputText(key="username")],
        [sg.Text("PASSWORD")],
        [sg.InputText(key="password")],
        [sg.Text("NEW MAC ADDRESS")],
        [sg.InputText(key="MacAddress")],
        [sg.Button(key="changeMacAddress", button_text="Change MAC Address")],
        [sg.FileBrowse(key="filecsv", button_text="Choose file csv")],
        [sg.Button(key="start", button_text="Bắt đầu")],
        [sg.Button(key="readcsv", button_text="Đọc csv")],
    ]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    rowCsv = []
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break
    if event == "start":
        # # read csv file
        # filePath = values["filecsv"]
        # with open(filePath, newline="", encoding="utf-8") as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         rowCsv.append(row)

        # start

        # 0925210591		Matkhau123!
        # 103.28.35.183:34567	VN022-8597	CuR037dX1212

        #PROXY

        PROXY = "103.28.35.183:34567"
        usernamePROXY = "VN022-8597"
        passwordPROXY = "CuR037dX1212"

        #SHOPEE

        sdt = "0925210591"
        passSDT = "Matkhau123!"

        options = {
            'proxy': {
                'http': f'http://{usernamePROXY}:{passwordPROXY}@{PROXY}',
                'https': f'https://{usernamePROXY}:{passwordPROXY}@{PROXY}',
                'no_proxy': 'localhost,127.0.0.1'
                }
            }
        driver = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=options)
        # interactionLogin(username=values["username"], password=values["password"], driver=driver)
        
        # for row in rowCsv:
        #     interactionProduct(driver=driver, infoProduct=row)

        # time.sleep(10)
        # driver.quit()
    if event == "changeMacAddress":
        print(getCurrentMac())
        changeCurrentMac(values["MacAddress"])
        print(getCurrentMac())
window.close()