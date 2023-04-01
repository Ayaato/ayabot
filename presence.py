from pypresence import Presence
import time
import random

client_id = 'yourCliendID'
RPC = Presence(client_id)
RPC.connect()

quotes = [
    "Kandil'e atom bombası fırlatıyor.",
    "Abdülhamid'i indiriyor.",
    "Menderes'i asıyor.",
    "Muharrem İnce'ye oy veriyor.",
    "İstiklal Harbine katılıyor.",
    "Cumaya gidiyor.",
    "Cumhuriyeti ilan ediyor.",
    "İstanbul'u fethediyor.",
    "Memlüklüleri tarihten siliyor.",
    "Turan'ı kuruyor.",
    "İHA-SİHA üretiyor.",
    "IŞİD üyelerinin kafasını kesiyor.",
    "İstiklal mahkemesinde Şeyh Sait'in idam kararını söylüyor.",
    "Çanakkale'yi savunuyor.",
    "Paris'e 2 saat uzaklıkta Osmanlı İmparatorluğunda kahve içiyor."
]


while True:

    RPC.update(
        large_image="soldier",
        large_text="Ayato",
        details="Ayabot şu anda:",
        state=random.choice(quotes),
        start=int(time.time()),
        buttons=[
            {
                "label":"Ayabot'u sunucuna ekle",
                "url":"https://discord.com/api/oauth2/authorize?client_id=968635789955186711&permissions=8&scope=bot"
                },
            {
                "label":"Ayabot'un kaynak kodu",
                "url":"https://github.com/Ayaato/ayabot"
                }
            ]
    )

    time.sleep(5)