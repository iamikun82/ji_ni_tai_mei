def display_pattern(n):
    if n < 2:
        print("2")
        return
    print(" ".join([str(n)] * n))
    display_pattern(n - 1)

