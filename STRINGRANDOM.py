import string
import secrets
import string
import random

sequence = [secrets.choice(string.ascii_letters) for i in range(100,200)]
print(sequence)
secrets.choice(sequence)

"""
    secrets.choice(sequence)
                   ^^^^^^^^
NameError: name 'sequence' is not defined
"""
exclusive_upper_bound = 200

secrets.randbelow(exclusive_upper_bound)


'''
    secrets.randbelow(exclusive_upper_bound)
                      ^^^^^^^^^^^^^^^^^^^^^
NameError: name 'exclusive_upper_bound' is not defined
'''


i=0
for i in range(1000):
    # Generate a random 16-byte token
    token_bytes = secrets.token_bytes(random.randint(100, 200))
    print(token_bytes)

    # Generate a cryptographically secure random password
    characters = string.ascii_letters + string.digits
    secure_password = ''.join(secrets.choice(characters) for i in range(16))
    print(secure_password)

