# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function：
测试场景：
1.支付成功
2，支付失败
3，超时，成功
4，超时，失败
5，超时，超时
"""

import unittest
from unittest import mock

from interface.API_Mock import payment


class PaymentTest(unittest.TestCase):

    def setUp(self):
        self.pay = payment.Payment()

    def test_success(self):
        """
        测试支付成功
        :return:
        """
        # 注意mock对象调用方法的时候不要给圆括号
        self.pay.requestOutofSystem = mock.Mock(return_value=200)
        resp = self.pay.doPay(user_id=1, card_num='56788654', amount='1000')
        self.assertEqual('success', resp)
        self.pay.requestOutofSystem.assert_called_once()

    def test_fail(self):
        """
        测试支付失败
        :return:
        """
        self.pay.requestOutofSystem = mock.Mock(return_value=500)
        resp = self.pay.doPay(user_id=2, card_num='56788654', amount='10000')
        self.assertEqual('fail', resp)

    def test_retry_success(self):
        """
        重试之后成功
        :return:
        """
        self.pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])
        resp = self.pay.doPay(user_id=3, card_num='56788655', amount='100000')
        self.assertEqual('success', resp)
        print("调用的次数",self.pay.requestOutofSystem.call_count)
        print("调用的参数",self.pay.requestOutofSystem.call_args)

    def test_retry_fail(self):
        """
        重试之后失败
        :return:
        """
        self.pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = self.pay.doPay(user_id=4, card_num='567886555', amount='1000000')
        self.assertEqual('fail', resp)

    def test_retry_retry(self):
        """
        重试之后依然超时
        :return:
        """
        self.pay.requestOutofSystem = mock.Mock(side_effect=TimeoutError)
        try:
            resp = self.pay.doPay(user_id=5, card_num='567886555', amount='20000')
        except TimeoutError as e:
            self.assertTrue(e)
