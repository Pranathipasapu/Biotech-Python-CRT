food_items = ["idly", "dosa", "puri", "tea", "coffee", "vada"]
price = (30, 40, 50, 10, 10, 30)

item = input("Enter your order: ")
quantity = int(input("Enter the quantity: "))

if item in food_items:
    index = food_items.index(item)
    p = price[index]
    Actual_Bill = quantity * p
    gst = Actual_Bill * 0.80  
    Total_bill = Actual_Bill + gst
    print(f"Total bill including 80% GST: ₹{Total_bill:.2f}")
else:
    print("Item not available.")

