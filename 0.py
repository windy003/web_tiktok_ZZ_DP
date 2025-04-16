from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback


# 创建配置对象
options = ChromiumOptions()
# options.set_argument('--headless=new')  # 使用新的无头模式
# options.set_argument('--no-sandbox')    # 在Linux系统中添加此参数
# options.set_argument('--disable-dev-shm-usage')  # 避免内存不足问题

options.set_argument('--user-data-dir=./chrome_data')


# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")


url = "https://www.tiktok.com/@tiffintech"


# 测试用的
# url = "https://www.tiktok.com/@user2634097387375"   



def scroll_page():
    try:
        # 使用 JavaScript 获取页面高度
        last_height = page.run_js('return document.documentElement.scrollHeight')
        time.sleep(1)  # 等待新内容加载
        page.scroll.to_bottom()
        print("等待1秒并执行了滚动命令")

        # 使用 JavaScript 获取新的页面高度
        new_height = page.run_js('return document.documentElement.scrollHeight')
        if last_height == new_height:
            time.sleep(2)
            last_height = page.run_js('return document.documentElement.scrollHeight')
            page.scroll.to_bottom()
            print("等待了2秒并执行了滚动命令")
            new_height = page.run_js('return document.documentElement.scrollHeight')
            if last_height == new_height:
                time.sleep(3)
                last_height = page.run_js('return document.documentElement.scrollHeight')
                page.scroll.to_bottom()
                print("等待了3秒并执行了滚动命令")
                new_height = page.run_js('return document.documentElement.scrollHeight')
                if last_height == new_height:
                    time.sleep(4)
                    last_height = page.run_js('return document.documentElement.scrollHeight')
                    page.scroll.to_bottom()
                    new_height = page.run_js('return document.documentElement.scrollHeight')
                    if last_height == new_height:
                        time.sleep(5)
                        last_height = page.run_js('return document.documentElement.scrollHeight')
                        page.scroll.to_bottom()
                        print("等待了5秒并执行了滚动命令")
                        new_height = page.run_js('return document.documentElement.scrollHeight')
                        if last_height == new_height:
                            time.sleep(6)
                            last_height = page.run_js('return document.documentElement.scrollHeight')
                            page.scroll.to_bottom()
                            print("等待了6秒并执行了滚动命令")
                            new_height = page.run_js('return document.documentElement.scrollHeight')
                            if last_height == new_height:
                                print("已到达页面底部，停止滚动。")
                                return
                            else:
                                scroll_page()
                        else:
                            scroll_page()
                    else:
                        scroll_page()
                else:
                    scroll_page()
            else:
                scroll_page()
        else:
          scroll_page()
 
                                        


    except Exception as e:
        print(f"滚动页面失败: {e}")



try:
    page.get(url)


    # page.run_js('document.body.style.zoom = "25%"')


    # 滚动页面并加载更多内容
    try:
        scroll_page()

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



