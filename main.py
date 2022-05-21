import time

print("===================")
print("KDV Hesaplayıcı v1.0 - developed by whiskydev")
print("===================")
print("Ana Menü")

secim = input("\nBaşlamak için bir işlem seçin \n[1] Programı Başlat \n[2] Krediler \n[3] Çıkış \n")

if (secim == "1"):
  print("Program başlatıldı. \n")
  try:
    fiyat1 = int(input("Ürün Fiyatı: "))
  except ValueError:
    print("Geçersiz bir fiyat belirtildiği için program sonlandırıldı.")
    exit()
  kdvoran = input("KDV Oranı: ")
  if (kdvoran.startswith("%")):
    print("===== Hesaplanıyor.. =====")
    time.sleep(2)
    oran = int(kdvoran.strip("%"))
    oran2 = (fiyat1 * oran) / 100
    sonuc = fiyat1 + oran2
    print("===== Sonuç ==============")
    print(f"KDV Oranı: {oran2} TL \nKDV'siz Fiyat: {fiyat1} TL \nKDV Eklenmiş Fiyat: {sonuc} TL")
    print("==========================")
  elif (kdvoran.endswith("%")):
    print("===== Hesaplanıyor.. =====")
    time.sleep(2)
    oran1 = int(kdvoran.strip("%"))
    oran3 = (fiyat1 * oran1) / 100
    sonuc2 = fiyat1 + oran3
    print("===== Sonuç ==============")
    print(f"KDV Oranı: {oran3} TL \nKDV'siz Fiyat: {fiyat1} TL \nKDV Eklenmiş Fiyat: {sonuc2} TL")
    print("==========================")
  else:
    print("===== Hesaplanıyor.. =====")
    time.sleep(2)
    oran4 = int(kdvoran.strip("%"))
    oran5 = (fiyat1 * oran4) / 100
    sonuc3 = fiyat1 + oran5
    print("===== Sonuç ==============")
    print(f"KDV Oranı: {oran5} TL \nKDV'siz Fiyat: {fiyat1} TL \nKDV Eklenmiş Fiyat: {sonuc3} TL")
    print("==========================")
elif (secim == "2"):
  print("Github: github.com/whiskydev11 \nWeb: whiskydev.xyz \n© 2022")
elif (secim == "3"):
  print("Çıkış Sağlandı.")
else:
  print("Geçersiz Kod")


