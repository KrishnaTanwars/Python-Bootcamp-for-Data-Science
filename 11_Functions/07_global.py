def sum(a,b):
    print("Hey I am summing")
    c = a + b
    global z # please modify global z
    z = 0 # refer to global z and not  create a local variable
    return c
z = 3
print(sum(3,6))
print(z)