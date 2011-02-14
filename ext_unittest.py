#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010 (´・ω・｀)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest

"""
ext_unittest はインスタンスの __dict__ で取得可能な属性を解析し、
オブジェクトの等価性を評価する拡張ユニットテストライブラリです。
unittest.TestCase クラスを継承しているため、従来のユニットテストコードを継続して
利用することが可能です。
"""
class TestCase(unittest.TestCase):
    
    def __create_joined_attributes_from_dict(self, dict):
        return ';'.join([unicode(value) for value in dict.values()])
    
    def __create_message(self, obj):
        """
        オブジェクトを適切な文字列表現に変換する。
        'ClassName (properties...)'
        """
        if hasattr(obj, '__dict__'):
            attributes = self.__create_joined_attributes_from_dict(obj.__dict__)
            return '%s (%s)' % (obj.__class__.__name__, attributes)
        if type(obj) is object:
            return 'object ()'
        if type(obj) is bool:
            return '1' if obj else '0'
        return str(obj)
    
    def assertEqualForProperties(self, first, second, label=None):
        """
        オブジェクト first, second のクラスまたは属性値が等しくない場合、テスト失敗を通知する。
        
        first, second を __create_message() メソッドにより、クラス名とプロパティ値の
        文字列表現に変換する。さらに、これらの文字列を TestCase.assertEqual() で検証する。
        """
        l = label + ': ' if label else ''
        f = self.__create_message(first)
        s = self.__create_message(second)
        msg = '%s%s != %s' % (l, f, s)
        super(TestCase, self).assertEqual(f, s, msg)
    
    def assertNotEqualForProperties(self, first, second, label=None):
        """
        オブジェクト first, second のクラスと属性値が等しい場合、テスト失敗を通知する。
        """
        l = label + ': ' if label else ''
        f = self.__create_message(first)
        s = self.__create_message(second)
        msg = '%s%s == %s' % (l, f, s)
        super(TestCase, self).assertNotEqual(f, s, msg)
   
    def assertFalseForObject(self, obj, label=None):
        """
        obj が真の場合、テスト失敗を通知する。
        オブジェクトの属性値付きのエラーメッセージを生成する。
        
        assertFalseForObject: ClassName (propeties) is not False
        """
        l = label if label else 'assertFalseForObject'
        expr = self.__create_message(obj) if obj else obj
        msg = '%s: %s is not False' % (l, expr)
        super(TestCase, self).assertFalse(obj, msg)
        
    
"""
__PrivateTestCase
"""
class __PrivateTestCase(unittest.TestCase):
    def runTest(self):
        pass
        
_private_test_case = __PrivateTestCase()

"""
関数
"""
def assert_(expr, msg=None):
    _private_test_case.assert_(expr, msg)
def failUnless(expr, msg=None):
    _private_test_case.failUnless(expr, msg)
def assertTrue(expr, msg=None):
    _private_test_case.assertTrue(expr, msg)
    
def assertEqual(first, second, msg=None):
    _private_test_case.assertEqual(first, second, msg)
def failUnlessEqual(first, second, msg=None):
    _private_test_case.failUnlessEqual(first, second, msg)

def assertNotEqual(first, second, msg=None):
    _private_test_case.assertNotEqual(first, second, msg)
def failIfEqual(first, second, msg=None):
    _private_test_case.failIfEqual(first, second, msg)

def assertAlmostEqual(first, second, places=7, msg=None):
    _private_test_case.assertAlmostEqual(first, second, places, msg)
def failUnlessAlmostEqual(first, second, places=7, msg=None):
    _private_test_case.failUnlessAlmostEqual(first, second, places, msg)

def assertNotAlmostEqual(first, second, places=7, msg=None):
    _private_test_case.assertNotAlmostEqual(first, second, places, msg)
def failIfAlmostEqual(first, second, places=7, msg=None):
    _private_test_case.failIfAlmostEqual(first, second, places, msg)

def assertRaises(exception, callable, *args, **kwargs):
    _private_test_case.assertRaises(exception, callable, *args, **kwargs)
def failUnlessRaises(exception, callable, *args):
    _private_test_case.failUnlessRaises(exception, callable, *args)

def failIf(expr, msg=None):
    _private_test_case.failIf(expr, msg)
def assertFalse(expr, msg=None):
    _private_test_case.assertFalse(expr, msg)

def fail(msg=None):
    _private_test_case.fail(msg)
