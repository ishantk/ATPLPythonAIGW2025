password = "         password123 "
new_password = password.strip()
print('password:', password)
print('new_password:', new_password)

data = "000035098700"
print('data:', data.strip("0"))
print('data:', data.lstrip("0"))
print('data:', data.rstrip("0"))

amount = 35.54000
new_amount = float(str(amount).strip('0'))
print('new_amount:', new_amount, type(new_amount))

quote = 'search the candle, rather than cursing the darkness'
new_quote = quote.replace('t', 'k')
print('quote:', quote)
print('new_quote:', new_quote)

name = 'John Watson'
# Expetced Output: *o*n *a*s*n
# write the code to replace alternate character with *

message = "No Internet Connection"
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

quote = 'search the candle, rather than cursing the darkness'
idx1 = quote.find('the')
idx2 = quote.find('dark')
idx3 = quote.rfind('the')


print('idx1:', idx1) # 7
print('idx2:', idx2) # 43
print('idx3:', idx3) # 39

print(quote[idx1: idx1+3]) # the
print(quote[idx2:]) # darkness