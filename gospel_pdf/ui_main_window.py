# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files/main_window.ui'
#
# Created: Tue May 23 08:27:34 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(663, 493)
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 397, 380))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNavigate = QtGui.QMenu(self.menubar)
        self.menuNavigate.setObjectName(_fromUtf8("menuNavigate"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        window.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(window)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(window)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setWindowTitle(_fromUtf8("    Outlines :"))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockSearch = QtGui.QDockWidget(window)
        self.dockSearch.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.dockSearch.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockSearch.setObjectName(_fromUtf8("dockSearch"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.findBackButton = QtGui.QPushButton(self.dockWidgetContents_2)
        self.findBackButton.setObjectName(_fromUtf8("findBackButton"))
        self.horizontalLayout.addWidget(self.findBackButton)
        self.findTextEdit = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.findTextEdit.setObjectName(_fromUtf8("findTextEdit"))
        self.horizontalLayout.addWidget(self.findTextEdit)
        self.findNextButton = QtGui.QPushButton(self.dockWidgetContents_2)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.horizontalLayout.addWidget(self.findNextButton)
        self.findCloseButton = QtGui.QPushButton(self.dockWidgetContents_2)
        self.findCloseButton.setText(_fromUtf8(""))
        self.findCloseButton.setObjectName(_fromUtf8("findCloseButton"))
        self.horizontalLayout.addWidget(self.findCloseButton)
        self.dockSearch.setWidget(self.dockWidgetContents_2)
        window.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuNavigate.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "Gospel PDF", None))
        self.menuFile.setTitle(_translate("window", "&File", None))
        self.menuNavigate.setTitle(_translate("window", "Navigate", None))
        self.menuView.setTitle(_translate("window", "&View", None))
        self.toolBar.setWindowTitle(_translate("window", "toolBar", None))
        self.dockSearch.setWindowTitle(_translate("window", "Search Text :", None))
        self.findBackButton.setText(_translate("window", "Find Back", None))
        self.findNextButton.setText(_translate("window", "Find/Next", None))

