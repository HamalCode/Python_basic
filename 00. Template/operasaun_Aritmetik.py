#aprende konvert temparatura 
#program konversi  celsius ke satuan lain
# print("\nPROGRAM KONVERT TEMPERATUR\n")
# celcius= float(input('Masukan Suhu dalam Celsius: '))
# print("Suhu adalah", celcius, "Celcius")

# #reamur
# reamur = (4/5) * celcius
# print ("suhu dalam reamur adalah",reamur, "Reamur")

# #farenheit
# fahrenheit= ((9/5) * celcius)+32
# print ("suhu dalam farenheit adalah",fahrenheit, "Fahrenheit")

# #kelvin
# kelvin= celcius + 273
# print ("suhu dalam kelvin adalah",kelvin, "Kelvin")

# print("====Trabalho====")

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273
    return kelvin

fahrenheit = float(input('Masukkan suhu dalam Fahrenheit: '))
kelvin = fahrenheit_to_kelvin(fahrenheit)
print("Suhu adalah", kelvin, "Kelvin")



def kelvin_to_farenheit (kelvin):
    fahrenheit=(kelvin -273) * 9/5 + 32
    return fahrenheit
print("Suhu adalah", fahrenheit, "fahrenheit")





