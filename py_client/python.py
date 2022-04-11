class A:
    def __init__(self, a, b):
        class B:
            def __init__(self, c):
                try:
                    self.b = A(c)
                except:
                    self.b = [c*2 for c in range(5)]
        self.b = [c*3 for c in range(5)]
e = A(1, 2)
print (e.b)