# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    output = ListNode(0)
    tail = output

    
    carry = 0
    c = 0 
    while l1 or l2 or carry:
        a,b,c = 0,0,0
        if l1:
            a = l1.val
        if l2:
            b = l2.val
        add = a+b+carry
        if add>=10:
            c = 1
            add = add - 10
            
        tail.next = ListNode(add)
        tail = tail.next
        carry = c
        
        if l1:
            l1 = l1.next
        else:
            l1=None
        if l2:
            l2=l2.next
        else:
            l2 = None
        
    return output.next


list1 = ListNode(9)
tail = ListNode(9)
list1.next = tail
for i in range(3):
    tail.next = ListNode(9)
    tail = tail.next

list2 = ListNode(9)
t = ListNode(9)
list2.next = t
for i in range(2):
    t.next = ListNode(9)
    t = t.next

c = 0



out = addTwoNumbers(list1,list2)
print()