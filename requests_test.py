import requests
import time
'''
A > B & C
A x B
A > B
A x C
A > C
A x B & C
'''
aIP = "192.168.1.173:9090"
bDeviceName = "OnCollab%20A10%206654,"
cDeviceName = "OnCollab%20A10%20666F"

urls = [
    "http://" + aIP + "/illuminet/multicast?enable=1",
    "http://" + aIP + "/illuminet/multicast/connect?client=" + bDeviceName +
    cDeviceName,
    "http://" + aIP + "/illuminet/multicast/disconnect?client=" + bDeviceName,
    "http://" + aIP + "/illuminet/multicast/connect?client=" + bDeviceName,
    "http://" + aIP + "/illuminet/multicast/disconnect?client=" + cDeviceName,
    "http://" + aIP + "/illuminet/multicast/connect?client=" + cDeviceName,
    "http://" + aIP + "/illuminet/multicast/disconnect?client=" + bDeviceName +
    cDeviceName,
]

# sleeps = [2, 8, 2, 6, 2, 6, 2]

count = 50
while count > 0:
    for i in range(7):
        try:
            response = requests.get(urls[i])
            if (response.status_code == 200):
                print("success: " + urls[i])
            else:
                print("error code: " + response.status_code + " " + urls[i])
        except Exception as e:
            print(e)

        # time.sleep(sleeps[i])
        time.sleep(10)

    count -= 1
