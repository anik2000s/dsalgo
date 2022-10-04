# Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

'''
AUTHOR: github.com/shreayan98c


PROBLEM STATEMENT:


Given an array of integers histograms representing the histogram's bar histogram where the width of each bar is 1, return 
the area of the largest rectangle in the histogram.


EXAMPLES:

Example 1:

Input: histograms = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: histograms = [2,4]
Output: 4


LOGIC:
1. The h-index is calculated by counting the number of publications for which an author has been cited by other authors
at least that same number of times.

2. First sort the citations list in reverse order.

3. Now traverse the reverse sorted list of the citations - At each index, it will give us a track of how many
publications have been counted yet and what is the number of citations at the current index.

4. If our number of publications that have been counted is greater than the current citation, we will be incrementing
the result by 1 since the current publication has to be included in the h - index.

5. Return the total number of the publications counted in the previous step.


COMPLEXITY:

Time Complexity: O(n), n is the length of the bars in the histogram.
Space Complexity: O(n), one list/stack is created or stored in the memory.
'''
from typing import List


class Solution:

    def largestHistogramArea(self, histogram: List[int]) -> int:
        histogram.append(0)  # the stack maintain the indexes of buildings with ascending height.
        # before adding a new building pop the building who is taller than the new one. 
        stack = [-1]
        ans = 0
        for i in range(len(histogram)):
            while histogram[i] < histogram[stack[-1]]:
                # The building popped out represent the height of a rectangle with the new building as the right 
                # boundary and the current stack top as the left boundary.
                h = histogram[stack.pop()]
                # Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        histogram.pop()
        return ans
