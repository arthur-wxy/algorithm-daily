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