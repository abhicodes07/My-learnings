# Creating a program demonstrating assignment operator
a = int(input("Enter the number: "))
b = a

a += b
print("a+=b: ", a)
a -= b
print("a-=b: ", a)
a /= b 
print("a/=b: ", a)
a *= b
print("a*=b: ", a)
a //= b
print("a//=b: ", a)
int(a)
print(type(a))
int(b)
print(type(b))

# Reinitalisinig a and b variable
a = 5
b = 10

# Left shift
a <<= 1
print("Left Shift a<<=3: ", a)

# Right shift
b >>= 1
print("Right Shift a>>=2: ", a)

a >= b
print("a>=b: ", a)
a <= b
print("a<=b: ", a)
a **= b
print("a**=b: ", a)
a |= b
print("a|=b: ", a)
a &= b
print("a&=b: ", a)




