from Modules import function as fc
import tkinter.filedialog as tkf
from datetime import datetime
from CTkTable import CTkTable
from datetime import datetime
import customtkinter as ctk
from PIL import Image   
import calendar
import sys
import os

directory = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
os.environ["PATH"] += os.pathsep + (fc.resource_path(directory+"/App"))
current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
fc.logger.add(fc.resource_path(f"{directory}/logs/log_{current_time}.log"))
fc.logger.debug(f"The script is on {directory}")
if not os.path.exists(fc.resource_path(f"{directory}/Cookies")):
    os.mkdir(fc.resource_path(f"{directory}/Cookies"))
    fc.logger.info("Cookies folder is created")
else:
    fc.logger.info("Cookies directory already exists")
app_state="system"
date_value=""
date_status=0
#color select
global_color=("#d8e2f9","#313443")
Reverse_global_color=("#313443","#d8e2f9")
frame_color=("#ced7ec","#2a2c39")
select_color=("#868e9f","#484c60")
hover_color=("#6a7082","#111d2f")
text_color=("#2c4f85","#b3bcd9")
#image
dl_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/dl_light.png")),dark_image=Image.open(fc.resource_path("resource/dl_drak.png")),size=(29, 29))
updata_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/updata_light.png")),dark_image=Image.open(fc.resource_path("resource/updata_dark.png")),size=(15,20))
browse_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/browse_light.png")),dark_image=Image.open(fc.resource_path("resource/browse_dark.png")),size=(25,25))
add_list_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/add_light.png")),dark_image=Image.open(fc.resource_path("resource/add_dark.png")),size=(28,28))
setting_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/setting_light.png")),dark_image=Image.open(fc.resource_path("resource/setting_dark.png")),size=(28,28))
del_list_image=ctk.CTkImage(light_image=Image.open(fc.resource_path("resource/delete_light.png")),dark_image=Image.open(fc.resource_path("resource/delete_dark.png")),size=(28,28))
#Main-windows
win=ctk.CTk(ctk.set_appearance_mode(app_state))
win.title("YouTube Video Downloader")
win.geometry("925x500") 
win.resizable(False,False)
#win.attributes("-topmost",True)
win.iconbitmap(fc.resource_path("resource/ytdlp_icon.ico"))
win.configure(fg_color=global_color)
#warningwindow
class WarningWindow:
    def __init__(self, icon_path, global_color, text_color, reverse_global_color, hover_color):
        # Initialize toplevel window
        self.warning_toplevel = ctk.CTkToplevel()
        self.warning_toplevel.title("warning")
        self.warning_toplevel.geometry("350x150")
        self.warning_toplevel.resizable(False, False)
        self.warning_toplevel.attributes("-topmost", True)
        self.warning_toplevel.iconbitmap(icon_path)
        self.warning_toplevel.configure(fg_color=global_color)

        # Create widgets
        self.warning_text = ctk.CTkLabel(
            self.warning_toplevel,
            text="Pleas write a URl and Path \nAnd choose Foramt and Quality",  # Original text preserved
            font=("Arial", 20),
            text_color=text_color
        )
        self.warning_text.pack()

        self.warning_btn = ctk.CTkButton(
            self.warning_toplevel,
            width=75,
            height=38,
            text="Ok",  # Original button text
            command=self.destroy_window,
            font=("Arial", 17),
            corner_radius=30,fg_color=global_color,
                           border_width=3,border_color=frame_color,
                         hover_color=hover_color,text_color=text_color)
        self.warning_btn.pack(pady=5)

    def destroy_window(self):
        """Destroy the toplevel window"""
        self.warning_toplevel.destroy()
