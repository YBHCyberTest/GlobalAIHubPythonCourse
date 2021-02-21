class PatlicanMusakka():
    def __init__(self,Siviyag,Ortaboykurusogan,Ortaboycarlistonbiber,ortaboypatlican,yaglikiyma,domatessalcasi,tuz,karabiber,kimyon,domates,su):
        self.Siviyag = Siviyag
        self.Ortaboykurusogan = Ortaboykurusogan
        self.Ortaboycarlistonbiber = Ortaboycarlistonbiber
        self.ortaboypatlican = ortaboypatlican
        self.yaglikiyma = yaglikiyma
        self.domatessalcasi = domatessalcasi
        self.tuz = tuz
        self.karabiber = karabiber
        self.kimyon = kimyon
        self.domates = domates
        self.su = su
    def UrunlerinMikariA(self):
        print("Patlıcan Musakka Tarifi İçin Malzemeler")
        print("=======================================")
        print(f"2 yemek kaşığı {self.Siviyag}\n1 adet {self.Ortaboykurusogan}\n3 adet {self.Ortaboycarlistonbiber}\n4 adet {self.ortaboypatlican}\n300 gram az {self.yaglikiyma}\n1 yemek kaşığı {self.domatessalcasi}\n1 çay kaşığı\n1 {self.tuz} çay kaşığı {self.karabiber}\n1 çay kaşığı {self.kimyon}\n2 adet {self.domates}\n1 su bardağ {self.su}\n" )
    def PatlicanMusakkaTarifi(self):
         print("Patlıcan Musakka Tarifi Nasıl Yapılır?")
         print("======================================")
         print("1) Patlıcanların uç kısımlarını aldıktan sonra kabuklarını alacalı şekilde soyun.Halka halka kestiğiniz patlıcanları, acısının çıkması için bol tuzlu suda bekletin.\n2) Sıvıyağını tavada kızdırın ve yemeklik doğradığınız soğanları üzerine ekleyip pembeleşinceye kadar kavurun.Üzerine biberi ilave edip kavurmaya devam edin.\n3) Kıymayı, salçayı, tuzu, karabiberi ve kimyonu da ekleyip pişirmeye devam edin.\n4) Küp doğradığınız domatesleri de ekleyip pişirmeye bırakın. Domatesler piştikten sonra ocaktan alın.\n5) Patlıcanları kızartmak için ayçiçek yağını geniş tabanlı bir tavada kızdırın. Acısının çıkması için tuzlu suda bekleyen             patlıcanların suyunu süzdürün. Salata kurutucusu ya da kağıt havlu yardımıyla patlıcanları kuruladıktan sonra kızgın yağda arkalı önlü ters çevirerek kızartın.\n6) Altın rengini alan patlıcanları kızgın yağdan çıkarın ve ayrı bir tencereye dizin.\n7) Üzerine hazırladığınız kıymalı harcı da ekledikten\n8) Sonra 1 su bardağı su ilave edip 15 dakika pişirmeye bırakın.\n9) Sıcak olarak servis edin.\n")
    def PrintTarifiBitisi(self):
        print("========== Yemeğiniz Hazır Afiyet Olsun :) ==========")
   
class Mucver(PatlicanMusakka):
    def __init__(self,kabak,yumurta,havuc,un,sogan,dereotu,tuz,karabiber):
        self.kabak = kabak
        self.yumurta = yumurta
        self.havuc = havuc
        self.un = un
        self.sogan = sogan
        self.dereotu = dereotu
        self.tuz = tuz
        self.karabiber = karabiber
    def UrunlerinMikariB(self):
        print("Mücver Tarifi İçin Malzemeler")
        print("=============================")
        print(f"3 adet {self.kabak}\n2 adet {self.yumurta} (çırpılmış)/n 1 adet {self.havuc}\n3 kahve fincanı {self.un}\n1 demet taze {self.sogan}\n1 demet { self.dereotu}\n1 tatlı kaşığı {self.tuz}\n1 çay kaşığı{self.karabiber}\n")
    def MucverTarifi(self):
         print("Mucver Tarifi Nasıl Yapılır?")
         print("============================")
         print("1) Bol suda yıkadığınız kabakları rendenin iri kısmıyla rendeleyin.\n2) Mücveri sulandırmaması için; rendelenmiş kabakların suyunu sıkarak çıkartın.\n3) Geniş bir kapta rendelenen kabakları, havucu, 2 adet çırpılmış yumurtayı, 1 demet taze soğanı, 1 demet dereotunu, 1 tatlı kaşığı tuzu, karabiberi ve 3 kahve" "fincanı unu birleştirin.\n4) Tüm malzemeler birbiriyle harmanlanıp, macun kıvamını alana kadar spatula yardımıyla karıştırın.\n5) Her bir mücver 1 tepeleme yemek kaşığı olacak şekilde ayarlayın.\n6) Kızgın yağda altın sarısı rengini alana kadar kızartın.\n7) Mücverlerin fazla yağını havlu kağıda süzdürdükten sonra servis tabağına alın ve çırpılmış yoğurt ile servis edin.\n ")
        
         
