import os

name = 1
files = os.listdir("C:/Python AIML/Programs and Projects/OSClearClutter/Stuffs")
print(files)
for i in files:
    if (i.endswith(".png")):
        os.rename(f"Stuffs/{i}", f"Stuffs/{name}.png")
        name = name + 1

