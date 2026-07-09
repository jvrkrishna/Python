class Test:

    def m1(self, a):
        print(a)

    def m1(self, a, b):
        print(a, b)

    def m1(self, a, b, c):
        print(a, b, c)


t = Test()

# t.m1(10)          # Error
# t.m1(10, 20)      # Error
t.m1(10, 20, 30)