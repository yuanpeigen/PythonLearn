from tkinter import *
import time

'''
距离下班时间倒计时
author: Czech.Yuan
date: 2021-05-17
'''


class GetOffWorkCountDown:
    def __init__(self):
        self.curr_time = None
        self.tk = None
        self.work_hour = None
        self.work_minute = None
        self.work_second = None
        self.down_label = None

    # 刷新当前时间
    def refresh_current_time(self):
        clock_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.curr_time.config(text=clock_time)
        self.curr_time.after(1000, self.refresh_current_time)

    # 刷新倒计时时间
    def refresh_down_time(self):
        # 当前时间戳
        now_time = int(time.time())
        # 下班时间分秒数据过滤
        work_hour_val = int(self.work_hour.get())
        if work_hour_val > 23:
            self.down_label.config(text='小时的区间为（00-23）')
            return
        work_minute_val = int(self.work_minute.get())
        if work_minute_val > 59:
            self.down_label.config(text='分钟的区间为（00-59）')
            return
        work_second_val = int(self.work_second.get())
        if work_second_val > 59:
            self.down_label.config(text='秒数的区间为（00-59）')
            return
        # 下班时间转为时间戳
        work_date = str(work_hour_val) + ':' + str(work_minute_val) + ':' + str(work_second_val)
        work_str_time = time.strftime('%Y-%m-%d ') + work_date
        time_array = time.strptime(work_str_time, "%Y-%m-%d %H:%M:%S")
        work_time = time.mktime(time_array)
        if now_time > work_time:
            self.down_label.config(text='已过下班时间')
            return
            # 距离下班时间剩余秒数
        diff_time = int(work_time - now_time)
        while diff_time > -1:
            # 获取倒计时-时分秒
            down_minute = diff_time // 60
            down_second = diff_time % 60
            down_hour = 0
            if down_minute > 60:
                down_hour = down_minute // 60
                down_minute = down_minute % 60
            # 刷新倒计时时间
            down_time = str(down_hour).zfill(2) + '时' + str(down_minute).zfill(2) + '分' + str(down_second).zfill(
                2) + '秒'
            self.down_label.config(text=down_time)
            self.tk.update()
            time.sleep(1)
            if diff_time == 0:
                # 倒计时结束
                self.down_label.config(text='已到下班时间')
                break
            diff_time -= 1

    def initView(self):
        self.tk = Tk()
        self.tk.geometry('400x280')
        self.tk.resizable(0, 0)  # 可调整大小
        self.tk.config(bg='white')
        self.tk.title('倒计时应用')
        Label(self.tk, text='下班倒计时', font='宋体 20 bold', bg='white').pack()
        # 设置当前时间
        Label(self.tk, text='当前时间：', font='宋体 15 bold', bg='white').place(x=50, y=60)
        self.curr_time = Label(self.tk, text='', font='宋体 15', fg='gray25', bg='white')
        self.curr_time.place(x=160, y=60)
        self.refresh_current_time()
        # 设置下班时间
        Label(self.tk, text='下班时间：', font='宋体 15 bold', bg='white').place(x=50, y=110)
        # 下班时间-小时
        self.work_hour = StringVar()
        Entry(self.tk, textvariable=self.work_hour, font='宋体 12', width=2).place(x=160, y=115)
        self.work_hour.set('18')
        # 下班时间-分钟
        self.work_minute = StringVar()
        Entry(self.tk, textvariable=self.work_minute, font='宋体 12', width=2).place(x=185, y=115)
        self.work_minute.set('00')
        # 下班时间-秒
        self.work_second = StringVar()
        Entry(self.tk, textvariable=self.work_second, font='宋体 12', width=2).place(x=210, y=115)
        self.work_second.set('00')
        # 设置剩余时间
        Label(self.tk, text='剩余时间：', font='宋体 15 bold', bg='white').place(x=50, y=160)
        self.down_label = Label(self.tk, text='', font='宋体 23', fg='gray25', bg='white')
        self.down_label.place(x=160, y=155)
        self.down_label.config(text='00时00分00秒')
        # 开始计时按钮
        Button(self.tk, text='开始', bd='5', command=self.refresh_down_time,
               bg='red',
               font='宋体 12 bold', width=20).place(x=100, y=220)
        self.tk.mainloop()


if __name__ == '__main__':
    gd = GetOffWorkCountDown()
    gd.initView()
