time_user = int(input('Enter time in seconds - '))

h = int(time_user / 3600)
m = int(time_user / 60 - (h * 60))
s = int(time_user - (h * 3600) - (m * 60))

print ('Time {:0=2}:{:0=2}:{:0=2}'.format(h, m, s))
