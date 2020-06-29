# js实现tab标签页切换

js已然忘得差不多了。有必要继续写笔记。

学习这篇：[JavaScript实现Tab标签页切换的最简便方式](https://www.cnblogs.com/-867259206/p/5664896.html)

用了第四种方式。

最后成果：

```
# js部分

var tabs = document.getElementsByClassName('tabs')[0].getElementsByTagName('button');
var contents = document.getElementsByName('tabContent');

(function changeTab(tab) {
    for(var i = 0, len = tabs.length; i < len; i++) {
        tabs[i].onclick = showTab;
    }
})();

function showTab() {
    for(var i = 0, len = tabs.length; i < len; i++) {
        if(tabs[i] === this) {
            contents[i].className = 'show';
        }
        else {
            contents[i].className = 'hidden';
        }
    }
}
```



```
# html部分

# tab标签部分
<div class="tabs">
	<button class="cateChoose" > 全部 </button>
	{% for cate in cates %}
		<button class="cateChoose" > {{cate.name}} </button>
	{% endfor %}
</div>

# 内容部分

<div class="tabContent">
	<div name="tabContent" class="show"> 第一部分内容</div>
	{% for cate in cates %}
		<div name="tabContent" class="hidden"> 后续各部分内容</div>
	{% endfor %}
```



```
# css部分

/*新闻类目选项卡的基础样式*/
.cateChoose{
    float: left;
    display: inline-block;
    text-indent: 0;
    padding: 2%;
    margin: 2% 1%;
    border: 0;
    background:#fff;
    font-size: 1.1em;
}

/*新闻类目选项卡的切换样式：鼠标*/
.cateChoose:hover{
    background: #06c;
    color:#fff;
}

/*新闻类目选项卡的切换样式：键盘*/
.cateChoose:focus{
    background: #06c;
    color:#fff;
}

.cateChoose::after {
      content: "";
      display: table;
      clear: both;
    }

/*新闻类目选项卡的切换样式：点击后无边框*/
button{
    outline: none;
}

/*新闻类目内容*/
.tabContent{
    clear: both;
    margin: 2% 8% ;
    overflow: hidden;
    height: 100%;
}

/*新闻类目内容：配合js的显示功能*/
.show{
    display: block;
}

/*新闻类目内容：配合js的隐藏功能*/
.hidden{
    display: none;
}
```


