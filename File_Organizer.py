import os


# Move to C: drive and start checking if each file is an image, pdf, spreadsheet, or document
def main_organizer():
    os.chdir('C:\\')
    print(os.getcwd())


if __name__ == '__main__':
    main_organizer()
else:
    print("This module is not meant to be imported yet...")
