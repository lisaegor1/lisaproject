def text():
    lines = []
    with open('main.tf') as f:
        lines = f.readlines()

    count = 0
    security_file = open("sg.txt", "w")
    buffer = 0
    brackets = 0
    for line in lines:
    #print(line)
        if (line.find("aws_security_group") == 10):
            buffer = buffer + 1
        if(buffer > 0):
            security_file.write(line)
            if(line.count("}") == 1):
                brackets = brackets + 1
            if(line.count("}") == 0):
                brackets = 0
        if(brackets == 2):
            buffer = 0
