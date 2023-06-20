largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        fn = float(num)
        if largest is None:
            largest = fn
        elif fn > largest:
            largest = fn
        elif smallest is None:
            smallest = fn
        elif fn < smallest:
            smallest = fn
    except:
        print('Invalid input')

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
