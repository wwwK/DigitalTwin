import serial #导入模块
import serial.tools.list_ports


def listIfHavePort():
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print('无可用串口')
    else:
        for i in range(0, len(port_list)):
            print(port_list[i])

    # # FileName : demo.py
    # # Author   : Adil
    # # DateTime : 2019/9/1 7:03
    # # SoftWare : PyCharm
    #
    #
    # import serial
    # # 这里使用的是windwos
    # from serial.tools.list_ports_windows import *
    #
    # plist = list(comports())
    #
    # if len(plist) <= 0:
    #     print ("The Serial port can't find!")
    # else:
    #     plist_0 =list(plist[0])
    #     serialName = plist_0[0]
    #     serialFd = serial.Serial(serialName,9600,timeout = 60)
    #     print ("check which port was really used >",serialFd.name)

def readPort():
    try:

        # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        portx = "COM3"
        # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = 115200
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        timex = 5
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)
        print("串口详情参数：", ser)

        print(ser.port)  # 获取到当前打开的串口名
        print(ser.baudrate)  # 获取波特率

        # result = ser.write("我是东小东".encode("gbk"))  # 写数据
        # print("写总字节数:", result)

        # print(ser.read())#读一个字节
        # print(ser.read(10).decode("gbk"))#读十个字节
        # print(ser.readline().decode("gbk"))#读一行
        # print(ser.readlines())#读取多行，返回列表，必须匹配超时（timeout)使用
        # print(ser.in_waiting)#获取输入缓冲区的剩余字节数
        # print(ser.out_waiting)#获取输出缓冲区的字节数

        # 循环接收数据，此为死循环，可用线程实现
        while True:
            if ser.in_waiting:
                str = ser.read(ser.in_waiting).decode("gbk")
                if (str == "exit"):  # 退出标志
                    break
                else:
                    print("收到数据：", str)
                    alist=str.split(' ')
                    alist=[float(i) for i in alist]
                    print(alist)
                    # for i in range(len(alist)):
                    #     print(float(alist[i])+1)


        print("---------------")
        ser.close()  # 关闭串口


    except Exception as e:
        print("---异常---：", e)

if __name__=='__main__':
    # listIfHavePort()
    readPort()