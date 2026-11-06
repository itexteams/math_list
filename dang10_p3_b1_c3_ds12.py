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


def bt_dang10_p3_b1_c3_ds12(self):
            # Khai báo biến
            # --- B3: Suy nghĩ cách random & Phép toán ---
            # Danh sách k để tạo cơ số m = 1/k (0.5, 0.25, 0.2, 0.1, 0.05, 0.04)
            k_values = [2, 4, 5, 10, 20, 25]
            k = random.choice(k_values)
            m = Rational(1, k)
            m_float = float(m)
            m_display = str(m_float).replace('.', ',')

            # Xác định a và b từ lý thuyết tích phân: a = k, b = m
            a_val = k
            b_val = m_float

            # Danh sách các biểu thức random (đảm bảo kết quả gọn đẹp)
            # Các biểu thức được thiết kế để kết quả không quá 4 ký tự
            expressions = [
                {'tex': 'a \\cdot b', 'val': a_val * b_val},
                {'tex': '\\frac{a}{b}', 'val': a_val / b_val},
                {'tex': 'a + b', 'val': a_val + b_val},
                {'tex': 'a - b', 'val': a_val - b_val},
                {'tex': 'a^2 \\cdot b', 'val': (a_val**2) * b_val}
            ]

            # Chọn ngẫu nhiên 1 biểu thức
            chosen = random.choice(expressions)
            bieu_thuc_tex = chosen['tex']
            ans_val = chosen['val']

            # Chuyển kết quả sang string, giới hạn 4 ký tự (ví dụ: 10,5 hoặc 100 hoặc 1,25)
            ans_str = str(float(ans_val)).replace('.', ',')
            if ans_str.endswith(',0'): ans_str = ans_str[:-2]
            ans_str = ans_str[:4] # Cắt tối đa 4 ký tự

            # --- B2: Viết lại theo mẫu code ---

            # Tạo đáp án nhiễu
            def tạo_nhiễu(goc):
                nhiễu = set()
                while len(nhiễu) < 3:
                    sai = goc + random.choice([-1, 1, 2, 10, -0.5, 0.5])
                    sai_str = str(float(sai)).replace('.', ',')
                    if sai_str.endswith(',0'): sai_str = sai_str[:-2]
                    if sai_str != ans_str:
                        nhiễu.add(sai_str[:4])
                return list(nhiễu)

            nhiễu_list = tạo_nhiễu(ans_val)

            list_ans = [
                '\\True $%s$' % ans_str,
                '$%s$' % nhiễu_list[0],
                '$%s$' % nhiễu_list[1],
                '$%s$' % nhiễu_list[2]
            ]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Giả sử $\\int (%s)^x dx = -\\frac{1}{\\ln a} \\cdot b^x + C$. Với $a, b$ là các hằng số dương. Giá trị của biểu thức $%s$ bằng bao nhiêu?''' 
                             % (m_display, bieu_thuc_tex))

            # Nội dung lời giải
            loigiai = ('''Ta có: $\\int (%s)^x dx = \\frac{(%s)^x}{\\ln %s} = \\frac{(%s)^x}{\\ln %s^{-1}} = -\\frac{(%s)^x}{\\ln %s} + C$. \\\\
                       Đối chiếu đề bài, ta có $a = %s$ và $b = %s$. \\\\
                       Vậy $%s = %s$.''' 
                       % (m_display, m_display, m_display, m_display, a_val, m_display, a_val,
                          a_val, m_display, bieu_thuc_tex, ans_str))
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ans_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

