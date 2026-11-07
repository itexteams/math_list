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
import random

def bt_dang31_p1_b1_c1_ds10(self):
        # Khai báo biến
        lisdang = ['1']
        dang = random.choice(lisdang)

        if dang == '1':
            # Khởi tạo các giá trị ngẫu nhiên cho bài toán bậc hai phủ định
            a = randint(1, 5)  # Hệ số của x
            b = randint(2, 9)  # Hệ số tự do

            # Định dạng chuỗi hiển thị biểu thức bậc hai vế phải
            if a == 1:
                ve_phai_str = "x + %s" % (latex(b))
            else:
                ve_phai_str = "%sx + %s" % (latex(a), latex(b))

            # Tạo đáp án đúng
            da = "{\\exists x \\in \\mathbb{R}: x^2 \\le %s}" % (ve_phai_str)

            # Tạo các phương án sai ngẫu nhiên khác nhau
            s = [
                "{\\forall x \\in \\mathbb{R}: x^2 \\le %s}" % (ve_phai_str),
                "{\\exists x \\in \\mathbb{R}: x^2 < %s}" % (ve_phai_str),
                "{\\exists x \\in \\mathbb{R}: x^2 > %s}" % (ve_phai_str),
                "{\\forall x \\in \\mathbb{R}: x^2 < %s}" % (ve_phai_str),
                "{\\forall x \\in \\mathbb{R}: x^2 \\ge %s}" % (ve_phai_str),
                "{\\exists x \\in \\mathbb{R}: x^2 \\ge %s}" % (ve_phai_str)
            ]

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # Câu hỏi
            noidungcauhoi = ('''Mệnh đề phủ định của mệnh đề "$\\forall x \\in \\mathbb{R}: x^2 > %s$" là'''
                                % (ve_phai_str))

            # Các đáp án
            da_d = ('\\True $' + str(da) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Mệnh đề ban đầu có dạng: "$P: \\forall x \\in \\mathbb{R}, A(x)$" với $A(x)$ là bất đẳng thức "$x^2 > %s$".\\\\
Theo lý thuyết logic mệnh đề, phủ định của mệnh đề chứa lượng từ "$\\forall$" (với mọi) là lượng từ "$\\exists$" (tồn tại), và phủ định của tỉnh chất $A(x)$ là mệnh đề $\\overline{A}(x)$.\\\\
Phủ định của dấu lớn hơn ($>$) là dấu nhỏ hơn hoặc bằng ($\\le$).\\\\
Do đó, mệnh đề phủ định của mệnh đề đã cho là: "$\\exists x \\in \\mathbb{R}: x^2 \\le %s$".'''
                        % (ve_phai_str, ve_phai_str))

        # Xuất câu trắc nghiệm
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