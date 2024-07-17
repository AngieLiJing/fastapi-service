with open('src/a.txt', 'r') as read_a:
    content = read_a.read()
    print(content)

if content:
    with open('src/b.txt', 'w') as write_b:
        write_b.write(content)

    with open('src/a.txt', 'w') as f:
        pass
