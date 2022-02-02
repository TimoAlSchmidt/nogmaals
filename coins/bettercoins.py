# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

money = {
  500 : 0,
  300: 0,
  200: 0,
  50 : 0,
  20 : 0,
  10 : 0,
  5 : 0,
  2 : 0,
  1 : 0,
  0 : 0
}

toPay = int(float(input('Amount to pay: '))* 100) # the amount to pay
paid = int(float(input('Paid amount: ')) * 100) # the amount it's paid
change = paid - toPay #the amount of change remaining
n = 0

if change > 0: #if we need to give change
  coinValue = list(money.keys())[n] #sets initial value of coinValue so we can lower it
  
  
  while change > 0 and coinValue > 0: # while we still have change and we have a value we can give
    nrCoins = change // coinValue #int divide

    if nrCoins > 0: #if can give coins from this amount
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Say how many coins we can maximally return
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #request how many coins we have given
      change -= nrCoinsReturned * coinValue #use the amount of coins given per coin to determine how much change we owe
      money[coinValue] = nrCoinsReturned
    
    n += 1
    coinValue = list(money.keys())[n]

print()
for coin in money.keys():
  if coin != 0:
    print("We've given",money[coin],"of",coin)
print()
if change > 0: #If we haven't given back all of our changes
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')