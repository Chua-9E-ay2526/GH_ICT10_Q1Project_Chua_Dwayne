from pyscript import display, document


#Receipt Calculations
def receiptget(e):
    ItemAPrice = document.getElementById("ItemA")
    ItemBPrice = document.getElementById("ItemB")
    ItemCPrice = document.getElementById("ItemC")
    ItemDPrice = document.getElementById("ItemD")
    subtotal = ((float(ItemAPrice.value) * ItemAPrice.checked) + (float(ItemBPrice.value) * ItemBPrice.checked) + (float(ItemCPrice.value) * ItemCPrice.checked) +
    (float(ItemDPrice.value) * ItemDPrice.checked))
    VAT=1.12
    Total=float(subtotal)*float(VAT)
    document.getElementById('receipt').innerHTML=f'Price:{subtotal}<br> VAT:12% <br>Total Price:{Total}'