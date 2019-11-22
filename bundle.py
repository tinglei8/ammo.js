import os, sys

bundle = open(sys.argv[1], 'a')
bundle.write(open('glue.js', 'r').read())
bundle.write('''
''')
bundle.close()

