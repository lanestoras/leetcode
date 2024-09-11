class Solution:
    def isPalindrome(self, x: int) -> bool:

        array=self.toArray(x)
        revArray=array[::-1]
        return array == revArray
        

    def toArray(self, x:int) -> list:
        array=[]
        for i in str(x):
            array.append(i)
        return array

 