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


def bt_dang12_p4_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random phân số a/b không tuần hoàn đơn giản
                b_list = [7, 9, 11, 13, 17, 19, 21, 23, 29]
                while True:
                    b = random.choice(b_list)
                    a = random.randint(1, b - 1)
                    val = a / b
                    v2 = round(val, 2)

                    # Tính sai số thực tế
                    delta_actual = abs(v2 - val)

                    # Tìm mức sai số trần ở chữ số thập phân thứ 3 (k * 0.001)
                    k = math.ceil(delta_actual * 1000)

                    # Đảm bảo sai số nằm trong khoảng hợp lý (không bằng 0 và không quá lớn)
                    if 0 < k <= 5:
                        break

                # Tính v3 (số thập phân 3 chữ số để chặn sai số)
                if val > v2:
                    v3 = v2 + k / 1000
                else:
                    v3 = v2 - k / 1000

                # Hàm định dạng số có dấu phẩy thay cho dấu chấm
                def fmt(num, decimals):
                    return f"{num:.{decimals}f}".replace('.', ',')

                v2_str = fmt(v2, 2)
                v3_str = fmt(v3, 3)

                # Chuỗi thập phân dài để hiện ở lời giải (lấy 12 chữ số)
                val_str_long = f"{val:.12f}"[:14] + "\\ldots"
                val_str_long = val_str_long.replace('.', ',')

                # Đáp án đúng
                ans_val = k / 1000
                da = fmt(ans_val, 3)

                # Tạo các đáp án nhiễu
                s_vals = [ans_val + 0.001, ans_val + 0.002, ans_val + 0.003, abs(ans_val - 0.001)]
                # Lọc bỏ giá trị 0 và trùng lặp
                s_vals = list(set([v for v in s_vals if v > 0]))
                s_vals = [x for x in s_vals if round(x, 3) != round(ans_val, 3)]
                s_vals = sorted(s_vals)[:3] # Lấy 3 đáp án nhiễu

                das1 = fmt(s_vals[0], 3)
                das2 = fmt(s_vals[1], 3)
                das3 = fmt(s_vals[2], 3)

                # Câu hỏi
                noidungcauhoi = (f"Cho giá trị gần đúng của $\\frac{{{a}}}{{{b}}}$ là ${v2_str}$. "
                                 f"Tìm sai số tuyệt đối của số ${v2_str}$.")

                # Các đáp án
                da_d = ('\\True $' + da + '$')
                da_s1 = '$' + das1 + '$'
                da_s2 = '$' + das2 + '$'
                da_s3 = '$' + das3 + '$'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Ta có $\\frac{{{a}}}{{{b}}} = {val_str_long}$ nên sai số tuyệt đối của ${v2_str}$ là \\\\ \n"
                           f"$\\Delta = \\left| {v2_str} - \\frac{{{a}}}{{{b}}} \\right| < |{v2_str} - {v3_str}| = {da}$.")


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

