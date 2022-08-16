#讀取檔案
products = []
with open('products list.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '名称, 値段' in line:
			continue
		name, price = line.strip().split(',')#切割完後放進name, price
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('pelase enter product price: ')
	#p = []
	#p.append(product)
	#p.append(price)
		#p = [product, price] 相同於上面三行
	price = int(price)
	products.append([name, price]) #相同於上面
print(products)
#print(products[0][0]) #第零個小清單中的第零個

#列出紀錄
for p in products:
	print('product name is ', p[0])
	print('product price is ', p[1])

#寫入檔案
with open('products list.csv', 'w', encoding = 'utf-8') as f:
	#utf-8確保不會亂碼
	f.write('名称, 値段\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')