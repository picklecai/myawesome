## 绝对路径和相对路径  

[HTML绝对路径和相对路径](http://www.adminwang.com/html/35.html)

原先的写法：  

```
	    <div class="nav_li" align="center" >
	      <ul>
	        <li><a href="/">开始记录</a></li>
	        <li><a href="history.html">查看历史</a></li>
	        <li><a href="baby.html">宝宝信息</a></li>
	        <li><a href="email.html">发送邮箱</a></li>
	        <li><a href="camera.html">宝宝拍照</a></li>
	        </li>
	      </ul>
	    </div>
```

修改后的写法：  

```
	    <div class="nav_li" align="center" >
	      <ul>
	        <li><a href="/">开始记录</a></li>
	        <li><a href="../history.html">查看历史</a></li>
	        <li><a href="../baby.html">宝宝信息</a></li>
	        <li><a href="../email.html">发送邮箱</a></li>
	        <li><a href="../camera.html">宝宝拍照</a></li>
	        </li>
	      </ul>
	    </div>
```

原先写法的问题是：如果离开了home页，其他页的打开地址是：`host/本页面.html/目标页面.html`，而不是预定的`host/目标页面.html`

修改后不再有这个问题。


