class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        
        #bruteforce
        #Got TLE
        #Time complexity of this is O(n*2) as we are calling max in a for loop

        # individualScores = [0]*len(questions)
        # for i in range(len(questions) - 1, -1, -1):
        #     points, skip = questions[i][0], questions[i][1]
        #     if(len(questions)-1-i > skip ):
        #         individualScores[i] = points + max(individualScores[i+skip+1:])
        #     else:
        #         individualScores[i] = points
        # return max(individualScores)

        #DP solution
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(len(questions) - 1, -1, -1):
            points, skip = questions[i]
            nextQ = i+skip+1
            # Option 1: take this question
            take = points + (dp[nextQ] if nextQ < n else 0)
            # Option 2: Skip this question
            skip = dp[i + 1]
            # Choose the better option
            dp[i] = max(take, skip)
        return dp[0]

        #Time complexity - O(n)