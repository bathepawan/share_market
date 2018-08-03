# Import smtplib for the actual sending function
import smtplib
import requests
from datetime import datetime

# Import the email modules we'll need
from email.mime.text import MIMEText


top_gainers_url = 'https://www.bseindia.com/markets/Equity/EQReports/mktwatchR.aspx?filter=Gainer*group$all$A&expandable=2'
top_lossers_url = 'https://www.bseindia.com/markets/Equity/EQReports/MktWatchR.aspx?filter=Loser*group$all$A&expandable=2'
top_gainers = requests.get(top_gainers_url)
top_lossers = requests.get(top_lossers_url)

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

_html = '<B>Top Gainers:</B>'
_html += top_gainers.text
_html += '<B>Top Lossers</B>'
_html += top_lossers.text

msg = MIMEText(_html, 'html')

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Market Alerts {} '.format(datetime.now())
msg['From'] = 'bathepawan@gmail.com'
msg['To'] = 'bathepawan@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login('bathepawan', 'ThisIs#1Pwdgm')
server.sendmail('bathepawan@gmail.com', ['bathepawan@gmail.com'], msg.as_string())
server.quit()

