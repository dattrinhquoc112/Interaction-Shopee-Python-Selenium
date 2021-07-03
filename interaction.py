from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
import time

def interactionLogin(username, password, driver):
    
    # go to login
    driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")
    time.sleep(5)
    # username/password
    usernameInput = driver.find_element_by_xpath("//input[@placeholder='Email/Số điện thoại/Tên đăng nhập']")
    usernameInput.send_keys(username)
    passwordInput = driver.find_element_by_xpath("//input[@placeholder='Mật khẩu']")
    passwordInput.send_keys(password)
    time.sleep(5)
    # click
    loginButton = driver.find_element_by_xpath("//button[contains(text(),'Đăng nhập')]")
    loginButton.click()
    time.sleep(5)

def interactionProduct(driver, infoProduct):
    # go product
    driver.get(infoProduct["Link sản phẩm"])
    time.sleep(5)
    # interaction

    # # chat
    
    # buttonChat = driver.find_element_by_xpath("//button[normalize-space()='Chat ngay']")
    # buttonChat.click()
    # time.sleep(5)

    # textFieldChat = driver.find_element_by_xpath("//textarea[contains(@placeholder,'Gửi tin nhắn')]")
    # textFieldChat.send_keys(infoProduct["Chat"])
    # time.sleep(5)

    # buttonSend = driver.find_element_by_class_name("src-components-ConversationDetailLayout-InputFieldLayout-ChatEditor-index__send-button--1uW8l")
    # buttonSend.click()
    # time.sleep(5)

    # Đọc bình luận

    comment = driver.driver.find_element_by_xpath("//div[@class='tuNfsN'][contains(text(),'đánh giá')]")
    comment.click()
    time.sleep(5)

    # add to cart
    addButton = driver.find_element_by_xpath("//span[contains(text(),'thêm vào giỏ hàng')]")
    addButton.click()
    time.sleep(5)