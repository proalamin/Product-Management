"""Generate test Excel file with 100+ products."""
import random

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Products"

# Header row
ws.append(['product_id', 'name', 'category', 'price', 'quantity'])

categories = [
    'Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports',
    'Toys', 'Beauty', 'Automotive', 'Garden', 'Office Supplies'
]

product_names = [
    'Widget', 'Gadget', 'Tool', 'Device', 'Kit', 'Set', 'Pack',
    'Bundle', 'System', 'Module', 'Unit', 'Component', 'Accessory',
    'Adapter', 'Charger', 'Stand', 'Cover', 'Case', 'Holder', 'Mount'
]

for i in range(1, 121):
    product_id = 1000 + i
    name = f"{random.choice(product_names)} {random.choice(['Pro', 'Max', 'Plus', 'Ultra', 'Lite', 'Mini', 'XL'])} {i}"
    category = random.choice(categories)
    price = round(random.uniform(5.00, 500.00), 2)
    quantity = random.randint(1, 500)
    ws.append([product_id, name, category, price, quantity])

wb.save('test_products.xlsx')
print(f"Created test_products.xlsx with 120 products")
