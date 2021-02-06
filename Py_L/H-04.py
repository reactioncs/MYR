def InputNum():
    try:
        num = int(input("Enter a integer: "))
    except:
        print("Try again! ", end="")
        num = InputNum()
    return num


num_get = InputNum()
print("=" * 30)
print("Number*10: %d" % (num_get * 10))
print("=" * 30)
