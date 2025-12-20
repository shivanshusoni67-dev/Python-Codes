import time
import sys 

print("🎵 NOW PLAYING - PAL PAL ❣ ")

def print_lyrics():
    lyrics = [ 
        "Mein Aab Kyu Hosh Mein Aata Nahi ?",
        "Sukoon Yeh Dil Kyon Pata Nahi ?",
        "Kyun Todun Khud Se Jo The Waade ",
        "Ke Aab Yeh Ishq Nibhana Nahi ?",
        "Mein Morrun Tum Je Jo Yeh Chehra ",
        "Doobara Nazar Milana Nahi",
        "Yeh Duniya Jaane Mera Dard ",
        "Tujhe Yeh nazar Kyu Aata Nahi ?",
        "Soneya Yun Tera Sharmana  " , 
        "Meri Jaan Na Lele"
    ]
    delays = [
        0.3 , 0.3 ,0.4, 0.3 , 0.3, 0.3 , 0.8
    ]

    print(" Pal Pal : /n ")
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
