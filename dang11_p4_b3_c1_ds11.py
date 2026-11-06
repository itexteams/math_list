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


def bt_dang11_p4_b3_c1_ds11(self):
            # Khai báo biến
            # Hàm tính BCNN của 2 phân số Rational
            def lcm_rational(r1, r2):
                num1, den1 = r1.p, r1.q
                num2, den2 = r2.p, r2.q
                lcm_num = math.lcm(num1, num2)
                gcd_den = math.gcd(den1, den2)
                return Rational(lcm_num, gcd_den)

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số
                A1 = random.choice([2, 3, 4])
                A2 = random.choice([2, 3, 4, 5])

                # Các cặp (a, b) trong hệ số của x là a/b
                frac1_list = [(3, 2), (5, 2), (4, 3), (3, 4)]
                frac2_list = [(2, 3), (3, 5), (2, 5), (5, 3)]

                a1, b1 = random.choice(frac1_list)
                a2, b2 = random.choice(frac2_list)

                c1, d1 = random.choice([(5, 6), (1, 6), (1, 3), (2, 3)])
                c2, d2 = random.choice([(1, 4), (3, 4), (1, 2), (1, 6)])

                # Tính chu kỳ T1, T2 dưới dạng Rational * pi
                r1 = Rational(2 * b1, a1)
                r2 = Rational(2 * b2, a2)

                T1_latex = latex(r1 * pi)
                T2_latex = latex(r2 * pi)

                # Chu kỳ tổng T = BCNN(T1, T2)
                r_t = lcm_rational(r1, r2)
                T_latex = latex(r_t * pi)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % T_latex]
                da = random.choice(du)

                # Tạo danh sách các phương án sai
                s_candidates = [
                    r1 * pi,
                    r2 * pi,
                    (r1 + r2) * pi,
                    Rational(r_t.p, r_t.q * 2) * pi if r_t.q != 1 else Rational(r_t.p * 2, 1) * pi,
                    Rational(r_t.p * 3, r_t.q) * pi
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

                # Định dạng chuỗi câu hỏi
                if a1 == 1:
                    str_a1x = "\\frac{x}{%s}" % str(b1)
                else:
                    str_a1x = "\\frac{%sx}{%s}" % (str(a1), str(b1))

                if c1 == 1:
                    str_c1pi = "\\frac{\\pi}{%s}" % str(d1)
                else:
                    str_c1pi = "\\frac{%s\\pi}{%s}" % (str(c1), str(d1))

                if a2 == 1:
                    str_a2x = "\\frac{x}{%s}" % str(b2)
                else:
                    str_a2x = "\\frac{%sx}{%s}" % (str(a2), str(b2))

                if c2 == 1:
                    str_c2pi = "\\frac{\\pi}{%s}" % str(d2)
                else:
                    str_c2pi = "\\frac{%s\\pi}{%s}" % (str(c2), str(d2))

                noidungcauhoi = ('''Tìm chu kỳ của hàm số $y = %s \\sin \\left( %s - %s \\right) + %s \\cos \\left( %s - %s \\right)$.'''
                                 % (str(A1), str_a1x, str_c1pi, str(A2), str_a2x, str_c2pi))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số $y_1 = %s \\sin \\left( %s - %s \\right)$ có chu kỳ $T_1 = \\frac{2\\pi}{\\left| \\frac{%s}{%s} \\right|} = %s$. \\\\
                         Hàm số $y_2 = %s \\cos \\left( %s - %s \\right)$ có chu kỳ $T_2 = \\frac{2\\pi}{\\left| \\frac{%s}{%s} \\right|} = %s$. \\\\
                         Chu kỳ của hàm số đã cho là $T = \\text{BCNN}(T_1, T_2) = %s$.'''
                         % (str(A1), str_a1x, str_c1pi, str(a1), str(b1), T1_latex,
                            str(A2), str_a2x, str_c2pi, str(a2), str(b2), T2_latex,
                            T_latex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

