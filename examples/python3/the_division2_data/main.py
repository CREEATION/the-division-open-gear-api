from Brands import Brands as b




brands = b()

five_11 = brands.five_11


for bonus in five_11[['set_bonus_1', 'set_bonus_2','set_bonus_3']].values[0]:
    if 'handling' in bonus.lower():
        print(f'This set improves handling {bonus}')
