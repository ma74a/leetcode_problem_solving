from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prv, cur = None, slow.next
        slow.next = None # disconnect the two halfs
        while cur:
            nex = cur.next
            cur.next = prv
            prv = cur
            cur = nex

        first, second = head, prv
        while second:
            t1, t2 = first.next, second.next
            first.next, second.next = second, t1
            first, second = t1, t2



##########################################################################################

# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        l, r = 0, len(lst) - 1
        while l < r:
            lst[l].next = lst[r]
            l += 1
            if l == r:
                break
            lst[r].next = lst[l]
            r -= 1
        lst[l].next = None