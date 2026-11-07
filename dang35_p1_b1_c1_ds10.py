import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang35_p1_b1_c1_ds10(self):
        lisdang = ['1']
        dang = random.choice(lisdang)

        if dang == '1':
            da = '\\exists x \\in \\mathbb{Z}, x = x^2'

            s = [
                '\\exists x \\in \\mathbb{R}, x^2 - x = 0',
                '\\exists x \\in \\mathbb{R}, x = x^2',
                '\\forall x \\in \\mathbb{Z}, x^2 = x',
                '\\forall x \\in \\mathbb{R}, x = x^2',
                '\\exists x \\in \\mathbb{Q}, x^2 = x'
            ]

            if da in s:
                s.remove(da)

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            noidungcauhoi = ('''Viết mệnh đề sau bằng kí hiệu $\\forall$ hoặc $\\exists$: "Có một số nguyên bằng bình phương của chính nó" ta được''')

            da_d = ('\\True $' + str(da) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = ('''Cụm từ "Có một" tương ứng với kí hiệu tồn tại $\\exists$.\\\\
Cụm từ "số nguyên" nghĩa là biến số thuộc tập hợp số nguyên $\\mathbb{Z}$, kí hiệu là $x \\in \\mathbb{Z}$.\\\\
Cụm từ "bằng bình phương của chính nó" được biểu diễn bằng mệnh đề chứa biến $x = x^2$ (hoặc $x^2 = x$).\\\\
Vậy mệnh đề đã cho được viết lại thành: $\\exists x \\in \\mathbb{Z}, x = x^2$.''')

        content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +
                    '\\choice \n'
                    '{' + str(list_1[1]) + '}\n'
                    '{' + str(list_1[2]) + '}\n'
                    '{' + str(list_1[3]) + '}\n'
                    '{' + str(list_1[0]) + '}\n'
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
        return content