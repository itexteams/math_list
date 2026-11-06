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


def bt_dang50_p4_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập thông số random bài toán
                # Chọn ngẫu nhiên giá trị cho tan(alpha) là một số nguyên dương khác 1 (để mẫu số không triệt tiêu)
                tan_alpha = randint(2, 6)

                # Chọn ngẫu nhiên dấu trong biểu thức: '-' hoặc '+'
                dau = random.choice(['-', '+'])

                # Để giữ bài toán đẹp như mẫu gốc, ta chọn góc đặc biệt là pi/4 (tan(pi/4) = 1)
                # Công thức: tan(alpha - pi/4) = (tan_alpha - 1) / (1 + tan_alpha)
                # Công thức: tan(alpha + pi/4) = (tan_alpha + 1) / (1 - tan_alpha)
                tan_pi_4 = 1

                if dau == '-':
                    str_bieu_thuc = '\\alpha - \\frac{\\pi}{4}'
                    kq_phan_so = Rational(tan_alpha - 1, 1 + tan_alpha)
                    tu_so_str = '%d - 1' % tan_alpha
                    mau_so_str = '1 + %d' % tan_alpha
                else:
                    str_bieu_thuc = '\\alpha + \\frac{\\pi}{4}'
                    kq_phan_so = Rational(tan_alpha + 1, 1 - tan_alpha)
                    tu_so_str = '%d + 1' % tan_alpha
                    mau_so_str = '1 - %d' % tan_alpha

                # Định dạng chuỗi LaTeX cho đáp án đúng
                da_dung_str = latex(kq_phan_so).replace('.', ',')
                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s_set = set()
                # Các giá trị nhiễu phổ biến bằng cách nghịch đảo dấu hoặc tính sai công thức
                nhiieu_list = [
                    Rational(tan_alpha + 1, 1 + tan_alpha), # = 1
                    -kq_phan_so,
                    Rational(tan_alpha, 3),
                    Rational(1, tan_alpha),
                    Rational(tan_alpha - 1, tan_alpha + 1) if dau == '+' else Rational(tan_alpha + 1, 1 - tan_alpha),
                    Rational(tan_alpha - 2, 3)
                ]

                for item in nhiieu_list:
                    p_an = '$%s$' % latex(item).replace('.', ',')
                    if p_an != da:
                        s_set.add(p_an)

                list_sai = list(s_set)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\tan \\alpha = %s$. Tính $\\tan \\left( %s \\right)$.'''
                                 % (latex(tan_alpha), str_bieu_thuc))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo đúng mẫu gốc
                if dau == '-':
                    cong_thuc_str = '\\frac{\\tan \\alpha - \\tan \\frac{\\pi}{4}}{1 + \\tan \\alpha \\tan \\frac{\\pi}{4}}'
                else:
                    cong_thuc_str = '\\frac{\\tan \\alpha + \\tan \\frac{\\pi}{4}}{1 - \\tan \\alpha \\tan \\frac{\\pi}{4}}'

                loigiai = ('''Ta có $\\tan \\left( %s \\right) = %s = \\frac{%s}{%s} = %s$.'''
                           % (str_bieu_thuc, cong_thuc_str, tu_so_str, mau_so_str, da_dung_str))

            # Xuất câu trắc nghiệm định dạng minipage TeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content                

