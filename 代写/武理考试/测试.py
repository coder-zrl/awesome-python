class Solution:
    def validPalindrome(self, mystr):
        flag=True
        i=0
        strlen=len(mystr)
        while i<strlen-i-1:
            if mystr[i]!=mystr[strlen-i-1]:
                flag=False
            i+=1
        if flag:
            print('true')
        else:
            print('false')
a=input()
solution=Solution()
solution.validPalindrome(a)