class TypeWarningWindow:
    def __init__(self, icon_path, global_color, text_color, reverse_global_color, hover_color):
        # Initialize toplevel window
        self.warning_toplevel = ctk.CTkToplevel()
        self.warning_toplevel.title("warning")
        self.warning_toplevel.geometry("350x150")
        self.warning_toplevel.resizable(False, False)
        self.warning_toplevel.attributes("-topmost", True)
        self.warning_toplevel.iconbitmap(icon_path)
        self.warning_toplevel.configure(fg_color=global_color)

        # Create widgets
        self.warning_text = ctk.CTkLabel(
            self.warning_toplevel,
            text="Pleas choose a \ncorrect format or quality",  # Original text preserved
            font=("Arial", 20),
            text_color=text_color
        )
        self.warning_text.pack()

        self.warning_btn = ctk.CTkButton(
            self.warning_toplevel,
            width=75,
            height=38,
            text="Ok",  # Original button text
            command=self.destroy_window,
            font=("Arial", 17),
            corner_radius=30,fg_color=global_color,
                           border_width=3,border_color=frame_color,
                         hover_color=hover_color,text_color=text_color)
        self.warning_btn.pack(pady=5)

    def destroy_window(self):
        """Destroy the toplevel window"""
        self.warning_toplevel.destroy()
#event
def main():
    fc.logger.info("Init download cmd")
    global directory
    def base_checker():
        fc.logger.info("Start base check")
        base_list=[]
        check_list=[url_entry,path_entry,common_format_options,quality_options,type_options]
        for check in check_list:
            if "entry" in str(check):
                temp=check.get()
                fc.logger.debug(f"Entry value is {temp}")
                if temp == "":
                    fc.logger.error("Null value")
                    Warning=WarningWindow(icon_path=fc.resource_path("resource/ytdlp_icon.ico"),global_color=global_color,text_color=text_color,reverse_global_color=Reverse_global_color,hover_color=hover_color)
                    return False
                else:
                    base_list.append(temp)
            else:
                temp=check.get().lower()
                fc.logger.debug(f"Options value is {temp}")
                if temp == "format" or temp == "quality":
                    fc.logger.error("Null value")
                    Warning=WarningWindow(icon_path=fc.resource_path("resource/ytdlp_icon.ico"),global_color=global_color,text_color=text_color,reverse_global_color=Reverse_global_color,hover_color=hover_color)
                    return False
                else:
                    base_list.append(temp)
        return base_list
    def advence_checker():
        switch_list=[thumbnail_inf_switch,metadata_switch,chapters_switch,subs_switch,retry_inf_switch]
        advence_options_list=[cookies_options,sb_options,date_options]
        avc_function_on=[]
        global date_value
        for switch in switch_list:
            status=switch.get()
            if status == 1:
                avc_function_on.append(switch.cget("text"))
        for avc_options in advence_options_list:
            status=avc_options.get()
            if "OFF" in status:
                return ""
            else:
                temp=avc_options.get()
                avc_function_on.append(temp)
        avc_function_on.append(date_value)
        return avc_function_on
    def type_checker():
        fc.logger.info("Start type check")
        global type_options,quality_options,common_format_options
        current_type=type_options.get()
        fc.logger.debug(f"Current type is {current_type}")
        current_quality=quality_options.get()
        fc.logger.debug(f"Current quality is {current_quality}")
        current_format=common_format_options.get()
        fc.logger.debug(f"Current format is {current_format}")
        if current_type == "Video":
            if current_format in ["MP4","Webm","Mkv","Mov","Avi","Flv"] and current_quality in ["Best","4320p","2160p","1440p","1080p","720p","480p","360p","240p","144p"]:
                return True
            else:
                fc.logger.error("worng type ,quality and format")
                Warning=TypeWarningWindow(icon_path=fc.resource_path("resource/ytdlp_icon.ico"),global_color=global_color,text_color=text_color,reverse_global_color=Reverse_global_color,hover_color=hover_color)
                return False
        else:   
            if current_format in ["MP3","M4a","Aac","Alac","Flac","Opus"] and current_quality in ["Best","192Kbps","160Kbps","128Kbps"]:
                return True
            else:
                fc.logger.error("worng type ,quality and format")
                Warning=TypeWarningWindow(icon_path=fc.resource_path("resource/ytdlp_icon.ico"),global_color=global_color,text_color=text_color,reverse_global_color=Reverse_global_color,hover_color=hover_color)
                return False
    if table.get() != [['No.', 'URL', 'Format', 'Quality']]:
        fc.logger.info("Getting table data")
        temp=table.get()
        adv_temp=advence_checker()
        fc.logger.debug(f"Adv settings is {adv_temp}")
        for i in range(temp[-1][0]):
            url=temp[i+1][1]
            fmt=temp[i+1][2]
            qlt=temp[i+1][3]
            type=type_options.get
            base_temp=[url,fmt,qlt,type]
            fc.logger.debug(f"Base settings is {base_temp}")
            type_temp=type_checker()
            fc.logger.debug(f"Type checker output is {type_temp}")
            if type_temp:
                fc.main(base_temp,adv_temp)
            else:
                break
    else:
        base_temp=base_checker()
        if base_temp:
            type_temp=type_checker()
            fc.logger.debug(f"Type checker output is {type_temp}")
            if type_temp:
                if base_temp:
                    fc.logger.debug(f"Base settings is {base_temp}")
                    adv_temp=advence_checker()
                    fc.logger.debug(f"Adv settings is {adv_temp}")
                    output=fc.main(base_temp,adv_temp,directory)
                    fc.logger.debug(f"Download output is {output}")
