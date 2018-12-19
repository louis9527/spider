### 说明：利用webdriver爬去代理网站免费代理。
+ urllib2_proxy：{"http":"122.143.134.59:80"}
+ requests_proxy：{"http":"http://122.143.134.59:80"}
+ scrapy_proxy："http://122.143.134.59:80"


zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表

实例：
```python
	>>>a = [1,2,3]
	>>> b = [4,5,6]
	>>> c = [4,5,6,7,8]
	>>> zipped = zip(a,b)     # 打包为元组的列表
	[(1, 4), (2, 5), (3, 6)]
	>>> zip(a,c)              # 元素个数与最短的列表一致
	[(1, 4), (2, 5), (3, 6)]
	>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
	[(1, 2, 3), (4, 5, 6)]

```

### install
```python
	pip install lxml
	pip install selenium
```

[PhantomJS下载地址](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip)