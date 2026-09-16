from pyscript import display, document


#Sku Generation
def getSKU(e):
    ProductClass = document.getElementById("Category").value
    Product = document.getElementById("Item").value
    Stock = document.getElementById("Quantity").value

    document.getElementById('receipt').innerHTML=f'SKU: {ProductClass}-{Product}-{Stock}'