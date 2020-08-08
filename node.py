# 遍历链表
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval =  None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # 开头插入数据
    def AtBagining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    # 末尾插入数据
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    # 在两个节点之间插入
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("the mentioned node is adbsent")
            return
            
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    

class Node1:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Slinked:
    def __init__(self):
        self.head = None

    def Atbagining(self, data_in):
        NewNode = Node1(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # 从链表中删除项目
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal =  None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.nextval

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data)
            printval = printval.next


llist = Slinked()
llist.Atbagining("Mon")
llist.Atbagining("Tue")
llist.Atbagining("Wed")
llist.Atbagining("Thu")
llist.Atbagining("Fri")
llist.RemoveNode("Fri")
llist.LListprint()




# list = SLinkedList()
# list.headval = Node("Monday")
# e2 = Node("Tuesday")
# e3 = Node("Wednesday")


# list.headval.nextval = e2
# e2.nextval = e3

# list.AtBagining("Sunday")
# list.AtEnd("Thursday")

# list.Inbetween(list.headval.nextval, "Friday")

# list.listprint()
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 非递归算法
    def _mergeTwoLists(self, l1, l2):
        # 建立两个值为-1的头指针，一个用来保存
        head = dummy = ListNode(-1)
        # 当两个链表都非空
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        # 当l1空了l2没空
        if l1:
            # 直接接l1剩下的
            head.next = l1
        # 当l2空了l1没空
        if l2:
            # 直接接l2剩下的
            head.next = l2
        # 返回头指针指向的头节点
        return dummy.next

    # 递归算法
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists([1,2,4], [1,3,4]))
