import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap: 
            print(0)
            continue
        else:
            print(heapq.heappop(heap)[1])
            continue
    heapq.heappush(heap,(abs(x),x))