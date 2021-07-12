from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def interactionProduct(driver, urlProduct):
    # go product
    driver.get(urlProduct)
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

    # comment = driver.driver.find_element_by_xpath("//div[@class='tuNfsN'][contains(text(),'đánh giá')]")
    # comment.click()
    # time.sleep(5)

    # add to cart
    # addButton = driver.find_element_by_xpath("//span[contains(text(),'thêm vào giỏ hàng')]")
    # addButton.click()
    # time.sleep(5)

    # click ảnh
    try:
        driver.execute_script('document.elementFromPoint(440, 340).click();')
        time.sleep(5)
    except:
        print("interaction: click image")
    # ActionChains(driver).move_by_offset(440, 340).click().perform()
    # driver.switch_to().defaultContent()
    try:
        ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
        time.sleep(5)
    except:
        print("interation: touch ESC")
    
    try:
        driver.execute_script('window.scrollBy(0,800)')
        time.sleep(5)
        driver.execute_script('window.scrollBy(0,0)')
        time.sleep(2)
    except:
        print("interaction: scroll")

    try:
        buttonAddToCart = driver.find_element_by_xpath("//span[contains(text(),'thêm vào giỏ hàng')]")
        buttonAddToCart.click()
        time.sleep(5)
    except:
        print("interaction: buttonAddToCart")