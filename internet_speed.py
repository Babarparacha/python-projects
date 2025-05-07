import speedtest as st
def speed_test():
    test=st.Speedtest()
    down_speed=test.download()
    down_speed=round(down_speed/10**6,2)
    print("download speed in Mbps is :",down_speed)
    up_speed=test.upload()
    up_speed=round(up_speed/10**6,2)
    print("uploaded speed in Mbps is :",up_speed)
    ping=test.results.ping
    print("pings:",ping)
speed_test()    
