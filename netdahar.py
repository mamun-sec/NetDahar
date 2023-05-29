import psutil
import os
from threading import Thread
from datetime import datetime
from datetime import date
import json
import time
from collections import namedtuple
from banner import BANNER

BANNER()
print("[+] NetDahar is running")

OWN_PATH = os.path.abspath(__file__)
OWN_DIR = os.path.dirname(OWN_PATH)
os.chdir(OWN_DIR)

UNIQUE_PROC_ID = []
OLD_COUNTER = 1

GLOBAL_PROC_DICT = {}
def GET_CONNECTIONS():
	global UNIQUE_PROC_ID
	global OLD_COUNTER
	global GLOBAL_PROC_DICT
	while True:
		for CONNECTION_X in psutil.net_connections():
			if CONNECTION_X.laddr and CONNECTION_X.raddr and CONNECTION_X.pid:
				try:
					PROC_OBJ = psutil.Process(CONNECTION_X.pid)

					PROC_NAME = PROC_OBJ.name()
					PROC_UNAME = PROC_OBJ.username()
					PROC_CPU = PROC_OBJ.cpu_percent()
					PROC_CMDLINE = PROC_OBJ.cmdline()
					PROC_CMDLINE = " ".join(str(each) for each in PROC_CMDLINE).replace(",", " ")
					PROC_EXEC_FILE = PROC_OBJ.exe()

					PROC_SRCIP = CONNECTION_X.laddr.ip
					PROC_SRCPORT = CONNECTION_X.laddr.port
					PROC_REMOTEIP = CONNECTION_X.raddr.ip
					PROC_REMOTEPORT = CONNECTION_X.raddr.port
					PROC_PID = CONNECTION_X.pid

					popenfile = namedtuple('popenfile', ['path', 'fd', 'position', 'mode', 'flags'])
					OPENED_FILE_PATHS = []
					EACH_PROCESS_X = psutil.Process(PROC_PID)
					try:
						PROC_OPEN_FILES = EACH_PROCESS_X.open_files()
						for PATH_TPL in PROC_OPEN_FILES:
							OPENED_FILE_PATHS.append(PATH_TPL.path)
					except:
						pass

					CURRENT_ID = str(PROC_SRCIP) + str(PROC_SRCPORT) + str(PROC_REMOTEIP) + str(PROC_REMOTEPORT)

					if PROC_NAME in GLOBAL_PROC_DICT and CURRENT_ID not in UNIQUE_PROC_ID:
						NEW_PROC_NAME = "(" + str(OLD_COUNTER) + ") " + str(PROC_NAME)
						GLOBAL_PROC_DICT[NEW_PROC_NAME] = GLOBAL_PROC_DICT.pop(PROC_NAME)
						LOG_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
						GLOBAL_PROC_DICT[PROC_NAME] = {"Log Time": LOG_TIME, "Source IP": PROC_SRCIP, "Source Port": PROC_SRCPORT, "Remote IP": PROC_REMOTEIP, "Remote Port": PROC_REMOTEPORT, "Process ID": PROC_PID, "Process File": PROC_EXEC_FILE , "Username": PROC_UNAME, "CPU Percentage": PROC_CPU, "Process CMDline": str(PROC_CMDLINE), "Opened Files": OPENED_FILE_PATHS}
						UNIQUE_PROC_ID.append(CURRENT_ID)
						OLD_COUNTER = OLD_COUNTER + 1

					elif PROC_NAME not in GLOBAL_PROC_DICT:
						LOG_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
						GLOBAL_PROC_DICT[PROC_NAME] = {"Log Time": LOG_TIME, "Source IP": PROC_SRCIP, "Source Port": PROC_SRCPORT, "Remote IP": PROC_REMOTEIP, "Remote Port": PROC_REMOTEPORT, "Process ID": PROC_PID, "Process File": PROC_EXEC_FILE , "Username": PROC_UNAME, "CPU Percentage": PROC_CPU, "Process CMDline": str(PROC_CMDLINE), "Opened Files": OPENED_FILE_PATHS}
						UNIQUE_PROC_ID.append(CURRENT_ID)
						OLD_COUNTER = OLD_COUNTER + 1

					time.sleep(1)

				except psutil.NoSuchProcess:
					continue

def FILE_WRITER():
	while True:
		now = datetime.now()
		CURRENT_DATE_TIME = now.strftime("%d/%m/%Y %H:%M:%S")
		WRITE_DICT = {}
		WRITE_DICT["Last Updated Time"] = str(CURRENT_DATE_TIME)
		WRITE_DICT["Network Log of Each Process"] = GLOBAL_PROC_DICT
		if "nt" in os.name:
			today = date.today()
			REPORT_FILE = ".\\Report\\" + str(today) + ".json"
			with open(REPORT_FILE, mode="w") as f:
				json.dump(WRITE_DICT, f, indent=4)
				print("[+] New log saved to '" + str(REPORT_FILE) + "' at " + str(CURRENT_DATE_TIME))
		else:
			today = date.today()
			REPORT_FILE = "./Report/" + str(today) + ".json"
			with open(REPORT_FILE, mode="w") as f:
				json.dump(WRITE_DICT, f, indent=4)
				print("[+] New log saved to '" + str(REPORT_FILE) + "' at " + str(CURRENT_DATE_TIME))
		time.sleep(20)

if __name__ == "__main__":
	connections_thread = Thread(target=GET_CONNECTIONS)
	connections_thread.start()
	file_write_thread = Thread(target=FILE_WRITER)
	file_write_thread.start()

