"""CP1404 internal seminar 1."""
# number = int(input("Number: "))
# if number < 0:
#     print(f"{number} is negative")
# else:
#     print(f"{number} is not negative")
# print("Done, yeah!!!!")
GST_RATE = 0.1

tax_amount = 0
item_price = float(input('Enter item price: $'))
gst_status = input('Does it have GST? (Y/N) ').upper()
if gst_status == 'Y':
    tax_amount = item_price * GST_RATE
final_price = item_price + tax_amount

print(f"Your item costs ${final_price:.2f}")
