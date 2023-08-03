import bcrypt

pw = "Password1!"

hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

given = input("Please enter password: ")

is_correct = bcrypt.checkpw(given.encode(), hashed)

if bcrypt.checkpw(given.encode(), hashed):
    print("Access Granted")
else:
    print("Access Denied")
