# 🔗 Python URL Kısaltıcı (Link Shortener)

Bu proje, uzun ve karmaşık web sitesi linklerini (URL) tek bir tıklamayla kısa hale getiren **Python**, **Tkinter**, **Requests** ve **Pyperclip** tabanlı bir masaüstü uygulamasıdır. Arka planda popüler **TinyURL API** altyapısını kullanır.

---

## ✨ Özellikler

* **⚡ Hızlı Kısaltma:** Uzun linkleri saniyeler içinde TinyURL API'sine göndererek kısaltılmış sürümlerini elde eder.
* **📋 Panoya Kopyalama:** "Kopyala" butonu sayesinde kısaltılan linki tek tıkla bilgisayarınızın kopyalama panosuna (clipboard) ekler.
* **🛡️ Akıllı Buton Durumu:** Link kısaltılmadan önce kopyalama butonu kilitlidir (`DISABLED`). İşlem başarıyla tamamlandığında otomatik olarak aktif (`NORMAL`) hale gelir.
* **💬 Kullanıcı Bilgilendirmesi:** İşlem bittiğinde kullanıcıya pop-up mesaj kutusu (`messagebox`) ile görsel geri bildirim sağlar.

---

## 🛠️ Gereksinimler ve Kurulum

Uygulamanın çalışabilmesi için internet bağlantınızın olması ve aşağıdaki harici Python kütüphanelerinin bilgisayarınızda yüklü olması gerekir. Terminal veya komut satırını açarak şu komutla yükleme yapabilirsiniz:

```bash
pip install requests pyperclip
```

*(Not: `tkinter` kütüphanesi Python ile birlikte yerleşik olarak geldiği için ekstra bir kurulum yapmanıza gerek yoktur.)*

---

## 🚀 Nasıl Çalıştırılır?

1. Bu depodaki kodları `link_kisaltici.py` adıyla bir dosyaya kaydedin.
2. Terminal veya komut satırından projenin bulunduğu klasöre gidin:
   ```bash
   cd projenin_bulundugu_klasor
   ```
3. Uygulamayı başlatmak için şu komutu çalıştırın:
   ```bash
   python link_kisaltici.py
   ```
4. Açılan pencereye uzun linkinizi yapıştırıp **Kısalt** butonuna basın, ardından **Kopyala** butonuyla kısaltılmış linkinizi dilediğiniz yerde kullanın!

---

## 📝 Kod Yapısı Hakkında Kısa Bilgi

* **`requests.get()`**: TinyURL servisine API isteği atarak web tabanlı kısaltma işlemini gerçekleştirir.
* **`pyperclip.copy()`**: İşletim sisteminin kopyala-yapıştır hafızasına erişerek harici bir işleme gerek kalmadan veriyi panoya kaydeder.
* **`cget("text")[17:]`**: Etiketteki `"kısaltılmıs link:"` başlık yazısını kırparak sadece ham linkin kopyalanmasını sağlar.
