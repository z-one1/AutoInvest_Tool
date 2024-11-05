from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 启动 Safari 浏览器
driver = webdriver.Safari()

# 打开网页
driver.get("https://www.google.com/")

# 查找网页元素
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OpenAI ChatGPT" + Keys.RETURN)

# 等待几秒以查看结果
time.sleep(5)

# 关闭浏览器

