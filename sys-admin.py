#import os
#os.system("ls")

import subprocess
subprocess.run(["ls", "-l", "README.md"])

command="uname"
commandArgument="-a"
print(f'\n Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'\n Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])