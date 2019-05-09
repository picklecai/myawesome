# time

[Python3 time.strftime()方法 - 码农教程](http://www.manongjc.com/article/665.html)

要紧的教训是，现在必须用大写的M和S来表示分和秒了。否则时间很奇怪。

```
now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
```

总是出现15:05，14:05，09:05，后来发现，由于用了小写m，其实人家表达的是现在是5月份。小写的s出来的秒是10位数字。

