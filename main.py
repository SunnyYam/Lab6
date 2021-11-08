def rot(num):
    stroke = str(num)
    i = stroke.find("6")
    if i != -1:
        stroke = stroke[0:i] + stroke[i].replace("6", "9") + stroke[i+1:]
    return int(stroke)
