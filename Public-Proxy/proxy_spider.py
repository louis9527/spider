from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait

"""
说明：利用webdriver爬去代理网站免费代理。
urllib2_proxy：{"http":"122.143.134.59:80"}
requests_proxy：{"http":"http://122.143.134.59:80"}
scrapy_proxy："http://122.143.134.59:80"

"""


def main_analysis(data):
    ip = data.xpath('//*[@id="tblproxy"]/tbody/tr/td[2]/text()')
    port = data.xpath('//*[@id="tblproxy"]/tbody/tr/td[3]/text()')
    for x, y in zip(ip, port):
        print('{0}:{1}'.format(x, y))
        with open('urllib2_proxy.txt', 'a+') as f1, \
                open('requests_proxy.txt', 'a+') as f2, open('scrapy_proxy.txt', 'a+') as f3:
            f1.write('{"http":"%s:%s"}\n' % (x, y))
            f2.write('{"http":"http://%s:%s"}\n' % (x, y))
            f3.write('"http://%s:%s"\n' % (x, y))


def analysis():
    data = etree.HTML(driver.page_source)
    index = data.xpath('//*[@id="psbform"]/div/a/text()')
    main_analysis(data)  # 解析第一页上的ip port

    for i in index:
        next_page = driver.find_element_by_class_name("pagenavi").find_element_by_link_text(i)
        next_page.click()
        data = etree.HTML(driver.page_source)
        main_analysis(data)  # 解析后续页面上的ip port


if __name__ == '__main__':
    url = "http://www.gatherproxy.com/zh/proxylist/country/?c=China"
    driver = webdriver.PhantomJS()
    WebDriverWait(driver, 5)
    driver.get(url)
    driver.find_element_by_class_name("button").click()
    analysis()
