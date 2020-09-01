# 例２：あたら得られた整数の遇奇を返す関数　is_even


# def is_even(number):
#     return number % 2
#
# if is_even == 0:
#     print(is_even)

#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

#上記を短くかくと
def is_even(number):
    return number % 2 == 0

# 先に、使い方のイメージから書いていく
print(is_even(2)) #True
print(is_even(3)) #False

