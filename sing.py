'''

'''
def chorus(student):
    dpl = [1 for _ in range(len(student))]
    dpr = [1 for _ in range(len(student))]
    dp = [0 for _ in range(len(student))]

    for i in range(len(dpl)):
        for j in range(i):
            if student[i] > student[j]:
                dpl[i] = max(dpl[i], dpl[j]+1)

    for i in range(len(dpr)-1, -1, -1):
        for j in range(i+1, len(dpr)):
            if student[i] > student[j]:
                dpr[i] = max(dpr[i], dpr[j]+1)

    maxk=0
    for k in range(len(dp)):
        dp[k] = dpl[k]+dpr[k]-1

    return max(dp)

while True:
    try:
        N=int(input())
        listStudent=list(map(int,input().split()))
        maxs=chorus(listStudent)
        print(N-maxs)
    except:
        break