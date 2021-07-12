import time
def login(username, password, driver):
    
    # go to login
    driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")
    time.sleep(5)
    # username/password
    try:
        usernameInput = driver.find_element_by_xpath("//input[@placeholder='Email/Số điện thoại/Tên đăng nhập']")
        usernameInput.send_keys(username)
    except:
        print("login: usernameInput")
    try:
        passwordInput = driver.find_element_by_xpath("//input[@placeholder='Mật khẩu']")
        passwordInput.send_keys(password)
    except:
        print("login: passwordInput")
    # click
    try:
        time.sleep(2)
        loginButton = driver.find_element_by_xpath("//button[contains(text(),'Đăng nhập')]")
        loginButton.click()
        time.sleep(10)
    except:
        print("login: loginButton")