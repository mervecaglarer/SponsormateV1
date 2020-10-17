import csv

clusterDict={
    "Kariyer Planlama" : ["youthall.com","toptalent.co","kariyer.net","anbean.co","anlatsin.com","secretcv.com","İşkur","Kosgeb"],
    "Market" : ["Migros","Metro Market","Makro Market","Onur Market"],
    "Banka-Sigorta" : ["Albaraka","Garanti BBVA","Türkiye İş Bankası","ING","Teb","Finansbank","Anadolubank","Halkbank","Yapı Kredi","Türkiye Finans Katılım Bankası","Akbank","Ak Sigorta","Axa Sigorta","Anadolu Sigorta","Allianz","Avivasa","Hopi","Troy","seninbankan.com","Metlife Emeklilik","Gelecek Varlık Yönetimi"],
    "Yemek" : ["Hmbrgr","Subway","Papa Jones","KFC","Hacı Hasan Oğulları Baklava Börek","Bülent Börekçilik","Dominos Pizza","Şampiyon Kokoreç","Çıtır Simit","Papa Johns Pizza","Arabica Coffee House","Pidem","Karaköy Güllüoğlu","Alaçatı Muhallebecisi","yemekumbara.com","zomato.com","Oses Çiğköfte","Kahve Durağı","Kahve Dünyası","Adıyaman Çiğköftecisi Ömer Aybak"],
    "Online Alışveriş" : ["sosyopix.com","robotistan.com","cimri.com","turna.com","obilet.com","biletbayi.com","biletino.com","trendyol.com","n11.com","Morhipo","hepsiburada.com","gittigidiyor.com","yemeksepeti.com","istegelsin.com"],
    "Kitap-Kırtasiye" : ["D&R","Edding Kalem","Uniball Pencil","Seçkin Yayıncılık","Abaküs Kitap","uzmankariyer.com","Kodlab"],
    "Medya" : ["Donanım Haber","Hürriyet Gazetesi","TGRT Haber","Bloomberg","Nisan Reklam","savunmasanayiidergilik.com","ekometre.com","biomedya.com","capital.com.tr","pazarlamaturkiye.com","haberinadresi.com","webtekno.com","shiftdelete.net","ceyrekmuhendis.com","muhendisbeyinler.net","bilimsenligi.com","uniaktivite.com","ogrencikariyeri.com","kampusetkinlikleri.com","universitemedya.com.tr","kampustenevar.com","endustrimuhendisligim.com","acunmedya.com","gzt.com","uludagsozluk.com","sliconf.com","Branding Türkiye","Turkishtime"],
    "İçecek" : ["Ofçay","Jacobs","Coca Cola","Pepsico","RedBull","Black Bruin Enerji İçecegi","Nescafe","Obsesso","Esperro Kahve","Kuru Kahveci Mehmet Efendi","Lipton","Çaykur","Doğuş Çay","Uludağ","Dimes","Fujitsu","Juss","Sırma","Sarıyer Gazoz","Oğuz Holding"],
    "Temizlik-Bakım" : ["P&G","Eczacıbaşı","Kotex","Colgate","Bioderma","Cosmed","Loreal Paris","Yves Rocher","platin.com.tr","Watsons","Gratis","Farmasi","Avon","Henkel","Hobby Kozmetik","La Prairie Parfüm","Diversey Hijyen Çözümleri"],
    "Gıda" : ["Unilever","Mondelez International","Ak Gıda","Özbesin","Pladis","Dr Oetker","Nestle","Pınar","Eti","Ülker","Elit Çikolata","Tadelle","Godiva","Cukulats","Gece Kuşu Cookies","7 Days Kruvasan","Yayla Bakliyat","Ankara Makarna","Oba Makarna","Arbella Makarna","Indomie Noodle","Tada","Uno","Feast","Hastavuk","Banvit","Tat","Eker","Sek","Patos","Mentos","Danone","Algida","Golf Dondurma","Pernigotti Dondurma","Balparmak","Asil Fırın","Juitox","Düzey Pazarlama"],
    "Seyahat-Tatil" : ["Met Global","Uber","Pamukkale Turizm","Çanakkale Truva Turizm","turluyoruz.com","gezimingo.com","eyobus.com.tr","zipcar.com.tr","THY","TAV Havalimanları"],
    "Kar Amacı Gütmeyen Kuruluşlar" : ["Türkiye Siber Güvenlik Kümelenmesi","Otomder(Otomotiv Mühendisliği Derneği)","MMO(Makine Mühendisleri Odası) İstanbul","İthib (İstanbul Tekstil ve Hammaddeleri İhracatçılar Birliği)","Athib (Akdeniz Tekstil ve Hammaddeleri İhracatçıları Birliği)","İKMİB(İstanbul Kimyevi Maddeler ve Mamulleri İhracatçıları Birliği","TÇMB(Türkiye Çimento Müstahsilleri Birliği)","Sabancı Üniversitesi","Kızılay","europass.gov.tr","askidanevar.com"],
    "Otomobil" : ["Ford Otosan","Honda","Mercedes","Volvo","Renault","Oyak Renault","BMC","Otokar","Tırsan","Karsan","Otokoç Otomotiv"],
    "Giyim" : ["Altınyıldız Classics","DS Damat","Hatemoğlu","İpekyol"," Tudors","Suwen","Beymen","LTB","Kiğılı","Defacto","Koton","LC Waikiki","Mavi","Decathlon","Flo","Ayakkabı Dünyası","So Chıc","Oz Pack","Allday Giyim","Orka Holding","Dönmezler Lisans"],
    "Mobilya-Ev" : ["Arçelik","Vestel","Bosch","Siemens","Doğtaş","Mondelez","Asedia Mobilya","Minteks Mobilya","Karaca","Ikea","Koçtaş","Silverline Ankastre"],
    "Petrol" : ["Aytemiz","Petrol Ofisi","Opet","Tüpraş"],
    "Danışmanlık" : ["Sinerji Eğitim & Organizasyon","Makers Türkiye","Workinton","KPMG Danışmanlık Hizmetleri","Caligo Danışmanlık","KornFerry","ACCA Global","Ernst & Young Türkiye","Deloitte Türkiye","İtibar Atölyesi Halkla İlişkiler Ajansı ","Workinlot","GSK Türkiye","PWC Turkey","Saina Danışmanlık ve Mühendislik"],
    "Sanayi" : ["TAI(Türk Havacılık ve Uzay Sanayii)","TEI(TUSAŞ Motor Sanayii)","Şişecam","Çalık Enerji","Aselsan","Havelsan","Roketsan","Turkish Technic (Türk Hava Yolları Teknik A.Ş)","Yeşilyurt Enerji","Borusan","Digitest Savunma ve Havacılık"],
    "Organizasyon" : ["If Performance","Hayal Kahvesi","Jolly Joker","MacFit Spor Salonu","6:45 Kaybedenler Kulübü"],
    "Eğitim" : ["Üniyurt","Dilko English","Connect Yurtdışı Eğitim Danışmanlığı","Endless Yurtdışı Eğitim","Bemar Kariyer Okulu","English Time Dil Okulu","American Life Dil Okulları","Amerikan Kültür Derneği Dil Okulları","British English Dil Okulu","British Centre Languages Course","British Town Language School","British Time Dil Okulları","Manchester Dil Okulları","Truva Akademi","Yds Academy","Mentora College","Pegem Akademi","Murat Eğitim Kurumları","Teol Dil Okulları","Berlitz Dil Okulu"],
    "Holding" : ["Anadolu Grubu","Koç Holding","Güriş Holding","Yıldız Holding","Doğuş Grubu","Borsan Grup","Kale Grubu","Esas Holding","Kipaş Holding","Scalex Startup","Akkim","Macgal Group","Sanko Holding","ALARKO Grubu","Kanık Group of Companies","Mars Turkey","Disney Türkiye"],
    "İnşaat" : ["STFA","Akçansa Çimento","TAV İnşaat","Fibrobeton","Betonex","Kordsa","Freysaş","Layher İskele","Özler Kalıp Ve İskele","Emay Uluslararası Mühendislik ve Müşavirlik","Urtim Kalıp ve İskele Sistemleri","GAP İnşaat","Rönesans Gayrimenkul Yatırım ","TEKFEN İnşaat","Hilti Yapı Malzemeleri","Autodesk Yazılım","Yapı Merkezi İnşaat ve Sanayi ","Cengiz İnşaat","Prota Mühendislik","Çimsa Çimento","Cat(İnşaat ve Madencilik Ekipmanları)","Rieter Tekstil Makineleri","Polisan","Egger Group","Knauf İnşaat Hizmetleri","Çelik Halat"],
    "Teknoloji-1" : ["Peak Games","Riot Games","JetBrains","Nvidia","Cisco","IBM","HP","Monster","Lenovo","Huawei","Nokia","s-Link","zeplin.io","Media Markt","Türk Telekom","Vodafone","Turkcell","Google","Microsoft","Instax Fujifilm","reeder"] ,
    "Teknoloji-2" : ["Etıya Yazılım","Netaş","Bigworks","connected2.me","Hotech Software","Pixery","Logo Yazılım","Bilge Adam","Trendyol Tech","Elmer","İga Bilişim","Enka Systems Yazılım","Maxim Integrated","GHS(ghs-globalhealth.com)","Commencis Technology Company","Adesso Yazılım"],
    "Teknoloji-3" : ["Neteks Teknoloji Ürünleri","Erguvan Creative","indir.com","tamindir.com","nonolive.com","hadilive.com","unikuni.com","peerbie.com","Ledeks Dijital Teknoloji ","Akınsoft","Artım Bilişim","Index Group","Intertech"],
    "Ankara Yerel" : ["Karikatur Kafe Mahall","Data Akademi","Odtü Teknokent","Bilkent Cyberpark Teknokent","Bitss Bilişim Hizmetleri ","Mimtek Akademi","Dört Beceri Yabancı Dil Okulları","Kocatepe Kahve Evi","Pizza Time","Latif Baba Dönercisi ","Baykuş Cafe","Çiftay İnşaat","Kazan Soda Elektrik"],
    "Bursa Yerel" : ["Nominal Şirketler Grubu","Ergün Kent İnşaat","Fil Döner","Aşgana","Lebon","Geveze Cafe","Kafe Servis"],
    "Muğla Yerel" : ["Afra Reklam","Özlem Pastanesi"],
    "Samsun Yerel" : ["Hor10 Toptan Satış"],
    "İstanbul Yerel" : ["ShakeShack","SimitBox","İsfanbul Temapark","İTÜNOVA TTO(Teknoloji Transfer Ofisi)","EnterTech Teknokent","ŞenayAkın Kuyumculuk Atölyesi","Akkurtlar Turizm","Smartpro Bilgisayar Akademisi","Çobanpınar Kaynak Suyu","Dorock","Pub Story","Adgager","Core Electronics","Vidimax Productions","Ticimax Yazılım","Üsküdar Gençlik Merkezi","Myfix Yapı Kimyasalları","Taypa Tekstil","TYH Tekstil","Merkaş Tekstil","Baykanlar Tekstil","Hassan Tekstil","Oğuz Tekstil","Desu Tekstil","Esmanur Butik","Taha Giyim","Aydın Mensucat Kumaş","Ayışığı Pansiyon","Ağva Seferoğulları Kamping","Bitti Gitti Shop","Güneş Kırtasiye"],
    "Kocaeli Yerel" : ["Coffee Chef"],
    "Balıkesir Yerel" : ["Çiğköfteci Ömer Usta"],
    "Antalya Yerel" : ["Bumin Yazılım","Santsg(SAN Tourism Software Group)","Robiduck(robiduck.com)","Koreli Otel"],
    "Osmaniye Yerel" : ["Bayram Efendi Osmanlı Kahvecisi","Cadde Döner","Çıtır Kuruyemiş"],
    "Düzce Yerel" : ["Palmiye Çiçekçilik","Uzunlar Reklam","Turan Ofset Matbaa","The Chef Fastfood Cafe","Masal Cafe","Choplin Cafe","Rigo Hookah Coffee","Demir Bektaşoğlu Kuaför & Güzellik Merkezi"],
    "Zonguldak Yerel" : ["Ofkar Madencilik","Asya Su"],
    "Eskişehir Yerel" : ["Mandarins Restaurant","More&More Coffee","112 Coffee","Bi Lookma","Marina Cafe","EsTo Künefe","Zeus Bargama Tostçusu","Adımlar Kitap&Kafe","Cups&Pups","Jaja Cafe","Nohut Dürüm","Pilove Point Ev Yemekleri","New York Cafe","Kedd Coffee","’78 Coffee","Walker’s Coffee","Tost Modern ","Koala Food","Aç-Ken Döner","Wanted Pizza","Cafe de Luca"]
}

