import os


text = os.getenv("MY_INPUT_STRING", "default_value")


print(f"Entered string: {text}")


reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")
