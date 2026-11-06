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


def bt_dang14_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Biểu thức gốc ứng với M = 1, N = 1. Ta random các hệ số nguyên dương dương để tạo bài toán mới.
                M = randint(1, 4)
                N = randint(1, 4)

                # Kết quả rút gọn đúng là M + N
                kq_dung = M + N

                # Định dạng các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq_dung))]
                da = random.choice(du)

                # Tạo phương án nhiễu không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_dung + randint(-4, 4)
                    if sai != kq_dung and sai != 0:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Thiết lập chuỗi hệ số hiển thị trực quan (nếu hệ số bằng 1 thì ẩn đi)
                M_str = '' if M == 1 else latex(M)
                N_str = '' if N == 1 else latex(N)

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$, khi đó giá trị của biểu thức $$P = %s\\frac{\\sin^3 \\frac{\\widehat{B}}{2}}{\\cos\\left(\\frac{\\widehat{A} + \\widehat{C}}{2}\\right)} + %s\\frac{\\cos^3 \\frac{\\widehat{B}}{2}}{\\sin\\left(\\frac{\\widehat{A} + \\widehat{C}}{2}\\right)} - %s\\frac{\\cos(\\widehat{A} + \\widehat{C})}{\\sin \\widehat{B}} \\cdot \\tan \\widehat{B}$$ bằng bao nhiêu?'''
                                 % (M_str, M_str, N_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Trong tam giác $ABC$, ta có $\\widehat{A} + \\widehat{B} + \\widehat{C} = \\pi$. \\\\
                           Suy ra: $\\frac{\\widehat{A} + \\widehat{C}}{2} = \\frac{\\pi}{2} - \\frac{\\widehat{B}}{2}$ và $\\widehat{A} + \\widehat{C} = \\pi - \\widehat{B}$. \\\\
                           Sử dụng các công thức góc liên kết, ta có: \\\\
                           + $\\cos\\left(\\frac{\\widehat{A} + \\widehat{C}}{2}\\right) = \\cos\\left(\\frac{\\pi}{2} - \\frac{\\widehat{B}}{2}\\right) = \\sin \\frac{\\widehat{B}}{2}$. \\\\
                           + $\\sin\\left(\\frac{\\widehat{A} + \\widehat{C}}{2}\\right) = \\sin\\left(\\frac{\\pi}{2} - \\frac{\\widehat{B}}{2}\\right) = \\cos \\frac{\\widehat{B}}{2}$. \\\\
                           + $\\cos(\\widehat{A} + \\widehat{C}) = \\cos(\\pi - \\widehat{B}) = -\\cos \\widehat{B}$. \\\\
                           Thay vào biểu thức $P$, ta được: \\\\
                           $P = %s\\frac{\\sin^3 \\frac{\\widehat{B}}{2}}{\\sin \\frac{\\widehat{B}}{2}} + %s\\frac{\\cos^3 \\frac{\\widehat{B}}{2}}{\\cos \\frac{\\widehat{B}}{2}} - %s\\frac{-\\cos \\widehat{B}}{\\sin \\widehat{B}} \\cdot \\tan \\widehat{B}$ \\\\
                           $P = %s\\sin^2 \\frac{\\widehat{B}}{2} + %s\\cos^2 \\frac{\\widehat{B}}{2} + %s\\cot \\widehat{B} \\cdot \\tan \\widehat{B}$ \\\\
                           $P = %s\\left(\\sin^2 \\frac{\\widehat{B}}{2} + \\cos^2 \\frac{\\widehat{B}}{2}\\right) + %s \\cdot 1$ \\\\
                           $P = %s \\cdot 1 + %s = %s$.'''
                           % (M_str, M_str, N_str,
                              M_str, M_str, N_str,
                              M_str, N_str,
                              latex(M), latex(N), latex(kq_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

