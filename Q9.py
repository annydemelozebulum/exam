def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = birthday.split("-")
    day = int(day)
    month = int(month)
    year = int(year)

    # Calculate the current year
    current_year = 2024

    # Calculate the total days passed excluding the birth year and the current year
    total_days_passed = (current_year - year - 2) * 365

    return total_days_passed


# Example usage:
birthday = "14-11-2003"
print("Days passed since birthday:", days_since_birthday(birthday))
