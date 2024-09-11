class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        palin=0
        num=x
        rev=0
        while num>0:
            dig=num%10
            print("dig=",dig)
            rev=rev*10+dig
            print("rev=",rev)
            num=int(num/10)
            print("num=",num)
        return (rev==x)



    def isPalindromeFast(self, x: int) -> bool:
        s=str(x)
        if x>=0:
           return s == s[::-1]
        else:
            return False

    def isPalindrome_first(self, x: int) -> bool:
        array=toArray(x)
        revArray=array[::-1]
        return array == revArray

        def toArray(self, x:int) -> list:
            array=[]
            for i in str(x):
                array.append(i)
            return array