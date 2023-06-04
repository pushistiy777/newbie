"""
Random Code Generator
"""

import random

def generate_random_code(length):
    code = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};:,.<>/?"
    
    for _ in range(length):
        code += random.choice(characters)
    
    return code

if __name__ == "__main__":
    length = 10
    random_code = generate_random_code(length)
    print(f"Random Code: {random_code}")
