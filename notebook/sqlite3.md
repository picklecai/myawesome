# sqlite3

## cursor不能作为context来用???   

```
def inputnew(data):
    with sqlite3.connect(ROOT + '/noterecord.db') as conn:
        with conn.cursor() as cursor:
            cursor.execute('create table if not exists record (time text, record text)')
            cursor.execute('insert into record (time, record) values (?, ?)', data)
        conn.commit()
```
运行这段代码，得到提示：  

```
    with conn.cursor() as cursor:
AttributeError: __enter__
```

在这里[MySQL Bugs: #89113: Connector/Python cursors cannot act as a context manager](https://bugs.mysql.com/bug.php?id=89113)，看到描述：  

> Connector/Python cursors cannot act as a context manager

暂时把with拿掉，可以运行。