def app_mode_event(mode):
  ctk.set_appearance_mode(mode)
  fc.logger.info(f"App change to {mode} mode")
def path_select_event():
  path=tkf.askdirectory(title="Chose a path to save")
  if path:
    path_entry.delete(0,"end")
    path_entry.insert(0,path)
def type_change_event(type):
    if type == "Video":
        fc.logger.info("Type change to video")
        quality_options.configure(values=["Quality","Best","4320p","2160p","1440p","1080p","720p","480p","360p","240p","144p"])
        quality_options.place(x=12.5,y=140)
        common_format_options.configure(values=["Format","MP4","Webm","Mkv","Mov","Avi","Flv"])
        common_format_options.place(x=12.5,y=80)
    elif type == "Audio":
        fc.logger.info("Type change to audio")
        quality_options.configure(values=["Quality","Best","192Kbps","160Kbps","128Kbps"])
        quality_options.place(x=12.5,y=140)
        common_format_options.configure(values=["Format","MP3","M4a","Aac","Alac","Flac","Opus"])
        common_format_options.place(x=12.5,y=80)
def add_to_table():
    fc.logger.info("Adding to the table")
    url = url_entry.get()
    fmt = common_format_options.get()
    quality = quality_options.get()
    if url and fmt != "Format" and quality != "Quality":
        current_data = table.get()
        row_number = len(current_data)
        new_row = [str(row_number), url, fmt, quality]
        table.add_row(index=row_number, values=new_row)
    else:
        fc.logger.error("Null value")
        warning_window=WarningWindow(icon_path=fc.resource_path("resource/ytdlp_icon.ico"),global_color=global_color,text_color=text_color,reverse_global_color=Reverse_global_color,hover_color=hover_color)
def delete_row(num):
    fc.logger.info("Deleting table value")
    try:
        row_index = int(num)
        if row_index >= 1:
            table.delete_row(row_index)
            current_data = table.get()
            for i in range(1, len(current_data)):
                current_data[i][0] = str(i)
            table.update_values(current_data)
            fc.logger.info("Successed delete the value")
        else:
            fc.logger.info("Value delete failed")
            fc.logger.error("overflowed")
    except ValueError:
        fc.logger.info("Value delete failed")
        fc.logger("valueerror")
def get_number():
    dialog = ctk.CTkInputDialog(text="Type a No. :", title="Delete a row",fg_color=global_color,
                                button_fg_color=global_color,button_hover_color=hover_color,
                                button_text_color=text_color,entry_fg_color=frame_color,entry_border_color=frame_color,
                                entry_text_color=text_color)
    num=dialog.get_input()
    delete_row(num)
