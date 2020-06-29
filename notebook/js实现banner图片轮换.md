# js实现banner图片轮换

这个类似于教材上的图片集。所以照着教材《JavaScript DOM编程艺术（第二版）》，也做出来了。



最后成果：

```
# js部分比较简单

function showPic(whichpic)
{
    var source = whichpic.getAttribute("href");
    var placeholder = document.getElementById("placeholder");
    placeholder.setAttribute("src", source);
}
```



```
# html部分

<div class="banner">
    <img id="placeholder" src="{% static '/images/hills.jpg' %} " class="banner" />
    {% include 'nav.html' %}
    <div class="bannerItem">
        <a href="{% static '/images/hills.jpg' %}" onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
        <a href="{% static '/images/stone.jpg' %}" onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
        <a href="{% static '/images/sea.jpg' %}"   onmouseover="showPic(this); return false;" onclick="return false;" >·</a></li>
    </div>            
</div>
```



```
# css部分

/*index页面banner轮播图*/
.banner{
    width: 100%;
    height: 450px;/**/
    position: relative;
}

.banner a{
    color: #fff;
}

/* 轮播图的切换按钮 */
.bannerItem {
    font-weight: bold;
    font-size: 3em;
    position: absolute;
    left:45%;
    bottom: 5%;
}
```


