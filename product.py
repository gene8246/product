import os

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '名称, 値段' in line:
				continue
			name, price = line.strip().split(',')#切割完後放進name, price
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('please enter product name: ')
		if name == 'q':
			break
		price = input('pelase enter product price: ')
		#p = []
		#p.append(name)
		#p.append(price)
			#p = [name, price] 相同於上面三行
		price = int(price)
		products.append([name, price]) #相同於上面
	print(products)
	return products
	#print(products[0][0]) #第零個小清單中的第零個

#列出紀錄
def print_products(products):
	for p in products:
		print('product name is ', p[0])
		print('product price is ', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		#utf-8確保不會亂碼
		f.write('名称, 値段\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
	filename = 'products list.csv'
	if os.path.isfile(filename):
		print('file exist')
		products = read_file(filename)
	else:
		print('file is missing')

	products = user_input(products)
	print_products(products)
	write_file('products list.csv', products)

main()
