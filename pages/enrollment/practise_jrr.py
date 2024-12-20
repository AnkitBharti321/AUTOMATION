def largestWord(s):
    s1 = sorted(s)
    print(s1)
    print(s1[-1])


if __name__ == "__main__":
    s = "Jyoti Ranjan"
    l = list(s.split(" "))
    largestWord(l)