print("===========================")
print("|     SELAMAT DATANG      |")
print("|   DI RUMAH SAKIT FUAD   |")
print("|         HUSADA          |")
print("===========================")

kapasitas_ruangan = {
    "Mawar": 5,
    "Anggrek": 5,
    "Melati": 5,
    "Tulip": 5
}

data_rumah_sakit = {
    "Mawar": [],
    "Anggrek": [],
    "Melati": [],
    "Tulip": []
}

def tambah_pasien():
    while True:
        print("\nPilih ruangan untuk pasien:")
        ruangan_list = list(data_rumah_sakit.keys())
        for i, ruangan in enumerate(ruangan_list, start=1):
            print(f"{i}. {ruangan} (Kapasitas: {len(data_rumah_sakit[ruangan])}/{kapasitas_ruangan[ruangan]})")
        
        pilihan = input("Pilih nomor ruangan (atau ketik 'Quit' untuk keluar): ")
        
        if pilihan.lower() == "quit":
            print("Keluar dari proses penambahan pasien.")
            break
        
        if not pilihan.isdigit():
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        
        pilihan = int(pilihan)
        
        if 1 <= pilihan <= len(ruangan_list):
            ruangan = ruangan_list[pilihan - 1]
        else:
            print("Nomor ruangan tidak valid. Silakan coba lagi.")
            continue
        
        if len(data_rumah_sakit[ruangan]) >= kapasitas_ruangan[ruangan]:
            print(f"Ruangan {ruangan} sudah penuh! Silakan pilih ruangan lain.")
            continue
        
        while True:
            nama = input("Masukkan nama pasien: ")
            if nama.replace(" ", "").isalpha():
                break
            print("Nama hanya boleh berisi huruf dan spasi. Silakan coba lagi.")
        
        while True:
            umur = input("Masukkan umur pasien: ")
            if umur.isdigit() and 0 < int(umur) < 100:
                umur = int(umur)
                break
            print("Umur harus berupa angka di bawah 100. Silakan coba lagi.")
        
        while True:
            penyakit = input("Masukkan penyakit pasien: ")
            if penyakit.replace(" ", "").isalpha():
                break
            print("Penyakit hanya boleh berisi huruf dan spasi. Silakan coba lagi.")
        
        valid_keparahan = {"Ringan", "Sedang", "Berat"}
        while True:
            tingkat_keparahan = input("Masukkan tingkat keparahan (Ringan/Sedang/Berat): ")
            if tingkat_keparahan.capitalize() in valid_keparahan:
                tingkat_keparahan = tingkat_keparahan.capitalize()
                break
            print("Tingkat keparahan harus salah satu dari: Ringan, Sedang, Berat.")
        
        while True:
            tanggal_kontrol = input("Tanggal kontrol (dd-mm-yyyy): ")
            try:
                day, month, year = map(int, tanggal_kontrol.split('-'))
                if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                    break
                else:
                    print("Tanggal tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Format tanggal harus dd-mm-yyyy. Silakan coba lagi.")
        
        pasien = {
            "Nama": nama,
            "Umur": umur,
            "Penyakit": penyakit,
            "Tingkat Keparahan": tingkat_keparahan,
            "Tanggal Kontrol": tanggal_kontrol
        }
        
        data_rumah_sakit[ruangan].append(pasien)
        print(f"Pasien berhasil ditambahkan ke ruangan {ruangan}!")


def lihat_semua_pasien():
    for ruangan, pasien_list in data_rumah_sakit.items():
        print(f"\nRuangan: {ruangan} (Kapasitas: {len(pasien_list)}/{kapasitas_ruangan[ruangan]})")
        if not pasien_list:
            print("  Tidak ada pasien.")
        else:
            for i, pasien in enumerate(pasien_list, start=1):
                print(f"Pasien {i}:")
                for key, value in pasien.items():
                    print(f"  {key}: {value}")

def lihat_pasien_per_ruangan():
    print("\nPilih ruangan untuk melihat pasien:")
    ruangan_list = list(data_rumah_sakit.keys())
    for i, ruangan in enumerate(ruangan_list, start=1):
        print(f"{i}. {ruangan}")
    pilihan = input("Pilih nomor ruangan: ")
    if not pilihan.isdigit():
        print("Pilihan harus berupa angka.")
        return
    pilihan = int(pilihan)
    if 1 <= pilihan <= len(ruangan_list):
        ruangan = ruangan_list[pilihan - 1]
    else:
        print("Pilihan ruangan tidak valid.")
        return

    pasien_list = data_rumah_sakit[ruangan]
    print(f"\nPasien di ruangan {ruangan} (Kapasitas: {len(pasien_list)}/{kapasitas_ruangan[ruangan]}):")
    if not pasien_list:
        print("  Tidak ada pasien.")
    else:
        for i, pasien in enumerate(pasien_list, start=1):
            print(f"Pasien {i}:")
            for key, value in pasien.items():
                print(f"{key}: {value}")

