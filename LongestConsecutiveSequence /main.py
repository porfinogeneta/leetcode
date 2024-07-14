def longestConsecutive(nums):
    mxSeq = 1
    ns = set(nums)
    for i in ns:
        hSeq = 1
        while (i + hSeq) in ns:
            hSeq += 1
        max(hSeq, mxSeq)
    return mxSeq
    # ns = set(nums)
    # mx_seq = 0
    # for i in ns:
    #     # if there is no previous number, the sequence begins
    #     if (i - 1) not in ns:
    #         help_seq = 0
    #         while (i + help_seq) in ns:
    #             help_seq += 1
    #         # switch max sequence
    #         mx_seq = max(mx_seq, help_seq)
    # return mx_seq



if __name__ == '__main__':
    print(longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))

