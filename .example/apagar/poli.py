class A:
    def __init__(self, a):
        self.a = a
    def oi(self):
        print('eu sou A')

class B:
    def __init__(self, b):
        self.b = b
    def oi(self):
        print('eu sou B')

class C:
    def __init__(self, c, a):
        self.c = C
        self.a = a
    def oi(self):
        print('eu sou C')

class X(A, B, C):
    def __init__(self, x, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        C.__init__(self, c, a)
        self.x = x

    def print_a(self):
        print(self.a)

x = X(x='x', a = 'a', b='b', c='c')

print(dir(x))

print('x:', x.x, 'a:', x.a, 'b:', x.b)

x.oi()

x.print_a()