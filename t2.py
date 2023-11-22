#递归方式
def josephus(n: int, m: int) -> int:
    if n == 1:
        return 1
    return (josephus(n-1,m)+m-1)%n+1

print(josephus(5,3))