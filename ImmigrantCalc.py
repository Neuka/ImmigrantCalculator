#!/usr/bin/env python
# coding: utf-8

# In[46]:


# money exchange rate
rate_crypto = 440
rate_bog = 456

# our expenses in peso
N_cash = 0
D_cash = 0
N_bog = 0
D_bog = 0
taxi = 0
# converting in $ and counting
sum_D = (D_bog + taxi)/rate_bog + D_cash/rate_crypto
sum_N = N_bog + (N_cash/rate_crypto)

# my wife deposite 
nastya_bog_sum = 288.8
# group summary
summary_all_week = sum_D+sum_N
summary_person_dol = summary_all_week/2
#check if Nastya pay more than me 
N_delta = summary_person_dol - sum_N

# automates the calculation of who owes who
if N_delta ==0:
    print('''Nastya doesn't owe anything''')
elif N_delta <0:
    print(f'Dasha owes Nastya: ${abs(round(N_delta, 2))}')
elif N_delta>0:
    print(f'Nastya pays: ${round(N_delta, 2)}')

# check the deposite
nastya_bog_sum = nastya_bog_sum - N_delta

print(f'''Nastya's amount on Dasha's card: ${round(nastya_bog_sum, 2)}''')
print(f'We spent in a week: ${round(summary_all_week, 2)}')


# In[ ]:




