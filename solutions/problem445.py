class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def generator(head):
            if head is None:
                return
            yield from generator(head.next)
            yield head.val
        gen_1 = generator(l1)
        gen_2 = generator(l2)
        num_1, num_2 = next(gen_1, None), next(gen_2, None)
        l3 = None
        coming_over = 0
        while num_1 is not None or num_2 is not None:
            val1 = num_1 if num_1 is not None else 0
            val2 = num_2 if num_2 is not None else 0
            
            total = val1 + val2 + coming_over
            coming_over = total // 10
            l3 = ListNode(val = total % 10, next = l3)

            num_1 = next(gen_1, None)
            num_2 = next(gen_2, None)

        if coming_over:
            l3 = ListNode(val=coming_over, next=l3)

        return l3


s = Solution()

node = ListNode(1)
node_2 = ListNode(2)
node.next = node_2
print(s.addTwoNumbers(node, node))