import sys

def main():
    name = input()
    rotation = 0
    current = 'a'

    for i in range(len(name)):
        rotation += min(abs(ord(name[i]) - ord(current)), 26 - abs(ord(name[i]) - ord(current)))
        current = name[i]

    print(rotation)

if __name__ == "__main__":
    main()
