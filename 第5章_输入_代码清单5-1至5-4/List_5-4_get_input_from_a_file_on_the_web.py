#从互联网上的文件中获取输入
import urllib.request
file = urllib.request.urlopen('http://helloworldbook3.com/data/message.txt')
message = file.read().decode('utf-8')
print(message)
