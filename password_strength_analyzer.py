import re

print("========== Password Strength Analyzer ==========")

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase
if re.search(r"[A-Z]", password):
    score += 1

# Check lowercase
if re.search(r"[a-z]", password):
    score += 1

# Check number
if re.search(r"\d", password):
    score += 1

# Check special character
if re.search(r"[!@#$%^&*()_+=<>?/{}~]", password):
    score += 1

print("\n========== Result ==========")

if score == 5:
    print("✅ Strong Password")
elif score >= 3:
    print("⚠️ Medium Password")
else:
    print("❌ Weak Password")

print("\nSuggestions:")

if len(password) < 8:
    print("- Use at least 8 characters.")
if not re.search(r"[A-Z]", password):
    print("- Add at least one uppercase letter.")
if not re.search(r"[a-z]", password):
    print("- Add at least one lowercase letter.")
if not re.search(r"\d", password):
    print("- Add at least one number.")
if not re.search(r"[!@#$%^&*()_+=<>?/{}~]", password):
    print("- Add at least one special character.")

print("\nThank you for using Password Strength Analyzer!")