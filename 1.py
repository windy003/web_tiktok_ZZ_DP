from DrissionPage import ChromiumPage, ChromiumOptions
import asyncio
import json
import concurrent.futures
import time
import traceback
from functools import partial

# 创建配置对象
options = ChromiumOptions()
options.set_argument('--user-data-dir=./chrome_data')

# 实际网页请求函数 - 在线程池中执行
def fetch_page_data(url, options):
    try:
        # 每个线程使用独立的页面对象
        page = ChromiumPage(options)
        page.get(url)
        
        # 获取发布时间
        pub_time = page.ele('xpath://span[@data-e2e="browser-nickname"]//span[3]')
        pub_time = pub_time.text if pub_time else None
        
        # 获取描述
        desc = page.ele('xpath://div[@data-e2e="browse-video-desc"]')
        desc_text = desc.text if desc else None
        
        return url, {'pub_time': pub_time, 'desc': desc_text}
    except Exception as e:
        print(f"处理URL {url} 时出错: {e}")
        traceback.print_exc()
        return url, {'pub_time': None, 'desc': None}

# 异步函数 - 将同步函数包装在线程池中
async def process_url_async(url, thread_pool, options):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        thread_pool, 
        partial(fetch_page_data, url, options)
    )

async def main():
    # 读取URL列表
    with open("tiff-100.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f]
    
    data = {}
    
    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as thread_pool:
        # 创建异步任务列表
        tasks = [process_url_async(url, thread_pool, options) for url in urls]
        
        # 使用异步方式等待所有任务完成
        print(f"开始处理 {len(urls)} 个URL...")
        results = await asyncio.gather(*tasks)
        
        # 收集结果
        for url, result in results:
            data[url] = result
    
    # 保存结果到JSON文件
    with open("1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"所有 {len(urls)} 个URL处理完成，结果已保存到1.json")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"总耗时: {(end_time - start_time)/60:.2f} 分钟")


