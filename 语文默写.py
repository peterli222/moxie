import tkinter as tk
from tkinter import messagebox
import random
import time

# 古诗文的前半句和后半句
shiwen = {
    "老吾老": "以及人之老",
    "吴楚东南坼": "乾坤日夜浮",
    "戎马关山北": "凭轩涕泗流",
    "六朝旧事随流水": "但寒烟衰草凝绿"
}

# 初始化游戏数据
fenshu = 0
zongti = 0
shengyu_shijian = 60
shangci_shiwen = ""


# 获取随机一句古诗文
def huoqu_suiji_shiwen():
    shiwen_key = random.choice(list(shiwen.keys()))
    return shiwen_key


# 显示古诗文的前半句
def xianshi_shiwen(shiwen_key):
    shiwen_label.config(text=shiwen_key)


# 检查答案是否正确
def jiancha_daan():
    user_input = entry.get()
    shiwen_key = shiwen_label.cget("text")

    global fenshu, zongti
    if user_input == shiwen[shiwen_key]:
        fenshu += 1
    else:
        messagebox.showinfo("答案错误", "正确答案是：" + shiwen[shiwen_key])

    zongti += 1
    xianshi_xiayi_shiwen()


# 更新剩余时间并检查游戏结束
def gengxin_shijian():
    global shengyu_shijian
    shijian_label.config(
        text="得分: " + str(fenshu) + " | 总做题数: " + str(zongti) + " | 剩余时间: " + str(shengyu_shijian) + "秒")
    if shengyu_shijian >= 0:
        shengyu_shijian -= 1
        window.after(1000, gengxin_shijian)
    else:
        end_time = time.time()
        elapsed_time = end_time - start_time
        percentage = (fenshu / zongti) * 100 if zongti > 0 else 0
        messagebox.showinfo("游戏结束", "游戏结束！您的得分是：" + str(fenshu) + "/" + str(zongti) + "，总共用时：" + str(
            int(elapsed_time)) + "秒，得分比例：" + "{:.2f}%".format(percentage))


# 显示下一句古诗文
def xianshi_xiayi_shiwen():
    global shangci_shiwen
    shiwen_key = huoqu_suiji_shiwen()
    while shiwen_key == shangci_shiwen:
        shiwen_key = huoqu_suiji_shiwen()

    xianshi_shiwen(shiwen_key)
    shangci_shiwen = shiwen_key


# 创建窗口
window = tk.Tk()
window.title("古诗文游戏")
window.geometry("400x200")

shiwen_label = tk.Label(window, text="", font=("Helvetica", 16))
shiwen_label.pack(pady=20)

entry = tk.Entry(window, font=("Helvetica", 12))
entry.pack(pady=10)

check_button = tk.Button(window, text="检查", command=jiancha_daan)
check_button.pack(pady=10)

shijian_label = tk.Label(window, text="得分: 0 | 总做题数: 0 | 剩余时间: " + str(shengyu_shijian) + "秒",
                         font=("Helvetica", 12))
shijian_label.pack(pady=10)

xianshi_xiayi_shiwen()
start_time = time.time()
gengxin_shijian()

window.mainloop()
