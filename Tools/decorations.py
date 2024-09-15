def start_finish(func):
    def wrapper():
        print("start")
        func()
        print("finish")
    return k

@start_finish
def test():
    print("test")

test()