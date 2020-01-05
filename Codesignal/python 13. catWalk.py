def catWalk(code):
    # replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.
    
    #For line = "def      m   e  gaDifficu     ltFun        ction(x):", the output should be catWalk(line) = "def m e gaDifficu ltFun ction(x):".
    
    return " ".join(code.split())
