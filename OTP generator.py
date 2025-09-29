import random

def otpgenrator(leangth=6):
    numbers="0123456789"
    otp=""
    for _ in  range(leangth):
        otp=random.choice(numbers)
        return otp

if __name__=="__main__":
    generated_otp=otpgenrator(leangth=6)
    print(f"{generated_otp} is your otp.")