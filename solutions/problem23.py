# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        duplicates_hash = {}
        big_list = []
        for list_head in lists:
            while list_head is not None:
                val = list_head.val
                if val not in duplicates_hash:
                    big_list.append(val)
                    duplicates_hash[val] = 1
                else:
                    duplicates_hash[val] += 1
                list_head = list_head.next
        big_list.sort()
        if len(big_list) == 0:
            return None
        head = ListNode(big_list[0])
        save_head = head
        duplicates_hash[big_list[0]] -= 1
        for elem in big_list:
            for _ in range(duplicates_hash[elem]):
                head.next = ListNode(elem)
                head = head.next
        return save_head