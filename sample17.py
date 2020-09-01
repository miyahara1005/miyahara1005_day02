# わざとError

def double(number):
    return 2 * number

#Q.こう呼び出すとどうなる？
# double(1, 2, 3, 4, 5)

# TypeError: double() takes 1 positional argument but 5 were given

#Q.じゃあ、こっちは？
double() #引数がたりないよ
# TypeError: double() missing 1 required positional argument: 'number'
