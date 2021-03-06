# groceries.py

products = [
    {
        "id":1, 
        "name": "Chocolate Sandwich Cookies", 
        "department": "snacks", 
        "aisle": "cookies cakes", 
        "price": 3.50
    },
    
    
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)

# PRODUCTS (Part 1)

print("------------")
print("THERE ARE " + str(len(products)) + " PRODUCTS:")
print("------------")

def product_name(product):
   return product.get("name")

products.sort(key=product_name)

for p in products:
    price_usd = p["price"] # "$4.99"
    price_usd = "(${0:.2f})".format(p["price"])
    print(p["name"] + " " + str(price_usd))

# DEPARTMENTS (Part 2)

x = ("department")

print("------------")
print("THERE ARE " + str(len(x)) + " DEPARTMENTS:")
print("------------")

department_dict = dict()

def add_count(department):
    if department_dict.get(department) is None:
        department_dict[department] = 1

    else: 
        department_dict[department] = department_dict.get(department) + 1
    
department_set = set()

for p in products:
    add_count(p.get("department"))
    department_set.add(p.get("department"))
    
department_set = list(department_set)

department_set.sort()

# if department_dict.get("department") is 1:
    # department_dict.get("department") + " product"
    
# else:
    # department_dict.get(department) = department_dict(department) + " products"

for p in department_set:
    # breakpoint()
    matching_products_count = department_dict.get(p) 
    if matching_products_count is 1:
        label = "product"
        
    else:
        label = "products"
    print(p.title() + " " + "(" + str(matching_products_count) + " " + label + ")")
