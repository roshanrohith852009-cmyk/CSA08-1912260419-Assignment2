
# Task 5: Functions, Parameters and Scope

print("===== DEFAULT ARGUMENT DEMONSTRATION =====")

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rohith")


print("\n===== MUTABLE DEFAULT ARGUMENT PROBLEM =====")

def add_subject(subject, subjects=[]):
    subjects.append(subject)
    return subjects

print("First call:", add_subject("Python"))
print("Second call:", add_subject("Java"))


print("\n===== SOLUTION USING NONE =====")

def add_subject_fixed(subject, subjects=None):
    if subjects is None:
        subjects = []

    subjects.append(subject)
    return subjects

print("First call:", add_subject_fixed("Python"))
print("Second call:", add_subject_fixed("Java"))


print("\n===== LOCAL AND GLOBAL SCOPE =====")

message = "Global Variable"

def display_message():
    message = "Local Variable"
    print("Inside function:", message)

display_message()
print("Outside function:", message)


print("\n===== PROGRAM COMPLETED =====")
