num = '1 - 2 * 2 - 3 * 3 / 7'
num = num.split()
print(num)
while len(num) > 1:
    while '*' in num or '/' in num :
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = float(num[num.index('*') - 1]) * float(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = float(num[num.index('/') - 1]) / float(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = float(num[num.index('*') - 1]) * float(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = float(num[num.index('/') - 1]) / float(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    while '+' in num or '-' in num :
        if num.count('+') > 0 and num.count('-') > 0:
            if num.index('+') < num.index('-'):
                num[num.index('+') - 1] = float(num[num.index('+') - 1]) + float(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = float(num[num.index('-') - 1]) - float(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
        else:
            if '+' in num:
                num[num.index('+') - 1] = float(num[num.index('+') - 1]) + float(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = float(num[num.index('-') - 1]) - float(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
print(round(num[0],2))
