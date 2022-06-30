#with parameter with return
def add(a,b):
    c=a+b
    return c
#with parameter no return
def sub(a,b):
    c=a-b
    print(c)
#no parameter no return
def mul():
    a=1
    b=2
    c=a*b
    print(c)

#no parameter with return
def div():
    a=1
    b=2
    c=a/b
    return c

class test:
    def test1(self):
        print("8888888888888888888888")
    def test2(self):
        print("888888888888888888777778888")
if __name__ == "__main__":#header of code/statement
    resu=add(12,34)
    print(resu)

    sub(13,15)

    mul()

    gg=div()

    print(gg)

    #class call
    oj=test()
    oj.test1()
    oj.test2()