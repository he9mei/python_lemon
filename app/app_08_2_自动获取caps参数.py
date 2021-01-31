'''

（二）如何动态获取caps参数
封装
1.adb命令---获取设备列表、获取设备的平台版本号
2.指定一个目录：专门用来放要测试的apk文件。---aapt
3.当apk版本有更新的时候，命令行安装新的apk到设备上。
注意：
python执行cmd命令
os.system("")只能执行，无法获取结果数据
需要用subprocess.Popen 具体用法见实例

实例见：app_muti_devices下的threading下的auto_get_caps_info.py

'''