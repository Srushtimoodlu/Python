# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        min_dist = float('inf')
        max_dist = 0

        while curr.next:
            # Check if current node is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = pos
                    last = pos
                else:
                    min_dist = min(min_dist, pos - last)
                    max_dist = pos - first
                    last = pos

            prev = curr
            curr = curr.next
            pos += 1

        if first == last:
            return [-1, -1]

        return [min_dist, max_dist]
        