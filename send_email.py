#sending email using python
import smtplib

fromaddr = 'your@gmail.com'
toaddrs  = 'user_you@gmail.com'
msg = 'First Email'
username = 'user_me@gmail.com'
password = 'pwd'

try:
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.ehlo()
  server.starttls()
  server.login(username,password)
  server.sendmail(fromaddr, toaddrs, msg)
  server.quit()
expect:
  print 'Something went wrong...'
  
