text = open("day8.txt", "r")

class Struct:
    def __init__(self, loc, left, right):
        self.loc = loc
        self.left = left
        self.right = right

RL = []

for line in text:
    line = line.strip()

    for i in range(len(line)):
        RL.append(line[i])

    if line == "":
        break

arr = []

for line in text:
    
    line = line.strip()
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("=", "")
    line = line.replace(",", "")
    line = line.split()

    arr.append(Struct(line[0], line[1], line[2]))

list_count = 0
dir_count = 0
start = 'AAA'
current = 'AAA'
finish = 'ZZZ'
count = 0

while True:

    if dir_count > len(RL)-1:
        dir_count = 0

    if list_count > len(arr)-1:
        list_count = 0

    if arr[list_count].loc == current:

        if RL[dir_count] == "R":
            current = arr[list_count].right
            count += 1

        elif RL[dir_count] == "L":
            current = arr[list_count].left
            count += 1

        dir_count += 1
        
    list_count += 1

    if current == finish:
        break

print(count)
