import tkinter as tk
from tkinter import ttk

class Alarm():
    def __init__(self):
        #Setting The Whole Window
        self.root=tk.Tk()
        self.root.geometry("852x552+250+80")
        self.root.minsize("852","552")
        self.root.maxsize("852","552")
        self.root.title("Alarm Clock")
        Icon = tk.PhotoImage(file="Icon/alarmclock.png")
        self.root.iconphoto(False,Icon)
        # self.root.configure(bg='ivory2')

        #Setting Up Label Inside Of Window
        self.set_alarm=tk.Frame(self.root)
        self.set_alarm.pack(anchor="nw",side="top")
        self.set_alarm_label=tk.Label(self.set_alarm,text="Set Alarm",font=("Times",30,"bold","italic"),width=88)
        self.set_alarm_label.pack(side="right",padx=10)

        #Setting Up Time Of the alarm,Label,Ringtone,Remind me After 10 min

        self.Alarm_frame=tk.Frame(self.root,height=250,width=800,bg="white")
        self.Alarm_frame.pack(side="top")

        self.set_alarm_frame=tk.Frame(self.Alarm_frame)
        self.set_alarm_frame.pack(anchor="nw",side="top",pady=7,padx=9)

        self.Alarm_time=tk.Label(self.set_alarm_frame,text="Alarm Time : ",font=("Times",13,"bold"))
        self.Alarm_time.grid(column=0,row=0)

        self.slash_label=tk.Label(self.set_alarm_frame,text=":",font=("Times",16,"bold"))

        clicked_hour=tk.StringVar()
        self.hour=ttk.Combobox(self.set_alarm_frame,width=3,textvariable=clicked_hour)
        self.hour['values']=('00','01','02','03','04','05','06','07','08','09','10','11','12')
        self.hour.grid(column=1,row=0)
        self.hour.current('00')

        self.slash_label.grid(column=2,row=0)

        clicked_min=tk.StringVar()
        self.min=ttk.Combobox(self.set_alarm_frame,width=3,textvariable=clicked_min)
        self.min['values'] = (
        '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
        '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35',
        '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
        '54', '55', '56', '57', '58', '59')
        self.min.current('00')
        self.min.grid(column=3,row=0)

        clicked_div=tk.StringVar()
        self.div=ttk.Combobox(self.set_alarm_frame,width=3,textvariable=clicked_div)
        self.div['values']=('AM','PM')
        self.div.grid(column=4,row=0,padx=5)


        self.set_alarm_label_frame=tk.Frame(self.Alarm_frame)
        self.set_alarm_label_frame.pack(anchor="nw",side="top",padx=9,pady=7)

        self.set_alarm_label_label=tk.Label(self.set_alarm_label_frame,text="Label : ",font=("Times",13,"bold"))
        self.set_alarm_label_label.grid(column=0,row=0)

        null_label=tk.Label(self.set_alarm_label_frame,text="")
        null_label.grid(column=1,row=0,padx=19)
        input_label = tk.StringVar()
        self.label = ttk.Entry(self.set_alarm_label_frame, textvariable = input_label,width=23)
        self.label.focus_force()
        self.label.grid(column=2,row=0)

        self.set_alarm_ringtone_frame=tk.Frame(self.Alarm_frame)
        self.set_alarm_ringtone_frame.pack(anchor="nw",side="top",padx=9,pady=7)

        self.set_alarm_ringtone_label=tk.Label(self.set_alarm_ringtone_frame,text="Ringtone :",font=("Times",13,"bold"))
        self.set_alarm_ringtone_label.grid(column=0,row=0)
        #will  setting up browse ringtone box

        self.set_alarm_remind_frame=tk.Frame(self.Alarm_frame)
        self.set_alarm_remind_frame.pack(anchor="nw",side="top",padx=9,pady=7)

        self.set_alarm_remind_label=tk.Label(self.set_alarm_remind_frame,text="Remind me after 10 min :",font=("Times",13,"bold"))
        self.set_alarm_remind_label.grid(column=0,row=0)
        #will setting up on off to use or not use this



        self.root.mainloop()
Alarm_clock=Alarm()