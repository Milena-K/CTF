msg = [9,0,9,0,9,0,9,0,7,8,3,4,0,7,6,5,4,3,2,0,7,8,6,5,4,2,0,2,3,4,0,7,2,3,8,4,5,0,2,3,4,5,6,7,8,0,7,6,0,7,2,3,8,4,5,0,2,3,4,5,6,7,0,2,3,8,4,5,0,2,3,8,4,5,0,2,3,8,6,5,0]

def slow_start():
    #pins = [ 0 for i in range(8) ]
    pins = ["null", "null","A", "B", "C", "D", "E", "F", "G", "DP"]
    message = ""
    for m in msg:
        if m > 0:
            message += pins[m]
    print(message)

slow_start()
