# Some data...
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

# Check if lists' length is same
if len(boys) == len(girls):
    # Pairing
    pairs = zip(sorted(boys),sorted(girls))

    # Output
    print('Идеальные пары:')
    for boy,girl in pairs:
        print(f'{boy} и {girl}')

else:
    print('кто-то может остаться без пары!')