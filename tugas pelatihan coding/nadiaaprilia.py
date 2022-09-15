def fungsi__python():
    print("menghitung konversi suhu")

print(str("pilih 1 untuk konversi suhu celcius ke kelvin "))
print(str("pilih 2 untuk kenversi suhu celcius ke reamur"))
print(str("pilih 3 untuk konversi suhu celcius ke farenheit"))
operator=input("pilih:")
if(operator =="1"):
    a=float(input("masukkan angka :"))
    celcius= a + 273,15
    print("hasil =",celcius,"derajat kelvin")
elif(operator == "2"):
    a=float(input("masukkan angka :"))
    celcius= 4/5 * a
    print("hasil =",celcius,"derajat reamur")
elif(operator=="3"):
    a=float(input("masukkan angka :"))
    celcius= 9/5 * a + 32
    print("hasil =",celcius,"derajat farenheit")
else:
    print("tidak ada dalam pilihan")