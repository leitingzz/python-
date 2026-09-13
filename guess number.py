import random
ans = random.randint(1, 100)
times = 0
guess = int(input("请输入一个数字："))
if(guess > ans):
    print("猜大了")
elif(guess < ans):
    print("猜小了")
times += 1
while guess != ans:
    guess = int(input("请输入一个数字："))
    if(guess > ans):
        print("猜大了")
    elif(guess < ans):
        print("猜小了")
    times += 1
print(f"回答正确！\n共猜{times}次")