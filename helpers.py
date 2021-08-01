def obfuscate(value):
  with open('values.p', 'a') as fp:
    fp.write(str(value) + '\n')