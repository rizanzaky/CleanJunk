import ConfigParser, os

config = ConfigParser.ConfigParser()
x = config.readfp(open('cleaner.conf'))
#config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])

print config.sections
print config
print x

print config.items("Section 1")
print config.items("Section 2")



#f = open('cleaner.conf', 'r')

#print f

#for line in f:
#    print line.strip()