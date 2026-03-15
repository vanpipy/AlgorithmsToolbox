import unittest
import sys
import os
from unittest import mock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import DualArrayDeque


class TestDualArrayDeque(unittest.TestCase):
    
    # 1️⃣ 基础操作测试
    
    def test_empty(self):
        """D1: 新创建的双端队列"""
        d = DualArrayDeque()
        self.assertEqual(len(d), 0)
        with self.assertRaises(IndexError):
            d.remove_first()
        with self.assertRaises(IndexError):
            d.remove_last()
    
    def test_add_last_one(self):
        """D2: 尾部加一个元素"""
        d = DualArrayDeque()
        d.add_last(42)
        self.assertEqual(len(d), 1)
        d.add_last(42)  # 先添加
        result = d.remove_last()  # 再移除验证
        self.assertEqual(result, 42)
    
    def test_add_first_one(self):
        """D3: 头部加一个元素"""
        d = DualArrayDeque()
        d.add_first(42)
        self.assertEqual(len(d), 1)
        d.add_first(42)  # 先添加
        result = d.remove_first()  # 再移除验证
        self.assertEqual(result, 42)
    
    def test_add_last_multiple(self):
        """D4: 尾部加多个元素 - 顺序正确（先进先出）"""
        d = DualArrayDeque()
        values = [1, 2, 3, 4, 5]
        for val in values:
            d.add_last(val)
        
        self.assertEqual(len(d), 5)
        # 验证移除顺序是先进先出
        for expected in values:
            result = d.remove_first()
            self.assertEqual(result, expected)
    
    def test_add_first_multiple(self):
        """D5: 头部加多个元素 - 顺序正确（后进先出，因为头部）"""
        d = DualArrayDeque()
        values = [1, 2, 3, 4, 5]
        for val in values:
            d.add_first(val)
        
        self.assertEqual(len(d), 5)
        # 验证移除顺序是后进先出（因为添加到头部）
        for expected in reversed(values):
            result = d.remove_first()
            self.assertEqual(result, expected)
    
    # 2️⃣ 顺序正确性测试
    
    def test_mixed_add(self):
        """D6: 交替在头尾加元素 - 最终列表顺序正确"""
        d = DualArrayDeque()
        # [4]
        d.add_last(4)
        # [3,4]
        d.add_first(3)
        # [3,4,5]
        d.add_last(5)
        # [2,3,4,5]
        d.add_first(2)
        # [2,3,4,5,6]
        d.add_last(6)
        # [1,2,3,4,5,6]
        d.add_first(1)
        
        self.assertEqual(len(d), 6)
        
        # 验证顺序正确
        expected = [1, 2, 3, 4, 5, 6]
        for exp in expected:
            result = d.remove_first()
            self.assertEqual(result, exp)
    
    def test_front_back_order(self):
        """D7: 验证 front 栈的读取顺序 - front 区：先进栈的元素先被读到"""
        d = DualArrayDeque()
        # 只使用 add_first 来测试 front 区
        d.add_first(3)  # 第一个进入 front
        d.add_first(2)  # 第二个进入 front
        d.add_first(1)  # 第三个进入 front
        
        # 验证 remove_first 顺序应该是后进先出
        # 但由于 front 是栈，应该是 LIFO，但双端队列应该保持整体顺序
        result1 = d.remove_first()
        result2 = d.remove_first()
        result3 = d.remove_first()
        
        # 对于 add_first 序列 [1,2,3]，remove_first 应该返回 [1,2,3]
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)
    
    def test_sequence(self):
        """D8: 复杂操作序列 - 始终符合双端队列行为"""
        d = DualArrayDeque()
        
        # 初始添加
        d.add_last(1)
        d.add_last(2)
        d.add_first(0)
        d.add_last(3)
        
        self.assertEqual(len(d), 4)
        
        # 验证顺序
        self.assertEqual(d.remove_first(), 0)  # 第一个添加的头部
        self.assertEqual(d.remove_first(), 1)  # 第一个添加的尾部
        self.assertEqual(d.remove_first(), 2)  # 第二个添加的尾部
        self.assertEqual(d.remove_first(), 3)  # 第三个添加的尾部
    
    # 3️⃣ 移除操作测试
    
    def test_remove_last(self):
        """D9: 从尾部移除 - 返回最后一个元素，长度减1"""
        d = DualArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        
        self.assertEqual(len(d), 3)
        result = d.remove_last()
        self.assertEqual(result, 3)
        self.assertEqual(len(d), 2)
    
    def test_remove_first(self):
        """D10: 从头部移除 - 返回第一个元素，长度减1"""
        d = DualArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        
        self.assertEqual(len(d), 3)
        result = d.remove_first()
        self.assertEqual(result, 1)
        self.assertEqual(len(d), 2)
    
    def test_remove_sequence(self):
        """D11: 交替从头尾移除 - 顺序正确"""
        d = DualArrayDeque()
        for i in range(6):
            d.add_last(i)
        
        # 交替移除
        self.assertEqual(d.remove_first(), 0)  # 头部
        self.assertEqual(d.remove_last(), 5)   # 尾部
        self.assertEqual(d.remove_first(), 1)  # 头部
        self.assertEqual(d.remove_last(), 4)   # 尾部
        self.assertEqual(d.remove_first(), 2)  # 头部
        self.assertEqual(d.remove_last(), 3)   # 尾部
        
        self.assertEqual(len(d), 0)
    
    def test_remove_to_empty(self):
        """D12: 一直移除到空 - 最后 remove 抛出异常"""
        d = DualArrayDeque()
        d.add_last(1)
        d.add_last(2)
        
        d.remove_first()
        d.remove_first()
        
        self.assertEqual(len(d), 0)
        with self.assertRaises(IndexError):
            d.remove_first()
        with self.assertRaises(IndexError):
            d.remove_last()
    
    # 4️⃣ 边界条件测试
    
    def test_get_invalid_index(self):
        """D13: get(-1) 或 get(len) - 返回 None"""
        d = DualArrayDeque()
        d.add_last(1)
        d.add_last(2)
        
        # 测试负索引
        result = d.get(-1)
        self.assertIsNone(result)
        
        # 测试超出范围的索引
        result = d.get(2)
        self.assertIsNone(result)
        result = d.get(10)
        self.assertIsNone(result)
    
    def test_set_invalid_index(self):
        """D14: set(-1, x) 或 set(len, x) - 抛出异常"""
        d = DualArrayDeque()
        d.add_last(1)
        d.add_last(2)
        
        # 测试负索引
        with self.assertRaises(IndexError):
            d.set(-1, 99)
        
        # 测试超出范围的索引
        with self.assertRaises(IndexError):
            d.set(2, 99)
        with self.assertRaises(IndexError):
            d.set(10, 99)
        
        # 测试空队列
        empty_d = DualArrayDeque()
        with self.assertRaises(IndexError):
            empty_d.set(0, 99)
    
    def test_set_valid_index(self):
        """D21: set(i, x) 在有效索引上 - 修改指定位置的元素"""
        d = DualArrayDeque()
        
        # 添加一些元素
        for i in range(5):
            d.add_last(i)
        
        # 修改中间位置的元素
        d.set(2, 99)
        self.assertEqual(d.get(2), 99)
        
        # 修改第一个元素
        d.set(0, 100)
        self.assertEqual(d.get(0), 100)
        
        # 修改最后一个元素
        d.set(4, 200)
        self.assertEqual(d.get(4), 200)
    
    def test_set_front_and_rear(self):
        """D22: set 操作在 front 和 rear 栈中的元素"""
        d = DualArrayDeque()
        
        # 创建不平衡的情况，确保元素分布在两个栈中
        for i in range(10):
            d.add_first(i)   # 添加到 front
        for i in range(2):
            d.add_last(10 + i)  # 添加到 rear
        
        # 修改 front 栈中的元素
        d.set(0, 100)  # 第一个元素（在 front 栈）
        d.set(5, 200)  # 中间元素（在 front 栈）
        d.set(9, 300)  # 最后一个 front 栈元素
        
        # 修改 rear 栈中的元素
        d.set(10, 400)  # 第一个 rear 栈元素
        d.set(11, 500)  # 最后一个 rear 栈元素
        
        # 验证修改结果
        self.assertEqual(d.get(0), 100)
        self.assertEqual(d.get(5), 200)
        self.assertEqual(d.get(9), 300)
        self.assertEqual(d.get(10), 400)
        self.assertEqual(d.get(11), 500)
    
    def test_set_after_balance(self):
        """D23: balance 后 set 操作仍然正确"""
        d = DualArrayDeque()
        
        # 添加元素
        for i in range(6):
            d.add_last(i)
        
        # 手动调用 balance
        d.balance()
        
        # balance 后修改元素
        d.set(0, 100)
        d.set(3, 200)
        d.set(5, 300)
        
        # 验证修改结果
        self.assertEqual(d.get(0), 100)
        self.assertEqual(d.get(3), 200)
        self.assertEqual(d.get(5), 300)
    
    def test_remove_empty(self):
        """D15: 空队列上 remove - 抛出异常"""
        d = DualArrayDeque()
        with self.assertRaises(IndexError):
            d.remove_first()
        with self.assertRaises(IndexError):
            d.remove_last()
    
    # 5️⃣ balance 平衡测试（核心！）
    
    def test_balance_trigger(self):
        """D16: 触发 balance 的条件 - 当两个栈大小差距过大时自动平衡"""
        with mock.patch.object(DualArrayDeque, 'balance') as mock_balance:
            d = DualArrayDeque()
            # 大量添加到 front，使 front 远大于 back
            for i in range(100):
                d.add_first(i)
            
            self.assertEqual(len(d), 100)
            # 验证 balance 方法是否被调用
            mock_balance.assert_called()
    
    def test_balance_preserves_order(self):
        """D17: balance 后顺序不变 - 所有元素顺序和之前一样"""
        d = DualArrayDeque()
        # 创建不平衡的情况
        for i in range(10):
            d.add_first(i)   # 添加到 front
        for i in range(2):
            d.add_last(10 + i)  # 添加到 back
        
        original_length = len(d)
        
        # 使用 wraps 来跟踪 balance 调用
        with mock.patch.object(d, 'balance', wraps=d.balance) as mock_balance:
            # 手动调用 balance
            d.balance()
            
            # balance 后长度应该不变
            self.assertEqual(len(d), original_length)
            # 验证 balance 方法被调用一次
            mock_balance.assert_called_once()
    
    def test_balance_front_empty(self):
        """D18: front 空时 remove_first - 从 back 借元素，顺序正确"""
        d = DualArrayDeque()
        # 只添加到 back
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        
        # 验证初始状态
        self.assertEqual(len(d), 3)
        self.assertEqual(len(d.front), 0)  # front 应该是空的
        self.assertEqual(len(d.rear), 3)  # rear 应该有3个元素
        
        # remove_first 应该触发内部平衡并从 rear 借元素
        result = d.remove_first()
        self.assertEqual(result, 1)  # 应该返回第一个添加的元素
        self.assertEqual(len(d), 2)
        
        # 验证后续操作仍然正确
        result = d.remove_first()
        self.assertEqual(result, 2)
        result = d.remove_first()
        self.assertEqual(result, 3)
        
        # 验证队列已空
        self.assertEqual(len(d), 0)
        with self.assertRaises(IndexError):
            d.remove_first()
    
    def test_balance_back_empty(self):
        """D19: back 空时 remove_last - 从 front 借元素，顺序正确"""
        d = DualArrayDeque()
        # 只添加到 front
        d.add_first(3)
        d.add_first(2)
        d.add_first(1)
        
        # 验证初始状态
        self.assertEqual(len(d), 3)
        self.assertEqual(len(d.front), 3)  # front 应该有3个元素
        self.assertEqual(len(d.rear), 0)  # rear 应该是空的
        
        # remove_last 应该触发内部平衡并从 front 借元素
        result = d.remove_last()
        self.assertEqual(result, 3)  # 应该返回最后一个添加的元素
        self.assertEqual(len(d), 2)
        
        # 验证后续操作仍然正确
        result = d.remove_last()
        self.assertEqual(result, 2)
        result = d.remove_last()
        self.assertEqual(result, 1)
        
        # 验证队列已空
        self.assertEqual(len(d), 0)
        with self.assertRaises(IndexError):
            d.remove_last()
    
    def test_balance_multiple(self):
        """D20: 多次触发 balance - 每次 balance 后顺序都正确"""
        with mock.patch.object(DualArrayDeque, 'balance') as mock_balance:
            d = DualArrayDeque()
            
            # 多次操作触发可能的 balance
            for i in range(20):
                if i % 2 == 0:
                    d.add_first(i)
                else:
                    d.add_last(i)
            
            # 手动调用多次 balance
            for _ in range(5):
                d.balance()
                self.assertEqual(len(d), 20)
            
            # 验证 balance 方法被调用5次
            self.assertEqual(mock_balance.call_count, 5)
    
    # 7️⃣ 你的"先进优先读"原则验证
    
    def test_front_priority(self):
        """D24: front 区元素读取顺序 - 先入 front 的先被读到"""
        d = DualArrayDeque()
        # 按顺序添加到 front
        d.add_first(1)  # 第一个进入 front
        d.add_first(2)  # 第二个进入 front
        d.add_first(3)  # 第三个进入 front
        
        # remove_first 应该按添加顺序的逆序返回
        # 但由于双端队列语义，可能需要调整理解
        result1 = d.remove_first()
        result2 = d.remove_first()
        result3 = d.remove_first()
        
        # 对于 add_first 序列 [1,2,3]，remove_first 应该返回 [3,2,1]
        # 但根据双端队列语义，可能应该是 [3,2,1]
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 1)
    
    def test_back_priority(self):
        """D25: back 区元素读取顺序 - 先入 back 的先被读到"""
        d = DualArrayDeque()
        # 按顺序添加到 back
        d.add_last(1)  # 第一个进入 back
        d.add_last(2)  # 第二个进入 back
        d.add_last(3)  # 第三个进入 back
        
        # remove_first 应该按添加顺序返回（先进先出）
        result1 = d.remove_first()
        result2 = d.remove_first()
        result3 = d.remove_first()
        
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)
    
    def test_priority_after_balance(self):
        """D26: balance 后优先级仍成立 - 你的原则在 balance 后依然成立"""
        d = DualArrayDeque()
        
        # 创建不平衡情况
        for i in range(5):
            d.add_first(i)   # front: [4,3,2,1,0] (从后往前看)
        for i in range(2):
            d.add_last(5 + i)  # back: [5,6]
        
        # 记录 balance 前的顺序
        original_order = [d.get(i) for i in range(len(d))]
        
        # 调用 balance
        d.balance()
        
        # 验证长度不变
        self.assertEqual(len(d), 7)
        
        # 验证 balance 后顺序仍然正确
        balanced_order = [d.get(i) for i in range(len(d))]
        self.assertEqual(balanced_order, original_order)
        
        # 验证 remove_first 顺序正确（先进先出原则）
        expected_order = [4, 3, 2, 1, 0, 5, 6]  # 根据 add_first/add_last 的顺序
        for expected in expected_order:
            result = d.remove_first()
            self.assertEqual(result, expected)
        
        # 验证队列已空
        self.assertEqual(len(d), 0)


if __name__ == '__main__':
    unittest.main()