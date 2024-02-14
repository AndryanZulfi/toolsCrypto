import math

def calculate_p_and_q(n):
    p = math.comb(n + 1, 2)
    q = math.comb(n + 2, 2)
    return p, q

n = 245841236512478852752909734912575581815967630033049838269083
p, q = calculate_p_and_q(n)
print(f"p: {p}, q: {q}")