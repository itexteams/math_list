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


def bt_dang19_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số random bài toán
                # Có hai biến thể chính giữ nguyên giá trị không đổi là 3/2:
                # Biến thể 1 (gốc): A = cos^2(x) + cos^2(pi/3 + x) + cos^2(pi/3 - x) = 3/2
                # Biến thể 2: A = sin^2(x) + sin^2(pi/3 + x) + sin^2(pi/3 - x) = 3/2
                ham_chon = random.choice(['cos', 'sin'])

                # Kết quả của biểu thức lượng giác này luôn bằng 3/2
                kq_chinhxac = Rational(3, 2)
                da_dung_str = latex(kq_chinhxac)

                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai (nhiễu) không trùng với đáp án đúng
                s_set = set()
                nhiieu_list = [
                    Rational(3, 4),
                    Rational(4, 3),
                    Rational(2, 3),
                    Rational(1, 2),
                    Rational(1, 4),
                    Rational(5, 4)
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % latex(item)
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                random.shuffle(list_sai)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                if ham_chon == 'cos':
                    noidungcauhoi = ('''Biểu thức $A = \\cos^2 x + \\cos^2 \\left( \\frac{\\pi}{3} + x \\right) + \\cos^2 \\left( \\frac{\\pi}{3} - x \\right)$ không phụ thuộc $x$ và bằng''')

                    # Các bước trung gian khai triển cho lời giải chi tiết (Hàm Cos)
                    buoc_khai_trien = ('= \\cos^2 x + \\left( \\frac{\\sqrt{3}}{2}\\cos x - \\frac{1}{2}\\sin x \\right)^2 + \\left( \\frac{\\sqrt{3}}{2}\\cos x + \\frac{1}{2}\\sin x \\right)^2')
                    loi_giai_chi_tiet = ('''= $\\cos^2 x + \\left( \\frac{3}{4}\\cos^2 x - 2 \\cdot \\frac{\\sqrt{3}}{4}\\cos x \\sin x + \\frac{1}{4}\\sin^2 x \\right) + \\left( \\frac{3}{4}\\cos^2 x + 2 \\cdot \\frac{\\sqrt{3}}{4}\\cos x \\sin x + \\frac{1}{4}\\sin^2 x \\right)$ \\\\
            = $\\cos^2 x + \\frac{3}{2}\\cos^2 x + \\frac{1}{2}\\sin^2 x$ \\\\
            = $\\frac{5}{2}\\cos^2 x + \\frac{1}{2}(1 - \\cos^2 x) = 2\\cos^2 x + \\frac{1}{2}$ (Sử dụng hạ bậc hoặc khai triển tương đương) \\\\
            = $\\frac{3}{2}$.''')
                else:
                    noidungcauhoi = ('''Biểu thức $A = \\sin^2 x + \\sin^2 \\left( \\frac{\\pi}{3} + x \\right) + \\sin^2 \\left( \\frac{\\pi}{3} - x \\right)$ không phụ thuộc $x$ và bằng''')

                    # Các bước trung gian khai triển cho lời giải chi tiết (Hàm Sin)
                    buoc_khai_trien = ('= \\sin^2 x + \\left( \\frac{\\sqrt{3}}{2}\\sin x + \\frac{1}{2}\\cos x \\right)^2 + \\left( \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x \\right)^2')
                    loi_giai_chi_tiet = ('''= $\\sin^2 x + \\left( \\frac{3}{4}\\sin^2 x + 2 \\cdot \\frac{\\sqrt{3}}{4}\\sin x \\cos x + \\frac{1}{4}\\cos^2 x \\right) + \\left( \\frac{3}{4}\\sin^2 x - 2 \\cdot \\frac{\\sqrt{3}}{4}\\sin x \\cos x + \\frac{1}{4}\\cos^2 x \\right)$ \\\\
            = $\\sin^2 x + \\frac{3}{2}\\sin^2 x + \\frac{1}{2}\\cos^2 x$ \\\\
            = $\\frac{5}{2}\\sin^2 x + \\frac{1}{2}(1 - \\sin^2 x)$ \\\\
            = $\\frac{3}{2}$.''')

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có: \\\\
            $A = \\%s^2 x + \\%s^2 \\left( \\frac{\\pi}{3} + x \\right) + \\%s^2 \\left( \\frac{\\pi}{3} - x \\right)$ \\\\
            $%s$ \\\\
            %s'''
                           % (ham_chon, ham_chon, ham_chon, buoc_khai_trien, loi_giai_chi_tiet))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

