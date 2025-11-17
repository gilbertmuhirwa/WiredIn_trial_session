import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+250780964667")
phone_number2 = phonenumbers.parse("+250788123456")
phone_number3 = phonenumbers.parse("+250722345678")
phone_number4 = phonenumbers.parse("+250734567890")

print("\nPhone Number Locations\n")

print("Number 1:", geocoder.description_for_number(phone_number1, "en"))
print("Number 2:", geocoder.description_for_number(phone_number2, "en"))
print("Number 3:", geocoder.description_for_number(phone_number3, "en"))
print("Number 4:", geocoder.description_for_number(phone_number4, "en"))
