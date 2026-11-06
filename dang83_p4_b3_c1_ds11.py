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


def bt_dang83_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số góc u = (a/b)x - (c/d)pi
                frac_list = [(3, 4), (2, 3), (1, 2), (3, 2), (4, 3), (5, 4), (1, 3)]
                a, b = random.choice(frac_list)

                c, d = random.choice([(1, 5), (1, 4), (1, 3), (1, 6), (2, 5)])

                # Chu kỳ T = b*pi / (2*a)
                r_t = Rational(b, 2 * a)
                T_latex = latex(r_t * pi)

                # Đáp án đúng
                du = ['$%s$' % T_latex]
                da = random.choice(du)

                # Các phương án sai
                s_candidates = [
                    Rational(2 * b, a) * pi,
                    Rational(b, a) * pi,
                    Rational(2 * b, 3 * a) * pi,
                    Rational(b, 4 * a) * pi,
                    Rational(4 * b, a) * pi
                ]

                s = []
                for val in s_candidates:
                    cand_str = '$%s$' % latex(val)
                    if cand_str != '$%s$' % T_latex and cand_str not in s:
                        s.append(cand_str)

                while len(s) < 3:
                    fake_r = r_t + random.choice([1, 2, -1, Rational(1, 2)])
                    if fake_r > 0:
                        cand_str = '$%s$' % latex(fake_r * pi)
                        if cand_str != '$%s$' % T_latex and cand_str not in s:
                            s.append(cand_str)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuỗi biểu diễn góc u = (a/b)x - (c/d)pi
                if a == 1:
                    str_ax = "\\frac{x}{%s}" % str(b) if b != 1 else "x"
                else:
                    str_ax = "\\frac{%sx}{%s}" % (str(a), str(b)) if b != 1 else "%sx" % str(a)

                if c == 1:
                    str_cpi = "\\frac{\\pi}{%s}" % str(d) if d != 1 else "\\pi"
                else:
                    str_cpi = "\\frac{%s\\pi}{%s}" % (str(c), str(d)) if d != 1 else "%s\\pi" % str(c)

                # Biểu diễn góc 2u và 4u
                w2_r = Rational(2 * a, b)
                p2_r = Rational(2 * c, d)
                str_2ax = latex(w2_r * x)
                str_2cpi = latex(p2_r * pi)

                w4_r = Rational(4 * a, b)
                p4_r = Rational(4 * c, d)
                str_4ax = latex(w4_r * x)
                str_4cpi = latex(p4_r * pi)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Tìm chu kỳ của hàm số $y = \\sin^6 \\left( %s - %s \\right) + \\cos^6 \\left( %s - %s \\right)$.'''
                                 % (str_ax, str_cpi, str_ax, str_cpi))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước
                loigiai = ('''Biến đổi hàm số: \\\\
                         $y = \\sin^6 \\left( %s - %s \\right) + \\cos^6 \\left( %s - %s \\right)$ \\\\
                         $y = \\left[ \\sin^2 \\left( %s - %s \\right) + \\cos^2 \\left( %s - %s \\right) \\right] \\left[ \\sin^4 \\left( %s - %s \\right) - \\sin^2 \\left( %s - %s \\right) \\cos^2 \\left( %s - %s \\right) + \\cos^4 \\left( %s - %s \\right) \\right]$ \\\\
                         $y = 1 - 3 \\sin^2 \\left( %s - %s \\right) \\cos^2 \\left( %s - %s \\right)$ \\\\
                         $y = 1 - \\frac{3}{4} \\sin^2 \\left( %s - %s \\right)$ \\\\
                         $y = 1 - \\frac{3}{4} \\cdot \\frac{1 - \\cos \\left( %s - %s \\right)}{2}$ \\\\
                         $y = \\frac{5}{8} + \\frac{3}{8} \\cos \\left( %s - %s \\right)$. \\\\
                         Hàm số $y = \\frac{5}{8} + \\frac{3}{8} \\cos \\left( %s - %s \\right)$ có chu kỳ $T = \\frac{2\\pi}{\\left| %s \\right|} = %s$.'''
                         % (str_ax, str_cpi, str_ax, str_cpi,
                            str_ax, str_cpi, str_ax, str_cpi,
                            str_ax, str_cpi, str_ax, str_cpi, str_ax, str_cpi, str_ax, str_cpi,
                            str_ax, str_cpi, str_ax, str_cpi,
                            str_2ax, str_2cpi,
                            str_4ax, str_4cpi,
                            str_4ax, str_4cpi,
                            str_4ax, str_4cpi, latex(w4_r), T_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

