## 1. 函数外加括号

时常见到js函数用括号括起来，而且后面还会跟着一对括号。不知道这是啥意思，看到这篇文章里有答案：

[请问js里两个括号是什么意思？ - 知乎](https://www.zhihu.com/question/48238548/answer/110184697)

> js的引擎会把这里的 function 看成是函数声明，而函数声明不允许没有函数名，因此会对匿名函数报错。

这句话的意思是匿名函数才需要？但也有不是匿名函数的时候这么用啊。

[Javascript模块化编程（一）：模块的写法 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2012/10/javascript_module.html)

"[立即执行函数](http://benalman.com/news/2010/11/immediately-invoked-function-expression/)

## 2. 打印变量值

[js的打印(输出)方式console.log(),console.dir(),console.table()_sunlizhen的专栏-CSDN博客_js打印输出con](https://blog.csdn.net/sunlizhen/article/details/73195471)

这个是在F12的console里看的。

## 3. name和id

读取某个div下并列层的div，通过上面的打印，发现居然不是并列取，而是从源代码顺序，逐个逐层，遇到就取出来。于是并列第一个的家伙，就取出了二十几个div。而我要的是它和它的兄弟节点。

又发现html代码中，id是唯一的，但name却不是。类似于人的名字和身份证。name就是名字，id就是身份证。

于是把`getElementsByTagName(div)`改成了`getElementsByName()`，为三个div取了相同的name值。

```
var contents = document.getElementsByName('tabContent');
```

[JavaScript实现Tab标签页切换的最简便方式 - 池月 - 博客园](https://www.cnblogs.com/-867259206/p/5664896.html)

它原本是这样的：

```
 contents = document.getElementsByClassName('tab-content')[0].getElementsByTagName('div');
```

