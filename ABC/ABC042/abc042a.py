from collections import Counter

def solve():
    c = Counter([int(c) for c in input().split()])
    print("YES" if c[5] == 2 and c[7] == 1 else "NO")

if __name__=="__main__":
    solve()