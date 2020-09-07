def nth_power(a):
    def exponent_of(b):
        return b ** a
    return exponent_of

square = nth_power(2)
cube = nth_power(3)

res1 = square(2)
res2 = square(3)

print(square(2))

print(res1)
print(res2)