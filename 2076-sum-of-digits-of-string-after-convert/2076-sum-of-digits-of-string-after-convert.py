class Solution:
    def convert(self, s: str) -> int:
        result = ''
        for c in s:
            result += str(ord(c) - 96)
        return int(result)

    def digitize(self, num: int) -> list:
        digits = [int(digit) for digit in str(num)]
        return digits

    def getLucky(self, s: str, k: int) -> int:
        num = self.convert(s)
        for i in range(k):
            digits=self.digitize(num)
            num = sum(digits)
        return num

    