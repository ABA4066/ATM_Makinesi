print("""
********************************

ATM Makinesine Hoş Geldiniz.

işlemler:

1.Bakiye Sorgula

2.Para Çek

3.Para Yatır

Çıkış için "q" basınız.

********************************\n
""")

bakiye=0

while True:
    islem = input("\nYapılacak işlem numarasını giriniz.\n")

    if islem == "1":
        print("\nMavcut Bakiyeniz {} Türk Lirasıdir\n".format(bakiye))
    elif islem == "2":
        tutar=int(input("\nÇekilecek tutarı giriniz\n"))
        if bakiye >= tutar:
            bakiye=bakiye-tutar
            print("\n{} Türk Lirası çekme işleminiz başarılıdır. Kalan bakiyenız {} Türk Lirasıdır.\n".format(tutar,bakiye))
        else:
            print("\nHesabınızda yeterli miktar bulunmamaktadır.\n")
    elif islem == "3":
        yatir=int(input("\nYatırılacak tutarı giriniz\n"))
        bakiye=bakiye+yatir
        print("\n{} Türk Lirası yatırma işleminiz başarılıdır. Güncel bakiyenız {} Türk Lirasıdır.\n".format(yatir, bakiye))
    elif islem == "q":
        print("\nATM Makinesinden Çıkılıyor.\nGüle Güle\n")
        break
    else:
        print("\nYanlış Giriş Yaptınız!\n")