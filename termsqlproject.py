import pypyodbc
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-67J30R8\SQLEXPRESS01;'
    'Database=Market;'
    'Trusted_Connection=True;'
)

cursor = db.cursor()

print("""
1-) Enter 1 to see Brand ID
2-) Enter 2 to see Brand Name
3-) Enter 3 to see Supplier Name
4-) Enter 4 to see Variety ID
5-) Enter 5 to see Variety Name
6-) Enter 6 to see Storage Criterion
7-) Enter 7 to see Product ID
8-) Enter 8 to see Product Name
9-) Enter 9 to see Price
10-) Enter 10 to see Stock 
""")

key = int(input("MAKE YOUR CHOİCE:  "))

if key == 1:
    table = 'Brands'
    column = 'BrandID'

elif key == 2:
    table = 'Brands'
    column = 'BrandName'

elif key == 3:
    table = 'Brands'
    column = 'SupplierName'

elif key == 4: 
    table = 'Variety'
    column = 'VarietyID'

elif key == 5:
    table = 'Variety'
    column = 'VarietyName'

elif key == 6:
    table = 'Variety'
    column = 'StorageCriterion'

elif key == 7:
    table = 'Product'
    column = 'ProductID'

elif key == 8:
    table = 'Product'
    column = 'ProductName'

elif key == 9:
    table = 'Product'
    column = 'Price'

elif key == 10:
    table = 'Product'
    column = 'Stock'


query = 'SELECT ' + column + ' FROM ' + table

cursor.execute(query)
for row in cursor:
    print(row)
