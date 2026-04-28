# Toplam sureyi hesaplayan method
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

# Ortalama sureyi hesaplayan method
def get_average_duration(songs):
    toplam = get_total_duration(songs)
    ortalama = toplam / len(songs)
    return ortalama

# Playlisti yazdiran method
def print_playlist(songs):
    print("---- PLAYLIST ----")
    sira = 1
    for sarki in songs:
        print(str(sira) + ". " + sarki["ad"] + " - " + sarki["sanatci"])
        print("   Sure: " + str(sarki["sure"]) + " saniye")
        print("   Dinlenme: " + str(sarki["dinlenme"]))
        print("------------------")
        sira = sira + 1

# En uzun sarkiyi bulan method
def get_longest_song(songs):
    en_uzun = songs[0]
    for sarki in songs:
        if sarki["sure"] > en_uzun["sure"]:
            en_uzun = sarki
    return en_uzun

# Sanatciya gore filtreleyen method
def filter_by_artist(songs, sanatci_adi):
    sonuc = []
    for sarki in songs:
        if sarki["sanatci"] == sanatci_adi:
            sonuc.append(sarki)
    return sonuc

# Dinlenmeye gore siralayan method
def sort_by_plays(songs):
    sirali = sorted(songs, key=lambda x: x["dinlenme"], reverse=True)
    return sirali

# Ana method
def main():
    # Sarki listesi (liste icinde sozluk)
    sarkilar = [
        {"ad": "Blinding Lights", "sanatci": "The Weeknd", "sure": 200, "dinlenme": 3500000},
        {"ad": "Shape of You", "sanatci": "Ed Sheeran", "sure": 234, "dinlenme": 5800000},
        {"ad": "Bohemian Rhapsody", "sanatci": "Queen", "sure": 355, "dinlenme": 2100000},
        {"ad": "Bad Guy", "sanatci": "Billie Eilish", "sure": 194, "dinlenme": 4200000},
        {"ad": "Perfect", "sanatci": "Ed Sheeran", "sure": 263, "dinlenme": 4900000}
    ]

    # Playlisti yazdir
    print_playlist(sarkilar)

    # Toplam sure
    toplam = get_total_duration(sarkilar)
    print("Toplam Sure: " + str(toplam) + " saniye")

    # Ortalama sure
    ortalama = get_average_duration(sarkilar)
    print("Ortalama Sure: " + str(round(ortalama, 1)) + " saniye")

    # En cok dinlenen
    en_populer = get_most_played_song(sarkilar)
    print("En Cok Dinlenen: " + en_populer["ad"] + " - " + en_populer["sanatci"])

    # BONUS: En uzun sarki
    en_uzun = get_longest_song(sarkilar)
    print("En Uzun Sarki: " + en_uzun["ad"] + " (" + str(en_uzun["sure"]) + " saniye)")

    # BONUS: Sanatciya gore filtreleme
    print("\nEd Sheeran Sarkilari:")
    filtreli = filter_by_artist(sarkilar, "Ed Sheeran")
    for sarki in filtreli:
        print("  - " + sarki["ad"])

    # BONUS: Dinlenmeye gore siralama
    print("\nDinlenmeye Gore Siralama:")
    sirali = sort_by_plays(sarkilar)
    for sarki in sirali:
        print("  " + sarki["ad"] + " - " + str(sarki["dinlenme"]) + " dinlenme")

main()
