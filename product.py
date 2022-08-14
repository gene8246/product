products = []
while True:
	product = input('please enter product name: ')
	if product == 'q':
		break
	price = input('pelase enter product price: ')
	#p = []
	#p.append(product)
	#p.append(price)
		#p = [product, price] 相同於上面三行
	price = int(price)
	products.append([product, price]) #相同於上面

print(products)
#print(products[0][0]) #第零個小清單中的第零個

for p in products:
	print('product name is ', p[0])
	print('product price is ', p[1])

with open('products list.csv', 'w', encoding = 'utf-8') as f:　＃加入編碼utf-8確保不會亂碼
	f.write('名称, 値段\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')