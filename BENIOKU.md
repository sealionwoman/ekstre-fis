# Döviz Ekstre → Masraf Fişi (test v0.6)

Kullanıcı yalnızca PDF ekstreyi yükler. İşlemler aylara ayrılır, TCMB kurları otomatik uygulanır, Excel iner.
PDF kullanıcının tarayıcısında okunur; hiçbir yere gönderilmez.

## Hızlı kurulum (Windows, önerilen)

1. github.com'da ücretsiz hesap açın ve e-postanızı doğrulayın.
2. Bu klasördeki **KUR.bat** dosyasına çift tıklayın.
3. Tarayıcı açılınca GitHub'a giriş yapın ve pencerede yazan 8 haneli kodu onaylayın.
4. Pencere "KURULUM TAMAM" yazınca sitenizin adresini gösterir. Kurlar birkaç dakika içinde dolar.

## Elle kurulum (yaklaşık 15 dakika)

1. github.com'da ücretsiz hesap açın.
2. Sağ üstte **+ → New repository**. Ad: `ekstre-fis`, **Public** seçin, **Create repository**.
3. **uploading an existing file** bağlantısına tıklayın. Bu klasördeki `index.html`, `BENIOKU.md` ile
   `scripts` ve `kurlar` klasörlerini sürükleyip bırakın, **Commit changes**.
4. Otomatik görev dosyası: **Add file → Create new file**. Dosya adı kutusuna aynen
   `.github/workflows/kurlar.yml` yazın, bu klasördeki `kurlar.yml` dosyasının içeriğini yapıştırın, **Commit changes**.
5. **Settings → Actions → General** en altta *Workflow permissions*: **Read and write permissions** seçip kaydedin.
6. **Settings → Pages**: *Source* = **Deploy from a branch**, *Branch* = **main** / **(root)**, **Save**.
7. **Actions** sekmesi → soldan **TCMB kurlarini guncelle** → **Run workflow** → başlangıç tarihine
   `2025-01-01` yazıp çalıştırın. Geçmiş kurlar birkaç dakikada dolar.

Siteniz: `https://KULLANICI-ADINIZ.github.io/ekstre-fis/`

Bundan sonra kurlar her iş günü 15:50'de kendiliğinden güncellenir; hiçbir şey yapmanız gerekmez.

## Notlar
- Kaynak: TCMB gösterge niteliğindeki kurlar, `tcmb.gov.tr/kurlar` resmi XML arşivi (döviz alış / satış).
- Desteklenen ekstre biçimi şimdilik: Garanti BBVA ticari kart PDF ekstreleri (USD / EUR).
- Depo herkese açıktır (kod görünür, içinde hiçbir kişisel veya şirket verisi yoktur). Kodu gizli tutmak
  istenirse ileride Cloudflare Pages gibi gizli depo destekleyen ücretsiz bir barındırmaya taşınabilir.
