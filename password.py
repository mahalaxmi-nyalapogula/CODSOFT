import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
length = 17  # You can set this to any desired length
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Generated Password: {password}")
import random
import string

# Define the length of the password
length = 17  # You can change this to any desired length

# Combine letters, digits, and punctuation into a single character pool
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print(f"Generated Password: {password}")

