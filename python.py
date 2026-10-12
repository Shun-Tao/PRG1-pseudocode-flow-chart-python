"""
base = 3.50
mile_rate = 1.20
rate_per_minute = 0.25

miles = float(input("distance: "))
minutes = float(input("Minutes: "))

distance_charge = miles * mile_rate
minutes_charge = minutes * rate_per_minute

total_fare = base + distance_charge + minutes_charge

print(f"Your total fare is: £{total_fare:.2f}")
"""

"""
free_delivery_threshold = 40.00
standard_delivery_charge = 4.99
heavy_delivery_charge = 9.99
heavy_weight_limit = 10.00

order_total = float(input("Order cost?"))
order_weight_kg = float(input("Total weight of order (Kg)?"))

if order_total >= free_delivery_threshold:
    delivery_charge = 0
elif order_weight_kg > heavy_weight_limit:
        delivery_charge = heavy_delivery_charge
else:
      delivery_charge = standard_delivery_charge

total_to_pay = order_total + delivery_charge

print(f"Delivery Charge: £{delivery_charge}")
print(f"Total to pay: £{total_to_pay}")
"""
"""

target_reps = int(input("Target reps?"))

rep_count = 0
user_stopped = False

while rep_count < target_reps and not user_stopped:
    signal = str(input("stop or continue?"))
    if signal == "stop":
        user_stopped = True
    else:
        rep_count = rep_count+1
        print(f"Rep count: {rep_count}")

if rep_count == target_reps:
    print("Well done")
else:
    print("Work harder in the next session")
    """
