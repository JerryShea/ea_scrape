from cookielib import CookieJar
import datetime
import os, sys, time
import urllib
import urllib2

def login(username, password):
  formdata = { "j_username" : username, "j_password": password }
  data_encoded = urllib.urlencode(formdata)
  response = opener.open("https://energyaustralia.opower.com/ei/app/login-process", data_encoded)
  if (response.getcode() != 200):
    # FIXME return code is always 200
    print >> sys.stderr, "Could not login"
    exit(1)
  
def get(year, month, day):
  url="https://energyaustralia.opower.com/ei/app/myEnergyUse/neighbors/day/%(year)d/%(month)d/%(day)d" % locals()
  response = opener.open(url)
  content = response.read()
  return content

def main(argv):
  if len(argv) != 3:
    print >> sys.stderr, "Download data from energy australia web site from specified date to now"
    print >> sys.stderr, "Usage: " + sys.argv[0] + " username password from(yyyy/mm/dd)"
    exit(1)

  username=argv[0]
  password=argv[1]
  start_date = datetime.datetime.strptime(argv[2], "%Y/%m/%d")
  end_date = datetime.datetime.now()

  #os.makedirs(store_dir)
  login(username, password)
  for n in range( ( end_date - start_date ).days + 1 ):
    d = ( start_date + datetime.timedelta( n ) )
    year = d.year
    month = d.month
    day = d.day
    content = get(year, month, day)
    filename = "%(year)d-%(month)d-%(day)d.html" % locals()
    if len(content) > 0:
      html_file = open(store_dir + filename, 'w')
      print >> html_file, content
      html_file.close()
    else:
      print >> sys.stderr, "No data for " + filename


# global vars
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
store_dir = 'store/'

if __name__ == '__main__':
  main(sys.argv[1:])

