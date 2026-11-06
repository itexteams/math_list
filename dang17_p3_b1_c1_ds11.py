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


def bt_dang17_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cot(alpha) = m/n
                n = randint(1, 4)
                m = randint(1, 5)
                cot_val = Rational(m, n)

                # Random các hệ số của biểu thức A = (a*sin + b*cos) / (c*sin - d*cos)
                # Đảm bảo mẫu số c*n - d*m > 0 để giá trị A > 0, tránh lặp vô hạn
                while True:
                    a = randint(2, 6)
                    b = randint(2, 6)
                    c = randint(2, 6)
                    d = randint(2, 6)

                    if c * n - d * m > 0:
                        break

                # Giá trị tử và mẫu trước khi rút gọn
                tu_1 = a * n + b * m
                mau_1 = c * n - d * m

                # Tính giá trị rút gọn của biểu thức A
                A_val = Rational(tu_1, mau_1)

                # Lấy tử số và mẫu số tối giản của A (đảm bảo b > 0)
                tu_so = A_val.p
                mau_so = A_val.q

                # Đáp án đúng là tổng a + b
                kq_dung = tu_so + mau_so

                # Định dạng đáp án đúng bằng LaTeX
                du = ['$%s$' % (latex(kq_dung))]
                da = random.choice(du)

                # Tạo các phương án nhiễu không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_dung + randint(-6, 6)
                    if sai != kq_dung and sai > 0:
                        s.add('$%s$' % (latex(sai)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Hiển thị cot dưới dạng phân số đẹp mắt
                cot_str = '\\frac{%s}{%s}' % (latex(m), latex(n)) if n > 1 else latex(m)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho $\\cot \\alpha = %s$. Biết giá trị của biểu thức $A = \\frac{%s\\sin \\alpha + %s\\cos \\alpha}{%s\\sin \\alpha - %s\\cos \\alpha} = \\frac{a}{b}$ (với $\\frac{a}{b}$ là phân số tối giản và $b > 0$). Tổng $a + b$ bằng bao nhiêu?'''
                                 % (cot_str, latex(a), latex(b), latex(c), latex(d)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Vì $\\cot \\alpha = %s$ nên $\\sin \\alpha \\neq 0$. \\\\
            Chia cả tử số và mẫu số của biểu thức $A$ cho $\\sin \\alpha$, ta được: \\\\
            $A = \\frac{%s + %s\\cot \\alpha}{%s - %s\\cot \\alpha}$. \\\\
            Thay $\\cot \\alpha = %s$ vào biểu thức trên, ta được: \\\\
            $A = \\frac{%s + %s \\cdot %s}{%s - %s \\cdot %s} = \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
            Vì $\\frac{%s}{%s}$ là phân số tối giản và có mẫu số dương nên ta chọn $a = %s$ và $b = %s$. \\\\
            Vậy tổng $a + b = %s + %s = %s$.'''
                           % (cot_str, latex(a), latex(b), latex(c), latex(d), cot_str,
                              latex(a), latex(b), cot_str, latex(c), latex(d), cot_str,
                              latex(tu_1), latex(mau_1), latex(tu_so), latex(mau_so),
                              latex(tu_so), latex(mau_so), latex(tu_so), latex(mau_so),
                              latex(tu_so), latex(mau_so), latex(kq_dung)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))
            # Xuất câu trắc nghiệm đúng cấu trúc LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

