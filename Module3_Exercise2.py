smallest = None
largest = None

while True :
    sline = input("Plase enter a number: ")
    if sline == "done" : break
    try:
        fline = float(sline)
    except:
        print("Invalid input")
        continue
    if largest is None or fline > largest : largest = fline
    if smallest is None or fline < smallest : smallest = fline

print('Maximum:',smallest)
print('Minimum:',largest)