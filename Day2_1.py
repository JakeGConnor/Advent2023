text = open("day2.txt", "r")

red = 12
green = 13
blue = 14

tot = 0

y = True

for line in text:
    line = line.strip()
    line = line.split(":")
    game = line[0].split(" ")
    games = line[1].split(";")
    
    for i in games:
        colors = i.split(",")
        
        for r in colors:
            each = r.split(" ")
            num = each[1]
            
            if each[2] == 'red':
                if int(each[1]) > red:
                    y = False
                    break
            elif each[2] == 'blue':
                if int(each[1]) > blue:
                    y = False
                    break
            elif each[2] == 'green':
                if int(each[1]) > green:
                    y = False
                    break
    
    if y == True:
        tot = tot + int(game[1])
    else:
        y = True

print(tot)