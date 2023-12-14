text = open("day4.txt", "r")

total = 0
points = 0
cnt = 0

for line in text:
    line = line.strip()
    line = line.split(":")
    card = line[0].split(" ")
    nums = line[1].split("|")
    winnums = nums[0].split(" ")
    mynums = nums[1].split(" ")
    
    for i in mynums:
        if i == '':
            continue
        for j in winnums:
            if j == '':
                continue
            if int(i) == int(j):
                print("match")
                if points == 0:
                    points = points + 1
                else:
                    points = points * 2
    total = total + points
    points = 0

print(total)