# opencv

又来做python挑战了。忘记了hugefile这对用户名密码的事情，冤枉了半天系统和chrome。还好后来一个网址一个网址地输入时发现了这一点。  

两幅图融合，用pillow没啥思路。搜索突然发现人家提opencv。于是装来用用看。刚刚打开一个文件就喜欢它了——随便一幅图，鼠标到哪里，哪里的坐标值和RGB就都有了，多帅啊！

[OpenCV学习笔记（Python） - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1178878)

[Python各类图像库的图片读写方式总结 - Madcola - 博客园](https://www.cnblogs.com/skyfsm/p/8276501.html)

[openCV—Python(6)—— 图像算数与逻辑运算 - jnulzl的专栏 - CSDN博客](https://blog.csdn.net/jnulzl/article/details/47129887)

## 打开图像  

[OpenCV Python教程（1、图像的载入、显示和保存） - vv鱼儿vv - 博客园](https://www.cnblogs.com/zangyu/p/5802142.html)

```
import cv2, os

im = cv2.imread(os.path.dirname(os.getcwd()) + '/files/cave.jpg')
cv2.namedWindow('Window')
cv2.imshow('Window', im)
cv2.waitKey(0)
```
> 如果不添最后一句，在IDLE中执行窗口直接无响应。在命令行中执行的话，则是一闪而过。

## 融合图像  

[Python-OpenCV 图像叠加or图像混合加权（cv2.addWeighted） - zh_jessica的博客 - CSDN博客](https://blog.csdn.net/zh_jessica/article/details/77992578)

特意找了两幅大小相同，格式相同的图片。

```
import cv2, os

img1 = cv2.imread(os.path.dirname(os.getcwd()) + '/files/eggs.jpg')
img2 = cv2.imread(os.path.dirname(os.getcwd()) + '/files/sea.jpg')
img_mix = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.namedWindow('img1')
cv2.namedWindow('img2')
cv2.namedWindow('img_mix')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img_mix', img_mix)

cv2.imwrite(os.path.dirname(os.getcwd()) + '/files/seaegg.jpg', img_mix)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

其中系数是alpha值，越大的越不透明。


### 图像相加  

[OpenCV-Python：图像的算数操作 – WTF Daily Blog](http://blog.topspeedsnail.com/archives/2098)

用`cv2.add()`可以直接相加，alpha不变。

```
import cv2, os

img1 = cv2.imread(os.path.dirname(os.getcwd()) + '/files/eggs.jpg')
img2 = cv2.imread(os.path.dirname(os.getcwd()) + '/files/sea.jpg')
img_add = cv2.add(img1, img2)
img_mix2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imwrite(os.path.dirname(os.getcwd()) + '/files/seaegg_add.jpg', img_add)
cv2.imwrite(os.path.dirname(os.getcwd()) + '/files/seaegg_mix.jpg', img_mix2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
两幅图像对比比较明显。相加的都是饱和的，而融合的则比较透明。  




