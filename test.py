from tracer_color import TracerColor

def main():
    color1 = TracerColor(100, 100, 100)
    color2 = TracerColor(100, 100, 100)

    print(color1)
    color1 = color1 + color2
    print(color1)
    color1 = color1 * 0.234
    print(color1)

def doshit(color):
    color = 0.5 * color
    return doshit(color)

if __name__ == "__main__":
    main()

