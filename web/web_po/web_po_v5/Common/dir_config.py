#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


# print(os.path.abspath(__file__))  C:\Users\lipan\PycharmProjects\python_lemon\web\web_po\web_po_v5\Common\dir_config.py
# print(os.getcwd())  C:\Users\lipan\PycharmProjects\python_lemon\web\web_po\web_po_v5\Common

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
print(screenshot_dir)  # C:\Users\lipan\PycharmProjects\python_lemon\web\web_po\web_po_v5\Outputs/screenshots