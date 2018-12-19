import requests
import re
import argparse
from tqdm import tqdm
from selenium import webdriver

"""
说明：批量下载小鹏奇葩行视频

"""


class XiaoPeng(object):

    def __init__(self):
        # 存储title
        self.temp_list = None
        self.instance = True
        self.headers = {"USER_AGENT": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36"
                                      " (KHTML, like G""ecko) Chrome/67.0.3396.99 Mobile Safari/537.36"}

    def parse_and_download(self):
        for i in range(args.start, args.stop):
            start_url = "http://www.xpqpx3.com/vod-play-id-19868-src-1-num-{0}.html".format(i)  # 小鹏奇啪说
            # start_url = "http://xiaopengqipaxing.com/vod-play-id-19867-src-1-num-{0}.html".format(i)  # 小鹏奇啪行*第一季
            # start_url = "http://xiaopengqipaxing.com/vod-play-id-19891-src-1-num-{0}.html".format(i)  # 小鹏奇啪行*第二季

            driver.get(start_url)
            result = driver.page_source
            if self.instance:
                # 解析video_title，只解析一次
                pattern = re.compile(r'(?<=false;">)\w+.*?(?=</a>)')
                self.temp_list = pattern.findall(result)
                self.instance = False

            # 解析video下载url
            pattern = re.compile(r'https://gss3.baidu.com/[a-z,A-Z,0-9]+/[-,a-z,A-Z,0-9]+/[_a-z,A-Z,0-9]+.mp4')
            video_url_li = pattern.findall(result)
            print(video_url_li[0])

            # 发起请求，返回响应，写入本地
            response = requests.get(video_url_li[0], headers=self.headers, stream=True)
            content_size = int(response.headers['Content-Length']) / 1024
            with open('./' + self.temp_list[i+2] + '.mp4', 'wb') as f:
                print("总计: ", content_size, 'k')
                for data in tqdm(iterable=response.iter_content(1024), total=content_size, unit='k'):
                    f.write(data)
                print("完成：" + self.temp_list[i+2] + '.mp4')

    def run(self):
        self.parse_and_download()


if __name__ == '__main__':
    # 终端传参
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="Link start mark(include start value)", type=int)
    parser.add_argument("stop", help="Link stop mark(not in stop value)", type=int)
    args = parser.parse_args()

    # 调用PhantomJS
    driver = webdriver.PhantomJS()
    xp = XiaoPeng()
    xp.run()



