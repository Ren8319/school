
hour = int(input("กรอกจำนวนชั่วโมง: "))
minute = int(input("กรอกจำนวนนาที: "))

# ตรวจสอบค่าติดลบ
if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    # คำนวณจำนวนชั่วโมงที่คิดเงิน
    total_hours = hour

    # ถ้ามีเศษนาที ให้ปัดเศษชั่วโมงขึ้น 1
    if minute > 0:
        total_hours += 1

    # คิดเงินเฉพาะชั่วโมงหลังชั่วโมงแรก
    chargeable_hours = max(total_hours - 1, 0)
    fee = chargeable_hours * 30

    # แสดงผลค่าจอดรถ
    print("ค่าจอดรถคือ", fee, "บาท")