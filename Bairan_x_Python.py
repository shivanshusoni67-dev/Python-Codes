import time
import sys 

print("🎵 NOW PLAYING - BANJARE-BAIRAN 💗")

def print_lyrics():
    lyrics = [ 
        "Je Tu Thodi Ghabraja,Meri Yadd Tanne Aaja" ,
        "Tu De Diye Awaaz,Re Mainn Aa Jaunga😊",
        "Todu Duniya KI Reet,Re Ke Haar,Re ke Jeet🥰" ,
        "Manne Chahiye Teri Preet,Main Nibha Jaunga 💑",
        "Dekh, Bawla Bana Gyi Manne Likhna Sikha gyi 🙌",
        "Hayee 💗 Noch - Noch Kha Gyi Teri Bairan Judai Manne "
    ]
    delays = [
        1.6 , 1.2 , 1.2, 0.7 , 0.3, 0.3 
    ]

    print(" BANJARE-BAIRAN : /n ")
    time.sleep(1.2)

    for i , line in enumerate (lyrics):
        for char in line :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8) 
print_lyrics()
