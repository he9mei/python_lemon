#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest

if __name__ == "__main__":
    # pytest.main()   # 同命令行-->pytest
    # pytest.main("-s", "-v")   # 执行路径下所有用例
    pytest.main(["-s", "-v", "test_study.py", "-m", "demo"])   # 命令列表(如果命令是空格隔开的，就要写成列表的两个元素)

    # 执行TestCases中的用例
    # pytest.main(["-s", "-v", "test_login_pytest_fixture.py"])
    # 直接执行报错ERROR: file or directory not found: test_login_pytest_fixture.py
    # 需要先切换路径到-->cd test_cases
    # 还是会报错。在 TestCases目录下，新建main.py文件再执行---成功解决



'''
命令执行的写法：
-->pytest -s -v test_study.py -m demo
'''
'''
执行结果中能看到root路径和初始化文件：
rootdir: C:\\Users\\lipan\\PycharmProjects\\python_lemon\\web\\web_po\\web_po_v5, 
configfile: pytest.ini
'''