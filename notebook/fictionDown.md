一个搞笑的错误：  

```
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-66-a0633c928f96> in <module>
     10     fictionID = (fictionList[i].get('href')).split('/')[2]
     11     fictionUrl = 'https://www.gutenberg.org/files/' + fictionID + '/' + fictionID + '-0.txt'
---> 12     with open(file ,'wb') as fictionFile:
     13         resFiction = requests.get(fictionUrl)
     14         for chunk in resFiction.iter_content(100000):

FileNotFoundError: [Errno 2] No such file or directory: '/Users/caimeijuan/github/myawesome/files/fiction/True Heart/Mind.txt'

```
原因是有一篇小说的名字叫“True Heart/Mind”，包含了'/'，被系统当作路径符号了。

解决办法有二：  
一是放弃join，直接写加号。  
另一个是判断小说名中是否有路径符号，如果有用空格代替。


