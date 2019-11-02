"""
syntax programming language consist of:
- Sequential
- Branching
- Loop
- Modularization using :
    a. Function
    b. Class
    c. Package

example program to be made :
Blog with Django
"""
judul = 'Menguasai python dalam 3 jam'
author = 'Nafis Faisal'
tanggal = '2019-11-02'

#jumlah_artikel = 100
#
#if jumlah_artikel > 100:
#    print ('Jumlah artikel besar, akan dipecah ke dalam beberapa halaman')
#for i in range(1,11):
#    print (i)

#list
angka = [1, 'loro', 3, 4.0]
#for item in angka:
#    print (item)

#dictionary
#kamus_cinta = {}
#kamus_cinta['love']='tresna'
#kamus_cinta['sayang']='kangen'
#print (kamus_cinta)

manusia = [{
    'nama' : 'Nafis Faisal',
    'alamat' : {
        'line 1' : 'Perumahan Greenland',
        'Kecamatan' : 'Bojongsari',
        'Kota' : 'Depok',
        'Provinsi' : 'Jawa Barat'
    }
}]
print (manusia[0]['nama'])
print (manusia[0]['alamat']['Kota'])