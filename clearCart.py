import time
def clear(driver):
    try:
        buttonCart = driver.find_element_by_xpath("//a[@class='cart-drawer flex v-center']//*[local-name()='svg']")
        buttonCart.click()
        time.sleep(5)
    except:
        print("clearCart: buttonCart")
    
    try:
        buttonSelectAll = driver.find_element_by_xpath("//div[@class='pcmall-cart_2LLjhp']//div[@class='stardust-checkbox__box']")
        buttonSelectAll.click()
        time.sleep(5)
    except:
        print("clearCart: buttonSelectAll")

    try:
        buttonClear = driver.find_element_by_xpath("//button[@class='clear-btn-style pcmall-cart_20LGiR']")
        buttonClear.click()
        time.sleep(2)
    except:
        print("clearCart: buttonClear")
    
    try:
        buttonOk = driver.find_element_by_xpath("//button[normalize-space()='có']")
        buttonOk.click()
    except:
        print("clearCart: buttonOk")
    

