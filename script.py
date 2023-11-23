import hashlib

# Initialize an empty dictionary to store usernames and their corresponding hashes
brute_force_dict = {}

# Read common passwords from the file and store them in a list
with open('password.txt', 'r') as password_list:
    common_passwords = password_list.read().splitlines()

# Read username hashes from the file and populate the brute_force_dict dictionary
with open('username_hashes.txt', 'r') as userNamehashes:
    text = userNamehashes.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash_value = user_hash.split(":")[1]
        brute_force_dict[username] = hash_value

# Iterate over the entries in the brute_force_dict dictionary
for username, stored_hash in brute_force_dict.items():
    # Iterate over the common passwords
    for password in common_passwords:
        # Hash the current password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Check if the hashed password matches the stored hash for the current username
        if hashed_password == stored_hash:
            # Print a message when a match is found
            print(f'HASH FOUND\n{username}:{password}')
