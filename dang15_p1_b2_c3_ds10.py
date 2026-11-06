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


def bt_dang15_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Lấy ngẫu nhiên số lượng vịt N từ 10 đến 20
                N = random.randint(10, 20) 

                # Sinh ngẫu nhiên trọng lượng (từ 1.0 kg đến 3.5 kg)
                raw_weights = [round(random.uniform(1.0, 3.5), 1) for _ in range(N)]

                # Sắp xếp trọng lượng theo thứ tự tăng dần
                sorted_weights = sorted(raw_weights)

                # Hàm hỗ trợ định dạng số thập phân theo chuẩn Việt Nam (dấu phẩy)
                def format_vn(num):
                    num = round(float(num), 2) # Xử lý sai số
                    if num.is_integer():
                        return str(int(num))
                    return str(num).replace('.', ',')

                # Sửa lỗi LaTeX: Đóng mở cặp dấu $ hợp lý khi có ngắt dòng (\\)
                if N > 10:
                    row1 = sorted_weights[:N//2]
                    row2 = sorted_weights[N//2:]
                    str_row1 = " \\quad ".join([format_vn(w) for w in row1])
                    str_row2 = " \\quad ".join([format_vn(w) for w in row2])
                    data_str = f"${str_row1}$ \\\\\n${str_row2}$"
                else:
                    data_str = "$" + " \\quad ".join([format_vn(w) for w in sorted_weights]) + "$"

                # Tìm trung vị dựa trên tính chẵn/lẻ của N
                if N % 2 != 0:
                    pos = (N + 1) // 2
                    Me = sorted_weights[pos - 1]
                    Me_str = format_vn(Me)

                    loigiai_calc = f"Dãy số trên đã được sắp xếp theo thứ tự tăng dần và gồm số lẻ số liệu ($N={N}$). Do đó số trung vị là giá trị thứ {pos} bằng ${Me_str}$."
                else:
                    pos1 = N // 2
                    pos2 = N // 2 + 1
                    val1 = sorted_weights[pos1 - 1]
                    val2 = sorted_weights[pos2 - 1]
                    Me = (val1 + val2) / 2
                    Me_str = format_vn(Me)

                    val1_str = format_vn(val1)
                    val2_str = format_vn(val2)

                    if val1 == val2:
                         loigiai_calc = f"Dãy số trên đã được sắp xếp theo thứ tự tăng dần và gồm số chẵn số liệu ($N={N}$). Do đó số trung vị là trung bình cộng của hai giá trị thứ {pos1} và {pos2} đều bằng ${val1_str}$ nên $M_e = {Me_str}$."
                    else:
                         loigiai_calc = f"Dãy số trên đã được sắp xếp theo thứ tự tăng dần và gồm số chẵn số liệu ($N={N}$). Do đó số trung vị là trung bình cộng của hai giá trị thứ {pos1} và {pos2}: $M_e = \\frac{{{val1_str} + {val2_str}}}{{2}} = {Me_str}$."

                # Đáp án đúng
                da = f"${Me_str}$"

                # Sinh các đáp án nhiễu
                distractors = set()
                while len(distractors) < 3:
                    delta = random.choice([-0.3, -0.2, -0.15, -0.1, -0.05, 0.05, 0.1, 0.15, 0.2, 0.3])
                    fake_Me = round(Me + delta, 2)

                    if fake_Me > 0:
                        fake_ans = f"${format_vn(fake_Me)}$"
                        if fake_ans != da:
                            distractors.add(fake_ans)

                distractors = list(distractors)
                das1 = distractors[0]
                das2 = distractors[1]
                das3 = distractors[2]

                # Câu hỏi
                # Lưu ý: Bỏ cặp $ bọc quanh {data_str} vì đã được xử lý ở trên
                noidungcauhoi = (f"Trọng lượng (tính bằng kg) của một đàn vịt gồm {N} con là\n"
                                 f"\\begin{{center}}\n"
                                 f"{data_str}\n"
                                 f"\\end{{center}}\n"
                                 f"Trung vị của mẫu số liệu là")

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = loigiai_calc

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

