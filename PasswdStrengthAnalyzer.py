import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Count how many criteria are met
    passed_criteria = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Strength logic
    if passed_criteria == 5:
        strength = "Strong"
    elif passed_criteria >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Detailed feedback
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters.")
    if lowercase_error:
        feedback.append("Add lowercase letters.")
    if uppercase_error:
        feedback.append("Add uppercase letters.")
    if digit_error:
        feedback.append("Add digits.")
    if special_char_error:
        feedback.append("Add special characters (e.g., !, @, #).")

    return strength, feedback

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"- {tip}")

if __name__ == "__main__":
    main()
