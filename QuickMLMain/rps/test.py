import os
import sys
from functools import partial
import pickle as pkl
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.models import Model

from PyQt5 import QtCore, QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Plot(FigureCanvas):
    def __init__(self, x_label, y_label, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.set_xticks(range(1, 100, 10))


class MultiPlot(Plot):
    def __init__(self, parent=None, x_axis_name='X', y_axis_name='Y', width=5, height=4, dpi=100):
        super().__init__(x_axis_name, y_axis_name, parent, width, height, dpi)
        self.compute_initial_figure()

    def compute_initial_figure(self):
        self.axes.set_xticks(range(0, 100, 10))

    def plot_multi_data(self, x_axis_name='X', y_axis_name='Y', plot_labels=None, y_list=None):
        if y_list is not None:
            self.axes.clear()

            graph_handles = []

            markers = ['b:', 'r']
            y_index = 0

            for y in y_list:

                x = range(1, len(y) + 1)
                label = plot_labels[y_index]

                new_plot, = self.axes.plot(x, y, markers[y_index], markersize=2, label=label)
                graph_handles.append(new_plot)
                y_index += 1

                self.axes.set_xticks(x, int(len(list(x))/10))
            self.axes.legend(handles=graph_handles, loc=0, fontsize=8, shadow=True)

        self.axes.set_xlabel(x_axis_name)
        self.axes.set_ylabel(y_axis_name)

        self.draw()


class TrainPlotCallback(Callback):
    def __init__(self, signal):
        Callback.__init__(self)
        self.train_err = []
        self.val_err = []
        self.signal = signal

    def on_epoch_end(self, epoch, logs={}):
        self.train_err.append(1 - logs.get('acc'))
        self.val_err.append(1 - logs.get('val_acc'))
        self.signal.emit(epoch, [self.train_err, self.val_err])

def classification_model(data_input_path, on_epoch_end_signal):

    # ///////////////////// TEST /////////////////////
    if os.path.exists(data_input_path):
        plot_losses = TrainPlotCallback(on_epoch_end_signal)
        with open(data_input_path, 'rb') as pickle_in:
            data = pkl.load(pickle_in)
            X = data[0]
            y = data[1]

        input_size = X.shape[1]

        # MODEL CREATION
        # ///////////////////// INPUT LAYER /////////////////////
        inputs = Input(shape=(input_size,))
        # ///////////////////// INPUT LAYER /////////////////////
        # ///////////////////// HIDDEN LAYER /////////////////////
        x = Dense(10, activation='relu', kernel_initializer='normal')(inputs)   # THE FIRST LAYER
        # ///////////////////// HIDDEN LAYER /////////////////////
        # ///////////////////// OUTPUT LAYERS /////////////////////
        predictions = Dense(len(y[0]), activation='softmax')(x)  # the length of the output layer is as the length of the classes being predicted.
        # ///////////////////// OUTPUT LAYERS /////////////////////
        # MODEL CREATION

        # ///////////////////// MODEL DEFINITION /////////////////////
        model = Model(inputs=inputs, outputs=predictions)
        model.compile(optimizer='Adam',
                      loss='categorical_crossentropy',
                      metrics=['acc'])
        # ///////////////////// MODEL DEFINITION /////////////////////

        # ///////////////////// MODEL TRAINING /////////////////////
        model.fit(X, y, validation_split=0.2, batch_size=100, epochs=100, callbacks=[plot_losses])
        # ///////////////////// MODEL TRAINING /////////////////////


class Worker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    epoch_end_signal = QtCore.pyqtSignal(int, list)  # signal that has epoch # as the first parameter, and a list that contains the error values for the train and validation.

    @QtCore.pyqtSlot(str)
    def start_task(self, input_path):
        self.started.emit()
        classification_model(data_input_path=input_path,
                             on_epoch_end_signal=self.epoch_end_signal)
        self.finished.emit()


class DashBoard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_v_box = QtWidgets.QVBoxLayout(self)
        self.input_data_path_str = ''
        self.progress_bar = QtWidgets.QProgressBar()
        self.run_model_btn = QtWidgets.QPushButton('Run')
        self.browse_train_data_file_path_btn = QtWidgets.QPushButton('Browse')
        self.in_training_plot = MultiPlot(x_axis_name='Epoch Number', y_axis_name='Error')
        self.train_data_file_path_le = QtWidgets.QLineEdit()
        self.init()
        self.pack()
        self.showMaximized()

    def init(self):
        self.worker = Worker()
        thread = QtCore.QThread(self)
        thread.start()
        self.worker.moveToThread(thread)
        self.progress_bar.hide()
        self.browse_train_data_file_path_btn.clicked.connect(self.on_btn_click)
        self.run_model_btn.clicked.connect(self.on_btn_click)
        self.worker.epoch_end_signal.connect(self.update_ui_on_epoch_end)
        self.worker.started.connect(self.progress_bar.show)
        self.worker.finished.connect(self.progress_bar.hide)
        self.worker.started.connect(partial(self.run_model_btn.setEnabled, False))
        self.worker.finished.connect(partial(self.run_model_btn.setEnabled, True))

    def pack(self):
        self.main_v_box.addWidget(self.train_data_file_path_le)
        self.main_v_box.addWidget(self.browse_train_data_file_path_btn)
        self.main_v_box.addWidget(self.in_training_plot)
        self.main_v_box.addWidget(self.run_model_btn)
        self.main_v_box.addWidget(self.progress_bar)

    def on_btn_click(self):
        btn_index = self.sender()

        if btn_index == self.browse_train_data_file_path_btn:
            self.input_data_path_str, _ = QtWidgets.QFileDialog.getOpenFileName(self, '.pickle files', os.getenv('HOME'), '*.pickle')
            self.train_data_file_path_le.setText(self.input_data_path_str)
        elif btn_index == self.run_model_btn:
            QtCore.QTimer.singleShot(0, partial(self.worker.start_task, self.input_data_path_str))

    def update_ui_on_epoch_end(self, current_epoch_num, error_lists):
        if current_epoch_num < 100:
            self.progress_bar.setValue(current_epoch_num)
        else:
            self.progress_bar.setValue(100)
        self.in_training_plot.plot_multi_data(x_axis_name='Epoch', y_axis_name='Error', plot_labels=['Train Accuracy', 'Validation Accuracy'], y_list=[error_lists[0], error_lists[1]])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_menu = DashBoard()
    sys.exit(app.exec_())