#calendar
def open_calendar(state):
    global date_status
    if "OFF" in state:
        return "offed"
    if date_status == 0:
        calendar_win = ctk.CTkToplevel(win)
        calendar_win.title("Choose a date")
        calendar_win.geometry("350x400")

        today = datetime.today()
        current_year, current_month = today.year, today.month

        selected_year = ctk.IntVar(value=current_year)
        selected_month = ctk.IntVar(value=current_month)

        def update_calendar():
            for widget in cal_frame.winfo_children():
                widget.destroy()

            year = selected_year.get()
            month = selected_month.get()
            header_label.configure(text=f"{calendar.month_name[month]} {year}")

            cal = calendar.monthcalendar(year, month)
            weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

            for col, day in enumerate(weekdays):
                lbl = ctk.CTkLabel(cal_frame, text=day, width=5, font=("Arial", 12))
                lbl.grid(row=0, column=col, padx=5, pady=2)

            for row_idx, week in enumerate(cal):
                for col_idx, day in enumerate(week):
                    if day == 0:
                        lbl = ctk.CTkLabel(cal_frame, text=" ", width=5)
                        lbl.grid(row=row_idx+1, column=col_idx, padx=5, pady=2)
                    else:
                        btn_date = datetime(year, month, day)
                        if btn_date > today:
                            btn = ctk.CTkButton(cal_frame, text=str(day), width=30, height=30, state="disabled")
                        else:
                            btn = ctk.CTkButton(
                                cal_frame,
                                text=str(day),
                                width=30,
                                height=30,
                                command=lambda d=day: select_date(year, month, d, calendar_win)
                            )
                        btn.grid(row=row_idx+1, column=col_idx, padx=2, pady=2)

        def select_date(year, month, day, win):
            global date_value
            global date_state
            # Changed to YYYYMMDD format for yt-dlp
            date_value = f"{year}{month:02d}{day:02d}"  # e.g., "20250717" instead of "17/07/2025"
            date_state = 0
            win.destroy()

        # Rest of your existing code (change_year, change_month, etc.) remains the same
        def change_year(delta):
            selected_year.set(selected_year.get() + delta)
            update_calendar()

        def change_month(delta):
            new_month = selected_month.get() + delta
            if new_month > 12:
                selected_month.set(1)
                change_year(1)
            elif new_month < 1:
                selected_month.set(12)
                change_year(-1)
            else:
                selected_month.set(new_month)
            update_calendar()

        control_frame = ctk.CTkFrame(calendar_win)
        control_frame.pack(pady=5)

        prev_year_btn = ctk.CTkButton(control_frame, text="<<", width=40, command=lambda: change_year(-1))
        prev_year_btn.grid(row=0, column=0, padx=5)

        prev_month_btn = ctk.CTkButton(control_frame, text="<", width=40, command=lambda: change_month(-1))
        prev_month_btn.grid(row=0, column=1, padx=5)

        header_label = ctk.CTkLabel(control_frame, text=f"{calendar.month_name[current_month]} {current_year}", font=("Arial", 14))
        header_label.grid(row=0, column=2, padx=10)

        next_month_btn = ctk.CTkButton(control_frame, text=">", width=40, command=lambda: change_month(1))
        next_month_btn.grid(row=0, column=3, padx=5)

        next_year_btn = ctk.CTkButton(control_frame, text=">>", width=40, command=lambda: change_year(1))
        next_year_btn.grid(row=0, column=4, padx=5)

        cal_frame = ctk.CTkFrame(calendar_win)
        cal_frame.pack(pady=10)

        update_calendar()
