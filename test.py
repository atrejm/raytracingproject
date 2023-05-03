from tracer_color import TracerColor

def main():
    print(calculate(338, 341, 369, 144, 2, 1, 3, 1))
    print(calculate(259, 222, 349, 100, 2, 1, 9, 2))
    print(calculate(319, 475, 287, 54, 2, 1, 10, 1))

def calculate(ba, za, apb, wrt, oi, od, pc, ps):
    return (ba + za + apb)/3 + (wrt*oi)/od + (pc -ps)*20
    

if __name__ == "__main__":
    main()

