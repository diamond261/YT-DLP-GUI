import subprocess
from loguru import logger
import os
import sys

def main(base_setup,adv_setup,path):
    logger.info("Checking adv settings")
    cmd=adv_checker(adv_setup,path)
    logger.info("Start download")
    return base_download(base_setup,cmd)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    path = os.path.join(base_path, relative_path)
    return os.path.normpath(path)
    
def update():
    command = "yt-dlp -U"
    logger.info("Update yt-dlp")
    output=subprocess.run(command, shell=True, capture_output=True, text=True)
    logger.debug(f"Update output is  {output}")
    
def base_download(base_setup,cmd):
    if base_setup[4] == "video":
        if "best" in base_setup[3]:
            command = f'yt-dlp {cmd}-P "{base_setup[1]}" --sleep-requests 5 -S vcodec:h264,res,acodec:aac -o"%(title).170B.%(ext)s"  --remux-video "{base_setup[2]}"  "{base_setup[0]}"'
            logger.debug(f"running  {command}")
        else:
            command = f'yt-dlp {cmd}-P "{base_setup[1]}" --sleep-requests 5 -o "%(title).170B.%(ext)s" --remux-video "{base_setup[2]}" -S "res:{str(base_setup[3]).replace("p","")}" "{base_setup[0]}"'
            logger.debug(f"running  {command}")
    else:
        if "best" in base_setup[3]:
            command = f'yt-dlp {cmd}-P "{base_setup[1]}" --sleep-requests 5 -x -o "%(title).170B.%(ext)s" --audio-format "{base_setup[2]}" "{base_setup[0]}"'
            logger.debug(f"running  {command}")
        else:
            command = f'yt-dlp {cmd}-P "{base_setup[1]}" --sleep-requests 5 -x -o "%(title).170B.%(ext)s" --audio-format "{base_setup[2]}" --audio-quality "{str(base_setup[3]).replace("bps","")}" "{base_setup[0]}"'
            logger.debug(f"running  {command}")
    return subprocess.run(command, shell=True, capture_output=True, text=True,encoding='utf-8',errors='replace')
    
def adv_checker(fc,path):
    cmd_temp = ""
    for i in fc:
        if "retry" in i:
            cmd_temp += "-R infinite "
        elif "thumbnail" in i:
            cmd_temp += "--embed-thumbnail "
        elif "metadata" in i:
            cmd_temp += "--embed-metadata "
        elif "chapters" in i:
            cmd_temp += "--embed-chapters "
        elif "subtitle" in i:
            cmd_temp += "--embed-subs "
        # Browser check
        for browser in ["Firefox", "Opera", "Brave", "Vivaldi", "Whale"]:
            if i == browser:
                cmd_temp += f'--cookies-from-browser "{i}" '
            else:
                cmd_temp+= f'--cookies {resource_path(f"{path}/Cookies/Cookies.txt")} '

        # SponsorBlock options
        if i == "Mark":
            cmd_temp += '--sponsorblock-mark all '
        elif i == "Remove":
            cmd_temp += '--sponsorblock-remove all '
        # Date handling
        if i == "Date Range OFF":
            pass  # No action needed
        elif i == "This day":
            if len(fc) > 0:  # Safety check
                cmd_temp += f'--date {fc[-1]} '
        elif i == "Before":
            if len(fc) > 0:
                cmd_temp += f'--datebefore {fc[-1]} '
        elif i == "After":
            if len(fc) > 0:
                cmd_temp += f'--dateafter {fc[-1]} '
    logger.debug(f"adv cmd {cmd_temp}")
    return str(cmd_temp)


if "__main__" == __name__:
    var1=["https://youtu.be/dQw4w9WgXcQ","D:\diamond261\Documents\For Me\VScode\Github\YT-DLP-GUI","mp3","best","audio"]
    print(base_download(var1,"")) 