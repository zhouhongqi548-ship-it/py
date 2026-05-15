employees = {
    "Jason": {"dept": "Engineering", "phone": "0912-345-678"},
    "Jimmy": {"dept": "Marketing", "phone": "0922-111-222"},
    "Peter": {"dept": "Engineering", "phone": "0933-444-555"},
    "Alice": {"dept": "HR", "phone": "0955-666-777"},
    "Bob": {"dept": "Marketing", "phone": "0988-777-666"},
    "Charlie": {"dept": "Finance", "phone": "0911-222-333"},
    "David": {"dept": "Engineering", "phone": "0966-888-999"},
    "Eve": {"dept": "HR", "phone": "0977-000-111"}
}

def add_employee(name,dept,phone):
    employees[name] = {"dept":dept,"phone":phone}
    print(f"已新增員工:{name}")

def get_info(name):
    try:
        info = employees[name]
        return f"姓名:{name},部門:{info["dept"]},聯絡電話:{info["phone"]}"
    except:
        return f"{name}不在員工名單內"
    
def list_all_depts():
    depts = set()

    for name,info in employees.items():
        depts.add(info["dept"])
    
    return depts

print(list_all_depts)
print(get_info(input("請輸入名字:")))