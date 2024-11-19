N = int(input()) # 시험장 수
A = list(map(int, input().split())) # 각 시험장에 있는 응시자 수
B, C = map(int, input().split()) # 총 감독관, 부 감독관이 한 시험장에서 감시할 수 있는 응시자 수
D = 0 # 감독관 수

for i in range(0, N):
    if A[i] <= B:
        D+=1
    elif(A[i] <= B+C):
        D+=2
    else:
        A[i]-=B
        D+=1
        D+=A[i] // C
        if A[i]%C != 0: D+=1

print(D)