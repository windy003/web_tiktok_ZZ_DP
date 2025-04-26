from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback
import json


# 创建配置对象
options = ChromiumOptions()
options.set_argument('--user-data-dir=./chrome_data')

# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")

with open("tiff-5.txt", "r", encoding="utf-8") as f:
    data = {}  # 初始化空字典
    
    for line in f:
        url = line.strip()
        page.get(url)

        # 获取描述
        desc = page.ele('xpath://div[@data-e2e="video-desc"]')
        print(desc)
        desc_text = desc.text if desc else None
        print(desc_text)



        # 获取发布时间
        pub_time_link = page.ele('xpath://a[contains(@class, "css-qvpt8d-StyledAuthorAnchor") and contains(@class, "e1g2yhv81") and contains(@class, "link-a11y-focus")]')
        print(pub_time_link)
        pub_time = pub_time_link.text if pub_time_link else None
        print(pub_time)


        # 将数据存入字典
        data[url] = {
            'desc': desc_text,
            'pub_time': pub_time
        }




with open("1.json", "a", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)  # 添加indent参数使json文件更易读


