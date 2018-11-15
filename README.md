# yltqO6lw
####作者邮箱 ：k2r8hms6v@outlook.com
#####赢商网（http://www.winshang.com/index.html）投票作弊系统

#工作原理
#####投票页面http://m.winshang.com/h5/2018xnfh/index.aspx?from=timeline&isappinstalled=0
#####1：检测是否在手机页面打开
#####2：设置一个cookie，点击选择按钮调用js addvote（）方法实现投票
####作弊原理
####python selenium chrome 模拟投票，chrome以手机打开，清空cookies，直接执行addvote（）方法

#程序运行
#####1:电脑配置PSC环境（python selenium chrome）
#####2：配置阿布云HTTP隧道动态版密钥，使用代理投票

#发布版本
##最新版本 v0.1.0
###单线程界面操作，每次投票多开几次软件，一般是5个，根据IP代理限制决定
###下一版本v0.2.0
###可配置多线程匿名浏览器投票操作
