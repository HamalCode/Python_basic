#  date and time


import datetime as dt
# lorn_ohin= dt.datetime.today()
# print ("Loron ohin mak:", lorn_ohin)#nia fo sai data ohin loron no horas

# print(lorn_ohin)
# print(f"loron ohin mak= {lorn_ohin:%A}")

# dias = dt.date(1998,11,25)
# print(dias)
# print(f"loron ohin mak= {dias:%A}")

print(" favor hatama data, \nbulan no tahun\n")

tanggal = input (" tanggal \t: ")
bulan =input (" bulan \t\t: ")
tahun =input (" tahun \t\t: ")

tanggal_lahir = dt.date(tanggal,bulan,tahun)
print(f"tanggal lahir anda adalah: {tanggal_lahir}")
