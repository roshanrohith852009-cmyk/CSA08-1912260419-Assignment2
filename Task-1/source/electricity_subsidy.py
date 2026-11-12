
units = int(input("Enter electricity units consumed: "))
print("\n--- Using Multiple if Statements ---")

if units <= 100:
    print("100% Subsidy")

if units > 100 and units <= 200:
    print("50% Subsidy")

if units > 200 and units <= 300:
    print("25% Subsidy")

if units > 300:
    print("No Subsidy")


print("\n--- Using if-elif-else ---")

if units <= 100:
    print("100% Subsidy")
elif units <= 200:
    print("50% Subsidy")
elif units <= 300:
    print("25% Subsidy")
else:
    print("No Subsidy")
