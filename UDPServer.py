import random
import sys
from socket import *

# Bir UDP socket oluşturuluyor
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 25400 portunu bekliyoruz
serverSocket.bind(('', 25400))
print("Started UDP server on port 25400") #Server başlıyor
while True:
    # Gelen veri ve verinin geldiği adres alınıyor
    message, address = serverSocket.recvfrom(1024)
    print (message)
    # Mesaj byte halinde geliyor, burada ise kaç byte olduğunu bakılıyor
    size = sys.getsizeof(message)
    # Gelen mesajın harfler büyütülüyor
    message = message.upper()
    newdata = ', Size : ' + str(size) + " Byte"
    # mesaj byte şeklinde olduğu için veri eklerken, ekleyeceğimiz veriyi de byte şeklinde değiştiriyoruz
    message += newdata.encode('utf-8')
    # serverdan dönüş olmaması için random değer atıyoruz
    rand = random.randint(0, 10)
    # random değer 4ten küçük olursa dönüş olmuyor ve time out oluyor
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
