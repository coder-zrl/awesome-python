def fuc(n):
    if n<=5:
        print('你的年龄是%s，建议保证睡眠12小时以上！'%n)
    elif 6<=n<=12:
        print('你的年龄是%s，建议保证睡眠9-12小时！' % n)
    elif 13<=n<=17:
        print('你的年龄是%s，建议保证睡眠8-10小时！' % n)
    elif 18 <= n <= 70:
        print('你的年龄是%s，建议保证睡眠7-8小时！' % n)
    else:
        print('你的年龄是%s，建议保证睡眠5.5-7小时！' % n)
age=eval(input())
fuc(age)