#frame
app_options_frame=ctk.CTkFrame(win,width=200,height=1300,fg_color=frame_color)
app_options_frame.place(x=0,y=-20)
dl_option_frame=ctk.CTkFrame(win,width=425,height=150,corner_radius=20,fg_color=frame_color)
dl_option_frame.place(x=215,y=120)
type_option_frame=ctk.CTkFrame(win,width=175,height=260,corner_radius=20,fg_color=frame_color)
type_option_frame.place(x=660,y=15)
#scrollableframe
table_scrollable_frame = ctk.CTkScrollableFrame(win, width=585, height=10,fg_color=global_color)
table_scrollable_frame.place(x=215, y=290)
#options
cookies_options=ctk.CTkOptionMenu(dl_option_frame,width=150,
                                  height=30,
                                  corner_radius=25,
                                  values=["Cookies import OFF","Cookies.txt", "Firefox", "Opera", "Brave","Vivaldi", "Whale"],
                                  font=("Arial",17),
                                    dropdown_font=("Arial",16),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color,
)
cookies_options.place(x=205,y=35,anchor="w")
sb_options=ctk.CTkOptionMenu(dl_option_frame,width=120,
                             height=30,
                             corner_radius=25,
                             values=["SponsorBlock OFF","Mark","Remove"],
                             font=("Arial",17),
                                   dropdown_font=("Arial",16),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color)
sb_options.place(x=205,y=75,anchor="w")
date_options=ctk.CTkOptionMenu(dl_option_frame,width=120,
                                   height=30,corner_radius=25,values=["Date Range OFF","This day","Before","After"],
                                   font=("Arial",17),
                                   dropdown_font=("Arial",16),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color,command=open_calendar)
date_options.place(x=205,y=115,anchor="w")
common_format_options=ctk.CTkOptionMenu(type_option_frame,
                                       width=150,
                                       height=45,
                                       corner_radius=25,
                                       values=["Format","MP4","Webm","Mkv","Mov","Avi","Flv"],
                                   font=("Arial",18),
                                   dropdown_font=("Arial",15),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color)
common_format_options.place(x=12.5,y=80)
quality_options=ctk.CTkOptionMenu(type_option_frame,width=150,
                                   height=40,corner_radius=25,values=["Quality","Best","4320p","2160p","1440p","1080p","720p","480p","360p","240p","144p"],
                                   font=("Arial",18),
                                   dropdown_font=("Arial",15),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color)
quality_options.place(x=13,y=140)
app_mode_options=ctk.CTkOptionMenu(app_options_frame,width=115,
                                   height=40,corner_radius=15,values=["System","Light","Dark"],
                                   font=("Arial",17),
                                   dropdown_font=("Arial",16),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color,
                                   command=app_mode_event)
app_mode_options.place(x=35,y=355)
type_options=ctk.CTkOptionMenu(type_option_frame,width=150,height=45,corner_radius=25,
                                       values=["Video","Audio"],
                                   font=("Arial",18),
                                   dropdown_font=("Arial",15),
                                   fg_color=global_color,
                                   button_color=global_color,
                                   text_color=text_color,
                                   button_hover_color=hover_color,
                                   dropdown_fg_color=global_color,
                                   dropdown_hover_color=hover_color,
                                   dropdown_text_color=text_color,
                                   command=type_change_event)
type_options.place(x=12.5,y=20)
#label
app_label=ctk.CTkLabel(app_options_frame,text="YouTube Video",font=("Arial",20),text_color=text_color)
app_label.place(x=30,y=27)
app_label_2=ctk.CTkLabel(app_options_frame,text="Downloader",font=("Arial",24),text_color=text_color)
app_label_2.place(x=30,y=65)
app_label_3=ctk.CTkLabel(app_options_frame,text="Appearance Mode :",font=("Arial",18),text_color=text_color)
app_label_3.place(x=20,y=320)
video_options_label=ctk.CTkLabel(app_options_frame,text="Other options:",font=("Arial",19),text_color=text_color)
video_options_label.place(x=675,y=10)
url_label=ctk.CTkLabel(win,text="URL :",font=("Arial",19),text_color=text_color)
url_label.place(x=210,y=17)
path_label=ctk.CTkLabel(win,text="Path :",font=("Arial",20),text_color=text_color)
path_label.place(x=210,y=72)
#Entry
url_entry=ctk.CTkEntry(win,width=380,height=40,placeholder_text="Video, playlist, channel",
                       font=("Arial",20),fg_color=frame_color,text_color=text_color,border_color=frame_color)
