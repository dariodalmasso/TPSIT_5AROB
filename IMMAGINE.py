from PIL import Image
import stepic

immagine = Image.open("patrick2.jpg")
messaggio = b"123456"
image_secret = stepic.encode(immagine, messaggio)
image_secret.save("password.png")
