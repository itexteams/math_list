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


def bt_dang85_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số bổ sung c để dịch chuyển tập giá trị (bài gốc c = 0)
                c = randint(-3, 3)

                # Tính toán các phân số cố định từ bài gốc dưới dạng Rational
                frac_1_4 = Rational(1, 4)
                frac_5_4 = Rational(5, 4)
                frac_3_4 = Rational(3, 4)
                frac_25_16 = Rational(25, 16)
                frac_25_8 = Rational(25, 8)
                frac_9_8 = Rational(9, 8)

                # Các giá trị thay đổi theo c (Sử dụng Rational để đồng bộ tính toán phân số)
                M_val = frac_9_8 + Rational(c)
                m_val = Rational(-2) + Rational(c)
                T_val = M_val + m_val # Tổng M + m = -7/8 + 2c

                # Chuỗi hiển thị cho hằng số tự do c trong đề bài
                if c > 0:
                    c_str = ' + %s' % (latex(c))
                elif c < 0:
                    c_str = ' - %s' % (latex(abs(c)))
                else:
                    c_str = ''

                # Phần cộng hằng số ở biến đổi dòng 1 của lời giải (1 + c)
                hang_so_dong_1 = 1 + c
                if hang_so_dong_1 > 0:
                    h1_str = ' + %s' % (latex(hang_so_dong_1))
                elif hang_so_dong_1 < 0:
                    h1_str = ' - %s' % (latex(abs(hang_so_dong_1)))
                else:
                    h1_str = ''

                # Phần cộng hằng số ở hằng đẳng thức dòng 1 (9/8 + c)
                hang_so_hdt = frac_9_8 + Rational(c)
                if hang_so_hdt > 0:
                    hdt_str = ' + \\frac{%s}{%s}' % (latex(hang_so_hdt.p), latex(hang_so_hdt.q))
                elif hang_so_hdt < 0:
                    hdt_str = ' - \\frac{%s}{%s}' % (latex(abs(hang_so_hdt).p), latex(abs(hang_so_hdt).q))
                else:
                    hdt_str = ''

                # Hàm định dạng phân số viết bằng tiếng Việt
                def format_fraction_vietnamese(fr):
                    fr = Rational(fr) # Đảm bảo đầu vào luôn là đối tượng Rational của SymPy
                    if fr.q == 1:
                        return latex(fr.p)
                    # Nếu là phân số âm, đặt dấu trừ ra trước phân số
                    if fr.p < 0:
                        return '-\\frac{%s}{%s}' % (latex(abs(fr.p)), latex(fr.q))
                    return '\\frac{%s}{%s}' % (latex(fr.p), latex(fr.q))

                da = format_fraction_vietnamese(T_val)
                du = ['$%s$' % (da)]
                da_choice = random.choice(du)

                # Tạo các phương án nhiễu (đảm bảo không trùng với đáp án đúng)
                s_nhieu = [
                    format_fraction_vietnamese(-T_val),
                    format_fraction_vietnamese(T_val + Rational(2)),
                    format_fraction_vietnamese(T_val - Rational(2)),
                    format_fraction_vietnamese(M_val),
                    format_fraction_vietnamese(m_val),
                    '-\\frac{7}{8}',
                    '\\frac{7}{8}'
                ]

                s = []
                for phuong_an in s_nhieu:
                    chuoi_pa = '$%s$' % (phuong_an)
                    if chuoi_pa != '$%s$' % (da) and chuoi_pa not in s:
                        s.append(chuoi_pa)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = \\sin x + \\cos 2x%s$. Khi đó $M + m$ bằng''' 
                                 % (c_str))

                # Các đáp án
                da_d = ('\\True ' + str(da_choice))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên (Đã sửa lỗi đưa vào trong khối if)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có $y = \\sin x + \\cos 2x%s = -2\\sin^2 x + \\sin x%s = -2\\left(\\sin x - \\frac{1}{4}\\right)^2%s$.\\\\
                           Do $-1 \\le \\sin x \\le 1 \\Leftrightarrow -\\frac{5}{4} \\le \\sin x - \\frac{1}{4} \\le \\frac{3}{4} \\Leftrightarrow 0 \\le \\left(\\sin x - \\frac{1}{4}\\right)^2 \\le \\frac{25}{16} \\Leftrightarrow -\\frac{25}{8} \\le -2\\left(\\sin x - \\frac{1}{4}\\right)^2 \\le 0$\\\\
                           $\\Leftrightarrow -2 \\le -2\\left(\\sin x - \\frac{1}{4}\\right)^2%s \\le %s \\Leftrightarrow -2%s \\le y \\le %s$.\\\\
                           Vậy $M = %s, m = %s \\Rightarrow M + m = %s$.'''
                           % (c_str, h1_str, hdt_str, 
                              hdt_str, format_fraction_vietnamese(hang_so_hdt), 
                              (' + ' + latex(c)) if c > 0 else (' - ' + latex(abs(c))) if c < 0 else '',
                              format_fraction_vietnamese(M_val),
                              format_fraction_vietnamese(M_val), format_fraction_vietnamese(m_val), format_fraction_vietnamese(T_val)))

            # Xuất câu trắc nghiệm đúng định dạng khung chương trình mẫu
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

