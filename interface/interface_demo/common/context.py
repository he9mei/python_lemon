#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 管理上下文
# 封装正则替换方法
import configparser
import re
from interface.interface_demo.common.config import config_handler


class Context:
    loan_id = None  # 标的ID，是变化的，需要加标成功后，到数据库查

    @classmethod
    # @staticmethod  这里设置成类方法或者静态方法，是为了不用实例化就能用。直接放在类外面也可以。
    def replace(cls, data):
        p = "#(.*?)#"
        pattern = re.compile(p)
        while pattern.search(data):
            key = pattern.search(data).group(1)

            try:
                value = config_handler.config_parser.get('userdata', key)
            # 如果EXCEL中匹配到的正则，在配置文件中没有找到对应的数据，则重新取值
            except configparser.NoOptionError as e:
                if hasattr(Context, key):
                    value = getattr(Context, key)
                # raise e

            data = pattern.sub(value, data, count=1)
        print(data)
        return data


if __name__ == '__main__':   # 反射
    # 获取类属性的值
    value = getattr(Context, 'loan_id')
    print(value)
    # 设置类属性的值
    setattr(Context,'loan_id', '123')
    value = getattr(Context, 'loan_id')
    print(value)