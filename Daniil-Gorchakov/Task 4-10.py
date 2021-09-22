# A function that takes a number as an argument and returns a dictionary {number:number^2}

def generate_squares(number):
    return {num: num**2 for num in range(1, number + 1)}

if __name__ == "__main__":
    print(generate_squares(5))
    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
