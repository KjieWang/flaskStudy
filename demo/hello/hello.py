from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
	return '<h1>Hello World</h1>'



from appium import webdriver

# 定义运行环境

desired_caps = {
	'devicename':'Android Emulator',
	'automationName':'appium',
	'platformName':'Android',
	'platformVersion':'7.0',
	'appPackage':'com.android.calculator2',
	'appActivity':'.Calculator',

}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()

driver.quit()