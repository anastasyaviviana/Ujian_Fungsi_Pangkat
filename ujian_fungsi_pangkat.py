print('\nPROGRAM PANGKAT')
print('(Misalkan anda ingin menghitung 2 pangkat 3, maka masukkan 2 pada "Angka Pertama" dan 3 pada "Angka Kedua")\n')
a=input('Angka Pertama :')
if a.isdigit():
    b=input('Angka Kedua   :')
    if b.isdigit():
        def pangkat(a,b):
            a=int(a)
            b=int(b)
            x=1
            i=1
            while i <=b:
                x=x*a
                i+=1
            return print('\nHasil dari',a,'pangkat',b,'adalah',x,'\n')
        pangkat(a,b)
    else:
        print('Maaf yang anda input bukan angka')
else:
    print('Maaf yang anda input bukan angka')
