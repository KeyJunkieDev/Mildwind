#Mildwind Save Manager
import os, sys

def printsaves():
	print("AVAILABLE SAVES")
	print(", ".join(map(str, os.listdir("saves"))))
	print("\n")

print("MILDWIND SAVE MANAGER (EXPERIMENTAL)")
	
try:
	os.listdir("saves")
	print("\n")
	print("With the save manager, you can type the following commands:\nDelete\nRefresh\nClear\nExit")

	while True:
		print("\n")
		printsaves()
		command = input(">").lower()
		if command == "delete":
			file = input("Type the name of the save file you want to delete.\n>")
			confirm = input("Are you sure you want to delete " + file + " (y/n)?\n>").lower()
			if confirm == "y":
				try:
					os.remove("saves/" + file)
				except FileNotFoundError:
					print("File not found.")
			else:
				print("Back to main menu.")
		elif command == "exit":
			confirm = input("Are you sure you want to exit (y/n)?\n>").lower()
			if confirm == "y":
				sys.exit()
			else:
				print("Back to main menu.")
		elif command == "refresh":
			pass
		elif command in ["clear", "cls"]:
			clear = "\n" *100
			print(clear)
		else:
			print("Invalid command entered.")
except FileNotFoundError:
	input("\nNo \"saves\" folder found. Run the game first.")