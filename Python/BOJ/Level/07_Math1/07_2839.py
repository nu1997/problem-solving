# 설탕 배달

'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
'''


N = int(input())
# 3x + 5y = N
# case 4. 모두 비해당하는가? 초기화.
ans = -1
# case 1. 5의 배수인가? 
if N % 5 == 0:
    ans = N // 5
# case 2. 5의 배수와의 차 계산 후 3의 배수가 되는가?
else:
    # case 3. 위의 케이스에 해당하지 않으며 3의 배수인가? 변수할당 순서로 인해 코드는 순서바꿈
    if N % 3 == 0:
        ans = N // 3
    for i in range(1, N // 5 + 1):
        if (N - 5 * i) % 3 == 0:
            ans = i + (N - 5 * i) // 3
print(ans)



# for - else는 for문 안에 break가 있을 때 break가 작동하지 않을 시 동작을 else문에 적는 것