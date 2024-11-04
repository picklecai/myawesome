# 问题
提醒您注意，我们已经宣布，我们要求在GitHub.com上贡献代码的用户启用双重身份验证（2FA）。您收到此通知是因为您的帐户符合此标准，并将被要求在2024年11月14日00:00（UTC）之前在2FA注册。

## 截止时间

2024年11月14日00:00（UTC）之前

## 官方提示
我可以使用哪些形式的 2FA ？
我们希望您能尽可能地获得最无缝的 2FA 体验，因此您可以选择以下一个或多个选项:

- 安全密钥

- GitHub移动版

- 身份验证器应用程序（TOTP）

- 短信（SMS）

  

  您应该设置至少其中两个选项，以确保您始终能够访问您的帐户。前往https://github.com/settings/security 注册更多2FA方法。



# 解决尝试

【某教程】
教程地址：https://cloud.tencent.com/developer/news/1302099

>  Github提供了四种2FA方式：
>
> - AuthenticatorApp(今天要分享的就是这个)
> - SMS/Text message: 由于SMS不支持国内手机号, 不可用
> - Security keys: 由于该方式需要物理设备等，不好
> - Github Mobile: 该方式也没问题(文末有下载方法)

## 问题：不知道什么是Authenticator App
问kimi，究竟这是什么APP？

>  问：Use an authenticator app or browser extension to scan.
> github的2FA验证提到使用authenticator app ，请问这是什么APP，在哪里可以获得它？

>  答：
> 对于GitHub的2FA验证，推荐使用基于时间的一次性密码（TOTP）应用程序，这类应用程序可以自动生成一个在一定时间后会变化的认证码。以下是一些常用的TOTP应用程序，你可以根据自己的需要选择：
>
> 1. Microsoft Authenticator：微软提供的认证器应用，支持安卓和苹果设备，可以在国内外的应用商店中下载到。
>
> 2. Google Authenticator：谷歌提供的认证器应用，也是广泛使用的TOTP应用程序之一。
>
> 3. Authy：一个支持云同步的2FA应用，可以在多个设备间同步你的2FA密钥。
>
> 4. 1Password：一个集成密码管理和2FA功能的应用程序。你可以在手机或桌面上下载这些TOTP应用程序之一。安装后，按照GitHub的设置指引操作，扫描GitHub提供的QR码来添加你的账户，并使用生成的动态验证码进行登录验证。这些应用程序都能在GitHub的官方文档中找到更多详细信息和配置步骤。

## 尝试一：
以上四个APP，在华为应用市场只能看到这个Authenticator（微软的），下载后不能使用，只能点拒绝，然后关闭。

## 尝试二：
网上下了1Password（下载地址：https://www.jb51.net/softs/248030.html），注册后添加帐户，刚开始没找到扫描二维码的地方，后来添加一次性密码，用出现的扫描二维码功能扫描Github提供的二维码，显示：内部错误，检测二维码失败。

根据https://zhuanlan.zhihu.com/p/514720664，重启手机，关闭权限（只有相机和位置两个权限，没有存储），再打开。再次扫描，仍然显示如上信息。

## 尝试三：
[GitHub强制要求开启两步验证了，但是1password要收费，怎么办？ - java技术圈 - java技术社区](http://www.itsharecircle.com/articles/4089)
这里说，可以使用chrome的一个叫做Authenticator的插件。

重新启用lantern，安装这个插件，成功了。

2024.11.04