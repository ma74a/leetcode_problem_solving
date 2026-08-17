from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity -> O(n), space compexity -> O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        cur = head
        nex = head.next
        while nex is not None:
            cur.next = prv
            prv = cur
            cur = nex
            nex = nex.next

        cur.next = prv

        return cur




