from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback
import json


# 创建配置对象
options = ChromiumOptions()
# options.set_argument('--headless=new')  # 使用新的无头模式
# options.set_argument('--no-sandbox')    # 在Linux系统中添加此参数
# options.set_argument('--disable-dev-shm-usage')  # 避免内存不足问题

# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")

with open("0.1.txt", "r", encoding="utf-8") as f:
    data={}
    
    for line in f:
        url = line.strip()
        page.get(url)
        time.sleep(3)

        desc=page.ele('xpath://div[@data-e2e="video-desc"]')

        if desc.text:   
            print(desc.text)
            data[url]=desc.text+'\n'

        time.sleep(3)

    with open("1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

