from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

caps = {
    # "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "10",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "GEY6R20507024610",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.reader",
    "appActivity": ".activity.GuideActivity",
    "noReset": True
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 获取当前所有的contexts
cons = driver.contexts
print("进入h5之前的cons:", cons)

# 进入h5页面
loc = (MobileBy.XPATH, "//*[@text='促销']")
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc))
driver.find_element(*loc).click()

# # 等待webview元素可见
# loc = (MobileBy.CLASS_NAME, "android.webkit.webview")
# WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(loc))
# sleep(1)
#
# # 获取当前所有的contexts
# cons = driver.contexts
# print("进入h5之后的cons:", cons)