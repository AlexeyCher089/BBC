import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
)

class TextAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.btn_analyze = QPushButton("Анализ:")
        self.btn_analyze.clicked.connect(self.analyze_text)
        layout.addWidget(self.btn_analyze)


        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def analyze_text(self):
        text = self.text_edit.toPlainText()

        vsego_simvol = len(text)
        probeli = text.count(" ")
        bez_probelov = len(text.replace(" ", ""))

        result = (
            f"Всего символов: {vsego_simvol}\n"
            f"Пробелов: {probeli}\n"
            f"Символов без пробелов: {bez_probelov}"
        )

        self.result_label.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextAnalyzer()
    window.show()
    sys.exit(app.exec())
