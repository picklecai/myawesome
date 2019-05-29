# csv文档处理 

## Reader对象  

```
import csv, os

exampleFile = open(os.path.dirname(os.getcwd()) + '/files/csv/example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row # ' + str(exampleReader.line_num) + ': ' + str(row))
```
这是正常运行可以打印出每行内容的代码

```
import csv, os

exampleFile = open(os.path.dirname(os.getcwd()) + '/files/csv/example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
for row in exampleReader:
    print('Row # ' + str(exampleReader.line_num) + ': ' + str(row))
```
加上`exampleData = list(exampleReader)`，即使下文并没有使用data变量，也不能打印出任何东西，而且程序并不报错。   

作者说：  

> Reader对象只能循环遍历一次，要再次读取csv文件，必须调用csv.reader，创建一个对象。  

不知道和这个有没有关系。  

## tsv文件  

还以为作者写错格式了。没想到真的有tsv文件：  

> TSV(为用制表符tab分隔的文件)

## open的路径  

打开一个文件时，沿路路径需要预先建立好，否则就说没有这样一个路径

```
csvFile = open(os.path.join(path, 'HeaderRemove', csvFilename), 'w', newline='') # 路径需要预先建立好
    csvWriter = csv.writer(csvFile)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFile.close()
```
这里的HeaderRemove文件夹，之前没有建立，运行时就报错。手动建了一个文件夹后，就正常运行了。

另外注意：line_num是从1开始的，不是从0开始。  

```
    for row in readerObj:
        if readerObj.line_num ==1:
            continue
        csvRows.append(row)
```



