import sys

# Read
with open(" ".join(sys.argv[1:]), "r") as file:
    filedata = file.read()

# Replace
filedata = filedata.replace(
    "</head>", '<link rel="stylesheet" href="custom.css" /></head>'
)

# Write
with open(" ".join(sys.argv[1:]), "w") as file:
    file.write(filedata)
