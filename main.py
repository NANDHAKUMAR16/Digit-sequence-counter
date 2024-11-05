import math
a = 111122223333
intToStr = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

pv = int(math.pow(10, len(str(a)) - 1))
count, prev = 0, (a // pv) % 10

while pv > 0:
    current_digit = (a // pv) % 10
    if current_digit == prev:
        count += 1
    else:
        while(count >0):
            if(count >=3 and count !=4):
                print("triple",intToStr[prev],end =" ")
                count -=3
            elif(count%2 == 0 or count == 4):
                print("double",intToStr[prev],end=" ")
                count -=2
            else:
                print(intToStr[prev],end=" ")
                count -=1
        prev = current_digit
        count = 1
    pv //= 10
while count > 0:
    if count >= 3 and count != 4:
        print("triple", intToStr[prev], end=" ")
        count -= 3
    elif count % 2 == 0 or count == 4:
        print("double", intToStr[prev], end=" ")
        count -= 2
    else:
        print(intToStr[prev], end=" ")
        count -= 1
print()



# OUTPUT:
# double one double one double two double two double three double three