def update_pasien():
    lihat_semua_pasien()
    ruangan = input("\nMasukkan nama ruangan pasien yang ingin diupdate: ")

    if ruangan not in data_rumah_sakit:
        print("Ruangan tidak valid.")
        return

    pasien_list = data_rumah_sakit[ruangan]
    if not pasien_list:
        print(f"Tidak ada pasien di ruangan {ruangan}.")
        return

    nomor_pasien = input("Masukkan nomor pasien yang ingin diupdate: ")
    if not nomor_pasien.isdigit():
        print("Nomor pasien harus berupa angka.")
        return
    nomor_pasien = int(nomor_pasien)
    if nomor_pasien < 1 or nomor_pasien > len(pasien_list):
        print("Nomor pasien tidak valid.")
        return

    pasien = pasien_list[nomor_pasien - 1]
    print("Masukkan data baru (tekan Enter untuk melewati):")
    pasien["Nama"] = input(f"Nama ({pasien['Nama']}): ") or pasien["Nama"]
    pasien["Umur"] = input(f"Umur ({pasien['Umur']}): ") or pasien["Umur"]
    pasien["Penyakit"] = input(f"Penyakit ({pasien['Penyakit']}): ") or pasien["Penyakit"]
    pasien["Tingkat Keparahan"] = input(f"Tingkat Keparahan ({pasien['Tingkat Keparahan']}): ") or pasien["Tingkat Keparahan"]
    pasien["Tanggal Kontrol"] = input(f"Tanggal Kontrol ({pasien['Tanggal Kontrol']}): ") or pasien["Tanggal Kontrol"]
    print("Data pasien berhasil diperbarui!")

def hapus_pasien():
    lihat_semua_pasien()
    ruangan = input("Masukkan nama ruangan pasien yang ingin dihapus: ")
    if ruangan in data_rumah_sakit:
        pasien_list = data_rumah_sakit[ruangan]
        if not pasien_list:
            print(f"Tidak ada pasien di ruangan {ruangan}.")
            return
        nomor_pasien = input("Masukkan nomor pasien yang ingin dihapus: ")
        if not nomor_pasien.isdigit():
            print("Nomor pasien harus berupa angka.")
            return
        nomor_pasien = int(nomor_pasien)
        if 0 < nomor_pasien <= len(pasien_list):
            pasien_list.pop(nomor_pasien - 1)
            print("Pasien berhasil dihapus!")
        else:
            print("Nomor pasien tidak valid.")
    else:
        print("Ruangan tidak valid.")

def pengelompokan_pasien():
    berat = []
    sedang = []
    ringan = []
    for ruangan, pasien_list in data_rumah_sakit.items():
        for pasien in pasien_list:
            tingkat = pasien["Tingkat Keparahan"]
            if tingkat == "Berat":
                berat.append(pasien["Nama"])
            elif tingkat == "Sedang":
                sedang.append(pasien["Nama"])
            elif tingkat == "Ringan":
                ringan.append(pasien["Nama"])
    print("\nPengelompokan Pasien Berdasarkan Tingkat Keparahan:")
    print("Pasien dengan keparahan Berat:")
    if berat:
        for nama in berat:
            print(f"- {nama}")
    else:
        print("Tidak ada")
    print("\nPasien dengan keparahan Sedang:")
    if sedang:
        for nama in sedang:
            print(f"- {nama}")
    else:
        print("Tidak ada")
    print("\nPasien dengan keparahan Ringan:")
    if ringan:
        for nama in ringan:
            print(f"- {nama}")
    else:
        print("Tidak ada")

def menu():
    while True:
        print("\nAda yang kami bisa bantu?")
        print("DAFTAR MENU RUMAH SAKIT FUAD HUSADA:")
        print("1. Tambah Pasien")
        print("2. Lihat Semua Pasien")
        print("3. Lihat Pasien per Ruangan")
        print("4. Update Pasien")
        print("5. Hapus Pasien")
        print("6. Pengelompokan Pasien")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")
        
        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            lihat_semua_pasien()
        elif pilihan == "3":
            lihat_pasien_per_ruangan()
        elif pilihan == "4":
            update_pasien()
        elif pilihan == "5":
            hapus_pasien()
        elif pilihan == "6":
            pengelompokan_pasien()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan pelayanan Rumah Sakit Fuad Husada!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()