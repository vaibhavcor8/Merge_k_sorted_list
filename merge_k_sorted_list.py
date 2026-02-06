import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
     
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
     
        for i in range(len(lists)):
            if lists[i]:
                
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
    
    # new file