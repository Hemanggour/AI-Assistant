import subprocess
import os

def open_application(app_name):
    try:
        if app_name.lower() == 'notepad':
            subprocess.Popen(['notepad.exe'])
        elif app_name.lower() == 'calculator':
            subprocess.Popen(['calc.exe'])
        elif app_name.lower() == 'paint':
            subprocess.Popen(['mspaint.exe'])
        elif app_name.lower() == 'wordpad':
            subprocess.Popen(['write.exe'])
        elif app_name.lower() == 'explorer':
            subprocess.Popen(['explorer.exe'])
        elif app_name.lower() == 'vlc':
            subprocess.Popen(['C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe'])        
        elif app_name.lower() == "youtube":
            subprocess.Popen(["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\chrome_proxy.exe"])
        else:
            print(f"Application '{app_name}' is not recognized.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app_name = input("Enter the name of the application to open: ")
    open_application(app_name)
