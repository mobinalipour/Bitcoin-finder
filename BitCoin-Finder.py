from bitcoin import *

bitcoin_addresses = []

with open('address.txt', 'r') as file:
    for line in file.readlines():
        bitcoin_address = line.strip()
        bitcoin_addresses.append(bitcoin_address)


while True:
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)

    if address in bitcoin_addresses:
        print(f"Found a match: {private_key}:{address}")
        break

    print(f"Not a match: {private_key}:{address}")