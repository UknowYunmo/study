# 어제 문제를 바꿔서 풀어보려고 했는데 그냥 그렇게 푸는 게 그 답이었다.
# 10번째 손님이 방 고르는거랑 20번째 손님이 방 고르는거랑 연관될 필요가 없음ㅠ
# 아쉽지만 다른 문제나 풀자

"""
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데,
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
첫 번째 줄에 Test case의 수 T가 주어진다.
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)
"""
floor_zero=[]
T=int(input())

for x in range(0,T):
    K=int(input())
    N=int(input())
    for i in range(0, 14):
        floor_zero.append(i+1)
    for k in range(0,K):
        for i in range(1,14):
            floor_zero[i]=floor_zero[i-1]+floor_zero[i]
    print(floor_zero[N-1])
    del floor_zero[:]

# 원래는 0층은 1씩 확정적으로 늘어나니까 floor_zero 배열 만들고, 다른 배열을 또 하나 만들어서
# floor_zero를 계속 더한 값을 원소로 하도록 만들려고 했는데, 생각해보니까 i 값이 바뀌기 전에 그 i 값을 더할 수 있으니
# 그럴 필요가 없다는 걸 깨달음. 대신 1호는 항상 1이기 때문에 1층 이상부터는 1호 값은 바뀌지 않도록 (1,14)로 선언해서 건드리지 않도록 한게 유효했던듯
