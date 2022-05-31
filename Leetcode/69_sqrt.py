# Runtime: 44 ms, faster than 28.36% of Python3 online submissions for Sqrt(x).
# Memory Usage: 14.4 MB, less than 6.24% of Python3 online submissions for Sqrt(x).

class Solution:
    def mySqrt(self, x: int) -> int:
        # 제곱근 구하기
        # 원리: 8인 경우. 1-8 사이 어딘가의 숫자를 곱하면 8이 나오겠지.
        # 가운데 값을 확인하고, 그 제곱이 x 보다 큰지 안큰지를 따져 반대쪽 절반으로 가거나 날리고,
        #  그런식으로 숫자가 하나만 남을때까지 반복.

        # 근데... 실제로는 그냥 math 패키지 써서 math.sqrt(x) 쓰는게 가장 속편한 방법일듯.
        # 확인할 숫자의 범위
        left = 1
        right = x
        # 0, 1 둘중하나면 본인이 그 제곱근이니.
        if x < 2:
            return x

        while left < right:
            # 가운데값 구하기.
            mid = int((left + right) / 2)
            # 가운데값의 제곱이 x인가?
            if mid ** 2 == x:
                return mid
            # x보다 큰 경우 그 값보다 더 큰 값들은 다 날린다.
            # 즉, right 을 중간값으로 변환
            elif mid ** 2 > x:
                right = mid
            # 더 적으면 정반대. mid 보다 하나 올린다
            else:
                left = mid + 1

        # 여기까지 왔다는건 어차피 정수로 딱 안나온다는 뜻.
        return left - 1
