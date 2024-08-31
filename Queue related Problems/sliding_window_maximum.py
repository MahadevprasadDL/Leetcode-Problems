 # question number 239

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        result = []
        dq = deque()

        l, r = 0, 0

        while r < n:
            
            while dq and nums[r] >= nums[dq[-1]]:
                dq.pop()

            dq.append(r)

            
            if dq[0] < l:
                dq.popleft()

    
            if r + 1 >= k:
                result.append(nums[dq[0]])
                l += 1

            r += 1

        return result
