import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # gerekli yapı oluşturuluyor
#server_addr = ('192.168.43.67', 25400) # server bilgileri giriliyor
server_addr = ('localhost', 25400) # server bilgileri giriliyor
ip = ''
sock.settimeout(2) # time out süresini belirliyoruz ( 2 sn )
success = 0
fail    = 0
total   = 0
try:
    for i in range(1, 7):
        total+=1
        messageNumber = ''
        for j in range(0,i): # mesaj boyutunun değişmesi için bu işlem yapılıyor
            messageNumber+= str(i)
        start = time.time() # Requestin başlangıç zamanı alınıyor
        message = 'Ping #' + messageNumber + " " + time.ctime(start)
        try:
            sent = sock.sendto(message.encode('utf-8'), server_addr) # veri akışı bytelar halinde olduğu için mesaj dönüştürülüyor
            print("Sent: " + message)
            data, server = sock.recvfrom(1024) # serverdan dönüş alınıyor
            ip = server
            print("Received: " + data.decode('utf-8')) # byte olarak dönen veri decode ediliyor
            end = time.time();
            elapsed = (end - start)*1000
            print("Request Time: " + str(elapsed)[:5] + " ms\n")
            success+=1
        except socket.timeout: # istek zaman aşımına uğrarsa bu kısıma gelecek
            end = time.time();
            elapsed = (end - start)
            print("#" + str(i) + " Requested Time out("+str(elapsed)[:1]+" seconds)\n")
            fail+=1

finally: # program bitişinde bu işlemi yapacak.
    print("Server: "+ str(ip) +" Success: "+ str(success) + " Fail: "+str(fail)+" Total: "+str(total))
    sock.close()
