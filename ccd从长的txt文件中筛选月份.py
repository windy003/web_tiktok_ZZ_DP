from DrissionPage import ChromiumPage, ChromiumOptions
import time
import traceback
import json
from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 获取当前年份
current_year = current_time.year


def process_url(url, url_list):
    # 获取当前 URL 在文件中的行号
    line_number = url_list.index(url) + 1  # 行号从 1 开始
    print(f"当前处理的 URL 在文件中的行号是：{line_number}")


    return line_number



# 创建配置对象
options = ChromiumOptions()
options.set_argument('--user-data-dir=./chrome_data')

# 使用配置创建页面对象
page = ChromiumPage(options)
# print("已启动无头浏览器...")










def get_first_matched_url_line_number(file_path, start_line_number, year, month):
    with open(file_path, "r", encoding="utf-8") as f:
        # 跳过 start_line_number 之前的行
        for _ in range(start_line_number - 1):
            next(f)
        
        # 从 start_line_number 开始读取
        for current_line_number, line in enumerate(f, start=start_line_number):
            url = line.strip()
            page.get(url)

            # 获取发布时间
            pub_time_element = page.ele('xpath://span[@data-e2e="browser-nickname"]//span[3]')
            pub_time = pub_time_element.text if pub_time_element else None
            print(pub_time)

            if pub_time.count('-') == 2:
                year_from_scrape, month_from_scrape = pub_time.split('-')[:2]
            else:
                year_from_scrape = current_year
                month_from_scrape = pub_time.split('-')[0]

            if int(year_from_scrape) == year and int(month_from_scrape) == month:
                with open(file_path, "r", encoding="utf-8") as f:
                    url_list = [line.strip() for line in f]  # 读取所有 URL 并存储到列表中

                matched_url_line_number_in_the_month = process_url(url, url_list)
                return matched_url_line_number_in_the_month
            else:
                continue

 




def extract_lines_to_new_file(input_file, output_file, start_line, end_line):
    """
    从 input_file 中读取从 start_line 到 end_line 的行，并写入 output_file。
    
    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :param start_line: 起始行号（从 1 开始）
    :param end_line: 结束行号（包含）
    """
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for current_line_number, line in enumerate(infile, start=1):  # 从 1 开始计数
            if start_line <= current_line_number <= end_line:  # 检查是否在目标行数段内
                outfile.write(line)
            elif current_line_number > end_line:  # 如果超出结束行号，提前退出
                break





if __name__ == "__main__":

    #这里是要设置的参数部分 
    txt_file_path = "tiff-all.txt"
    year_to_scrape = 2025
    month_to_scrape = 3

    first_matched_url_line_number = get_first_matched_url_line_number(txt_file_path,1,year_to_scrape,month_to_scrape)

    last_matched_url_line_number = get_first_matched_url_line_number(txt_file_path,first_matched_url_line_number,year_to_scrape,month_to_scrape-1)

    print(first_matched_url_line_number)
    print(last_matched_url_line_number)

    extract_lines_to_new_file(txt_file_path, "filtered_urls.txt", first_matched_url_line_number, last_matched_url_line_number)


