# coding=utf-8
import os
import re
import time
import random

import pdfkit
from bs4 import BeautifulSoup
from selenium import webdriver


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""


class QiangTangAdventuresSpider(object):

    def __init__(self):
        self.name = None  # pdf文件名字
        self.local_html_file_name = []

    def scroll_mouse(self):
        # 模拟鼠标滚动
        height = driver.execute_script("return (document.body.scrollHeight)")
        print("body部分高度: {0}".format(height))
        for i in range((height//700)):
            driver.execute_script("window.scrollBy(0,1000)")
            time.sleep(random.uniform(0.2, 0.5))

    def parse_html(self):
        if "pointer" in driver.find_element_by_xpath("/html/div[2]/div").get_attribute("style"):
            # 去掉页面弹窗，根据css中style属性的pointer值来定位点击关闭弹窗
            driver.find_element_by_xpath("/html/div[2]/div/img").click()
            time.sleep(random.randint(3, 5))

            flag = 1
            while True:
                if flag == 1:
                    self.scroll_mouse()

                    # 获取页面源码
                    data = driver.page_source

                    soup = BeautifulSoup(data, 'html.parser')
                    # 仅获取标题，作pdf文件名用
                    title = soup.find(class_="art-title").get_text()
                    # 去掉文件名中的非法字符
                    self.name = re.sub('[\/:*?"<>|]', '-', title)
                    # 获取指定节点下的html内容，包括：标题 + 正文内容
                    body = soup.find_all(class_="blk-container blk-BGContainer")[0]
                    html = html_template.format(content=body)
                else:
                    self.scroll_mouse()
                    data = driver.page_source

                    # 获取指定节点下的html内容，不包括：标题
                    soup = BeautifulSoup(data, 'html.parser')
                    body = soup.find_all(class_="art-content art-content-old")[0]
                    html = html_template.format(content=body)

                yield html

                # 循环计数+1
                flag += 1
                try:
                    # 点击下一页
                    driver.find_element_by_class_name('art-page').find_element_by_link_text('下一页').click()
                    time.sleep(3)
                except Exception as e:
                    driver.quit()
                    break

    def write_html(self, htmls):
        for i, html in enumerate(htmls):
            with open(str(i) + ".html", 'w', encoding='utf-8') as f:
                f.write(html)
            self.local_html_file_name.append(str(i)+".html")

    def html_to_pdf(self):
        pdfkit.from_file(self.local_html_file_name, self.name + ".pdf")

        # 删除本地html文件
        for f in self.local_html_file_name:
            os.remove(f)

    def run(self):
        # 解析
        htmls = self.parse_html()
        # 写入本地
        self.write_html(htmls)
        # 打印名字
        print(self.name)
        # html转换pdf
        self.html_to_pdf()


if __name__ == '__main__':
    start_url = "http://www.8264.com/youji/512349-1.html"
    driver = webdriver.Chrome()
    driver.get(start_url)
    qt = QiangTangAdventuresSpider()
    qt.run()
