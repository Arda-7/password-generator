import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
soru = int(input("parolanın uzunluğu kaç harf olsun? :"))
           
for i in range(soru):
    password += random.choice(characters)

print(password)