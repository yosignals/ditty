import random
import string
import hashlib

def generate_fake_extract():
    domain = 'gchq.local'
    user_count = 720  # Number of fake user accounts to generate

    fake_extract = []

    # Generate a static hash for uuid1
    static_uuid1 = hashlib.new('md4', 'static_hash'.encode('utf-16le')).hexdigest()

    # List of generic European first names
    european_first_names = [
        'Maria', 'Anna', 'Emil', 'Sophia', 'Lucas',
        'Amelia', 'Jack', 'Mila', 'Oliver', 'Laura'
        # Add more first names as needed
    ]

    # List of generic European last names
    european_last_names = [
        'Schmidt', 'Mueller', 'Petrov', 'Larsson', 'Varga',
        'Rossi', 'Pavlov', 'Hernandez', 'Lopez', 'Fischer'
        # Add more last names as needed
    ]

    for _ in range(user_count):
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  # Generate a random username
        digits = random.randint(100000, 999999)  # Generate a 6-digit number
        uuid1 = static_uuid1  # Use the static hash for uuid1

        # Generate varying duplicate hashes for uuid2
        if random.random() < 0.3:  # 30% chance of having a duplicate hash
            duplicate_count = random.choice([2, 3, 4, 20, 30, 100])  # Vary the duplicate count
            duplicate_uuid2 = hashlib.new('md4', 'duplicate_hash'.encode('utf-16le')).hexdigest()

            for _ in range(duplicate_count):
                first_name = random.choice(european_first_names)
                last_name = random.choice(european_last_names)
                name = f'{first_name}.{last_name.lower()}'
                entry = f'{domain}\\{name}:{digits}:{uuid1}:{duplicate_uuid2}:::'
                fake_extract.append(entry)
        else:
            first_name = random.choice(european_first_names)
            last_name = random.choice(european_last_names)
            name = f'{first_name}.{last_name.lower()}'
            uuid2 = hashlib.new('md4', str(random.randint(100000000, 999999999)).encode('utf-16le')).hexdigest()
            entry = f'{domain}\\{name}:{digits}:{uuid1}:{uuid2}:::'
            fake_extract.append(entry)

    return fake_extract

# Generate a fake extract
fake_ntds_dit_extract = generate_fake_extract()

# Print the generated extract
for entry in fake_ntds_dit_extract:
    print(entry)
