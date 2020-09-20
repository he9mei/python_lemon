'''
上传操作
windows弹框上传，selenium无法对其操作（selenium只能对网页操作，貌似也能完成部分Android系统操作）
.pywin32这个库，实现与Windows系统的连接

上传需要的步骤：
进入上传选择windows框---输入文件名---点击打开按钮上传

1.元素定位
如何识别windows框中的输入框和上传按钮？使用工具WinSpy--64位
自己下载：https://sourceforge.net/projects/winspyex/files/latest/download
下载后，解压，点击WinSpy64.exe或者WinSpy32.exe，即可打开WinSpy定位框。可以发送快捷方式到桌面。
拖动左上角的圆形图标，来确认要定位的元素位置。然后查看相关信息。

接下来讲了WinSpy工具的定位方式，主要是通过text和class来定位，属于绝对路径定位。
切换到“windows“tab下可以看到子窗口、兄弟窗口、父窗口。
class是不会变的；title可能会变，不同浏览器打开的可能标题不同。我们这里就是用class来定位的。

实操：
以百度上传为例
首先找到文件名输入框的class是Edit
Edit
然后找到祖先，定位最外层框，title是请选择文件/文件夹，class是#32770
然后切回到文件名输入框，去“windows”tab下找到文件名输入框的父元素，点击即可切换到父元素的class属性
ComboBox---ComboBoxEx32---#32770
那文件名输入框的元素定位关系就是：Edit---ComboBox---ComboBoxEx32---#32770
再看打开按钮的元素定位：Button---#32770

2.安装pywin32 (安装后重启电脑，否则可能识别不了)
安装教程：https://www.cnblogs.com/yjlch1016/p/8469429.html
Python3.8不能直接使用pip安装，手动按安装。
下载地址 https://github.com/mhammond/pywin32/ ---most recent release---pywin32-228.win-amd64-py3.8.exe
安装完成后，pycharm---terminal--->import win32gui (还是找不到，但是cmd能找到)
解决：
File-->Settings-->Project Interpreter-->add解释器，选择Python安装目录的Python.exe文件
'''

import win32gui
import win32con

# edit - combox - comboBoxEx32 - #32770


# 我这里是百度网盘验证的，不需要浏览器，所以去掉了浏览器的传入
def upload(file_path):
    title = '请选择文件/文件夹'

    # 找元素
    # 一级窗口"#32770","请选择文件/文件夹"
    dialog = win32gui.FindWindow("#32770", title)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)    # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "存入百度网盘")   # 二级

    # 往编辑当中，输入文件路径 。
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)    # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)    # 点击打开按钮


upload("D:\\Program Files\\Python38\\chromedriver.exe")
# 绝对路径\要写成\\
# 执行这个函数的前提是，先打开上传框
# 验证：先打开百度网盘输入框，再执行这个函数，结果上传成功！