with open('eventsWsponsors.csv', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    newList = []
    maxClass = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        dictForCSV = {'Etkinlik Adı':row[0],'Düzenleyen Grup':row[1]}
        clusters = {"Cluster " + str(item): "" for item in range(1,20)}
        dictForCSV = {**dictForCSV, **clusters}
        idx = 1
        for sponsorIDX in range(len(row[2:])):
            sit = False
            for className,brands in clusterDict.items():
                if row[sponsorIDX+2] in brands:
                    sit = True
                    if className not in list(dictForCSV.values()):
                        dictForCSV["Cluster "+str(idx)] = className
                        idx = idx + 1
                        break
                    else:
                        break
            if sit == False and row[sponsorIDX+2] != '':
                f = open("text.txt", "a", encoding="UTF-8")
                f.write("Alert: " + str(row[sponsorIDX+2]) + '\n')
                f.close()
        if idx - 1 > maxClass:
            maxClass = idx - 1 
        newList.append(dictForCSV)
        line_count += 1
print(maxClass)

with open('parsed.csv', mode='w', encoding="UTF-8", newline='') as csv_file:
    clusters = ["Cluster " + str(item) for item in range(1,20)]
    fieldnames = ['Etkinlik Adı', 'Düzenleyen Grup']
    fieldnames = fieldnames + clusters
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    writer.writeheader()

    for row in newList:
        writer.writerow(row)