a=66528
b=52920
p=26513
q=32321

def euclid(x,y):
    while y:
        x,y=y,x%y
    return x

print(euclid(a,b))


''' attempt? at extended euclids algorithm - not working
def extended():
    x=(euclid(p,q)-y*q)/p
    y=(euclid(p,q)-x*p)/q
    return x,y

print(extended())
'''
def extended_euclid(a, b):
    """Return (g, x, y) such that g = gcd(a, b) and ax + by = g."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t

print(extended_euclid(p,q))

'''Multiple ways to understand what’s happening
Perspective A – The “repeated subtraction” story
Think of the ordinary Euclidean algorithm as repeatedly subtracting multiples of the smaller number from the larger until nothing remains. Extended Euclid tracks the same process but also keeps score of how many pieces of a and b we used in each subtraction. By the end, the left-over piece (the gcd) is literally a combination x * a + y * b. The coefficient trackers old_s, s and old_t, t are that running scoreboard.

Perspective B – The algebraic derivation
Every time we write old_r = old_r - q * r, we’re actually creating a new remainder that can itself be written as a linear combination of a and b. Because we start with a and b written trivially as 1*a + 0*b and 0*a + 1*b, each algebraic step maintains the invariant “current remainder = (some coefficient)*a + (some coefficient)*b”. The updates to old_s/s and old_t/t enforce that invariant automatically. When we stop looping, the invariant tells us the gcd is precisely old_s*a + old_t*b.

Perspective C – The programmer’s state machine
View each pair (old_r, r), (old_s, s), (old_t, t) as the current state. Each loop iteration takes the state as input and produces a new state using the same transformation: divide, multiply, subtract. There’s no recursion or stack—just a tight loop updating a small fixed-size state machine until it hits a terminal condition (r == 0). Tuple assignment is the concise way to perform the state transition without temporary variables.'''