class EtSote(PatlicanMusakka):
    def __init__(self, danaeti,zeytinyagi,ortaboykurusogan,ortaboydomates,ortaboyyesilbiber,domatessalcasi,bibersalcasi,sicaksu,tuz,tazecekilmistanekarabiber,kekik):
        self.danaeti = danaeti
        self.zeytinyagi = zeytinyagi
        self.ortaboykurusogan = ortaboykurusogan
        self.ortaboydomates = ortaboydomates
        self.ortaboyyesilbiber = ortaboyyesilbiber
        self.domatessalcasi = domatessalcasi
        self.bibersalcasi = bibersalcasi
        self.sicaksu = sicaksu
        self.tuz = tuz
        self.tazecekilmistanekarabiber = tazecekilmistanekarabiber
        self.kekik = kekik
    def UrunlerinMikariC(self):
        print("Et Sote Tarifi İçin Malzemeler")
        print("==============================")
        print("600 gram sotelik {self.danaeti}\n4 yemek kaşığı {self.zeytinyagi}\n1 adet {self.ortaboykurusogan}(yemeklik doğranmış)\n2 adet {self.ortaboydomates}(kabukları soyulmuş, doğranmış)\n3 adet {self.ortaboyyesilbiber}(doğranmış)\n1 tatlı kaşığı {self.domatessalcasi}\n1/2 tatlı kaşığı {self.bibersalcasi}\n1 su bardağıs {self.sicaksu}\n1 çay kaşığı {self.tuz}\n1/2 çay kaşığı {self.tazecekilmistanekarabiber} \n1 tatlı kaşığı {self.kekik}\n")
    def EtSoteTarifi(self):
        print("Et Sote Tarifi Nasıl Yapılır?")
        print("=============================")
        print("1) Döküm bir tavada 4 yemek kaşığı zeytinyağını kızdırın. 1 adet yemeklik ince doğradığınız soğanları tavaya ekleyin.\n2) Renk alan soğanların üzerine 3 adet doğranmış yeşil biber ekleyin ve sotelemeye devam edin.\n3) Sotelik doğradığınız 600 gram dana etini ilave edin.\n4) Suyunu salmaması, lezzet ve vitamin değerini hapsetmesi için; yüksek ateşte, yaklaşık 2-3 dakika hiç karıştırmadan mühürleyin.\n 5) Dış kısmı renk alan etleri aralarda karıştırarak yüksek ateşte sotelemeye devam edin.\n6) 3 adet soyulmuş ,doğranmış domatesi ekleyerek karıştırın. Ardından 1 çay kaşığı tuz, karabiber, 1 tatlı kaşığı kekiği de ekleyin.\n7) Birer yemek kaşığı biber ve domates salçasını 1 su bardağı sıcak su ile sulandırdıktan sonra azar azar tavaya ekleyin.\n 8) Kısık ateşte etler yumuşayana kadar pişirin.\n9) Etleri yumuşayan soteyi, lezzetli suyuyla birlikte servis tabaklarına alın ve sıcak sıcak servis edin.\n")
    
patlicanMusakka=PatlicanMusakka("Sıvıyağ","Orta boy kuru soğan","Orta boy çarliston biber","orta boy patlıcan","yaılı kıyma","domates salçası","tuz","karabiber","kimyon","domates","su")
mucver=Mucver("kabak","yumurta","havuç","un","soğan","dereotu","tuz","karabiber")
etSote=EtSote("dana eti","zeytinyaği","orta boy kuru soğan","orta boy domates","orta boy yeşil biber","domates salçası","biber salçası","sıcak su","tuz","taze çekilmiş tane karabiber","kekik")

while(True):
    print("=======================================")
    print("*====  YemekLerin Tarif Listesi : ====*")
    print("|     1- Patlican Musakka Tarifi.     |\n|     2- Mucver Tarifi                |\n|     3 - Et Sote Tarifi              |")
    print("=======================================\n")
    Sectim=int(input("Hangi Yemek Tarifini Bilmek İstersiniz ? 1 , 2 ya da 3 Şeklinde Bir Seçenek Yazın : "))
    if(Sectim==1):
        patlicanMusakka.UrunlerinMikariA()
        patlicanMusakka.PatlicanMusakkaTarifi()
        patlicanMusakka.PrintTarifiBitisi()
    elif(Sectim==2):
        mucver.UrunlerinMikariB()
        mucver.MucverTarifi()
        mucver.PrintTarifiBitisi()

    elif(Sectim==3):
        etSote.UrunlerinMikariC()
        etSote.EtSoteTarifi()
        etSote.PrintTarifiBitisi()
    else:
        print("Girdiğimiz Seçenek Size Sunduğumuz Seçeneklerin Arasında Bulunmamaktadır.Lüfen 1 , 2 ya da 3 Şeklinde Bir Seçeneklenden Bir Tane Seçin ")
    devam=input("Başka Bir Yemek TarSSSSSSifine Bakmak İsiyor musunuz? E/H Seklinde Bir Seçenek Giriniz : ")
    if(devam == "H" or devam == "h") :
        print("Uygulamamızı Kullandığınız İçin Teşekkür ederiz :)")
        break

    




    
    

    
    

    
    

    
    



        
        
    

        










    
