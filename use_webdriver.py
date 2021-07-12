import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
# from selenium import webdriver
from interaction import interactionProduct
from read_file_csv import content_csv
from login import login
from clearCart import clear

# PROXY
PROXY = "103.28.35.183:34567"
usernamePROXY = "VN022-8597"
passwordPROXY = "CuR037dX1212"

# SHOPEE
sdt = "0944558023"
passSDT = "Datcute1102"

# read file Product

filePath = os.path.join(os.path.dirname(__file__), "Testinteraction Shopee.csv")
contentProduct = content_csv(filePath)

# read file account
fileAccount = os.path.join(os.path.dirname(__file__), "account.csv")
contentAccount = content_csv(fileAccount)

# start

options = {
    'proxy': {
        'http': f'http://{contentAccount[0]["proxyUsername"]}:{contentAccount[0]["proxyPassword"]}@{contentAccount[0]["proxyURL"] + ":" + contentAccount[0]["proxyPORT"]}',
        'https': f'https://{contentAccount[0]["proxyUsername"]}:{contentAccount[0]["proxyPassword"]}@{contentAccount[0]["proxyURL"] + ":" + contentAccount[0]["proxyPORT"]}',
        'no_proxy': 'localhost,127.0.0.1'
    }
}
options1 = {
    'proxy': {
        'http': f'http://{usernamePROXY}:{passwordPROXY}@{PROXY}',
        'https': f'https://{usernamePROXY}:{passwordPROXY}@{PROXY}',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "http://VN022-8597:CuR037dX1212@103.28.35.183:34567"
# prox.socks_proxy = "http://VN022-8597:CuR037dX1212@103.28.35.183:34567"
# prox.ssl_proxy = "http://VN022-8597:CuR037dX1212@103.28.35.183:34567"

# capabilities = webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy":"http://VN022-8597:CuR037dX1212@103.28.35.183:34567",
#     "ftpProxy":"http://VN022-8597:CuR037dX1212@103.28.35.183:34567",
#     "sslProxy":"http://VN022-8597:CuR037dX1212@103.28.35.183:34567",
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "class":"org.openqa.selenium.Proxy",
#     "autodetect":False
# }

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=https://VN022-8597:CuR037dX1212@103.28.35.183:34567')

driver = webdriver.Chrome(ChromeDriverManager().install(), seleniumwire_options=options)

# driver.get("http://whoer.net")

login(sdt, passSDT, driver=driver)

for product in contentProduct:
    interactionProduct(driver, product["Link sản phẩm"])

# ActionChains(driver).move_by_offset(50, 50).click().perform()

# driver.execute_script('document.fin')

clear(driver)
time.sleep(5)

driver.quit()
