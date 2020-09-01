# if と　for　の組み合わせ
# 60点以上なら合格、60点未満なら不合格としたい
scores = [33, 70, 99, 10]

for score in scores:
    if score >= 60:
        print('合格')
    if score <= 60:
        print('不合格')
