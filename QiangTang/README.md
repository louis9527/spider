#Python 爬虫：将8264网站的《北方的空地，孤身穿越大羌塘无人区（完）》转换成pdf

### 自用python3.7


### 准备工具

+ html转换pdf工具：wkhtmltopdf
+ wkhtmltopdf的Python封装包：pdfkit
+ Web的自动化测试工具：Selenium
+ 谷歌浏览器驱动：chromedriver


chromedrive下载地址：[http://npm.taobao.org/mirrors/chromedriver/](http://npm.taobao.org/mirrors/chromedriver/)
+ 注意：chromedrive与谷歌浏览器版本 必须对应。


### windows下偷懒安装chromedrive
+ 把 chromedriver.exe 放到 python2 和 python3 的目录下即可


### 相关包pip安装指令
```python
pip install selenium
pip install beautifulsoup4
pip install pdfkit

```

### 安装 wkhtmltopdf
Windows平台直接在：[http://wkhtmltopdf.org/downloads.html](http://wkhtmltopdf.org/downloads.html) 下载安装，然后将安装目录下的bin/目录路径添加进系统环境 $PATH 变量中。


### Linux系统可直接下列命令安装
```shell
$ sudo apt-get install wkhtmltopdf  # ubuntu
$ sudo yum intsall wkhtmltopdf      # centos
```





