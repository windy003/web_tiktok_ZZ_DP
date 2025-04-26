from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback
import json
from datetime import datetime




# 创建配置对象
options = ChromiumOptions()
options.set_argument('--user-data-dir=./chrome_data')

# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")



def main():
    with open(file_path, "r", encoding="utf-8") as f:
        data = {}

        for line in f:
            url = line.strip()
            page.get(url)

            # 获取发布时间
            pub_time_element = page.ele('xpath://span[@data-e2e="browser-nickname"]//span[3]')
            pub_time = pub_time_element.text if pub_time_element else None
            print(pub_time)


            
            # 获取描述
            desc = page.ele('xpath://div[@data-e2e="browse-video-desc"]')
            print(desc)
            desc_text = desc.text if desc else None
            print(desc_text)


            # 将数据存入字典
            data[url] = {
                'pub_time': pub_time,
                'desc': desc_text
            }


    with open("1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # 添加indent参数使json文件更易读



if __name__ == "__main__":
    start_time = time.time()
    file_path = "tiff3月.txt"
    main()
    end_time = time.time()
    print(f"程序运行时间: {(end_time - start_time)/60} 分钟")
