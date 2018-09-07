def f(n):
    result = []
    j = 0
    for i in range(n):
        j = i * n + j
        j += n
        result.append(j)
    return result

if __name__ == '__main__':
    print(f(5))
