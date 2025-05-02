import time
import datetime
import sys
import webbrowser

def printtext():

    user_input = input("PRINT>> ")
    print(user_input)



def bootos():
    # Simulating a user input scenario
    return input(
        "-------------------------------------------------------"
        "\n- Choose A Number, This Key Will Tell What It Will Do -"
        "\n- 1 = TS-KERNEL 1.0.1.1 Codename 'Pulse'            -"
        "\n- 2 = Exit                                            -"
        "\n-------------------------------------------------------\n")


def boot():
    print("starting BOOT...")
    time.sleep(1)
    print(f"Reading root\\boot\\bootloader\\BOOT\\__pycache__\\boot.cpython-{sys.version_info.major}{sys.version_info.minor}.pyc")
    time.sleep(1)
    print("DONE PROCESS: 0% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: Commands Booting help As Expanple...")
    time.sleep(1)
    try:
        print("Commands:")
        print("help - Show this help message")
        print("exit - Exit the console")
        print("clear - Clear the console")
        print("whoami - Show the current user")
        print("tskerlan - start The TS-KERNEL-LANAGUAGE Interpiler")
        print("tsdesktop - start TS-DESKTOP and end cmd.exe")
        print("switch user --USER - Switch to user USER")
        print("shutdown --host_os - Shutdown Windows")
        print("ts-package - starts ts-package")
        print("time - Tells The Time")
        print("admindo - If A Linux User Is Seeing this, It's the Same As sudo")
        print("ts-distro - Same As neofetch")
        print("tscli - Same As ts-distro But with tscli")
        print("python - Same As The python Command In Other Terminals And Shells")
        print("boot - Boot Again")
        print("msnetwork - Start The Microsoft Network")
        print("version - Show the version of the distro and kernel")
        print("git - Same As The git Command In Other Terminals And Shells")
        print("gh - Same As The gh Command In Other Terminals And Shells")
        time.sleep(0.05)
        print("DONE PROCESS: 20% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: Commands")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(1)
    print("DONE PROCESS: 20% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTING: tskerlan Booting print Code From tskerlan For Test...")
    try:
        printtext()
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    time.sleep(0.05)
    print("DONE PROCESS: 40% TIME: SYSTEM READABLE TIME NOT SET HUMAN READABLE TIME NOT SET BOOTED: tskerlan")
    time.sleep(1)
    print("DONE PROCESS: 40% TIME: SETTING UP SYSTEM READABLE TIME HUMAN READABLE TIME NOT SET BOOTING: time.time()")
    try:
        print(time.time())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 60% TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTED: time.time()")
    time.sleep(1)
    print("DONE PROCESS: 60% TIME:", time.time(), "HUMAN READABLE TIME NOT SET BOOTING: datetime.datetime.now")
    try:
        print(datetime.datetime.now())
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 80% TIME:", time.time(), datetime.datetime.now(), "BOOTED: datetime.datetime.now()")
    time.sleep(1)
    print("DONE PROCESS: 80% TIME:", time.time(), datetime.datetime.now(), "BOOTING: Default Network (Microsoft Network (MSN))")
    try:
        webbrowser.open("https://www.msn.com")
    except Exception as e:
        print(f"BOOT: ERROR: Error Code 634: {e}")
        return False
    print("DONE PROCESS: 100% TIME:", time.time(), datetime.datetime.now(), "BOOTED: Default Network (Microsoft Network (MSN))")
    time.sleep(1)
    print("BOOT: BOOT has done booting and testing, booting TS-KERNEL and tscli...")
    time.sleep(2)
    return True