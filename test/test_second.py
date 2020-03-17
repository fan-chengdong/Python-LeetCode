#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_second.py    
@Contact :   437918310@qq.com
@License :   (C)Copyright 2019-2020
@Modify Time      @Author           @Version    @Desciption
------------      -------           --------    -----------
2020-02-14 13:32   Fan Chengdong     1.0         None
'''
from typing import List, NamedTuple

class Job(NamedTuple):
    start:int
    end:int
    profit:int

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        N = len(startTime)
        for i in range(N):
            job = Job(start=startTime[i], end=endTime[i], profit=profit[i])
            jobs.append(job)
        jobs.stort(key=lambda j:j.start)

        def make_profit(start:int, i:int):
            if i >= N:
                return 0
            doi_prifit = 0
            jobi = jobs[i]
            if jobi.start >= start:
                doi_prifit = jobi.profit + make_profit(jobi.end,i+1)
            notdoi_profit = make_profit(start,i+1)
            return max(doi_prifit,notdoi_profit)
        return make_profit(start=1, i=0)