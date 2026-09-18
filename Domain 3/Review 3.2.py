items = ['wand', 'rock', 'pogo stick']
levels = [1, 2, 3]
for level in levels:
    for item in items:
        if level == 2 and item == 'rock':
            continue
        else:
            print(f"you can get a {item} at level {level}")