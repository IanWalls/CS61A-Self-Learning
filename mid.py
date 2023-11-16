def cycle(f1, f2, f3):
    # def mid(f1, f2, f3, n):
    #     if n == 0:
    #         return lambda x: x
    #     else:
    #         return(lambda x: mid(f2, f3, f1, n-1)(f1(x)))
        
    # return lambda n: mid(f1, f2, f3, n)
    
    
    cycle = [f1, f2, f3]
    def mid(n):
        ret = lambda x: x
        for i in range(n):
            print(i,"______")
            m = lambda f: lambda x: cycle[i % 3](f(x))(ret)
            ret = m
        return ret  
    return mid
    
def add1(x):
    return x + 1

def times2(x):
    return x * 2

def add3(x):
    return x + 3

my_cycle = cycle(add1, times2, add3)

identity = my_cycle(2)
print(identity(5))