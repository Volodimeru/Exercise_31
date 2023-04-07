def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            a,b = fraction.split("/")
            c = (int(a)/int(b))*100
            if c != 0 and b > a:
                 return c
            else: fraction = input("Fraction: ")
            pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if 0 <= percentage <= 1.0 :
        return "E"
    elif 99.0 <= percentage <= 100.0 :
        return "F"
    else:
        return str(percentage) + "%"
    
if __name__=="__main__":
    main()