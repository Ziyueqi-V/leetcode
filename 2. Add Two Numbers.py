# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表(实例化一个节点，但是赋给了两个变量，这保证了计算过程中，res在变化，但是最后给出结果时，head未变)
        head = res = ListNode()
        # 设置节点累加值和进位值均为0
        val = carry = 0
        # 当三者有一个不为空时继续循环
        # 任意一个链表不空，加法没有进行完
        # 进位值不空，向最高位的进位没有写进去，例如：“9+9=18”，产生的位数比原来的数多一位，也要记录到结果中
        while carry or l1 or l2:
            # 因为结果节点值需要时两个节点值相加再加上一个进位值（也就是三个数相加），所以此时可以理解为把结果节点值清空，然后先加进位值，即val = 0 + carry
            val = carry
            # 因为是逆序排列的，所以有值就加，为空就是加完了（节点值为0的情况不是空），两个链表都一样
            if l1:
                # 累计值累加上链表1中的节点值
                val = l1.val + val
                # 更新链表状态，指向下一节点
                l1 = l1.next
            if l2:
                # 累计值累加上链表2中的节点值
                val = l2.val + val
                # 更新链表状态，指向下一节点
                l2 = l2.next
            # 累计进行完毕（3个数加完了），进行累计值的处理
            # 得出新一轮的进位值
            carry = val // 10
            # 得到新的结果的当前节点值（去掉进位，因为已经记录了，留下一位的数字）
            val = val % 10

            # 实现链表的连接
            # 把结果的单个位数的值放入节点，进行实例化，并作为res的下一节点
            res.next = ListNode(val)
            # 把res进行更新，res原来是值为0，下一节点为空的一个节点，现在更新，指向刚加的节点
            res = res.next
        # 这里直接返回的是head的下一个节点，初始化时存在的前导零很自然被跳过了，刚好符合要求
        return head.next
