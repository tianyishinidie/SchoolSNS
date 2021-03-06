from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chatWindow(object):
    def setupUi(self, chatWindow):
        chatWindow.setObjectName("chatWindow")
        chatWindow.resize(908, 759)
        self.scrollArea = QtWidgets.QScrollArea(chatWindow)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 871, 471))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFixedHeight(400)
        
        messageList = QtWidgets.QVBoxLayout()
        messageList.setObjectName("messageList")

        groupBox = QtWidgets.QWidget()
        groupBox.setLayout(messageList)
        
        self.scrollArea.setWidget(groupBox)
        self.textarea = QtWidgets.QTextEdit(chatWindow)
        self.textarea.setGeometry(QtCore.QRect(20, 510, 871, 181))
        self.textarea.setObjectName("textarea")
        self.sendBut = QtWidgets.QPushButton(chatWindow)
        self.sendBut.setGeometry(QtCore.QRect(650, 700, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.sendBut.setFont(font)
        self.sendBut.setObjectName("sendBut")

        self.retranslateUi(chatWindow)
        QtCore.QMetaObject.connectSlotsByName(chatWindow)

    def retranslateUi(self, chatWindow):
        _translate = QtCore.QCoreApplication.translate
        chatWindow.setWindowTitle(_translate("chatWindow", "与 某某用户 交谈中"))
        self.sendBut.setText(_translate("chatWindow", "发送"))


class Ui_registerWindow(object):
    def setupUi(self, registerWindow):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(652, 510)
        registerWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.accountInput = QtWidgets.QLineEdit(registerWindow)
        self.accountInput.setGeometry(QtCore.QRect(190, 90, 261, 41))
        self.accountInput.setObjectName("accountInput")
        self.nickInput = QtWidgets.QLineEdit(registerWindow)
        self.nickInput.setGeometry(QtCore.QRect(192, 160, 261, 41))
        self.nickInput.setObjectName("nickInput")
        self.passwordInput = QtWidgets.QLineEdit(registerWindow)
        self.passwordInput.setGeometry(QtCore.QRect(192, 230, 261, 41))
        self.passwordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setReadOnly(False)
        self.passwordInput.setObjectName("passwordInput")
        self.rePasswordInput = QtWidgets.QLineEdit(registerWindow)
        self.rePasswordInput.setGeometry(QtCore.QRect(190, 300, 261, 41))
        self.rePasswordInput.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.rePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rePasswordInput.setReadOnly(False)
        self.rePasswordInput.setObjectName("rePasswordInput")
        self.label = QtWidgets.QLabel(registerWindow)
        self.label.setGeometry(QtCore.QRect(70, 100, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(registerWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(registerWindow)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(registerWindow)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 101, 16))
        self.label_4.setObjectName("label_4")
        self.registerBut = QtWidgets.QPushButton(registerWindow)
        self.registerBut.setGeometry(QtCore.QRect(370, 400, 241, 51))
        self.registerBut.setObjectName("registerBut")

        self.retranslateUi(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "Dialog"))
        self.label.setText(_translate("registerWindow", "学号"))
        self.label_2.setText(_translate("registerWindow", "昵称"))
        self.label_3.setText(_translate("registerWindow", "密码"))
        self.label_4.setText(_translate("registerWindow", "再次输入密码"))
        self.registerBut.setText(_translate("registerWindow", "注册"))


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(400, 300)
        self.registerBut = QtWidgets.QPushButton(loginWindow)
        self.registerBut.setGeometry(QtCore.QRect(230, 240, 93, 28))
        self.registerBut.setObjectName("registerBut")
        self.loginBut = QtWidgets.QPushButton(loginWindow)
        self.loginBut.setGeometry(QtCore.QRect(90, 240, 93, 28))
        self.loginBut.setObjectName("loginBut")
        self.accountInput = QtWidgets.QLineEdit(loginWindow)
        self.accountInput.setGeometry(QtCore.QRect(180, 90, 113, 21))
        self.accountInput.setObjectName("accountInput")
        self.passwordInput = QtWidgets.QLineEdit(loginWindow)
        self.passwordInput.setGeometry(QtCore.QRect(180, 140, 113, 21))
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setGeometry(QtCore.QRect(110, 90, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.showLab = QtWidgets.QLabel(loginWindow)
        self.showLab.setGeometry(QtCore.QRect(110, 180, 171, 16))
        self.showLab.setText("")
        self.showLab.setObjectName("showLab")
        self.showLab_2 = QtWidgets.QLabel(loginWindow)
        self.showLab_2.setGeometry(QtCore.QRect(110, 190, 171, 20))
        self.showLab_2.setText("")
        self.showLab_2.setObjectName("showLab_2")

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "登录"))
        self.registerBut.setText(_translate("loginWindow", "注册"))
        self.loginBut.setText(_translate("loginWindow", "登录"))
        self.label.setText(_translate("loginWindow", "账号"))
        self.label_2.setText(_translate("loginWindow", "密码"))


class Ui_friWindow(object):
    def setupUi(self, friWindow):
        friWindow.setObjectName("friWindow")
        friWindow.resize(400, 705)
        self.avatar = QtWidgets.QGraphicsView(friWindow)
        self.avatar.setGeometry(QtCore.QRect(20, 20, 80, 80))
        self.avatar.setObjectName("avatar")
        self.nick = QtWidgets.QLabel(friWindow)
        self.nick.setGeometry(QtCore.QRect(110, 30, 111, 16))
        self.nick.setObjectName("nick")
        self.account = QtWidgets.QLabel(friWindow)
        self.account.setGeometry(QtCore.QRect(110, 70, 72, 15))
        self.account.setObjectName("account")
        self.friendInvite = QtWidgets.QPushButton(friWindow)
        self.friendInvite.setGeometry(QtCore.QRect(240, 20, 141, 31))
        self.friendInvite.setObjectName("friendInvite")
        self.addFriend = QtWidgets.QPushButton(friWindow)
        self.addFriend.setGeometry(QtCore.QRect(240, 60, 141, 31))
        self.addFriend.setObjectName("addFriend")
        self.setting = QtWidgets.QPushButton(friWindow)
        self.setting.setGeometry(QtCore.QRect(290, 660, 93, 31))
        self.setting.setObjectName("setting")
        
        self.scrollArea = QtWidgets.QScrollArea(friWindow)
        self.scrollArea.setGeometry(QtCore.QRect(20, 120, 361, 500))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 338, 498))
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        friList = QtWidgets.QVBoxLayout()
        friList.setObjectName("friList")
        friList.setAlignment(QtCore.Qt.AlignTop)
        scrollAreaWidgetContents.setLayout(friList)
        self.scrollArea.setWidget(scrollAreaWidgetContents)

        self.retranslateUi(friWindow)
        QtCore.QMetaObject.connectSlotsByName(friWindow)

    def retranslateUi(self, friWindow):
        _translate = QtCore.QCoreApplication.translate
        friWindow.setWindowTitle(_translate("friWindow", "Dialog"))
        self.nick.setText(_translate("friWindow", "nick"))
        self.account.setText(_translate("friWindow", "account"))
        self.friendInvite.setText(_translate("friWindow", "好友邀请"))
        self.addFriend.setText(_translate("friWindow", "添加好友"))
        self.setting.setText(_translate("friWindow", "账户设置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    friWindow = QtWidgets.QDialog()
    ui = Ui_friWindow()
    ui.setupUi(friWindow)
    from friWindow import friListItem
    friWindow.findChild(QtWidgets.QVBoxLayout,'friList').addWidget(
        friListItem({'nick':'sdsd',
                        'avatar':'1',
                        'id':'1212',
                        'unread':0,
                        'online':'0'}))
    friWindow.show()
    sys.exit(app.exec_())
