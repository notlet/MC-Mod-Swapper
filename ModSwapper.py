from pprint import pprint
import json
import shutil, os

print('')
print(' m    m            #   mmmm')
print(' ##  ##  mmm    mmm#  #"   "m     m  mmm   mmmm   mmmm    mmm    m mm')
print(' # ## # #" "#  #" "#  "#mmm "m m m" "   #  #" "#  #" "#  #"  #   #"  "')
print(' # "" # #   #  #   #      "# #m#m#  m"""#  #   #  #   #  #""""   #')
print(' #    # "#m#"  "#m##  "mmm#"  # #   "mm"#  ##m#"  ##m#"  "#mm"   #')
print('                                           #      #')
print('                                           "      "')
print('')

with open('data.json', 'r') as infile:
    data = json.load(infile)

print("[0] Add new folder.")
for i, item in enumerate(data):
    print("[" + str(i + 1) + "] " + item["displayname"] + " (" + item["mcversion"] + ")")

action = input('\nAction:\n')
print("")

try:
    if action == "0":
        displayname = input("Enter new display name:\n")
        dirname = input("\nEnter directory name:\n")
        mcversion = input("\nEnter minecraft version:\n")

        data.append({
        'displayname':displayname,
        'dirname':dirname,
        'mcversion':mcversion,
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

        os.mkdir(os.path.join("files", dirname))
        print("Created new directory at " + os.path.join("files", dirname))

    else:
        homedir = os.path.expanduser("~")
        targetdir = os.path.join(homedir, "AppData\Roaming\.minecraft\mods")

        if len(os.listdir(targetdir)) != 0:
            for filename in os.listdir(targetdir):
                file_path = os.path.join(targetdir, filename)
                print("Deleting " + filename + "...")
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        print("")
        srcdir = os.path.join("files", data[int(action) - 1]["dirname"])
        allfiles = os.listdir(srcdir)
        shutil.copytree(srcdir, targetdir, dirs_exist_ok=True)
        for i, item in enumerate(allfiles):
            print("Copying " + item + "...")

except Exception as e:
    print('Failed to copy. Reason: %e')

finally:
    input("\nPress ENTER to exit the program.")