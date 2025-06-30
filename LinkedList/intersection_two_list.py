# Brute Force


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headA:
            cur = headB
            while cur:
                if headA == cur:
                    return headA
                cur = cur.next
            headA = headA.next
        return None


# Hash Set


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        nodeSet = set()
        cur = headA
        while cur:
            nodeSet.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in nodeSet:
                return cur
            cur = cur.next
        return None


# Two Pointers


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
