import os
while True:
    num = input()
    if num == "" or num == "exit":
        break
    else:
        num = int(num)
    s = open(f"tasks {num}.txt")
    count = 0
    count_done = 0
    for i in s:
        if os.listdir().count(f"block {num} task {i.rstrip()}.py") == 1 or os.listdir().count(f"{i.rstrip()}.xlsx") == 1:
            print(f"{i}", end="")
            count_done += 1
            count += 1
        else:
            print("https://astra.fipi.ru/bank/index.php?proj=B9ACA5BBB2E19E434CD6BEC25284C67F&qid=" + i, end="")
            count += 1
    print()
    print(f"{count_done}/{count}", str(count_done / count * 100)[:5]+"%")


