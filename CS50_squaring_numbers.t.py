from CS50_squaring_numbers import square

def test_square():
    if square(2) != 4:
        print("2 squared is not 4")
    if square(3) != 9:
        print("3 squared is not 9")

if __name__ == "__test_square__":
    test_square()