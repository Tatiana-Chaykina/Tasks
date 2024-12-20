import os
command = "ls" if os.name != "nt" else "dir"
result = os.popen(command).read()
print("Результат выполнения комманды:", result)