url_entry.place(x=270,y=15)
path_entry=ctk.CTkEntry(win,width=300,height=40,placeholder_text="Video or Audio's save path",
                       font=("Arial",20),fg_color=frame_color,text_color=text_color,border_color=frame_color)
path_entry.place(x=270,y=70)
#Button
update_btn=ctk.CTkButton(app_options_frame,
                         width=75,height=38,
                         text="Updata",image=updata_image,
                         command=fc.update,font=("Arial",17),
                         corner_radius=12.5,fg_color=global_color
                         ,hover_color=hover_color,
                         text_color=text_color)
update_btn.place(x=40,y=425)
download_btn=ctk.CTkButton(win,width=50,height=40,
                           text="",image=dl_image,
                           command=main,corner_radius=30,fg_color=global_color,
                           border_width=3,border_color=frame_color,
                         hover_color=hover_color,text_color=text_color)
download_btn.place(x=840,y=15)
browse_btn=ctk.CTkButton(win,width=50,height=40,corner_radius=30,fg_color=global_color,
                         text="",
                         hover_color=hover_color,text_color=text_color,
                         border_width=3,border_color=frame_color,
                         command=path_select_event,image=browse_image)
browse_btn.place(x=580,y=70)
add_list_btn=ctk.CTkButton(win,width=75,height=40,text="",
                           image=add_list_image,
                           command=add_to_table,
                           corner_radius=30,fg_color=global_color,
                           border_width=3,border_color=frame_color,
                         hover_color=hover_color,text_color=text_color)
add_list_btn.place(x=840,y=75)
delete_list_btn=ctk.CTkButton(win,width=75,height=40,text="",
                           image=del_list_image,
                           command=get_number,
                           corner_radius=30,fg_color=global_color,
                           border_width=3,border_color=frame_color,
                         hover_color=hover_color,text_color=text_color)
delete_list_btn.place(x=840,y=135)
#Switch
thumbnail_inf_switch=ctk.CTkSwitch(dl_option_frame,text="Embed thumbnail ",font=("Arial",18),
                                   progress_color=global_color,button_color=Reverse_global_color,button_hover_color=Reverse_global_color)
thumbnail_inf_switch.place(anchor="w",x=10,y=25)
metadata_switch=ctk.CTkSwitch(dl_option_frame,text="Embed metadata ",font=("Arial",18),
                                   progress_color=global_color,button_color=Reverse_global_color,button_hover_color=Reverse_global_color)
metadata_switch.place(anchor="w",x=10,y=50)
chapters_switch=ctk.CTkSwitch(dl_option_frame,text="Embed chapters ",font=("Arial",18),
                                   progress_color=global_color,button_color=Reverse_global_color,button_hover_color=Reverse_global_color)
chapters_switch.place(anchor="w",x=10,y=75)
subs_switch=ctk.CTkSwitch(dl_option_frame,text="Embed subtitle",font=("Arial",18),
                                   progress_color=global_color,button_color=Reverse_global_color,button_hover_color=Reverse_global_color)
subs_switch.place(anchor="w",x=10,y=100)
retry_inf_switch=ctk.CTkSwitch(dl_option_frame,text="Infinite retry",font=("Arial",18),
                                   progress_color=global_color,button_color=Reverse_global_color,button_hover_color=Reverse_global_color)
retry_inf_switch.place(anchor="w",x=10,y=125)
#table
table = CTkTable(table_scrollable_frame, row=1, column=4, values=[["No.", "URL", "Format", "Quality"]])
table.pack(expand=True, fill="both", padx=10, pady=5)

if __name__ == "__main__":
    fc.logger.info("Start GUI")
    win.mainloop()
    fc.logger.info("App closed")