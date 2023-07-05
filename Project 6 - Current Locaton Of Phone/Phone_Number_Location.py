# Install packarges
import phonenumbers 
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number with +880: ")

phone = phonenumbers.parse(number)
