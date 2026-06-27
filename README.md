# 🐍 Docker Yılan Oyunu (Terminal)

Bu proje, Python kullanılarak geliştirilmiş ve tamamen terminal üzerinde oynanan klasik bir yılan oyunudur. Projenin en önemli özelliği, **Docker** container'ı içerisinde çalışacak şekilde paketlenmiş olmasıdır. Bu sayede bilgisayarınıza ekstra bir Python kütüphanesi kurmanıza gerek kalmaz.

## 🚀 Özellikler
* Terminal tabanlı basit ve retro yapı (`curses` kütüphanesi kullanılmıştır).
* Docker entegrasyonu sayesinde her ortamda sorunsuz çalışma.
* Yön tuşlarıyla anlık klavye kontrolü.

## 🛠️ Kurulum ve Çalıştırma

Oyunu oynamak için bilgisayarınızda **Docker**'ın yüklü ve çalışır durumda olması yeterlidir.

**1. İmajı Oluşturun (Build):**
Terminalinizde proje klasörünün içindeyken şu komutu çalıştırın:
docker build -t dockeryilanoyun .

**2. Oyunu Başlatın (Run):**
İmaj oluştuktan sonra oyunu oynamak için (etkileşimli terminal modunda) şu komutu girin:
docker run -it dockeryilanoyun

## 🎮 Nasıl Oynanır?
* Yılanı yönlendirmek için klavyenizdeki **Yön Tuşlarını** (⬆️, ⬇️, ➡️, ⬅️) kullanın.
* Haritadaki yemleri yiyerek büyüyün ve skorunuzu artırın.
* Duvarlara veya kendi kuyruğunuza çarparsanız oyun biter.
* Oyun bittiğinde skorunuz terminal ekranına yazdırılır.
