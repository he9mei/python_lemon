from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

caps = {
    # "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "5.1",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    # "deviceName": "MJA68TGES4S4SKAY",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "deviceName": "UGW8SOWWEY75NNDM",   # lenevo手机-5.1；oppo手机-7.1.1
    "appPackage": "com.dangdang.reader",
    "appActivity": ".activity.GuideActivity",
    "noReset": True,
    "chromedriverExecutable": "E:\\chromedriver\\2.21_46-50\\chromedriver.exe"  # 指定chromedriver
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 获取当前所有的contexts
cons = driver.contexts
print("进入h5之前的cons:", cons)  # 进入h5之前的cons: ['NATIVE_APP']

# 原生
# loc_tab = (MobileBy.ID, 'com.dangdang.reader:id/tab_item_name')
# loc_search = (MobileBy.ID, 'com.dangdang.reader:id/store_search_bg')
# loc_cart = (MobileBy.ID, 'com.dangdang.reader:id/shopping_cart_iv')

# 进入h5页面---点击电子书tab
loc_tab = (MobileBy.ID, 'com.dangdang.reader:id/tab_item_name')
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc_tab))
driver.find_elements(*loc_tab)[1].click()

# 等待webview元素可见
loc_webview = (MobileBy.CLASS_NAME, "android.webkit.WebView")
# loc_webview = (MobileBy.ID, 'com.dangdang.reader:id/webView')
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc_webview))  # 这里使用的所有元素加载完成
sleep(1)

# 获取当前所有的contexts
cons = driver.contexts
print("进入h5之后的cons:", cons)  #进入h5之后的cons: ['NATIVE_APP', 'WEBVIEW_com.dangdang.reader']

# 切换到webview
# driver.switch_to.context(cons[-1])
driver.switch_to.context("WEBVIEW_com.dangdang.reader")
print("已切换到：WEBVIEW_com.dangdang.reader")

# 定位web元素,并操作（定位方式见笔记）---可以先用UC devtools拿到链接再用chrome查看元素（直接用uc devtools查看不是很好用）
# loc_h5 = (MobileBy.XPATH, "//dl[@alt='促销']")
loc_h5 = (By.XPATH, "//dl[@alt='促销']")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_h5))   # ====报错===
driver.find_element(*loc_h5).click()
sleep(2)
driver.press_keycode(4)

# 切换回到native
driver.switch_to.context("NATIVE_APP")
print("已切换到：NATIVE_APP")

# 再操作native---点击精选
driver.find_elements(*loc_tab)[0].click()

sleep(5)
driver.quit()

'''
Chrome '46.0.2490'
'''
