def sum_ab_file(path1, path2):
    file = open(path1)
    s = file.readline()
    a, b = map(int, list(s.split()))
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
        open(path2, "w").write(str(a + b))
    file.close()



sum_ab_file("input3.txt", "output3.txt")