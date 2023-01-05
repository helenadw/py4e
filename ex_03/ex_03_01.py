hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

if h > 40 :
    reg = (h * r)
    otp = (h - 40) * (r * 0.5)
    print(reg + otp)
else :
    print(h * r)
