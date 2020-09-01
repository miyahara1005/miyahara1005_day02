# 3. リスト内の特定の要素の数を調べたい！
balls = ['red', 'red', 'blue', 'red']

print(balls.count('red')) #3
print(balls.count('blue')) #1

# Q. これはどうなる？
print(balls.count('yellow')) #0

# 4.要素は全部で何個ある？
scores = [33, 10, 99]
print(len(scores)) # len = length #3

# 5.最大値は？最小値は？
print(max(scores))  #99
print(min(scores))  #10


