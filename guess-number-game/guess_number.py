# 猜数字游戏
# 这是一个用Python实现的猜数字游戏
# 计算机会随机生成一个数字，玩家需要猜出这个数字

import random

def play_game():
    """
    单轮游戏函数
    """
    # 生成一个1-100之间的随机数
    target_number = random.randint(1, 100)
    
    # 初始化尝试次数
    attempts = 0
    max_attempts = 10
    
    print("欢迎来到猜数字游戏！")
    print(f"我想了一个1-100之间的数字，你有{max_attempts}次机会猜出来。\n")
    
    # 游戏循环
    while attempts < max_attempts:
        try:
            # 获取用户输入
            guess = int(input("请输入你的猜测（1-100）: "))
            
            # 验证输入范围
            if guess < 1 or guess > 100:
                print("请输入1-100之间的数字！\n")
                continue
            
            attempts += 1
            
            # 判断猜测结果
            if guess < target_number:
                print(f"太小了！剩余尝试次数：{max_attempts - attempts}\n")
            elif guess > target_number:
                print(f"太大了！剩余尝试次数：{max_attempts - attempts}\n")
            else:
                print(f"恭喜你！你用{attempts}次就猜出了正确答案：{target_number}")
                return True
        
        except ValueError:
            print("请输入一个有效的整数！\n")
            continue
    
    # 游戏失败
    print(f"\n很遗憾，你没有在{max_attempts}次内猜出来。")
    print(f"正确答案是：{target_number}")
    return False

def main():
    """
    主函数：处理多轮游戏
    """
    while True:
        # 进行一轮游戏
        play_game()
        
        # 询问是否继续
        while True:
            choice = input("\n想再玩一次吗？(是/否): ").strip().lower()
            if choice in ['是', 'y', 'yes']:
                print("\n" + "="*50 + "\n")
                break
            elif choice in ['否', 'n', 'no']:
                print("感谢游玩！再见！")
                return
            else:
                print("请输入'是'或'否'！")

if __name__ == "__main__":
    main()
