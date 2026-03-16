import qrcode

link = "https://portfolio-909wsxxbg-zainab-farooqui-s-projects.vercel.app/"
qr = qrcode.make(link)
qr.save("scan-QR/web_qr.png")
