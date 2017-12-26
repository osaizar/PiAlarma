import time
import smtplib

MAIL = ""
PASS = ""

ALARMA_MEZUA = """
Gaztetxeko alarma!
ADI!
"""

def bidali_alarma(korreoa):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	try:
		server.login(MAIL, PASS)

		msg = ALARMA_MEZUA # Noiz gertatu den gehitu daiteke agian
		server.sendmail(MAIL, korreoa, msg)
		server.quit()
	except Exception, e:
		print "Extepzioa alarma korreora bidaltzean "+str(e)
		print "Jarraitu egingo da..."

	return True

def sensorea_irakurri():
    return 0

def lortu_korreoak():
    k = open("korreoak.txt","r").read()
    return k.split("\n")

def alarma():
    korreoak = lortu_korreoak()
    for k in korreoak:
        bidali_alarma(k)

def main():
    while True:
        sensorea = sensorea_irakurri()
        if sensorea == 1:
            time.sleep(60) # minutu bat itxoin
            alarma()
        time.sleep(0.01) # 10 ms

if __name__ == "__main__":
    main()
