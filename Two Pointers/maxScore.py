class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftsum = 0
        for i in range (k): # calculate sum where all cards on the left side
            leftsum += cardPoints[i]
        rightsum = 0
        rightindex = n # pointer for the right cards
        ans = leftsum
         # Now I have to shrink down the window by taking out the elements and this element is k-1th index, after that k-2th index and vice varca
        for leftIndex in range (k-1, -1, -1) : # this is the function for (i = k - 1; i >= 0; i--)
            leftsum -= cardPoints[leftIndex] # transition between choices
            rightindex -= 1
            rightsum += cardPoints[rightindex]
            
            ans = max(ans, leftsum + rightsum)
        return ans