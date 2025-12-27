def classify_stock_level(quantity):
    if quantity < 30:
        return "Low Stock"
    elif quantity < 70:
        return "Medium Stock"
    else:
        return "Sufficient Stock"
