import os

os.chdir('folder path')

# Get current working directory
print(os.getcwd())

for f in os.listdir():
    print(f)

