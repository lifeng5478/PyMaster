import datetime,time
import sys
import serial
import serial.tools.list_ports
import os
import threading
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from UpSendOS import Ui_mainWindow

CHAR_TO_UP = 255


class mwindow(QMainWindow, Ui_mainWindow):
    ser = serial.Serial()
    sigle1 = pyqtSignal(str)
    sigle2 = pyqtSignal(int)
    statusSigle = pyqtSignal(str)

    def __init__(self, parent=None):
        super(mwindow, self).__init__(parent)
        self.setupUi(self)
        self.Get_Serial_No()
        self.KeyNum1 = 0
        self.t1 = None
        self.iBytes = None
        self.openfile_name = None
        self.openfile_size = 0
        self.Pint1 = 0
        self.NumToSend = 0
        self.CHAR_TO_UP = 255
        self.BCC_Num = None
        self.BufferDate = []
        self.OpenSerialB.clicked.connect(self.Open_Close_Port)
        self.OpenFileB.clicked.connect(self.Open_File)
        self.SendB.clicked.connect(self.Send_Data)
        self.ClearB.clicked.connect(self.Clear_Windows)
        self.sigle1.connect(self.Recv_Data)
        self.sigle2.connect(self.Probar_Disp)
        self.statusSigle.connect(self.StatuBar_Message)

    def Get_Serial_No(self):
        print("获取串口号")
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            print('无可用串口')
            self.PortComb.clear()
            self.PortComb.addItem("没有串口！")
            self.statusSigle.emit("没有串口！")

        else:
            self.PortComb.clear()
            for i in range(0, len(port_list)):
                port = list(port_list[i])
                self.PortComb.addItem(str(port[0]))
                self.statusBar.showMessage(str(port[0]))

    def Open_Close_Port(self):
        self.KeyNum1 += 1
        if self.PortComb.currentText() != "没有串口！":
            if self.KeyNum1 == 1:
                print("打开串口")
                self.ser.port = self.PortComb.currentText()
                self.ser.baudrate = self.BaudComb.currentText()
                try:
                    self.ser.open()
                    if self.ser.is_open:
                        self.OpenSerialB.setText("关闭串口")
                        self.statusSigle.emit("串口打开成功！")
                        print("当前端口号为： %s" % self.ser.port)
                        print("串口波特率为： %d" % self.ser.baudrate)
                        # self.statusBar.showMessage("一切就绪！")
                except:
                    self.KeyNum1 = 0
                    self.statusSigle.emit("请检查串口是否被占用！")

            elif self.KeyNum1 == 2:
                print("关闭串口")
                self.OpenSerialB.setText("打开串口")
                self.SendB.setText("开始发送")
                self.ser.close()
                if self.ser.isOpen():
                    self.statusSigle.emit("串口关闭失败！")
                else:
                    self.NumToSend = 0
                    self.statusSigle.emit("串口关闭成功！")
                self.KeyNum1 = 0
        else:
            self.statusSigle.emit("请检查串口连接！")

    def Send_Data(self):
        self.CHAR_TO_UP = int(self.PackComb.currentText())
        if self.ser.is_open:
            if self.FilePath.text() != 'FileName':
                with open(self.FilePath.text(), 'rb') as f:
                    self.iBytes = f.read()
                self.ser.reset_input_buffer()
                self.t1 = threading.Thread(target=self.Send_File_Threading)
                self.t1.start()
                # self.t1.join()
                if self.t1.is_alive():
                    self.NumToSend = 0
                    self.statusSigle.emit("发送中...")
                    self.SendB.setText("正在发送！")

            else:
                print("没有文件！")
                self.statusSigle.emit("没有文件！")
        else:
            print("串口未准备好！")
            self.statusSigle.emit("串口未打开！")

    def Send_File_Threading(self):
        i = 0
        self.sigle1.emit("clear")
        header = "#LS=UPGRADE,'" + os.path.basename(self.openfile_name[0]) + "'"
        stopCMD = '#LS=FTE,"' + os.path.basename(self.openfile_name[0]) + '"'
        print(header.encode())
        self.ser.write(header.encode())
        # self.ser.write("#LS=UPGRADE,"+os.path.basename(self.openfile_name[0])+"'")
        while self.ser.in_waiting == 0:
            print("wait Huiying！")
            time.sleep(1)
        huiying = self.ser.read(self.ser.in_waiting).decode()
        self.sigle1.emit(huiying)
        if huiying =="#LS=UPGRADE,OK\r\n":
            header1 = '#LS=FT,"' + os.path.basename(self.openfile_name[0]) + '",' + str(self.openfile_size)
            print(header1.encode())
            self.sigle1.emit("第一阶段校验成功！")
            self.statusSigle.emit("MCU准备就绪准备下载！")
            self.ser.reset_input_buffer()
            self.ser.write(header1.encode())
        else:
            print("单片机未准备好")
            self.SendB.setText("重新发送")
            self.statusSigle.emit("可能文件过大！")
            return
        while self.ser.in_waiting == 0:
            print("wait Huiying2！")
            time.sleep(1)
        huiying2 = self.ser.read(self.ser.in_waiting).decode()
        self.sigle1.emit(huiying2)
        if huiying2=="#LS=FT,OK\r\n":
            print("启动！")
            self.sigle1.emit("第二阶段校验成功！开始下载！")
            self.statusSigle.emit("MCU开始下载！")
            self.ShouFlag = 1
        else:
            self.statusSigle.emit("发送验证失败！")
            print("单片机未准备好")
            self.SendB.setText("重新发送")
            return
        if self.ShouFlag == 1:
            # for i in range(0, len(self.iBytes), 3):
            head = [0x23, 0x4c, 0x53, 0x3d, 0x46, 0x54, 0x54]
            while True:
                self.BufferDate = self.iBytes[i:i + self.CHAR_TO_UP]
                buflist = list(self.BufferDate)
                LenH = len(self.BufferDate) >> 8
                LenL = len(self.BufferDate) & 0xff
                buflist.insert(0, LenL)
                buflist.insert(0, LenH)
                NumH = self.NumToSend >> 8
                NumL = self.NumToSend & 0xff
                buflist.insert(0, NumL)
                buflist.insert(0, NumH)
                ReadyToSend2 = head + buflist
                self.BCC_Check(ReadyToSend2[7:len(ReadyToSend2)])
                ReadyToSend2.append(self.BCC_Num)
                print(bytes(ReadyToSend2).hex())
                # ReadyToSend = (bytes('#LS=FTT',encoding='utf-8') +bytes(hex(self.NumToSend),encoding='utf-8') +bytes(hex(len(self.BufferDate)),encoding='utf-8') + self.BufferDate)
                # ReadyToSend = ReadyToSend+str(self.BCC_Num).encode()
                # print(self.BCC_Num)
                self.BinText.setText(str(self.NumToSend))
                self.ser.write(bytes(ReadyToSend2))
                self.Pint1 = int(i * 100 / len(self.iBytes))
                self.sigle2.emit(self.Pint1)
                # print(i)
                if (i + self.CHAR_TO_UP) >= len(self.iBytes):
                    print("发送完毕！")
                    self.NumToSend = 0
                    self.sigle2.emit(100)
                    self.SendB.setText("发送完毕！")
                    self.statusSigle.emit("MCU升级成功！")
                    time.sleep(1)
                    self.ser.write(stopCMD.encode())
                    self.statusSigle.emit("App已启动！！")
                    break
                nowTime = datetime.datetime.now()
                # print(nowTime)
                while self.ser.in_waiting == 0:
                    DelayTime = datetime.datetime.now()
                    if ((DelayTime - nowTime).seconds) > 5:
                        print("超时数据！")
                        time.sleep(1)

                    # None
                    # print(os.times())
                    # self.statusBar.showMessage("发送超时！")
                print("反馈数据长度是：",self.ser.in_waiting)
                #Reply_RX=self.ser.readall().decode()
                #while(self.ser.in_waiting!=0)
                Reply_RX = self.ser.read(self.ser.in_waiting).decode()
                print("接收到的是：",Reply_RX)
                if len(Reply_RX) > 9:
                    if Reply_RX== ('#LS=FTT,OK,'+str(self.NumToSend)+'\r\n'):
                        print("接收成功！")
                        self.statusSigle.emit("接收成功！")
                        # self.MCUTextEdit.appendPlainText(str(tou))
                        self.sigle1.emit(Reply_RX)
                        i += self.CHAR_TO_UP
                        self.NumToSend += 1
                    elif Reply_RX[8:13]== 'Error':
                        print("指令头错误！")
                        self.sigle1.emit(Reply_RX)
                        self.statusSigle.emit("指令头错误！")
                        # break
                    else:
                        print("接收回复指令错误！")
                        break
                else:
                    print("错误指令！")
                    self.statusSigle.emit("错误指令！")
                    # break

                self.ser.reset_input_buffer()

        else:
            print("校验失败！")
            # break

        # while True:
        #     if self.ser.in_waiting:
        #         print(self.ser.read_all())

    def Recv_Data(self, str):
        if str == "clear":
            self.Clear_Windows()
        else:
            self.MCUTextEdit.appendPlainText(str)

    def Open_File(self):
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Bin files(*.hex, *.bin)')
        if self.openfile_name[0] == '':
            print("文件未打开！")
        else:
            print(self.openfile_name[0])
            self.FilePath.setText(self.openfile_name[0])
            self.openfile_size = os.path.getsize(self.openfile_name[0])
            self.FileSize.setText(str(self.openfile_size))
            self.statusSigle.emit("文件打开成功！")

    def Clear_Windows(self):
        self.MCUTextEdit.clear()

    def Probar_Disp(self, num):
        self.PrograssBar.setValue(num)

    def StatuBar_Message(self, str):
        self.statusBar.showMessage(str)

    def BCC_Check(self, listS):
        t = None
        for i in range(0, len(listS)):
            if i:
                t ^= listS[i]
            else:
                t = listS[i] ^ 0
        self.BCC_Num = t
        print("校验码是", self.BCC_Num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mwindow()
    myWin.show()
    sys.exit(app.exec_())
