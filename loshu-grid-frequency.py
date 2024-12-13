import numpy as np
from termcolor import colored
from collections import Counter

def calculate_mulank(date):
    """Calculate the Mulank (sum of the digits of the day of birth)."""
    return sum(map(int, str(date))) % 9 or 9

def calculate_bhagyank(dob):
    """Calculate the Bhagyank (sum of all digits in the date of birth)."""
    return sum(map(int, dob.replace('-', ''))) % 9 or 9

def calculate_kua_number(year, gender):
    """Calculate the Kua number based on the year and gender."""
    year_sum = sum(map(int, str(year))) % 9 or 9
    if gender.lower() == 'female':
        kua_number = (year_sum + 4) % 9 or 9
    elif gender.lower() == 'male':
        kua_number = (11 - year_sum) % 9 or 9
    else:
        raise ValueError("Invalid gender. Use 'male' or 'female'.")
    return kua_number

def generate_loshu_grid(mulank, bhagyank, dob):
    """Generate the personalized Lo Shu Grid with number frequencies."""
    # Original Lo Shu Grid
    loshu_grid = np.array([
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ])
    
    # Calculate all digits in DOB and additional numbers
    all_digits = [int(d) for d in dob.replace('-', '')]
    all_digits.extend([mulank, bhagyank])  # Include only Mulank and Bhagyank
    
    # Count the frequency of each digit
    digit_frequency = Counter(all_digits)
    
    # Determine missing numbers
    missing_numbers = [num for num in range(1, 10) if num not in all_digits]
    
    # Create a grid that shows repeated numbers
    personalized_grid = []
    for row in loshu_grid:
        new_row = []
        for num in row:
            if num in all_digits:
                # Display the frequency of the number
                freq = digit_frequency[num]
                new_row.append(str(num) * freq)
            else:
                new_row.append(0)
        personalized_grid.append(new_row)
    
    return np.array(personalized_grid), missing_numbers, digit_frequency

def main():
    """Main function to analyze the Lo Shu Grid."""
    # Example input: Date of Birth and Gender
    dob = "22-10-1991"
    gender = "male"
    
    # Extract day, month, and year
    day, month, year = map(int, dob.split('-'))
    
    # Calculate Mulank, Bhagyank, and Kua number
    mulank = calculate_mulank(day)
    bhagyank = calculate_bhagyank(dob)
    kua_number = calculate_kua_number(year, gender)
    
    # Generate personalized Lo Shu Grid
    personalized_grid, missing_numbers, digit_frequency = generate_loshu_grid(mulank, bhagyank, dob)
    
    # Output Results
    print(f"\n{colored('Your Mulank:', 'green')} {colored(mulank, 'green')}")
    print(f"{colored('Your Bhagyank:', 'blue')} {colored(bhagyank, 'blue')}")
    print(f"{colored('Your Kua Number:', 'magenta')} {colored(kua_number, 'magenta')}")
    
    print(f"\n{colored('Missing Numbers:', 'red')} {missing_numbers}")
    
    print("\nYour Lo Shu Grid:")
    for row in personalized_grid:
        print([colored(str(num), 'cyan') if num is not None else "" for num in row])
    
    print("\nDigit Frequencies:")
    for num, freq in sorted(digit_frequency.items()):
        print(f"{colored(num, 'yellow')}: {colored(freq, 'yellow')} time(s)")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()

# Note: To run this script, you need to install termcolor
# Install using: pip install termcolor
