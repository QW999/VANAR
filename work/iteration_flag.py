
start = 0
end = 10
step = start
flag1 = 2
flag2 = 7
print('Starting from step ', step)

while step < end:
    step = step + 1
    print('step: ', step)
    if step == flag1 or step == flag2:
        print("Found the flag")
print("Ending at step: ", step)

