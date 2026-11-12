
# Task 2: OTP Verification System

correct_otp = "123456"
max_attempts = 3
attempts = 0

print("===== OTP VERIFICATION SYSTEM =====")

while attempts < max_attempts:
    otp = input("Enter your 6-digit OTP: ")
    
    if len(otp) != 6:
        print("Invalid OTP length. Try again.")
        continue

    attempts += 1

    if otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Incorrect OTP.")

else:
    print("Maximum attempts reached.")

print("\n===== FOR LOOP DEMONSTRATION =====")

for number in range(1, 6):
    if number == 2:
        continue
    elif number == 4:
        pass
    print("Attempt number:", number)

print("\n===== PROGRAM COMPLETED =====")
