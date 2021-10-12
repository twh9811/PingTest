#!/usr/bin/python3
import os
import subprocess
from sys import stdout
import time

"""
The purpose of this file is to run various ping tests to tell the user whether or not their network is running properly.
@author Travis Hill
date: 9/16/2021
"""

def clear_Shell():
    """
    Clears the terminal window when ran
    """
    subprocess.run('clear', shell=True)

def ping(ip,url):
    """
    Runs the ping command using either the IP or the url.
    Can only be one or the other.
    """
    if url == None:
        exitCode = os.system("ping -c 1 " + ip)
    elif ip == None:
        exitCode = os.system("ping -c 1 " + url)
    return exitCode

def fail_Or_Not(exitCode):
    """
    Determines whether or not the ping was successful
    """
    if exitCode == 0:
        print("Test suceeded!")
    else:
        print("Test failed. Contact your system Administrator")
    time.sleep(2)
    clear_Shell()

def get_Default_Gateway():
    """
    Runs an IP route command which then sorts the output using grep and it gets the default gateway IP in one long string
    It then splits the string on spaces to get ONLY the ip address.
    """
    comProcess = subprocess.Popen(["ip route","|","grep default"], shell=True,stdout=subprocess.PIPE)
    gateway = comProcess.stdout.read().decode()
    default = gateway.split(" ")
    return default[2]

def test_Gateway_Connectivity():
    """
    Tests the default gateway connectivity utilizing the ping and get_Default_Gateway functions
    """
    clear_Shell()
    ip = get_Default_Gateway()
    print("Running test... pinging " + ip)
    time.sleep(2)
    response = ping(ip, None)
    clear_Shell()
    fail_Or_Not(response)
    
def test_Remote_Connectivity():
    """"
    Tests remote connections utilizing the ping function. 129.21.3.17 is RITs DNS Server.
    """
    clear_Shell()
    ip = "129.21.3.17"
    print("Running test... pinging " + ip)
    time.sleep(2)
    response = ping(ip, None)
    clear_Shell()
    fail_Or_Not(response)
    

def test_DNS_Resolution():
    """
    Tests whether or not DNS is working properly on the system.
    """
    clear_Shell()
    hostname = "www.google.com"
    print("Resolving DNS... pinging " + hostname)
    time.sleep(2)
    response = ping(None, hostname)
    clear_Shell()
    fail_Or_Not(response)

def display_Gateway_IP():
    """
    Displays the default gateway
    """
    clear_Shell()
    ip = get_Default_Gateway()
    print("Your default gateway is " + ip)
    time.sleep(2)
    clear_Shell()



def main():
    """
    Takes user input to determine what functionality they want to test on their network.
    It then calls the proper functions
    """
    clear_Shell()
    print("Ping Test Trouble Shooter")
    print("")
    while(True):
        print("1 - Test the connectivity to your gateway")
        print("2 - Test for remote connectivity")
        print("3 - Test for DNS Resolution")
        print("4 - Display gateway IP Address.")
        command = input("Please enter a number 1-4 or Q to quit the program: ")
        if command.upper() == "Q":
            break
        elif command == "1":
            clear_Shell()
            print("Testing connectivity to your gateway...")
            time.sleep(2)
            test_Gateway_Connectivity()
        elif command == "2":
            clear_Shell()
            print("Testing remote connectivity...")
            time.sleep(2)
            test_Remote_Connectivity()
        elif command == "3":
            clear_Shell()
            print("Testing for DNS Resolution...")
            time.sleep(2)
            test_DNS_Resolution()
        elif command == "4":
            clear_Shell()
            display_Gateway_IP()
        else:
            clear_Shell()
            print("Invalid option, try again.")
            time.sleep(1)
            clear_Shell()
            continue
    clear_Shell()
    print("Goodbye!")

main()
