# ============================================
# Music Playlist Analysis System
# Python Bireysel Odevi
# ============================================

# Tum sarkilarin toplam suresini hesaplayan method
def get_total_duration(songs):
    toplam = 0
    for sarki in songs:
        toplam = toplam + sarki["sure"]
    return toplam


# En cok dinlenen sarkiyi bulan method
def get_most_played_song(songs):
    en_cok = songs[0]
    for sarki in songs:
        if sarki["dinlenme"] > en_cok["dinlenme"]:
            en_cok = sarki
    return en_cok


# Ortalama sarki suresini hesaplayan method
def get_average_duration(songs):
    toplam = get_total_duration(songs)
    ortalama = toplam / len(songs)
    return ortalama


# Playlisti duzenli sekilde yazdiran method
def print_playlist(songs):
    print("=" * 50)
    print("        PLAYLIST")
    print("=" * 50)
    sira = 1
    for sarki in songs:
        print(f"{sira}. Sarki: {sarki['ad']}")
        print(f"   Sanatci: {sarki['sanatci']}")
        print(f"   Sure: {sarki['sure']} saniye")
        print(f"   Dinlenme: {sarki['dinlenme']} kez")
        print("-" * 50)
        sira = sira + 1


# BONUS: En uzun sarkiyi bulan method
def get_longest_song(songs):
    en_uzun = songs[0]
    for sarki in songs:
        if sarki["sure"] > en_uzun["sure"]:
            en_uzun = sarki
    return en_uzun


# BONUS: Sanatciya gore filtreleme yapan method
def filter_by_artist(songs, sanatci_adi):
    sonuc = []
    for sarki in songs:
        if sarki["sanatci"] == sanatci_adi:
            sonuc.append(sarki)
    return sonuc


# BONUS: Dinlenme sayisina gore siralama yapan method
def sort_by_plays(songs):
    # Listeyi kopyalayalim ki orijinal liste bozulmasin
    kopya = []
    for sarki in songs:
        kopya.append(sarki)

    # Basit siralama (Bubble Sort)
    n = len(kopya)
    for i in range(n):
        for j in range(0, n - i - 1):
            if kopya[j]["dinlenme"] < kopya[j + 1]["dinlenme"]:
                gecici = kopya[j]
                kopya[j] = kopya[j + 1]
                kopya[j + 1] = gecici
    return kopya


# Ana method - programin calistigi yer
def main():
    # Sarki listesi olusturma (liste icinde sozluk)
    sarkilar = [
        {
            "ad": "Blinding Lights",
            "sanatci": "The Weeknd",
            "sure": 200,
            "dinlenme": 3500000
        },
        {
            "ad": "Shape of You",
            "sanatci": "Ed Sheeran",
            "sure": 234,
            "dinlenme": 5800000
        },
        {
            "ad": "Bohemian Rhapsody",
            "sanatci": "Queen",
            "sure": 355,
            "dinlenme": 2100000
        },
        {
            "ad": "Bad Guy",
            "sanatci": "Billie Eilish",
            "sure": 194,
            "dinlenme": 4200000
        },
        {
            "ad": "Perfect",
            "sanatci": "Ed Sheeran",
            "sure": 263,
            "dinlenme": 4900000
        },
        {
            "ad": "Starboy",
            "sanatci": "The Weeknd",
            "sure": 230,
            "dinlenme": 3100000
        }
    ]

    # Playlisti yazdir
    print_playlist(sarkilar)

    # Toplam sureyi hesapla ve yazdir
    toplam_sure = get_total_duration(sarkilar)
    print(f"\nToplam Sure: {toplam_sure} saniye")
    print(f"Toplam Sure: {toplam_sure // 60} dakika {toplam_sure % 60} saniye")

    # Ortalama sureyi hesapla ve yazdir
    ortalama = get_average_duration(sarkilar)
    print(f"\nOrtalama Sarki Suresi: {ortalama:.1f} saniye")

    # En cok dinlenen sarkiyi bul ve yazdir
    en_populer = get_most_played_song(sarkilar)
    print(f"\nEn Cok Dinlenen Sarki: {en_populer['ad']} - {en_populer['sanatci']}")
    print(f"   Dinlenme Sayisi: {en_populer['dinlenme']} kez")

    # BONUS: En uzun sarkiyi bul ve yazdir
    en_uzun = get_longest_song(sarkilar)
    print(f"\nEn Uzun Sarki: {en_uzun['ad']} - {en_uzun['sanatci']}")
    print(f"   Sure: {en_uzun['sure']} saniye")

    # BONUS: Sanatciya gore filtreleme
    print("\n" + "=" * 50)
    aranan_sanatci = "Ed Sheeran"
    print(f"'{aranan_sanatci}' Sarkilari:")
    print("=" * 50)
    filtreli = filter_by_artist(sarkilar, aranan_sanatci)
    for sarki in filtreli:
        print(f"  - {sarki['ad']} ({sarki['sure']} saniye)")

    # BONUS: Dinlenme sayisina gore siralama
    print("\n" + "=" * 50)
    print("Dinlenme Sayisina Gore Siralama:")
    print("=" * 50)
    sirali = sort_by_plays(sarkilar)
    sira = 1
    for sarki in sirali:
        print(f"  {sira}. {sarki['ad']} - {sarki['dinlenme']} dinlenme")
        sira = sira + 1


# Programi calistir
main()
