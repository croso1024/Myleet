"""
    題意 :
    給定若干會議的時間區間 intervals,其中 intervals[i] = [starti, endi]。
    回傳要讓所有會議都能召開,最少需要幾間會議室。

    一場會議的結束時間到了,那間會議室就可以給下一場用。
    結束時刻與下一場的開始時刻相同,算同一間可以接上,不需要多開一間。

    LeetCode 253 · Medium
    URL : https://leetcode.com/problems/meeting-rooms-ii/
    ※ 此題在 LeetCode 為 Premium 鎖定題。
      題意採用 NeetCode 的通用敘述。
    免費可練 : https://neetcode.io/problems/meeting-schedule-ii

    Example :
    intervals = [[0,30],[5,10],[15,20]] -> 2
    intervals = [[7,10],[2,4]]          -> 1

    Constraint :
    1 <= intervals.length <= 10^4
    0 <= starti < endi <= 10^6

    思路 :

    先思考 , Naive 的做法,先排序 , 排序上採用 先排開始時間由小到大,開始時間相等則結束時間早的在前
    然後開始一間間檢查，同時維護一個 "已經建立的Meeting Room"

    之後開始走訪，維護已經建立的Meeting Room 這件事應該可以再進行排序一次.但變成以結束時間作為排序. 
    每一次看到一間新的 , 由於排序 , 起始時間一定 >= 目前看過的任何一間.
    先從已經開啟的會議室清單中去找 , 結束時間 <= 新一間開始時間的, 找得到就合併並更新已開會議室的清單, 否則就開一間新的會議室. 
    可能的優化是透過 Binary Search 去快速定位可以用的會議室

    第一版解答的時間複雜度 :
    Sorting : O(NlogN) , 之後走訪Room的過程每一次都要去看已經開過的Room , Worse Case為 O(N^2),空間複雜度上,最多要儲存N個已經開的Room , 因此為O(N)

    優化版的方案是為了快速找到已經開啟的會議室中最早結束的那一個. 所以應該可以用 Heap 去處理維護已經開啟的會議室.
    這樣子每一次找到會議室,以及更新的複雜度變為 O(LogN) , 整體時間複雜度降低到 O(NlogN)

    Trade-off :

"""

from heapq import heappop , heappush
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 先進行排序 O(NlogN)
        intervals.sort()

        # 排序完成之後開始走訪,走訪前維護一個可用會議室清單 , 由於 Interval >= 1 , 至少先放一間開好的會議室. 
        opened_meeting_rooms = [intervals[0]] 

        # 開始拜訪每一間會議室. 
        for i in range(1,len(intervals)): 
            room = intervals[i]

            # 每一間會議室,都先找出是否有可合併的會議室。檢查方式是找到任何一間 , 結束時間 <= 新會議開始時間的會議室
            mergeable_room = None 
            for opened_room in opened_meeting_rooms : 
                # 若某一個已經開會議室的結束時間<=新會議室的開始時間 , 就可以合併
                if opened_room[1] <= room[0] : 
                    mergeable_room = opened_room
                    break 
            # 如果找到可合併的 , 就將這間會議室的結束時間改為新會議的結束時間
            if mergeable_room : 
                mergeable_room[1] = room[1] 
            # 如果找不到,就得開一間新的會議室
            else : 
                opened_meeting_rooms.append(room)

        # 最終回傳總共開了幾間會議室        
        return len(opened_meeting_rooms)


# Solution 2 , Min-Heap版本
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 先進行排序 O(NlogN)
        intervals.sort() 

        # 我預期 Heap 只存單一數值 "結束時間" , 因為開始時間不重要.
        min_heap = [] 

        for i in range(len(intervals)): 

            room = intervals[i] 

            # 接著比較 min heap , 如果 min heap 為空或著 min_heap 最小值(結束時間) 沒有 <= 當前開始,才開新的Room
            
            # 如果拿得到結束時間 <= 新會議開始時間的房間,就可以合併. 
            if min_heap and min_heap[0] <= room[0] : 
                # 取出原有的最早結束會議時間 , 更新並丟回 Heap , O(LogN)
                heappop(min_heap) 
                heappush(min_heap , room[1])
            # 如果沒有 room , 才需要開新的
            else : 
                heappush(min_heap,room[1])
        
        return len(min_heap)

if __name__ == "__main__":
    c = Solution()

    # (intervals, 預期, 說明)
    test_set = [
        (
            [[0, 30], [5, 10], [15, 20]],
            2,
            "官方範例",
        ),
        ([[7, 10], [2, 4]], 1, "官方範例"),
        ([[1, 5]], 1, "邊界:只有一場"),
        ([[1, 5], [5, 10]], 1, "結束時刻等於下一場開始"),
        ([[1, 5], [2, 6], [3, 7]], 3, "三場時間重疊"),
        (
            [[1, 10], [2, 3], [4, 5], [6, 7]],
            2,
            "一場較長,三場較短",
        ),
        ([[9, 10], [4, 9], [4, 17]], 2, "輸入未排序"),
        ([[1, 2], [2, 3], [3, 4]], 1, "三場首尾相接"),
        (
            [[0, 30], [5, 10], [15, 20], [5, 15]],
            3,
            "四場會議",
        ),
        ([[13, 15], [1, 13]], 1, "前一場結束時刻等於後一場開始"),
        ([[1, 2], [1, 2], [1, 2]], 3, "三場時間完全相同"),
        ([[8, 10], [1, 3], [2, 6]], 2, "輸入未排序"),
    ]

    for intervals, expected, note in test_set:
        result = c.minMeetingRooms(intervals)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={intervals} | expected={expected} | got={result}")
