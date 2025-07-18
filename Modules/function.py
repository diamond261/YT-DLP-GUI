import subprocess
import os
import sys

directory = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
os.environ["PATH"] += os.pathsep + ("D:\diamond261\Documents\For Me\VScode\Github\YT-DLP-GUI\App")

def main(base_setup,adv_setup):
    cmd=adv_checker(adv_setup)
    base_download(base_setup,cmd)
           
def update():
    command = "yt-dlp -U"
    subprocess.run(command, shell=True, capture_output=True, text=True)
    
def base_download(base_setup,cmd):
    if base_setup[4] == "video":
        if "best" in base_setup[3]:
            command = f'yt-dlp {cmd} -P "{base_setup[1]}" -S vcodec:h264,res,acodec:aac -o"%(uploader).30B - %(title).170B.%(ext)s"  --remux-video "{base_setup[2]}"  "{base_setup[0]}"'
        else:
            command = f'yt-dlp {cmd} -P "{base_setup[1]}" -o "%(title).170B.%(ext)s" --remux-video "{base_setup[2]}" -S "res:{str(base_setup[3])[:2].replace("p","")}" "{base_setup[0]}"'
    else:
        if "best" in base_setup[3]:
            command = f'yt-dlp {cmd} -P "{base_setup[1]}" -x -o "%(title).170B.%(ext)s" --audio-format "{base_setup[2]}" --audio-quality 0 "{base_setup[0]}"'
        else:
            command = f'yt-dlp {cmd} -P "{base_setup[1]}" -x -o "%(title).170B.%(ext)s" --audio-format "{base_setup[2]}" -S "abr:{str(base_setup[3]).replace("kbps","")}" "{base_setup[0]}"'
    return subprocess.run(command, shell=True, capture_output=True, text=True,encoding='utf-8',errors='replace')
def adv_checker(fc):
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
        for browser in ["Chrome", "Edge", "Firefox", "Opera", "Brave", "Vivaldi", "Whale"]:
            if i == browser:
                cmd_temp += f'--cookies-from-browser "{i}" '

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

    return str(cmd_temp)


if "__main__" == __name__:
    var1=["https://www.youtube.com/watch?v=Rp4iHpTvBY8","D:\diamond261\Documents\For Me\VScode\Github\YT-DLP-GUI","mp3","best","audio"]
    print(base_download(var1)) 