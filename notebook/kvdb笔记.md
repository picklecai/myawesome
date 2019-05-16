# KVDB笔记  

在python3环境下，直接安装sae总是失败。于是直接安装kvdb，没想到成功了。

## 0. 安装

`source activate python35`
`pip3 install kvdb` 

## 1. 如何用

之前的句法已经不对了。现在新的参考：  [rcbensley/kvdb: Key Value Database is a toy abstraction layer to persist Python Dictionaries to MariaDB 10.3+](https://github.com/rcbensley/kvdb)

```
import kvdb

db = kvdb.db()
db.setup()

```
到此为止就出错了，错误如下：  

```
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' ([Errno 61] Connection refused)")
```

后来据说是python3.4以后的版本不支持mysql，转而用pymysql。我试图用pip安装pymysql，不料说系统已经有了：  

```
(python35) ^$ pip3 install pymysql
Requirement already satisfied: pymysql in /Users/caimeijuan/anaconda/envs/python35/lib/python3.7/site-packages (0.9.3)

```
那就到此为止吧。不玩kvdb了。  



