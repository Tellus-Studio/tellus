from PySide2 import QtWidgets


class AssetTreeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AssetTreeWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.search_line = QtWidgets.QLineEdit(placeholderText='请输入要搜索的关键字')
        self.asset_tree = QtWidgets.QTreeWidget()
        layout.addWidget(self.search_line)
        layout.addWidget(self.asset_tree)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    atw = AssetTreeWidget()
    atw.show()
    app.exec_()
