class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag = 0
        arr = []
        for i,char in  enumerate(word):
            arr.append(char)
            if char == ch and flag == 0:
                arr=arr[::-1]
                flag=1
        return "".join(arr)