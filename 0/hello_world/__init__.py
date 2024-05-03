import time
import cv2
from pytesseract import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Open page
driver.get("https://darkagesworld.ru")
print('https://darkagesworld.ru')
time.sleep(2)

# step1 Sign In
# a enter username
username_locator = driver.find_element(By.ID, "edit-name")
username_locator.send_keys("MikeR")
print('MikeR')

# b enter password
password_locator = driver.find_element(By.NAME, "pass")
password_locator.send_keys("rommicdomotecmike")
print('Password')

# c click continue
continue_locator = driver.find_element(By.ID, "edit-submit")
continue_locator.click()
time.sleep(2)

# d verify new page URL contains https://stage.climatetechhub.x.studio/home
actual_url = driver.current_url
assert actual_url == "https://darkagesworld.ru/vr?check_logged_in=1"
print('I am in')


# step3 Cut the tree
# a Captcha chat GPT solution


def captcha():
    driver.refresh()
    print('Refresh in function')
    time.sleep(6)

    def captcha_screenshot():
        captcha_element = driver.find_element(By.XPATH, (
            "//img[@title='CAPTCHA на основе изображений']"))
        captcha_element.screenshot("captcha.png")

    try:
        captcha_screenshot()
    except:
        captcha()

    captcha_image = cv2.imread("captcha.png")

    whitelist = ' 0123456789'
    config = f'--psm 6 tessedit_char_whitelist={whitelist}'
    captcha_text = pytesseract.image_to_string(captcha_image, config=config)
    print(captcha_text)

    # b enter received from tesseract OCR numbers
    captcha_field_locator = driver.find_element(By.ID, "edit-captcha-response")
    captcha_field_locator.send_keys(captcha_text)
    print('Entering numbers')
    time.sleep(2)

    # c click cut
    cut_tree_locator = driver.find_element(By.ID, "submit_alb_mine")
    if cut_tree_locator.is_displayed():
        cut_tree_locator.click()
    else:
        print("Captcha is correct. Waiting for 3 minutes...")
        time.sleep(190)  # 180 seconds = 3 minutes
        print("3 minutes later")
        captcha()
    # cut_tree_locator.click()
    print('To cut is clicked')

    if cut_tree_locator.is_displayed():
        print("Captcha isn't correct. Repeating...")
        captcha()
    else:
        print("Captcha is correct. Waiting for 3 minutes before repeating.")
        time.sleep(190)  # 180 seconds = 3 minutes
        captcha()


captcha()
