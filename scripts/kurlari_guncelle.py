"""TCMB gösterge kurlarını resmi XML arşivinden çekip kurlar/YYYY.json dosyalarına yazar.

Kullanım:
  python scripts/kurlari_guncelle.py               -> son 10 günü kontrol eder (günlük görev)
  python scripts/kurlari_guncelle.py 2024-01-01    -> verilen tarihten bugüne doldurur (ilk kurulum)
Kaynak: https://www.tcmb.gov.tr/kurlar/YYYYAA/GGAAYYYY.xml (hafta sonu ve tatillerde dosya yoktur)
"""
import json, sys, time, datetime as dt, urllib.request, urllib.error, xml.etree.ElementTree as ET
from pathlib import Path

KLASOR = Path(__file__).resolve().parent.parent / "kurlar"
UA = {"User-Agent": "Mozilla/5.0 (kur-arsivi; +https://github.com)"}


def cek(gun):
    url = f"https://www.tcmb.gov.tr/kurlar/{gun:%Y%m}/{gun:%d%m%Y}.xml"
    for deneme in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # hafta sonu / resmi tatil: TCMB kur yayımlamaz
            time.sleep(3)
        except Exception:
            time.sleep(3)
    raise RuntimeError(f"TCMB'ye ulaşılamadı: {url}")


def coz(xml_bytes):
    kok = ET.fromstring(xml_bytes)
    out = {}
    for c in kok.findall("Currency"):
        kod = c.get("CurrencyCode")
        try:
            birim = float(c.findtext("Unit") or 1)
            alis = c.findtext("ForexBuying")
            satis = c.findtext("ForexSelling")
            if alis and satis:
                out[kod] = [round(float(alis) / birim, 6), round(float(satis) / birim, 6)]
        except ValueError:
            continue
    return out


def main():
    bugun = dt.date.today()
    bas = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else bugun - dt.timedelta(10)
    KLASOR.mkdir(exist_ok=True)
    yillar, degisti = {}, set()
    gun = bas
    while gun <= bugun:
        y = gun.year
        if y not in yillar:
            f = KLASOR / f"{y}.json"
            yillar[y] = json.loads(f.read_text()) if f.exists() else {}
        anahtar = gun.isoformat()
        if gun.weekday() < 5 and anahtar not in yillar[y]:
            veri = cek(gun)
            if veri:
                yillar[y][anahtar] = coz(veri)
                degisti.add(y)
                print("eklendi", anahtar)
            time.sleep(0.4)
        gun += dt.timedelta(1)
    for y in degisti:
        (KLASOR / f"{y}.json").write_text(json.dumps(dict(sorted(yillar[y].items())), separators=(",", ":")))
    print("güncellenen yıllar:", sorted(degisti) or "yok")


if __name__ == "__main__":
    main()
