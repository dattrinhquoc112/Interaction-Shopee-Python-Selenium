import PySimpleGUI as sg
import csv
from interaction import interactionLogin, interactionProduct
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

layout = [
        [sg.Text("USERNAME")],
        [sg.InputText(key="username")],
        [sg.Text("PASSWORD")],
        [sg.InputText(key="password")],
        # [sg.Button("Choose file csv")],
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
        # read csv file
        filePath = values["filecsv"]
        with open(filePath, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rowCsv.append(row)

        # start
        driver = webdriver.Chrome(ChromeDriverManager().install())
        interactionLogin(username=values["username"], password=values["password"], driver=driver)
        
        for row in rowCsv:
            interactionProduct(driver=driver, infoProduct=row)

        time.sleep(20)
        driver.quit()

window.close()