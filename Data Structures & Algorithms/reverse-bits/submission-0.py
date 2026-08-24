class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = [0] * 32
        count = 0
        while count < 32:
            reverse[count] = str(n % 2)
            count += 1
            n = n >> 1
        
        binary = "".join(reverse)
        print(binary)
        return int(binary, 2)
