import json
from settings import url_data_products

def select_cheepest_product(products):
	print(products)
	min_price = min(i.get("price_of_unit") for i in products)
	cheepest_product = [i for i in products if i.get("price_of_unit") == min_price]
	return cheepest_product

def select_all_cheepest_product_by_categories(categories):
	f = open(url_data_products, encoding='utf-8')
	data = json.load(f)
	products = data.get("products") 
	f.close()

	all_cheepest_products = {}

	for category in categories:
		print(category, "category")
		cheepest_products_in_category = select_cheepest_product(products.get(category))
		all_cheepest_products[category] = cheepest_products_in_category
	return all_cheepest_products

def get_total_price(all_cheepest_products):
	total_price = 0
	for  i in all_cheepest_products:
            for j in all_cheepest_products[i]:
            	print(j)
            	if all_cheepest_products[i].index(j)==0:
                	total_price += j["price_of_unit"]
	return total_price
