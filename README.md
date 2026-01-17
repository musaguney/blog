##UzakPC
Bu proje, yerel ağdaki veya uzaktaki Pardus (Linux) işletim sistemine sahip bilgisayarların, merkezi bir web arayüzü üzerinden yönetilmesini, izlenmesini ve verilerinin kayıt altına alınmasını sağlayan bir Django web uygulamasıdır.

🚀 Proje Hakkında
Bu uygulama, staj süresince geliştirilmiş olup, sistem yöneticilerinin Pardus makinelerine SSH protokolü üzerinden bağlanarak temel sistem bilgilerini çekmesini ve bunları veritabanında saklamasını sağlar. Paramiko kütüphanesi kullanılarak güvenli bir şekilde uzaktaki makineye komut gönderilir ve çıktılar işlenerek kullanıcıya sunulur.

Özellikler
SSH Bağlantısı: Paramiko kütüphanesi ile uzaktaki Pardus bilgisayarlara IP, Kullanıcı Adı, Şifre ve Port bilgileriyle güvenli bağlantı.

Cihaz Yönetimi (CRUD):

Yeni Pardus bilgisayar ekleme (linuxaddarticle).

Kayıtlı bilgisayar bilgilerini güncelleme (updatelinux).

Sistemden bilgisayar silme (deletelinux).

Sistem İzleme (Dashboard): Kayıtlı tüm bilgisayarların listelendiği yönetim paneli (linuxdashboard).

Detaylı Analiz: Seçilen bir bilgisayara anlık bağlanarak komut çıktılarının alınması ve veritabanına kaydedilmesi (linuxdetail).

Kullanıcı Bazlı Yönetim: Eklenen bilgisayarlar, ekleyen kullanıcıya (author) atanır ve kullanıcı silindiğinde ilişkili kayıtlar da silinir (on_delete koruması).

Dinamik URL Yapısı: ID değerine göre değişen dinamik sayfa yapıları.

🛠️ Kullanılan Teknolojiler
Backend: Python 3, Django Framework

Veritabanı: SQLite (Django default)

Kütüphaneler: Paramiko (SSH bağlantısı için)

Frontend: HTML5, CSS, Django Template Engine (Layout extends yapısı)

📂 Proje Yapısı
Sağlanan dökümanlara göre uygulamanın temel dosya yapısı şöyledir:

App Adı: linux

Views (views.py):

linuxdashboard: Ana yönetim paneli.

linuxaddarticle: Yeni cihaz ekleme formu.

linuxdetail: Cihaz detaylarını görüntüleme ve SSH ile veri çekme.

updatelinux: Cihaz bilgilerini düzenleme.

deletelinux: Cihazı sistemden kaldırma.

Templates: linuxdashboard.html, linuxdetail.html, linuxaddarticle.html, linuxupdate.html, linuxs.html (pasif).
