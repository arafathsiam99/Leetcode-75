class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_dummy = ListNode()
        greater_than_dummy = ListNode()

        less_than_head = less_than_dummy
        greater_than_head = greater_than_dummy

        while head:
            if head.val < x:
                less_than_head.next = head
                less_than_head = less_than_head.next
            else:
                greater_than_head.next = head
                greater_than_head = greater_than_head.next

            head = head.next

        greater_than_head.next = None
        less_than_head.next = greater_than_dummy.next

        return less_than_dummy.next
