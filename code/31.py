# 문제 31 : 파이썬 자료형의 복잡도
# 다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌 것은?
"""
1) l[i]
2) l.append(5)
3) l[a:b]      (O)
4) l.pop()
5) l.clear()
"""

# 1) index = O(1)
# 2) append = O(1)
# 3) Slice = O(b-a)
# 4) pop = O(1)
# 5) clear = O(1)
