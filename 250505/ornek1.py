toplam = 0
s1 =int(input("Küçük olan sayıyı girin :"))
s2 =int(input("Büyük olan sayıyı girin : "))
 
 for sayi in range(s1,s2):
    if sayi % 2 == 0:
        toplam = toplam + sayi 
print(s1,"ile",s2,"sayıları arasındakı çift sayıların toplamı:",toplam)