from data_loader import load_inventory_data
from inventory_manager import check_stock_level
from demand_predictor import predict_demand

data = load_inventory_data("../data/inventory_data.csv")

quantities = data["quantity_sold"].tolist()

prediction = predict_demand(quantities)

for qty in quantities:
    print(check_stock_level(qty))

print("Predicted future demand:", prediction)
