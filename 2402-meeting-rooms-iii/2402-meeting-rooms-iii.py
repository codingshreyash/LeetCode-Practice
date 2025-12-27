import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        unused_rooms = list(range(n))
        heapq.heapify(unused_rooms)
        busy_rooms = [] # stores end_time and. room_index
        
       # meeting count per room
        room_counts = [0] * n
        
        for start, end in meetings:
            # frees up room
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(unused_rooms, room_idx)
            
            if unused_rooms:
                # unused room is free
                room_idx = heapq.heappop(unused_rooms)
                heapq.heappush(busy_rooms, (end, room_idx))
            else:
                # need to wait
                earliest_end, room_idx = heapq.heappop(busy_rooms)
                # actual end of previous + original duration
                new_end = earliest_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room_idx))
            
            room_counts[room_idx] += 1
            
        # max meetings
        max_meetings = max(room_counts)
        for i in range(n):
            if room_counts[i] == max_meetings:
                return i