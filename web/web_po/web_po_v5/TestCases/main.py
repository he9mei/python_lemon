#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest

if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_login_pytest_fixture.py"])
    # terminal中的当前路径不在TestCases下,该main文件在TestCases下---可以正常使用该main方法执行TestCases下的用例。

'''
--->pytest -s -v test_login_pytest_fixture.py
如果使用命令行执行，则需要关注当前路径，如果当前路径不在TestCases下，则找不到。
解决方法：-->cd TestCases 然后再执行===解决

总结：
terinal命令行执行,需要确认当前路径，在用例相同路径下；
main.py执行，无需考虑当前路径，main.py文件放在用例相同路径下即可。
'''