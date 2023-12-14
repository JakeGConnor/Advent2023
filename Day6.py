text = open("day6.txt", "r")

times = []
dist = []

tot = 0
ans = 1

for line in text:
    line = line.strip()
    line = line.split(":")
    if line[0] == "Time":
        tm = line[1].split()
        for i in tm:
            times.append(i)
    elif line[0] == "Distance":
        ds = line[1].split()
        for j in ds:
            dist.append(j)

for a in range(len(times)):
    tot = 0

    for b in range(int(times[a])):
        time = int(times[a]) - b
        total = time * b

        if total > int(dist[a]):
            tot = tot + 1

    ans = ans * tot

print(ans)
