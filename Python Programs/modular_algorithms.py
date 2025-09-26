# Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b*mod(m).
# Another way of saying this, is that when we divide the integer a by m, the remainder is b.
# This tells you that if m divides a (this can be written as m∣a) then a ≡ 0*mod(m).

# 11 ≡ x mod 6
# 11 % 6 == x % 6
# pow(11, x, 6)
# x = 11 mod 6

def congruence(a,m):
    b = a % m
    return b

print(congruence(11,6))
print(congruence(8146798528947, 17))

