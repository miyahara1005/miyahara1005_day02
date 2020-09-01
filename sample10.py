# 1  から　9まで
for i in range(1, 10):
    print(i)

# 1　から　15　まで
for i in range(1, 16):
    print(i)

# 0 から 23　まで
for i in range(0, 23 + 1):
    print(i)

# お題: 1から30までのうち、偶数のみを出力してください
# ただし、　if for をつかうこと
#　偶数　⇔　2の倍数　⇔　「2で割った時のあまり」が「０」である


for i in range(1, 11):
    if i % 2 == 0:
        print(i)