import socket
import os
import subprocess

from get_hosts import hostlist

def host_status(csvfile):
    hostsdict = hostlist(csvfile)
    return hostsdict

def  validate_host(csvfile):
    hostsdict = host_status(csvfile)
    statusdict = {}
    for name, ip in hostsdict.items():
        dns_response = subprocess.call(['ping', '-c', '1', '-t', '5', name])
        if dns_response == 0:
            statusdict[name] = "Good"
        elif dns_response == 2:
            statusdict[name] = "No Response"
        else:
            statusdict[name] = "Fail"

    return statusdict


    # name = {}
    # CI = {}
    # hostname = {}
    # status = {}
    #
    # for name, ip in hostsdict:
    #     try:
    #         ip = socket.gethostbyname(CI)
    #     except socket.error:
    #         pass
    #     name = socket.getfqdn(CI)
    #     data = name
    #
    #     hostname = rows['CI_Name']
    #     response = subprocess.Popen(['ping.exe',hostname], stdout = subprocess.PIPE).communicate()[0]
    #     response = response.decode()
    #     print(response)
    #     if 'bytes=32' in response:
    #         status = 'Up'
    #     elif 'destination host unreachable' in response:
    #         status = 'Unreachable'
    #     else:
    #         status = 'Down'
    #     if status == 'Down':
    #         ip = 'Not Found'
    #     with open('Output Final.csv', 'a', newline='') as csvoutput:
    #         output = csv.writer(csvoutput)
    #         output.writerow([hostname] + [data] + [status] + [ip])
#
if __name__ == '__main__':
    output = validate_host('hosts.xlsx')
    print(output)