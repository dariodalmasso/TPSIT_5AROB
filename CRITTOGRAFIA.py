from PIL import Image
import stepic

immagine = Image.open("patrick.jpg")
messaggio = b"messaggio segreto"
image_secret = stepic.encode(immagine, messaggio)
image_secret.save("segreto.png")
messaggio_segreto = stepic.decode(immagine)
print = messaggio_segreto


