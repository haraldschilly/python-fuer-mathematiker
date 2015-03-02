def profile_me(e):
    x = 1
    z = [0]
    import math
    while z[-1] < e:
        v = math.sin(x)
        for i in range(x):
            v2 = v + math.sqrt(i)
        z.append(v2)
        x += 1
    return x
