# очень медленно
def god(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

# быстро, но риск переполнения стека рекурсии
def god2(m, n):
    if n == 0:
        return m
    return god2(n, m % n)

# быстро и оптимально
def god3(m, n):
    while n != 0:
        m, n = n, m % n
    return m

print(god3(540, 24458732646))