def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    print("GCD and LCM Calculation Program")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if num1 <= 0 or num2 <= 0:
            print("Please enter positive integers.")
            return
        
        print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")
        print(f"LCM of {num1} and {num2}: {lcm(num1, num2)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
