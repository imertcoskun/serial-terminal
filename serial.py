import serial
import io
import time

ser = serial.Serial()
ser.baudrate = 1***** #Serial baudrate belirt
ser.port = 'COM*' #Port yolu belirt
ser.timeout = 2
# open("C:\\Users\\***\\****\\login.txt", "r") txt icerigi degistirildi. Github'dan hazirladigin repoyu kullan
try:
	ser.open()
	while ser.is_open:
		username = "admin" #daha düzgün bir brute force için repo kullanılabilir veya hazırlanılabilir...
		password = "blabla" #daha düzgün bir brute force için repo kullanılabilir veya hazırlanılabilir...

		for i in range(1,5):
			ser.write(b'\r\n')
			
			output = ser.readline()
			output = "".join(map(chr, output))
			if "login:" == output:
				print("tamam")
				break

		ser.write(bytes(username+'\r\n','utf-8'))
		time.sleep(0.5)
		for i in range(1,5):
			time.sleep(0.5)
			output = ser.readline()
			output = "".join(map(chr, output))
			if "Password:" == output:
				ser.write(bytes(password+'\r\n','utf-8'))
				print("tamam2")
				break
		ser.close()
	
except:
	print("Baglanamiyorum ya reis...")
