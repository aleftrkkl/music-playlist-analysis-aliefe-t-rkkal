# music-playlist-analysis-aliefe-t-rkkal
şarkı playlist analiz ödevi
## Proje Amaci

Bu proje, bir muzik playlist analiz sistemi olusturmayi amaclamaktadir. Program, sarki listesi uzerinde cesitli analizler yaparak toplam sure, ortalama sure, en cok dinlenen sarki gibi bilgileri hesaplar ve kullaniciya sunar. Proje, Python programlama dilinde method kullanimi ve veri yapilari (liste, sozluk) konularini pekistirmek icin hazirlanmistir.

## Veri Yapisi

Her sarki asagidaki bilgileri icerir ve liste icinde sozluk olarak tutulur:

- **ad**: Sarki adi
- **sanatci**: Sanatci adi
- **sure**: Sarki suresi (saniye cinsinden)
- **dinlenme**: Dinlenme sayisi

## Method Aciklamalari

| Method | Aciklama |
|--------|----------|
| `get_total_duration(songs)` | Tum sarkilarin toplam suresini saniye olarak hesaplar |
| `get_most_played_song(songs)` | En cok dinlenen sarkiyi bulur ve dondurur |
| `get_average_duration(songs)` | Ortalama sarki suresini hesaplar |
| `print_playlist(songs)` | Playlist icerigini duzenli bir sekilde ekrana yazdirir |
| `get_longest_song(songs)` | *(Bonus)* En uzun sureye sahip sarkiyi bulur |
| `filter_by_artist(songs, sanatci_adi)` | *(Bonus)* Belirtilen sanatcinin sarkilarini filtreler |
| `sort_by_plays(songs)` | *(Bonus)* Sarkilari dinlenme sayisina gore buyukten kucuge siralar |
| `main()` | Sarki listesini olusturur ve tum methodlari calistirir |

## Calistirma Bilgisi

Programi calistirmak icin terminal veya komut satirinda asagidaki komutu yaziniz:

```
python main.py
```

## Kullanilan Teknolojiler

- Python 3
- Liste ve Sozluk veri yapilari

## Ornek Cikti

```
==================================================
        PLAYLIST
==================================================
1. Sarki: Blinding Lights
   Sanatci: The Weeknd
   Sure: 200 saniye
   Dinlenme: 3500000 kez
--------------------------------------------------
2. Sarki: Shape of You
   Sanatci: Ed Sheeran
   Sure: 234 saniye
   Dinlenme: 5800000 kez
--------------------------------------------------
...

Toplam Sure: 1476 saniye
Toplam Sure: 24 dakika 36 saniye

Ortalama Sarki Suresi: 246.0 saniye

En Cok Dinlenen Sarki: Shape of You - Ed Sheeran
   Dinlenme Sayisi: 5800000 kez
```
