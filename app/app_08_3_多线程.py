'''

（三）多线程
如果要在多个设备同时运行，需要几个chromedriver？
---需要多个。AppiumDesktop也需要启动多个，端口号如4723、4728
补充：
命令行启动appium服务（咱们是通过桌面可视化版本启动的）
（1）进入appium安装目录（小技巧：进入目录后直接在路径位置输入cmd就能跳转到已经进入该路径下的cmd页面）
-->cd C:\Program Files\Appium\resources\app\node_modules\appium\build\lib
(2)执行main.js文件
-->node main.js -p 端口号 （如4723)
# -->mode main.js --help (查看所有参数)---可以看到所有的启动参数
实例(指定端口号和日志路径)
-->node main.js -p 4723 -g E:\\appium_server_4723.log

实例见：app_muti_devices下的threading下的appium_server.py/adb.py/main.py文件。

'''