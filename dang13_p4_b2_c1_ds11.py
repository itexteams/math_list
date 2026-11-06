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


def bt_dang13_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Chọn giá trị của sin(alpha) dạng 1/sqrt(n) để giữ nguyên cấu trúc gốc bài toán
                # n có thể chọn ngẫu nhiên từ {2, 3, 5}
                n = random.choice([2, 3, 5])
                sin_val = 1 / sqrt(n)

                # Tính cos^2(alpha) = 1 - sin^2(alpha) = 1 - 1/n = (n-1)/n
                cos2_val = Rational(n - 1, n)

                # Vì 0 < alpha < pi/2 nên cos(alpha) > 0
                cos_val = sqrt(cos2_val)

                # Biểu thức cần tính: cos(alpha + pi/3) = cos(alpha)*cos(pi/3) - sin(alpha)*sin(pi/3)
                # cos(pi/3) = 1/2, sin(pi/3) = sqrt(3)/2
                cos_pi_3 = Rational(1, 2)
                sin_pi_3 = sqrt(3) / 2

                kq_chinhxac = cos_val * cos_pi_3 - sin_val * sin_pi_3

                # Biến đổi biểu thức giống hệt từng bước của mẫu gốc để xuất lời giải và đáp án
                # Bước trung gian 1: (1/2)*cos(alpha) - (sqrt(3)/2)*sin(alpha)
                # Bước trung gian 2: Quy đồng hoặc rút gọn phân số liên tiếp
                str_cos_alpha = latex(cos_val)
                str_sin_alpha = latex(sin_val)

                # Rút gọn biểu thức cuối cùng theo định dạng phân số lớn
                mau_so_chung = 2 * sqrt(n)
                tu_so_chung = sqrt(n - 1) - sqrt(3)
                da_str = '\\frac{%s - \\sqrt{3}}{2\\sqrt{%s}}' % (latex(sqrt(n - 1)), latex(n))

                da = '$%s$' % da_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Tạo tập hợp phương án nhiễu không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    '\\sqrt{%s} - 3' % latex(2*n),
                    '\\frac{1}{\\sqrt{%s}} - \\frac{1}{2}' % latex(2*n),
                    '\\sqrt{%s} - \\frac{1}{2}' % latex(2*n),
                    '\\frac{%s + \\sqrt{3}}{2\\sqrt{%s}}' % (latex(sqrt(n - 1)), latex(n)),
                    '\\frac{\\sqrt{3} - %s}{2\\sqrt{%s}}' % (latex(sqrt(n - 1)), latex(n))
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % item
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\sin \\alpha = \\frac{1}{\\sqrt{%s}}$ với $0 < \\alpha < \\frac{\\pi}{2}$. Tính $\\cos \\left( \\alpha + \\frac{\\pi}{3} \\right)$.'''
                                 % latex(n))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết bám sát từng bước biến đổi của ảnh gốc
                loigiai = ('''Ta có: $\\sin^2 \\alpha + \\cos^2 \\alpha = 1 \\Leftrightarrow \\cos^2 \\alpha = \\frac{%s}{%s} \\Leftrightarrow \\cos \\alpha = %s$ (vì $0 < \\alpha < \\frac{\\pi}{2}$ nên $\\cos \\alpha > 0$). \\\\
            Ta có: $\\cos \\left( \\alpha + \\frac{\\pi}{3} \\right) = \\frac{1}{2}\\cos \\alpha - \\frac{\\sqrt{3}}{2}\\sin \\alpha = \\frac{1}{2} \\cdot %s - \\frac{\\sqrt{3}}{2} \\cdot \\frac{1}{\\sqrt{%s}} = %s$.'''
                           % (latex(n-1), latex(n), str_cos_alpha, str_cos_alpha, latex(n), da_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

