# İşte Karşınızda Salcomp'un Telefon Sayısı Takip Sistemi! 📱📊

Proje, bir telefon barkod kayıt ve izleme uygulamasını içerir. Uygulama, kullanıcının telefonların barkodlarını okutmasına izin verir 📸📚 ve her bir telefonun kaç kez geçildiğini izler 🔄📈. Aynı zamanda kullanıcılar tarafından eklenen telefonları saklar 📂 ve veritabanında tutar 💾.

## Gereksinimler 📋🔧
Proje çalıştırılmadan önce aşağıdaki gereksinimlerin karşılandığından emin olunmalıdır:

- Python (3.x sürümü önerilir) 🐍
- Tkinter (grafiksel kullanıcı arayüzü oluşturmak için kullanılır) 🖥️
- SQLite (hafif bir veritabanı sistemi) 💼

Gereksinimleri kurmak için şu komutları kullanabilirsiniz:

```
pip install tk
```

## Proje Yapısı 📁🏗️
Proje, aşağıdaki bileşenleri içerir:

1. `telefon_barkod.db`: SQLite veritabanı dosyası, telefon bilgilerini ve geçiş sayılarını saklar 💽📊.
2. `telefon_barkod.py`: Ana Python kodu, grafik arayüz ve veritabanı işlemleri dahil olmak üzere uygulamanın işlevselliğini sağlar 🖥️🐍.

## Kullanım 🚀📝
Uygulamayı kullanmak için aşağıdaki adımları izleyebilirsiniz:

1. Proje dosyalarını bir dizinde saklayın 📂.
2. Terminal veya komut istemcisini açın ve proje dizinine gidin 🖥️.
3. `telefon_barkod.py` dosyasını çalıştırın 🐍.

Uygulama başladığında, bir grafik arayüz penceresi açılacaktır. Bu pencere, barkod okuma, geçiş sayısı izleme ve telefonları görüntüleme işlevlerini içerir.

## Uygulama Kullanımı 📱🔍
Uygulamayı kullanırken şu adımları izleyebilirsiniz:

1. **Barkodu Okutun 📸👉**: Barkodu okutmak için "Barkodu Okutun" etiketi altındaki giriş kutusuna bir barkod numarası yazın 📝 ve "Okut" düğmesine tıklayın 🔄. Bu, belirli bir telefonun geçişini kaydedecektir.

2. **Telefonları Görüntüle 📱👁️**: "Telefon Listesi" bölümü, veritabanında kaydedilen telefonları ve ilgili geçiş sayılarını görüntüler 📊. Bu liste her barkod okutulduğunda otomatik olarak güncellenir 🔄.

3. **Çıkış ✋🚪**: Uygulamadan çıkmak için "Çıkış" düğmesine tıklayın 🏁.

## Uygulama Mantığı 🤖🧠
Uygulama, bir SQLite veritabanı kullanarak telefon bilgilerini ve geçiş sayılarını saklar 💽📈. Her barkod okutulduğunda, ilgili telefonun geçiş sayısı artırılır 🔄📊 ve bu bilgi veritabanında güncellenir 💾.

## Ek Notlar 📝🤔
- Barkod okuma işlevselliği eklemek isterseniz, bir barkod okuyucu cihazı ve uygun bir kütüphane kullanmanız gerekebilir 📸📚.
- Uygulama, veritabanı işlemleri için SQLite kullanır, ancak daha büyük ölçekli projeler için farklı bir veritabanı sistemi tercih edilebilir 💼📊.

Şimdi, her bir metodu daha ayrıntılı olarak açıklayalım:

### `veritabani_olustur()` Metodu 📂💽
![Img1](https://i.hizliresim.com/on6930n.png)

Bu metod, SQLite veritabanını oluşturur veya var olan bir veritabanına bağlanır. Veritabanı, telefon bilgilerini ve geçiş sayılarını saklamak için kullanılır.

### `telefonlari_kontrol_et_ve_kaydet()` Metodu 📝📅
![Img2](https://i.hizliresim.com/1rh878w.png)

Bu metod, veritabanında herhangi bir telefon kaydının olup olmadığını kontrol eder. Eğer veritabanında hiç telefon kaydı yoksa, telefonları rastgele barkodlarla kaydeder. Bu işlem, uygulama başladığında sadece bir kez gerçekleştirilir.

### `telefon_gecildi(barkod)` Metodu 📸🔄
![Img3](https://i.hizliresim.com/ekq1azz.png)

Bu metod, kullanıcının bir barkodu okuttuğunda çağrılır. Barkod, veritabanında bulunursa ilgili telefonun geçiş sayısını artırır. Aksi takdirde, bir hata mesajı verir.

### `barkod_okut()` Metodu 📸📝
![Img4](https://i.hizliresim.com/jt9vtbf.png)

Bu metod, kullanıcının bir barkodu okutmak için "Okut" düğmesine tıkladığında çağrılır. Giriş kutusundan okunan barkodu alır ve `telefon_gecildi()` metodunu çağırarak işlemi gerçekleştirir.

### `telefonlari_getir()` Metodu 📊📁
![Img5](https://i.hizliresim.com/385r6tu.png)

Bu metod, veritabanından tüm telefonları ve ilgili geçiş sayılarını alır ve bir liste olarak döndürür. Bu liste, "Telefon Listesi" bölümünde görüntülenir.

### `guncelle_liste()` Metodu 📊🔄
![Img6](https://i.hizliresim.com/5fzc88o.png)

Bu metod, "Telefon Listesi" bölümünü günceller. Veritabanından alınan telefon bilgilerini kullanarak mevcut listeyi günceller. Bu, yeni geçişlerin anlık
