"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit
 of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there
 are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
"""
from bisect import bisect_right


def job_scheduling(start_times, end_times, profits):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    sorted_end_times = [x[1] for x in jobs]
    n = len(jobs)

    dp = [0] * n
    dp[0] = jobs[0][2]

    for i in range(1, n):
        current_start, _, current_profit = jobs[i]
        # Find the latest job that finishes before the current job starts
        j = bisect_right(sorted_end_times, current_start) - 1
        if j >= 0:
            current_profit += dp[j]

        dp[i] = max(current_profit, dp[i - 1])

    return dp[-1]


# startTime = [1, 2, 3, 4, 6]
# endTime = [3, 5, 10, 6, 9]
# profit = [20, 20, 100, 70, 60]
#
# startTime = [1, 1, 1]
# endTime = [2, 3, 4]
# profit = [5, 6, 4]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50, 10, 40, 70]

print(job_scheduling(startTime, endTime, profit))
