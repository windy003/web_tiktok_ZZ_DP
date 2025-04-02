from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback


# 创建配置对象
options = ChromiumOptions()
# options.set_argument('--headless=new')  # 使用新的无头模式
# options.set_argument('--no-sandbox')    # 在Linux系统中添加此参数
# options.set_argument('--disable-dev-shm-usage')  # 避免内存不足问题

# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")


url = "https://www.tiktok.com/@ai.christianson?lang=zh-Hans"



try:
    page.get(url)

    # 滚动页面并加载更多内容
    try:
        # 使用 JavaScript 获取页面高度
        last_height = page.run_js('return document.documentElement.scrollHeight')
        while True:
            # 滚动到底部
            page.scroll.to_bottom()
            print("已滚动到底部，等待新内容加载...")
            time.sleep(3)  # 等待新内容加载

            # 使用 JavaScript 获取新的页面高度
            new_height = page.run_js('return document.documentElement.scrollHeight')
            if new_height == last_height:
                print("已到达页面底部，停止滚动。")
                break
            else:
                last_height = new_height

    except Exception as e:
        print(f"滚动页面失败: {e}")





    # 获得文章和微头条链接块包括标题
    data = ""

    try:
        eles = page.eles('xpath://a[contains(@href, "https://www.tiktok.com/@")]')
        for ele in eles:
            # 使用attr()方法获取href属性
            href = ele.attr('href')
            if href:  # 确保href存在
                data += href + "\n"
    except Exception as e:
        traceback.print_exc()


    try:
        with open('0.txt', 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print(f"保存数据失败: {e}")
    


except Exception as e:
    print(f"访问页面失败: {e}")


# finally:
#     page.close()

