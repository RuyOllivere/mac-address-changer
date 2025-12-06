#!/usr/bin/env python3
import subprocess
import random
import os
import platform

class Mac:
    def __init__(self):
        self.interface = input("Enter the interface (e.g., wlan0, eth0): ")

    def clean(self):
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def get_mac(self):
        try:
            output = subprocess.check_output(["ifconfig", self.interface]).decode()
            for line in output.split("\n"):
                if "ether" in line or "HWaddr" in line:
                    return line.strip()
        except subprocess.CalledProcessError:
            return "Error obtaining MAC."

    def change_mac(self, new_mac):
        os.system(f"ifconfig {self.interface} down")
        os.system(f"ifconfig {self.interface} hw ether {new_mac}")
        os.system(f"ifconfig {self.interface} up")

    def random_mac(self):
        hex_chars = "0123456789ABCDEF"
        return ":".join("".join(random.choice(hex_chars) for _ in range(2)) for _ in range(6))

    def show_menu(self):
        while True:
            self.clean()
            print("\n========= MENU =========")
            print("1 - Show current MAC")
            print("2 - Change MAC manually")
            print("3 - Change MAC randomly")
            print("4 - Exit")
            print("========================")

            option = input("Choose an option: ")

            if option == "1":
                mac = self.get_mac()
                print(f"\nCurrent MAC: {mac}")
                input("Press Enter to continue...")
                self.clean()

            elif option == "2":
                new_mac = input("Enter the new MAC (e.g., 00:11:22:33:44:55): ")
                self.change_mac(new_mac)
                print("MAC changed successfully!")
                input("Press Enter to continue...")
                self.clean()

            elif option == "3":
                random_mac_address = self.random_mac()
                prev_mac = self.get_mac()
                self.change_mac(random_mac_address)
                print(f"MAC changed randomly: {random_mac_address}")
                print(f"Previous MAC: {prev_mac}")
                input("Press Enter to continue...")
                self.clean()

            elif option == "4":
                print("Exiting...")
                break

            else:
                print("Invalid option!")
                input("Press Enter to continue...")

if __name__ == "__main__":
    main_program = Main()
    main_program.show_menu()
