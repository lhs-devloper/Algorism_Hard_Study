# Euclid Geometry
def Eculid_gcd_Algorism(a, b):
    if a < b:
        s = a
        a = b
        b = s
    if a % b == 0:
        return a
    return Eculid_lcm_Algorism(b, a % b)


def Eculid_lcm_Algorism(a, b):
    return int(a * b / Eculid_gcd_Algorism(a, b))


print(Eculid_gcd_Algorism(12, 100))
print(Eculid_lcm_Algorism(12, 100))
