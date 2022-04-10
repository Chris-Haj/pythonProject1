from typing import List, Optional
from abc import ABC, abstractmethod


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def rotate(self, nums, k):
        if k % len(nums) == 0:
            return
        moves = k % len(nums)
        while moves > 0:
            temp = nums[len(nums) - 1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp
            moves -= 1

    def moveZeroes(self, nums) -> None:
        cur=0
        for i in range(len(nums)):
            i=cur
            cur+=1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                cur=i
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        h = head
        while h:
            nodes.append(h)
            h=h.next
        prev = len(nodes) - n - 1
        h = nodes[prev]
        nex = h.next
        h.next = nex.next
        return head


