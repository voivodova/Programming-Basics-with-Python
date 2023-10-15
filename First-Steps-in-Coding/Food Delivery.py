chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegatarian_menu = 8.15
delivery_price = 2.50
total_price_menus = chicken_menu*price_chicken_menu\
    +fish_menu*price_fish_menu\
    +vegetarian_menu*price_vegatarian_menu
dessert_price = total_price_menus*0.2
total_sum = total_price_menus+dessert_price+delivery_price
print(total_sum)