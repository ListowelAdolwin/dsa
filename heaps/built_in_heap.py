"""There is a built in python heap that can be used to ease work
It is contained in the heapq module
It is able to convert a list into a heap

Should-know methods;
1. heapq.heapify(listname); converts a list to a heap
2. heapq.heappop(heapname); removes the top value while maintaining the heap properties
3. heapq.heappush(heapname, value); adds a value to the heap while maintaining the heap properties
4.heapq.nlargest(n, heapname); returns the top n largest elements of the heap
4. heapq.nsmallest(n, heapname); returns the top n smallest elements of the heap
"""

import heapq

nums = [3, 43, 23, 4, 0, 13, 9]

heapq.heapify(nums)
heapq.heappush(nums, 342)
heapq.heappush(nums, 21)
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

print(nums)
