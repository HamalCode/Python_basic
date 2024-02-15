#operasi manipulasi string

# 1. menyambung string (concatenate)
naran_proprio= "Silvino"
naran_klaran ="de Jesus"
naran_apelido="Albano"

naran_kompletu= naran_proprio + "" + naran_klaran + "'"+ naran_apelido
print (naran_kompletu)

# 2.menhituhn panjannya string uza len

panjang =len(naran_kompletu)
print("panjang dari "+ naran_kompletu + "=" + str(panjang))

# operatot untuk string
# cek apakah iha komponen char ou string iha string

d= "Jesus'Albano"
status = d in naran_kompletu
print(d + "iha" + naran_kompletu +"=" + str(status))

# menulang string
print ("H"*10)
print (15*"H")

print("\n==========Indexin=====")
# indexin
print("index ke-0:" + naran_kompletu[0])
print("index ke-6:" + naran_kompletu[6])
print("index ke-(-1):" + naran_kompletu[-1])#nia foti husi kotuk

print("index ke-(-2):" + naran_kompletu[-2])#nia foti husi kotuk
print("index ke-(0,2,4,6,8,10):" + naran_kompletu[0:11:2])


# item nebe kik liu
print("paling kik liu:" + min(naran_kompletu))
print("paling bot liu:" + max(naran_kompletu))#bot liu


ascii_code = ord(" ")
print("ASCII code untuk spasi besar adalah" + str(ascii_code))
data= 117

print("Char untuk ASCII 117 adalah " + chr(data))

# 4.operator dalam bentuk method
data= "otong sarotong parotong"
jumlah= data.count("g")
print("Jumlah g pada " + data + " = " + str(jumlah))