import PySimpleGUI as sg
import csv

from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from interaction import interactionLogin, interactionProduct

from webdriver_manager.chrome import ChromeDriverManager
import time
from seleniumwire import webdriver

layout = [
        [sg.Text("Account thứ: ")],
        [sg.InputText(key="rankAccount")],
        [sg.FileBrowse(key="fileCSVaccount", button_text="Chọn file csv Account")],
        [sg.FileBrowse(key="fileCSVproduct", button_text="Chọn file csv Sản phẩm")],
        [sg.Button(key="start", button_text="Bắt đầu")],
        [sg.Button(key="readcsv", button_text="Đọc csv")],
    ]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    rowCSVaccount = []
    rowCSVproduct = []

    #PROXY
    PROXY = "103.28.35.183:34567"
    usernamePROXY = "VN022-8597"
    passwordPROXY = "CuR037dX1212"

    #SHOPEE
    sdt = "0925210591"
    passSDT = "Matkhau123!"
        
    if event == sg.WIN_CLOSED:
        break
    
    if event == "start":
        # read csv account file
        filePath = values["fileCSVaccount"]
        with open(filePath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rowCSVaccount.append(row)

        # read csv product file
        filePath = values["fileCSVproduct"]
        with open(filePath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            values["filenameCSVproduct"] = csvfile.name
            for row in reader:
                rowCSVproduct.append(row)

        # start

        options = {
            'proxy': {
                'http': f'http://{usernamePROXY}:{passwordPROXY}@{PROXY}',
                'https': f'https://{usernamePROXY}:{passwordPROXY}@{PROXY}',
                'no_proxy': 'localhost,127.0.0.1'
                }
            }
        # driver = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=options)
        # interactionLogin(username=values["username"], password=values["password"], driver=driver)
        
        # for row in rowCsv:
        #     interactionProduct(driver=driver, infoProduct=row)

        # time.sleep(10)
        # driver.quit()

    window.close()