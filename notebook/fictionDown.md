## 下载

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

## 简繁体转换  

### 问题一：  

转换到中途，出现了非常妖孽的一个错误：  

```
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-22-7649ebb3fb37> in <module>
      9     with open(os.path.join(pathJianti, fileNameJianti), 'w') as fileJianti:
     10         with open(os.path.join(pathFanti, fileNameFanti)) as fileFanti:
---> 11             contentFanti = fileFanti.readlines()
     12             for sentenceFanti in contentFanti:
     13                 sentenceJianti = Converter('zh-hans').convert(sentenceFanti)

~/anaconda3/lib/python3.7/codecs.py in decode(self, input, final)
    320         # decode input (taking the buffer into account)
    321         data = self.buffer + input
--> 322         (result, consumed) = self._buffer_decode(data, self.errors, final)
    323         # keep undecoded input until the next call
    324         self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdb in position 79: invalid continuation byte

```
这是哪儿来的unicode编码问题呢？  于是打印出文件列表来看，  

```
莊子的故事.txt',
 '閒情偶寄.txt',
 '琵琶記.txt',
 '子不語.txt',
 '.DS_Store',

```
居然是.DS_Store导致的。真是妖孽啊。   

解决办法有二：  

一是删掉非txt文件；  
二是只读取文件夹中的txt文件。

试了一下，即使打开隐藏文件，也无法看到.DS_Store，所以采取方法二解决。

### 问题二：  
```
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-24-facf22a06af4> in <module>
     12     with open(os.path.join(pathJianti, fileNameJianti), 'w') as fileJianti:
     13         with open(os.path.join(pathFanti, fileNameFanti)) as fileFanti:
---> 14             contentFanti = fileFanti.readlines()
     15             for sentenceFanti in contentFanti:
     16                 sentenceJianti = Converter('zh-hans').convert(sentenceFanti)

~/anaconda3/lib/python3.7/codecs.py in decode(self, input, final)
    320         # decode input (taking the buffer into account)
    321         data = self.buffer + input
--> 322         (result, consumed) = self._buffer_decode(data, self.errors, final)
    323         # keep undecoded input until the next call
    324         self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 926: invalid continuation byte

```

乍一看和上面那个妖孽一样。但是看文件，眼下是简体文件夹中已经建立了文件，但内容为空，说明是读取繁体文件内容出错。  

回到繁体文件夹，果然这个文件打不开，说非utf-8编码创建的。用编辑器打开则是一堆乱码。


