from covid_india import states 

# print(states.getdata())
print(states.getdata('Madhya Pradesh'))
mp = states.getdata('Madhya Pradesh')
print('Total cases:',mp['Total'])
print('Dead cases :',mp['Death'])
