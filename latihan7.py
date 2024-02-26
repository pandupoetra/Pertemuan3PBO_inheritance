class Contoh:
    def __init__(self, nilai):
        self.nilai = nilai

# Membuat objek dan mengisi atribut
objek = Contoh(10)
print("Nilai sebelum dihapus:", objek.nilai)

# Menghapus atribut 'nilai' dari objek menggunakan delattr()
delattr(objek, 'nilai')
try:
    print("Nilai setelah dihapus dengan delattr:", objek.nilai)  # Ini akan menimbulkan AttributeError karena 'nilai' telah dihapus
except AttributeError:
    print("Atribut 'nilai' telah dihapus dari objek.")

# Membuat objek baru
objek_baru = Contoh(20)
print("Nilai objek_baru sebelum dihapus:", objek_baru.nilai)

# Menghapus objek secara keseluruhan menggunakan del
del objek_baru
try:
    print("Nilai objek_baru setelah dihapus:", objek_baru)  # Ini akan menimbulkan NameError karena objek sudah dihapus
except NameError:
    print("Objek_baru sudah dihapus dari memori.")
