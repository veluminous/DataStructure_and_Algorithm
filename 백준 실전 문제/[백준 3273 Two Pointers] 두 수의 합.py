# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 이 문제에 대한 풀이는 두 가지 방법이 있을 것 같다.
# 처음 생각해본 방법은 이진 탐색을 이용한 방법이다. 수열을 오름차순 정렬 후, 왼쪽부터 차례로 left를 이동해가며
# x - nums[left] 값을 이진 탐색으로 찾는 것이다. 시간 복잡도도 Nlog(N)을 보장한다.
# 다만, 이번 문제는 투 포인터 연습으로 풀고 싶어서 접근을 해봤는데, 아이디어가 잘 떠오르지 않아 다른 풀이를 참고했다.
# 투 포인터를 한 쪽에서 증가하는 방향으로만 생각했는데, 양 쪽 방향에서 서로 이동시키니 문제가 쉽게 풀렸다.
# 투 포인터 접근에서는 정렬 수행이 가장 오래 걸려서, 시간 복잡도가 첫 번째 방법과 동일하게 O(Nlog(N))이 된다.

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

cnt = 0  # (ai, aj) 쌍의 갯수
left = 0  # 왼쪽 인덱스
right = n - 1  # 오른쪽 인덱스

nums.sort()  # 오름차순으로 정렬 수행

# 두 포인터가 교차할 때까지
while left < right:
    _sum = nums[left] + nums[right]
    # 두 쌍의 합이 x와 같으면 갯수를 셈
    if _sum == x:
        cnt += 1
    # 두 쌍의 합이 x보다 크면 오른쪽 인덱스를 1 감소시키고, 작으면 왼쪽 인덱스를 1 증가시킴
    if _sum > x:
        right -= 1
        continue
    left += 1

# 갯수 출력
print(cnt)
