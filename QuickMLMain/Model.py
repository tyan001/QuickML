# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Model6.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow.keras.optimizers as optimizers
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import json



class Ui_MainWindow(object):
    def __init__(self):
        self.input_shape = False
        self.flatten = False
        self.model = tf.keras.Sequential()
        self.folder_path = os.getcwd()
        self.target_size = (150, 150)
        self.history = None
        self.class_labels = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.ToolButton.setGeometry(QtCore.QRect(10, 10, 25, 19))
        self.ToolButton.setObjectName("ToolButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 509, 901, 73))
        self.frame.setStyleSheet("QWidget{color: rgb(48, 58, 255); }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, -10, 901, 82))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OptimizerComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.OptimizerComboBox.setObjectName("OptimizerComboBox")
        self.OptimizerComboBox.addItem("")
        self.OptimizerComboBox.addItem("")
        self.OptimizerComboBox.addItem("")
        self.gridLayout_3.addWidget(self.OptimizerComboBox, 1, 2, 1, 1)
        self.CompileButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.CompileButton.setEnabled(False)
        self.CompileButton.setObjectName("CompileButton")
        self.gridLayout_3.addWidget(self.CompileButton, 1, 0, 1, 1)
        self.LossComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.LossComboBox.setObjectName("LossComboBox")
        self.LossComboBox.addItem("")
        self.LossComboBox.addItem("")
        self.gridLayout_3.addWidget(self.LossComboBox, 1, 3, 1, 1)
        self.LearningRateLine = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LearningRateLine.sizePolicy().hasHeightForWidth())
        self.LearningRateLine.setSizePolicy(sizePolicy)
        self.LearningRateLine.setObjectName("LearningRateLine")
        self.gridLayout_3.addWidget(self.LearningRateLine, 1, 1, 1, 1)
        self.OptimizerLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.OptimizerLabel.setFont(font)
        self.OptimizerLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.OptimizerLabel.setObjectName("OptimizerLabel")
        self.gridLayout_3.addWidget(self.OptimizerLabel, 0, 2, 1, 1)
        self.LossLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LossLabel.setFont(font)
        self.LossLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.LossLabel.setObjectName("LossLabel")
        self.gridLayout_3.addWidget(self.LossLabel, 0, 3, 1, 1)
        self.LearningRateLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LearningRateLabel.setFont(font)
        self.LearningRateLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.LearningRateLabel.setObjectName("LearningRateLabel")
        self.gridLayout_3.addWidget(self.LearningRateLabel, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 4, 1, 1)
        self.EpochLine = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EpochLine.sizePolicy().hasHeightForWidth())
        self.EpochLine.setSizePolicy(sizePolicy)
        self.EpochLine.setObjectName("EpochLine")
        self.gridLayout_3.addWidget(self.EpochLine, 1, 4, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(10, 480, 1081, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(98, 114, 146);\n"
                                       "border-style: none;\n"
                                       "border-radius: 10px;\n"
                                       "text-align:center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "border-radius:10px;    \n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.511, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(170, 0, 255, 255));\n"
                                       "}\n"
                                       "")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.DataDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.DataDirectory.setGeometry(QtCore.QRect(40, 10, 1051, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DataDirectory.setFont(font)
        self.DataDirectory.setObjectName("DataDirectory")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(930, 510, 160, 83))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SaveButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout_2.addWidget(self.SaveButton, 0, 0, 1, 1)
        self.RunButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.RunButton.setObjectName("RunButton")
        self.gridLayout_2.addWidget(self.RunButton, 1, 1, 1, 1)
        self.NextButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.NextButton.setObjectName("NextButton")
        self.gridLayout_2.addWidget(self.NextButton, 0, 1, 1, 1)
        self.HistoryButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.HistoryButton.setObjectName("HistoryButton")
        self.gridLayout_2.addWidget(self.HistoryButton, 2, 0, 1, 2)
        self.ModelSummary = QtWidgets.QTextBrowser(self.centralwidget)
        self.ModelSummary.setGeometry(QtCore.QRect(540, 40, 551, 431))
        self.ModelSummary.setObjectName("ModelSummary")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 521, 431))
        self.widget.setStyleSheet("QWidget{color: rgb(48, 58, 255); }\n"
                                  "")
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.KernelSizeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.KernelSizeLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KernelSizeLabel.sizePolicy().hasHeightForWidth())
        self.KernelSizeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.KernelSizeLabel.setFont(font)
        self.KernelSizeLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.KernelSizeLabel.setObjectName("KernelSizeLabel")
        self.gridLayout.addWidget(self.KernelSizeLabel, 0, 2, 1, 1)
        self.DenseAcitvationBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.DenseAcitvationBox.setObjectName("DenseAcitvationBox")
        self.DenseAcitvationBox.addItem("")
        self.DenseAcitvationBox.addItem("")
        self.DenseAcitvationBox.addItem("")
        self.gridLayout.addWidget(self.DenseAcitvationBox, 3, 3, 1, 1)
        self.PoolingKernelBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.PoolingKernelBox.setObjectName("PoolingKernelBox")
        self.PoolingKernelBox.addItem("")
        self.PoolingKernelBox.addItem("")
        self.gridLayout.addWidget(self.PoolingKernelBox, 2, 2, 1, 1)
        self.ActivationLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ActivationLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ActivationLabel.sizePolicy().hasHeightForWidth())
        self.ActivationLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ActivationLabel.setFont(font)
        self.ActivationLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.ActivationLabel.setObjectName("ActivationLabel")
        self.gridLayout.addWidget(self.ActivationLabel, 0, 3, 1, 1)
        self.LayersLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.LayersLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LayersLabel.sizePolicy().hasHeightForWidth())
        self.LayersLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LayersLabel.setFont(font)
        self.LayersLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.LayersLabel.setObjectName("LayersLabel")
        self.gridLayout.addWidget(self.LayersLabel, 0, 0, 1, 1)
        self.KernelLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.KernelLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KernelLabel.sizePolicy().hasHeightForWidth())
        self.KernelLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.KernelLabel.setFont(font)
        self.KernelLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.KernelLabel.setObjectName("KernelLabel")
        self.gridLayout.addWidget(self.KernelLabel, 0, 1, 1, 1)
        self.DenseAddButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.DenseAddButton.setObjectName("DenseAddButton")
        self.gridLayout.addWidget(self.DenseAddButton, 3, 4, 1, 1)
        self.ConvolutionLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ConvolutionLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvolutionLabel.sizePolicy().hasHeightForWidth())
        self.ConvolutionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ConvolutionLabel.setFont(font)
        self.ConvolutionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ConvolutionLabel.setObjectName("ConvolutionLabel")
        self.gridLayout.addWidget(self.ConvolutionLabel, 1, 0, 1, 1)
        self.DenseLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DenseLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DenseLabel.sizePolicy().hasHeightForWidth())
        self.DenseLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DenseLabel.setFont(font)
        self.DenseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DenseLabel.setObjectName("DenseLabel")
        self.gridLayout.addWidget(self.DenseLabel, 3, 0, 1, 1)
        self.ConvolutionLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvolutionLineEdit.sizePolicy().hasHeightForWidth())
        self.ConvolutionLineEdit.setSizePolicy(sizePolicy)
        self.ConvolutionLineEdit.setObjectName("ConvolutionLineEdit")
        self.gridLayout.addWidget(self.ConvolutionLineEdit, 1, 1, 1, 1)
        self.ConvKernelBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ConvKernelBox.setObjectName("ConvKernelBox")
        self.ConvKernelBox.addItem("")
        self.ConvKernelBox.addItem("")
        self.ConvKernelBox.addItem("")
        self.gridLayout.addWidget(self.ConvKernelBox, 1, 2, 1, 1)
        self.PoolingLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PoolingLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PoolingLabel.sizePolicy().hasHeightForWidth())
        self.PoolingLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PoolingLabel.setFont(font)
        self.PoolingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PoolingLabel.setObjectName("PoolingLabel")
        self.gridLayout.addWidget(self.PoolingLabel, 2, 0, 1, 1)
        self.PoolingAddButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PoolingAddButton.setObjectName("PoolingAddButton")
        self.gridLayout.addWidget(self.PoolingAddButton, 2, 4, 1, 1)
        self.ConvActivationBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ConvActivationBox.setObjectName("ConvActivationBox")
        self.ConvActivationBox.addItem("")
        self.ConvActivationBox.addItem("")
        self.ConvActivationBox.addItem("")
        self.gridLayout.addWidget(self.ConvActivationBox, 1, 3, 1, 1)
        self.ConvolutionAddButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ConvolutionAddButton.setObjectName("ConvolutionAddButton")
        self.gridLayout.addWidget(self.ConvolutionAddButton, 1, 4, 1, 1)
        self.DenseLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DenseLineEdit.sizePolicy().hasHeightForWidth())
        self.DenseLineEdit.setSizePolicy(sizePolicy)
        self.DenseLineEdit.setObjectName("DenseLineEdit")
        self.gridLayout.addWidget(self.DenseLineEdit, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.RunButton.setDisabled(True)

        # Push Buttons Functions
        self.ConvolutionAddButton.clicked.connect(lambda: self.add_layer(0))
        self.PoolingAddButton.clicked.connect(lambda: self.add_layer(1))
        self.DenseAddButton.clicked.connect(lambda: self.add_layer(2))
        self.ToolButton.clicked.connect(lambda: self.pick_folder())
        self.CompileButton.clicked.connect(lambda: self.model_compile())
        self.RunButton.clicked.connect(lambda: self.run_model())
        # self.AuxButton.clicked.connect(lambda: self.test_func())
        self.HistoryButton.clicked.connect(lambda: self.show_history())
        self.SaveButton.clicked.connect(lambda: self.save_model())
        # Push Buttons

        # Check Events #
        self.ConvolutionLineEdit.textChanged.connect(lambda: self.on_line_edit_changed(0))
        self.DenseLineEdit.textChanged.connect(lambda: self.on_line_edit_changed(1))
        self.EpochLine.textChanged.connect(lambda: self.on_line_edit_changed((2)))
        # Check Events #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ToolButton.setText(_translate("MainWindow", "..."))
        self.OptimizerComboBox.setItemText(0, _translate("MainWindow", "Adam"))
        self.OptimizerComboBox.setItemText(1, _translate("MainWindow", "RMSProp"))
        self.OptimizerComboBox.setItemText(2, _translate("MainWindow", "SGD"))
        self.CompileButton.setText(_translate("MainWindow", "Compile"))
        self.LossComboBox.setItemText(0, _translate("MainWindow", "binary_crossentropy"))
        self.LossComboBox.setItemText(1, _translate("MainWindow", "categorical_crossentropy"))
        self.LearningRateLine.setText(_translate("MainWindow", "0.001"))
        self.OptimizerLabel.setText(_translate("MainWindow", "Optimizer"))
        self.LossLabel.setText(_translate("MainWindow", "Loss Function"))
        self.LearningRateLabel.setText(_translate("MainWindow", "Learning rate"))
        self.label_8.setText(_translate("MainWindow", "Epochs"))
        self.EpochLine.setText(_translate("MainWindow", "10"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.RunButton.setText(_translate("MainWindow", "Run"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.HistoryButton.setText(_translate("MainWindow", "History"))
        self.KernelSizeLabel.setText(_translate("MainWindow", "Kernel Size"))
        self.DenseAcitvationBox.setItemText(0, _translate("MainWindow", "sigmoid"))
        self.DenseAcitvationBox.setItemText(1, _translate("MainWindow", "tanh"))
        self.DenseAcitvationBox.setItemText(2, _translate("MainWindow", "relu"))
        self.PoolingKernelBox.setItemText(0, _translate("MainWindow", "(2,2)"))
        self.PoolingKernelBox.setItemText(1, _translate("MainWindow", "(3,3)"))
        self.ActivationLabel.setText(_translate("MainWindow", "Activation"))
        self.LayersLabel.setText(_translate("MainWindow", "Layers"))
        self.KernelLabel.setText(_translate("MainWindow", "Kernel/Neurons"))
        self.DenseAddButton.setText(_translate("MainWindow", "Add"))
        self.ConvolutionLabel.setText(_translate("MainWindow", "Convolution"))
        self.DenseLabel.setText(_translate("MainWindow", "Dense"))
        self.ConvolutionLineEdit.setText(_translate("MainWindow", "16"))
        self.ConvKernelBox.setItemText(0, _translate("MainWindow", "(2,2)"))
        self.ConvKernelBox.setItemText(1, _translate("MainWindow", "(3,3)"))
        self.ConvKernelBox.setItemText(2, _translate("MainWindow", "(4,4)"))
        self.PoolingLabel.setText(_translate("MainWindow", "Max Pooling"))
        self.PoolingAddButton.setText(_translate("MainWindow", "Add"))
        self.ConvActivationBox.setItemText(0, _translate("MainWindow", "sigmoid"))
        self.ConvActivationBox.setItemText(1, _translate("MainWindow", "tanh"))
        self.ConvActivationBox.setItemText(2, _translate("MainWindow", "relu"))
        self.ConvolutionAddButton.setText(_translate("MainWindow", "Add"))
        self.DenseLineEdit.setText(_translate("MainWindow", "256"))
        #
        self.DataDirectory.setText(QtCore.QDir.currentPath())
        #

    def test_func(self):
        #print(self.class_labels)
        # with open('test.json', 'a') as f:
        #     json.dump(self.class_labels,f)
        #     f.write("\n")
        with open('test.json') as f:
            for line in f:
                labels = json.loads(line)
        print(labels)

    def model_summary(self):
        """
        Function to print model summary onto a text box.
        :return:
        """
        try:
            string_list = []
            self.model.summary(line_length=65, print_fn=lambda x: string_list.append(x))
            short_model_summary = "\n".join(string_list)
            self.ModelSummary.setText(short_model_summary)
        except:
            self.quick_message_box('No model', 'There was no model to show', icon=QtWidgets.QMessageBox.Question)

    def add_layer(self, layer):
        """
        This function is used to add the layers to the model with the use of corresponding buttons. Since we only need
        to put the input shape once we have a boolean operation to just put it once, same goes for the flatten layer
        operation.

        :param layer:
        Which layer you want to use, 0 for Convolution2D layer, 1 for MaxPooling2D layer, 2 for Dense layer
        """

        if layer == 0:
            # print(self.input_shape)
            if not self.input_shape:
                self.model.add(tf.keras.layers.Conv2D(int(self.ConvolutionLineEdit.text()),
                                                      eval(self.ConvKernelBox.currentText()),
                                                      activation=self.ConvActivationBox.currentText(),
                                                      input_shape=(self.target_size[0], self.target_size[1], 3)))
                self.input_shape = True
            else:
                self.model.add(tf.keras.layers.Conv2D(int(self.ConvolutionLineEdit.text()),
                                                      eval(self.ConvKernelBox.currentText()),
                                                      activation=self.ConvActivationBox.currentText()
                                                      ))

        elif layer == 1:
            self.model.add(tf.keras.layers.MaxPool2D(eval(self.PoolingKernelBox.currentText())))

        elif layer == 2:
            # print(self.flatten)
            if not self.flatten:
                self.model.add(tf.keras.layers.Flatten())
                self.model.add(tf.keras.layers.Dense(int(self.DenseLineEdit.text()),
                                                     activation=self.DenseAcitvationBox.currentText()))
                self.ConvolutionAddButton.setEnabled(False)
                self.PoolingAddButton.setEnabled(False)
                self.CompileButton.setEnabled(True)
                self.flatten = True
            else:
                self.model.add(tf.keras.layers.Dense(int(self.DenseLineEdit.text()),
                                                     activation=self.DenseAcitvationBox.currentText()))

        self.model_summary()

    def on_line_edit_changed(self, value):
        """
        This function is used as a checker for when a QLineEdit object is changed.
        :param value:
        When value is set to 0 it checks on the QLineEdit for the Convolutional section
        When value is set to 1 it checks on the QLineEdit for the Dense section
        """
        try:
            if value == 0:
                x = int(self.ConvolutionLineEdit.text())
                if x > 32:
                    self.ConvolutionLineEdit.setText('32')
            elif value == 1:
                x = int(self.DenseLineEdit.text())
                if x > 512:
                    self.DenseLineEdit.setText('512')
            elif value == 2:
                x = int(self.EpochLine.text())
                if x > 50:
                    self.EpochLine.setText('50')
        except:
            return


    def pick_folder(self):
        """
        Function for file dialog to pick a folder
        """

        self.folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Directory")
        self.DataDirectory.setText(self.folder_path)

    def run_model(self):
        if self.directory_error_check():
            training_dir, testing_dir, num_categories = self.data_directories()
        else:
            return

        if num_categories > 2 and self.LossComboBox.currentText() == self.LossComboBox.itemText(0):
            self.quick_message_box(title='Warning', message='detected more than 2 categories set loss to categorical',
                                   btn=QtWidgets.QMessageBox.Ok, icon=QtWidgets.QMessageBox.Warning)
            return

        datagen = ImageDataGenerator(1. / 255)

        if self.LossComboBox.currentText() == self.LossComboBox.itemText(0):
            train_generator = datagen.flow_from_directory(training_dir,
                                                          target_size=self.target_size,
                                                          class_mode='binary',
                                                          batch_size=32)

            testing_generator = datagen.flow_from_directory(testing_dir,
                                                            target_size=self.target_size,
                                                            class_mode='binary',
                                                            batch_size=32)

            self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
            self.model_summary()

        elif self.LossComboBox.currentText() == self.LossComboBox.itemText(1):
            print(training_dir)
            print(testing_dir)
            train_generator = datagen.flow_from_directory(training_dir,
                                                          target_size=self.target_size,
                                                          class_mode="categorical",
                                                          batch_size=32)

            testing_generator = datagen.flow_from_directory(testing_dir,
                                                            target_size=self.target_size,
                                                            class_mode="categorical",
                                                            batch_size=32)

            self.model.add(tf.keras.layers.Dense(num_categories, activation='softmax'))
            self.model_summary()

        self.class_labels = train_generator.class_indices
        callback = Epoch_Callback(int(self.EpochLine.text()), self.progressBar)
        self.history = self.model.fit(train_generator, validation_data=testing_generator,
                                      epochs=int(self.EpochLine.text()), callbacks=[callback])

    def model_compile(self):
        opt = self.ret_optimizer(self.OptimizerComboBox.currentText())
        self.model.compile(optimizer=opt, loss=self.LossComboBox.currentText(), metrics=['acc'])
        self.ModelSummary.append("Model has been compiled with {}, {}".format(self.OptimizerComboBox.currentText(),
                                                                              self.LossComboBox.currentText()))
        self.RunButton.setDisabled(False)

    def directory_error_check(self):
        """
        Function to check that the directory that was pass is structure correctly
        """
        self.folder_path = self.DataDirectory.text()
        training_dir = os.path.join(self.folder_path, 'training').replace("\\", '/')
        testing_dir = os.path.join(self.folder_path, 'testing').replace("\\", '/')
        is_dir1 = os.path.isdir(training_dir)
        is_dir2 = os.path.isdir(testing_dir)

        # print(os.path.join(self.folder_path, 'train').replace("/", '\\'))
        # print(os.path.join(self.folder_path, 'test').replace("/", "\\"))

        if not is_dir1:
            # print("Do not find training directory under {}".format(self.folder_path))
            msg = "Do not find training directory under {}".format(self.folder_path)
            self.quick_message_box(title='error', message=msg)
            return False
        if not is_dir2:
            # print("Do not find testing directory under {}".format(self.folder_path))
            msg = "Do not find testing directory under {}".format(self.folder_path)
            self.quick_message_box(title='error', message=msg)
            return False

        return True

    def data_directories(self):
        """
        Function to check that the directory that was pass to start training on model is structure correctly
        :return:
        training_dir = path to the training directory
        testing_dir = path to the testing directory
        """

        training_dir = os.path.join(self.folder_path, 'training').replace("\\", '/')
        testing_dir = os.path.join(self.folder_path, 'testing').replace("\\", '/')
        num_folders = 0

        for _, dir_names, filenames in os.walk(training_dir):
            # ^ this idiom means "we won't be using this value"
            num_folders += len(dir_names)
        # print(num_folders)

        return training_dir, testing_dir, num_folders

    def ret_optimizer(self, i):
        switcher = {
            self.OptimizerComboBox.itemText(0): optimizers.Adam(float(self.LearningRateLine.text())),
            self.OptimizerComboBox.itemText(1): optimizers.RMSprop(float(self.LearningRateLine.text())),
            self.OptimizerComboBox.itemText(2): optimizers.SGD(float(self.LearningRateLine.text()))
        }

        return switcher.get(i, 'Invalid')

    @staticmethod
    def quick_message_box(title='', message='', btn=QtWidgets.QMessageBox.Ok, icon=QtWidgets.QMessageBox.Warning):
        """
        Function to make quick message boxes for errors or warnings.
        :param title: Title of the message box
        :param message: The message that will be in the message box
        :param btn: buttons you want on the message box,
                    ex: QtWidgets.QMessageBox.Ok, (QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        :param icon: icon to put on message box
                     QtWidgets.QMessageBox.Warning, QtWidgets.QMessageBox.Question, QtWidgets.QMessageBox.Question
        :return:
        """

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(btn)
        msg_box.setIcon(icon)
        msg_box.exec()

    def show_history(self):
        try:
            Window = History(history=self.history)
            Window.plot()
            Window.exec()
        except:
            self.quick_message_box('No History', 'There is no history of a model')
            return


    def save_model(self):
        save_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Choose Directory")
        text, ok = QtWidgets.QInputDialog.getText(None, 'Save file name', 'What do you want to name the file')

        path = os.path.join(save_path,text).replace("\\", '/')
        model_filename = path + '.h5'
        self.model.save(model_filename)

        json_fname = path + '_Label_Names.json'

        with open(json_fname, 'a') as f:
            json.dump(self.class_labels, f)
            f.write("\n")


class History(QtWidgets.QDialog):

    # constructor
    def __init__(self, parent=None, history=tf.keras.callbacks.History):
        super(History, self).__init__(parent)
        self.history = history

        # a figure instance to plot on

        self.figure, self.ax = plt.subplots(1,2, figsize=(10,4), dpi=80)
        self.figure.tight_layout()


        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvasQTAgg(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # creating a Vertical Box layout
        layout = QtWidgets.QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # setting layout to the main window
        self.setLayout(layout)

    def plot(self):
        self.ax[0].plot(self.history.history['loss'], '-*')
        self.ax[0].plot(self.history.history['val_loss'], '-ro')
        self.ax[0].set(xlabel='epoch', ylabel='loss')
        self.ax[0].set_title('loss')
        self.ax[0].legend(['loss', 'val_loss'])
        self.ax[1].plot(self.history.history['acc'], '-*')
        self.ax[1].plot(self.history.history['val_acc'], '-ro')
        self.ax[1].set(xlabel='epoch', ylabel='acc')
        self.ax[1].set_title('accuracy')
        self.ax[1].legend(['acc', 'val_acc'])
        self.canvas.draw()




class Epoch_Callback(tf.keras.callbacks.Callback):

    def __init__(self, total_epoch, progressBar=QtWidgets.QProgressBar):
        self.total_epoch = total_epoch
        self.progressBar = progressBar

    def on_epoch_end(self, epoch, logs={}):
        percent_done = int(((epoch + 1) / self.total_epoch) * 100)
        self.progressBar.setValue(percent_done)


class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
