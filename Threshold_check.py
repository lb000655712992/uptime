from database.CRUD import config_table_backend, data_table_backend, eMail_backend
import email_send
import time


def email_content(hostname, value, threshold):
    result = "This is alarm for router {} over the threshold {} over {}.".format(hostname, value, threshold)
    return result


vms = data_table_backend.read()
config = config_table_backend.read()[0]
eMails = eMail_backend.read()
while True:
    vms = data_table_backend.read()
    config = config_table_backend.read()[0]
    eMail = eMail_backend.read()
    for vm in vms:
        print(vm)
        if int(vm["Uptime"]) > int(config["Threshold"]):
            print(vm["Hostname"], vm["Uptime"], config["Threshold"])
            content = email_content(vm["Hostname"], vm["Uptime"], config["Threshold"])
            for eMail in eMails:
                email_send.email_send(eMail["eMail"], content)     # email_send(to, Text)
    time.sleep(300)
