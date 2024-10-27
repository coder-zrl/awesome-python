month=input('month=')
investment=eval(input('investment='))
share=eval(input('share='))
print('投资月份为{:*^6}月，总投资{:^10,}元，投资份额为{:*<12,.2f}'.format(month,investment,share))