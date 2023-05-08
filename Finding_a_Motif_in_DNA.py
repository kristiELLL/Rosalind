s = "GATATATGCATATACTT"
t = "ATAT"

index = -1
while True:
    index = s.find(t, index + 1)
    if index == -1:
        break
    print(index + 1, end=" ")
