import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang26_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Cặp (a, b, c) tương ứng với biểu thức: a + b*sqrt(c)
            du_lieu = [
                (7, 4, 3),   # 49 - 48 = 1
                (2, 1, 3),   # 4 - 3 = 1
                (3, 2, 2),   # 9 - 8 = 1
                (4, 1, 15),  # 16 - 15 = 1
                (8, 3, 7),   # 64 - 63 = 1
                (1, 1, 2)    # 1 - 2 = -1
            ]

            # Chọn ngẫu nhiên một bộ số
            a_val, b_val, c_val = random.choice(du_lieu)

            # Tạo số mũ ngẫu nhiên n và n-1 (thường lấy năm hiện tại)
            n_exp = randint(2025, 2030)
            n_minus_1 = n_exp - 1

            # Xử lý hiển thị căn thức b*sqrt(c)
            if b_val == 1:
                B_str = "\\sqrt{%s}" % (latex(c_val))
            else:
                B_str = "%s\\sqrt{%s}" % (latex(b_val), latex(c_val))

            # Tính toán giá trị logic
            B_val_math = b_val * sqrt(c_val)
            tich_coso = (b_val**2 * c_val) - (a_val**2) # Kết quả của (B-A)(B+A)

            # Xác định dấu của kết quả dựa trên số mũ n-1
            # Nếu (tich_coso)^(n-1) = 1 thì kết quả là (a + B_val_math)
            # Nếu (tich_coso)^(n-1) = -1 thì kết quả là -(a + B_val_math)
            val_pow = tich_coso**n_minus_1

            if val_pow == 1:
                da = "$%s$" % (latex(a_val + B_val_math))
                loai_dau = ""
            else:
                da = "$-(%s)$" % (latex(a_val + B_val_math))
                loai_dau = "-"

            # Tạo các đáp án nhiễu
            s = [
                "$%s$" % (latex(a_val - B_val_math)),
                "$%s$" % (latex(B_val_math - a_val)),
                "$1$",
                "$-1$",
                "$%s$" % (latex(2*a_val)),
                "$%s$" % (latex(2*B_val_math))
            ]
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Câu hỏi
            noidungcauhoi = ("Giá trị của biểu thức $P = (%s + %s)^{%s} (%s - %s)^{%s}$ bằng"
                             % (latex(a_val), B_str, latex(n_exp), B_str, latex(a_val), latex(n_minus_1)))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Ta có: \\\\
                         $P = (%s + %s) \\cdot [(%s + %s)(%s - %s)]^{%s}$ \\\\
                         $P = (%s + %s) \\cdot [(%s)^2 - %s^2]^{%s}$ \\\\
                         $P = (%s + %s) \\cdot (%s - %s)^{%s}$ \\\\
                         $P = (%s + %s) \\cdot (%s)^{%s}$ \\\\
                         $P = %s(%s + %s) =$ %s.'''
                       % (latex(a_val), B_str, B_str, latex(a_val), B_str, latex(a_val), latex(n_minus_1),
                          latex(a_val), B_str, B_str, latex(a_val), latex(n_minus_1),
                          latex(a_val), B_str, latex(b_val**2 * c_val), latex(a_val**2), latex(n_minus_1),
                          latex(a_val), B_str, latex(tich_coso), latex(n_minus_1),
                          loai_dau, latex(a_val), B_str, da))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

