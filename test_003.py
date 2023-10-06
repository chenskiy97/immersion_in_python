import json
import csv
import random
import math

def store_in_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as f:
                json.dump({
                    "parameters": {"a": args[0], "b": args[1], "c": args[2]},
                    "result": result
                }, f)
                f.write('\n')  # to make the file more human-readable
            return result
        return wrapper
    return decorator

def quadratic(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                func(a, b, c)
    return wrapper

@store_in_json('results.json')
def quadratic_equation_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    else:
        print(f"Cannot compute roots for equation {a}x^2 + {b}x + {c} = 0, discriminant is negative.")
        return None, None

def generate_csv_file(filename):
    with open(filename, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[random.randint(1, 100) for _ in range(3)] for _ in range(100)])

@quadratic
def print_roots(a, b, c):
    x1, x2 = quadratic_equation_roots(a, b, c)
    if x1 is not None and x2 is not None:
        print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are {x1} and {x2}")

generate_csv_file('test.csv')
print_roots('test.csv')
