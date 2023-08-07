class KalpHastalikTahmini:
    def __init__(self):
        self.sorular = [
            "Yaşınız kaç?",
            "Cinsiyetiniz nedir? (Erkek/Kadın)",
            "Ağrı tipiniz nasıl? (Göğüs ağrısı/Mide ağrısı/Hiçbiri)",
            "Tansiyonunuz yüksek mi? (Evet/Hayır)",
            "Kolestrol seviyeniz yüksek mi? (Evet/Hayır)",
        ]
        self.cevaplar = []

    def sorulari_sor(self):
        for soru in self.sorular:
            cevap = input(soru + " ")
            self.cevaplar.append(cevap)

    def risk_tahmin_et(self):
        risk_skoru = 0

        yas = int(self.cevaplar[0])
        if yas > 50:
            risk_skoru += 2

        cinsiyet = self.cevaplar[1]
        if cinsiyet.lower() == "erkek":
            risk_skoru += 1

        agrı_tipi = self.cevaplar[2]
        if agrı_tipi.lower() == "göğüs ağrısı":
            risk_skoru += 3

        tansiyon = self.cevaplar[3]
        if tansiyon.lower() == "evet":
            risk_skoru += 2

        kolestrol = self.cevaplar[4]
        if kolestrol.lower() == "evet":
            risk_skoru += 1

        if risk_skoru <= 3:
            return "Düşük riskli."
        elif risk_skoru <= 6:
            return "Orta riskli."
        else:
            return "Yüksek riskli."

    def calistir(self):
        print("Kalp Hastalığı Riski Tahmin Aracına Hoş Geldiniz!")
        print("Lütfen aşağıdaki soruları yanıtlayın:")
        self.sorulari_sor()
        sonuc = self.risk_tahmin_et()
        print("Tahmin sonucu:", sonuc)


if __name__ == "__main__":
    uygulama = KalpHastalikTahmini()
    uygulama.calistir()
