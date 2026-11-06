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


def bt_dang80_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dạng 1: Giữ nguyên cặp số thực tế đẹp chứa căn 3 giống bài gốc
                # y = \sqrt{3}sin(x) - cos(x) - c
                c = randint(1, 5)
                R_val = 2

                # Tính biên tập giá trị
                min_y = -R_val - c
                max_y = R_val - c

                # Định dạng chuỗi LaTeX cho các thành phần
                a_str = '\\sqrt{3}'
                b_str = '1'
                c_str = str(c)

                da = '[%s;%s]' % (latex(min_y), latex(max_y))

                # Các đáp án nhiễu (Bảo đảm không bị trùng đáp án đúng)
                s = [
                    '[-2;\\sqrt{3}]',
                    '[-\\sqrt{3}-%s;\\sqrt{3}-1]' % (latex(c)),
                    '[-2;0]',
                    '[%s;%s]' % (latex(min_y + 1), latex(max_y + 1)),
                    '[%s;%s]' % (latex(-c), latex(c))
                ]
                if da in s:
                    s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Tập giá trị của hàm số $y = \\sqrt{3}\\sin x - \\cos x - %s$ là''' % (latex(c)))

                # Nội dung lời giải chi tiết theo đúng các bước của đề gốc
                loigiai = ('''Xét $y = \\sqrt{3}\\sin x - \\cos x - %s = 2\\left(\\sin x \\cdot \\cos\\frac{\\pi}{6} - \\cos x \\cdot \\sin\\frac{\\pi}{6}\\right) - %s = 2\\sin\\left(x - \\frac{\\pi}{6}\\right) - %s$\\\\
                           Ta có $-1 \\le \\sin\\left(x - \\frac{\\pi}{6}\\right) \\le 1 \\Rightarrow -2 \\le 2\\sin\\left(x - \\frac{\\pi}{6}\\right) \\le 2 \\Rightarrow %s \\le 2\\sin\\left(x - \\frac{\\pi}{6}\\right) - %s \\le %s \\Rightarrow %s \\le y \\le %s$ với mọi $x \\in \\mathbb{R}$\\\\
                           Vậy tập giá trị của hàm số là $[%s;%s]$.''' 
                           % (latex(c), latex(c), latex(c), latex(-2-c), latex(c), latex(2-c), latex(min_y), latex(max_y), latex(min_y), latex(max_y)))

            elif dang=='2':
                # Dạng 2: Phát triển sang bộ số Pytago nguyên (3, 4, 5) để tạo câu hỏi phong phú
                # y = 3sin(x) - 4cos(x) - c
                a, b, R_val = 3, 4, 5
                c = randint(1, 6)

                min_y = -R_val - c
                max_y = R_val - c

                a_str = str(a)
                b_str = str(b)
                c_str = str(c)

                da = '[%s;%s]' % (latex(min_y), latex(max_y))

                s = [
                    '[%s;%s]' % (latex(-a-c), latex(b-c)),
                    '[%s;%s]' % (latex(-R_val), latex(R_val)),
                    '[-4;3]',
                    '[%s;%s]' % (latex(min_y - 2), latex(max_y + 2)),
                    '[%s;%s]' % (latex(-c), latex(c))
                ]
                if da in s:
                    s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                noidungcauhoi = ('''Tập giá trị của hàm số $y = %s\\sin x - %s\\cos x - %s$ là''' % (latex(a), latex(b), latex(c)))

                loigiai = ('''Xét $y = %s\\sin x - %s\\cos x - %s = %s\\left(\\sin x \\cdot \\frac{%s}{%s} - \\cos x \\cdot \\frac{%s}{%s}\\right) - %s$\\\\
                           Đặt $\\cos\\alpha = \\frac{%s}{%s}$ và $\\sin\\alpha = \\frac{%s}{%s}$, khi đó:\\\\
                           $y = %s\\sin(x - \\alpha) - %s$\\\\
                           Ta có $-1 \\le \\sin(x - \\alpha) \\le 1 \\Rightarrow -%s \\le %s\\sin(x - \\alpha) \\le %s \\Rightarrow %s \\le %s\\sin(x - \\alpha) - %s \\le %s \\Rightarrow %s \\le y \\le %s$ với mọi $x \\in \\mathbb{R}$\\\\
                           Vậy tập giá trị của hàm số là $[%s;%s]$.''' 
                           % (latex(a), latex(b), latex(c), latex(R_val), latex(a), latex(R_val), latex(b), latex(R_val), latex(c),
                              latex(a), latex(R_val), latex(b), latex(R_val),
                              latex(R_val), latex(c),
                              latex(R_val), latex(R_val), latex(R_val), latex(-R_val-c), latex(R_val), latex(c), latex(R_val-c), latex(min_y), latex(max_y),
                              latex(min_y), latex(max_y)))

            # Các đáp án chuẩn hóa đầu ra
            da_d = ('\\True ' + '$' + str(da) + '$')
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

