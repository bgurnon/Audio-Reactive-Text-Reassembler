def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def beginread(logfile):
    loglines = follow(logfile)
    for line in loglines:
        print(line)

beginread('output_text.txt')