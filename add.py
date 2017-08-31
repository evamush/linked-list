class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        resultNode=None
    
        add=0
        while True:
            if l1.val==-1:
                l1.val=0
            if l2.val==-1:
                l2.val=0

            tSum=(l1.val+l2.val+add)%10
            add=(l1.val+l2.val+add)/10
            listn=ListNode(tSum)

            if resultNode==None:
                resultNode=listn
                flagNode=resultNode
            else:
                flagNode.next=listn
                flagNode=flagNode.next


            if l1.next!=None:
                l1=l1.next
            else:
                l1.val=-1

            if l2.next!=None:
                l2=l2.next
            else:
                l2.val=-1
            
            if l1.val == -1 and l2.val == -1:
                break


        return resultNode

if __name__ == '__main__':
    print "----------------- start -----------------"
    
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3
    
    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3
    
    l3_1 = Solution().addTwoNumbers(l1_1,l2_1)
    while l3_1 != None:
        print l3_1.val
        l3_1 = l3_1.next



