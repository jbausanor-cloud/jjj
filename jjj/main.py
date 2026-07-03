# ฟังก์ชันตรวจสอบและหักเงินจาก Wallet
def process_payment(wallet_balance, item_price):
    if wallet_balance >= item_price:
        wallet_balance -= item_price
        print("Payment Success")
        print("Wallet Balance คงเหลือ:", wallet_balance)
        return wallet_balance
    else:
        print("Error: เงินใน Wallet ไม่เพียงพอ")
        return wallet_balance


# ฟังก์ชันแสดงคิวที่มีสถานะ Pending
def display_active_queues(orders):
    print("\n=== Active Queues ===")
    for order in orders:
        if order["status"] == "Pending":
            print(f"Queue ID : {order['queue_id']}")
            print(f"Menu     : {order['menu']}")
            print(f"Price    : {order['total_price']} บาท")
            print(f"Status   : {order['status']}")
            print("------------------------")


# ----------------------------
# ข้อมูลตัวอย่าง
# ----------------------------
wallet_balance = 350.00
item_price = 50.00

orders = [
    {"queue_id": 101, "menu": "ข้าวมันไก่", "total_price": 50.00, "status": "Ready"},
    {"queue_id": 102, "menu": "ก๋วยเตี๋ยว", "total_price": 45.00, "status": "Pending"},
    {"queue_id": 103, "menu": "ชาไทย", "total_price": 30.00, "status": "Pending"}
]

# เรียกใช้งานฟังก์ชัน
wallet_balance = process_payment(wallet_balance, item_price)
display_active_queues(orders)