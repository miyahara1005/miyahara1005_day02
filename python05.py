# 1. 要素を追加したい
members = ['Bob', 'Tom', 'Ken']
print(members)

members.append('John')
print(members)

members.append('Alice')
print(members)

# 2. 要素を並べ替える
scores = [33, 10, 99]
print(scores) #[33, 10, 99]

scores.sort()
print(scores) #[10, 33, 99]

scores.sort(reverse=True)
print(scores)