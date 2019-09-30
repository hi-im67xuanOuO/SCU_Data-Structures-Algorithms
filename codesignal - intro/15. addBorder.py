def addBorder(picture):
    # For picture = ["abc",
    #                "ded"]
    # the output should be
    # addBorder(picture) = ["*****",
    #                       "*abc*",
    #                       "*ded*",
    #                       "*****"]
    x = []
    x.append("*"*(len(picture[0])+2))
    for i in range(len(picture)):
        x.append("*"+picture[i]+"*")
    x.append("*"*(len(picture[0])+2))
    return x
