class ReverseInteger:
    #7. Reverse Integer - Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0
    def reverse(self, x: int) -> int:
        remainder = 0
        myList = []
        readRange = 0
        
        if x < 0:
            myList.insert(0, 1)
            x*=(-1)
        else:
            myList.insert(0, 0)
                
        #Load x to int array
        while (x > 0):
            remainder = x%10
            x = x//10
            myList.insert(1,remainder)
            
        #swap
        readRange = (len(myList)-1) // 2
        for i in range(1, readRange + 1):
            temp = myList[i]
            myList[i] = myList[-1*i]
            myList[-1*i] = temp
            
        #Load back and return
        x = 0
        for i in range (1, len(myList)):
            x += myList[-1*i]*(10**(i-1))
        if myList[0] == 1:
            x*=(-1)
        
        #Check out of range or negative inputs
        if x > 2147483647 or x < -2147483648:
            return 0
        return x