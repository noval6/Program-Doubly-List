#Buat Memulai doubly list
class Node:
    def __init__ (self, data):
        self.next = None
        self.prev = None
        self.data = data

#Membuat pengembangan dari doubly list agar bisa memiliki dua pointer "next" dan "prev" / head and tail
class Doubly:
    def __init__ (self):
        self.head_node = None

    def Lagu_Baru(self, data):
        if self.head_node is None:
            nodeBaru = Node(data)
            nodeBaru.prev = None
            self.head_node = nodeBaru
            
        else:
            nodeBaru = Node(data)
            saatIni = self.head_node 
            while saatIni.next:
                saatIni = saatIni.next
            saatIni.next = nodeBaru
            nodeBaru.prev = saatIni
            nodeBaru.next = None


#membuat doublylink list yang head
    def Putar_Musik(self):
        if self.head_node is None:
            print("*"*30)
            print("Playlist mu belum terisi!")
            print("*"*30)
            return
        else:
            saatIni = self.head_node
            out = saatIni.data.split(',')

        print(f"Kamu sedang mendengarkan lagu {out[0]} - {out[1]}")

#sesuai dengan di ilustrasi disini tersedia fitur next doublylist
    def NextMusic(self):
        if self.head_node is None:
            print("*"*30)
            print("Playlist mu belum ada!")
            print("*"*30)
            return
        else:
            saatIni = self.head_node = self.he1ad_node.next
            out = saatIni.data.split(',')
        print(f"Kamu sedang memutar lagu {out[0]} , dari {out[1]}")

#selanjut nya saya menambahkan fitur previous music agar bisa mengembalikan lagu yang di putar
    def PrevMusic(self):
        if self.head_node is None:
            print("*"*30)
            print("Playlist mu belum ada")
            print("*"*30)
            return
        else:
            saatIni = self.head_node = self.head_node.prev
            out = saatIni.data.split(',')

        print(f"Kamu sedang memutar lagu {out[0]} , dari {out[1]}")

    def Show(self):
        if self.head_node is None:
            print("*"*30)
            print("Playlist mu belum ada!")
            print("*"*30)
            return
            
        else:
            no = 0
            saatIni = self.head_node
            print("Playlist Anda")
            print("*"*30)
            while saatIni is not None:
                no +=1
                print(f"{no}.", saatIni.data)
                saatIni = saatIni.next
            print("*"*30)


show = Doubly()
while True:

    menu = int(input("""\n ~~~ PLAYLIST MUSIC NOVAL ~~~ 
1. Ayo Buat playlist mu!
2. Play song
3. Next song
4. Previous song
5. Lihat playlist
0. exit.



\nMenu Pelihan : """))
#Membuat fitur insert untuk memasukan playlist dan judul serta penyanyi nya
    if menu == 1:
        jumlah = int(input("Masukan jumlah lagu dalam playlist yang kamu inginkan : "))
        for i in range(jumlah):
            input_lagu = input(f"Masukkan lagu ke-{i+1} (judul, singer) : ")
            show.Lagu_Baru(input_lagu)

        else:
            print("~"*35)
            print("Playlist Berhasil di Tambahkan.")
            print("~"*35)
    elif menu == 2:
        show.Putar_Musik()
    elif menu == 3:
        show.NextMusic()
    elif menu == 4:
        show.PrevMusic()
    elif menu == 5:
        show.Show()
    elif menu == 0:
        exit()