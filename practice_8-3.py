price_menu = {
    "Laptop": 30000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 5000
}

raw_order = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Mouse", "Webcam"]

def count_items(order_list):
    counts = {}

    for item in order_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] =  1
    
    return counts

item_counts = count_items(raw_order)
print(f"統計結果:{item_counts}")

def calculate_total(item_counts):
    total_price = 0

    for item,count in item_counts.items():
        try:
            price = price_menu[item]
            total_price += price*count
        except:
            print(f"找不到{item}的價格，已跳過該商品。")
            continue
    
    return total_price

items_price = calculate_total(item_counts)
print(f"總價格:{items_price}")