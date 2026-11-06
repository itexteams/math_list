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


def bt_dang15_p1_b2_c1_ds11(self):

            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập tham số random bài toán
                # Sử dụng bộ số Pythagore phổ biến: (3, 4, 5) hoặc (5, 12, 13)
                bo_ba = random.choice([(3, 4, 5), (5, 12, 13)])
                doi = bo_ba[0]
                ke = bo_ba[1]
                huyen = bo_ba[2]

                # Chọn ngẫu nhiên khoảng của góc alpha:
                # Cung phần tư II: (\pi/2; \pi) -> sin dương, cos âm
                # Cung phần tư III: (\pi; 3\pi/2) -> sin âm, cos âm
                khoang_alpha = random.choice(['II', 'III'])

                if khoang_alpha == 'II':
                    sin_alpha = Rational(doi, huyen)
                    cos_alpha = -Rational(ke, huyen)
                    str_khoang = '\\left(\\frac{\\pi}{2}; \\pi\\right)'
                    str_cos_giai_thich = 'Do $\\alpha \\in \\left(\\frac{\\pi}{2}; \\pi\\right) \\Rightarrow \\cos \\alpha < 0$ nên $\\cos \\alpha = %s$' % latex(cos_alpha)
                else:
                    sin_alpha = -Rational(doi, huyen)
                    cos_alpha = -Rational(ke, huyen)
                    str_khoang = '\\left(\\pi; \\frac{3\\pi}{2}\\right)'
                    str_cos_giai_thich = 'Do $\\alpha \\in \\left(\\pi; \\frac{3\\pi}{2}\\right) \\Rightarrow \\cos \\alpha < 0$ nên $\\cos \\alpha = %s$' % latex(cos_alpha)

                # Chọn ngẫu nhiên góc lượng giác dịch chuyển trong biểu thức cos(alpha - phi)
                # Ta chọn dạng k*pi/4 với k lẻ giống mẫu gốc (ví dụ: 21pi/4, 19pi/4, 23pi/4)
                k_le = random.choice([17, 19, 21, 23])
                goc_phi = Rational(k_le, 4)

                # Tính toán giá trị cos(k*pi/4) và sin(k*pi/4) bằng SymPy
                cos_phi_val = cos(goc_phi * pi)
                sin_phi_val = sin(goc_phi * pi)

                # Tính giá trị biểu thức: cos(alpha - phi) = cos(alpha)*cos(phi) + sin(alpha)*sin(phi)
                kq_chinh_xac = cos_alpha * cos_phi_val + sin_alpha * sin_phi_val

                # Định dạng chuỗi đáp án đúng
                da_dung_str = latex(kq_chinh_xac).replace('.', ',')
                da = '$%s$' % da_dung_str
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai (nhiễu) không trùng đáp án đúng
                s_set = set()
                nhiieu_list = [
                    -kq_chinh_xac, # Sai dấu toàn bộ
                    cos_alpha * cos_phi_val - sin_alpha * sin_phi_val, # Sai công thức cộng thành trừ
                    -(cos_alpha * cos_phi_val - sin_alpha * sin_phi_val),
                    Rational(ke, huyen) * cos_phi_val + sin_alpha * sin_phi_val # Lấy nhầm cos alpha dương
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
                noidungcauhoi = ('''Cho $\\sin \\alpha = %s, \\alpha \\in %s$. Giá trị $\\cos \\left( \\alpha - \\frac{%s\\pi}{4} \\right)$ bằng'''
                                 % (latex(sin_alpha), str_khoang, latex(k_le)))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các bước trung gian phục vụ biểu diễn lời giải chi tiết
                sin_alpha_binh = '\\frac{%s}{%s}' % (latex(doi**2), latex(huyen**2))
                cos_alpha_binh = '\\frac{%s}{%s}' % (latex(ke**2), latex(huyen**2))
                cos_tuyet_doi = '\\frac{%s}{%s}' % (latex(ke), latex(huyen))

                # Chuỗi hiển thị bước tính tổng cuối cùng
                # Định dạng chuỗi hiển thị số âm có dấu ngoặc đơn
                def format_parentheses(val):
                    str_val = latex(val)
                    if val < 0:
                        return '\\left(%s\\right)' % str_val
                    return str_val

                loigiai = ('''Ta có: $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = %s \\Leftrightarrow \\cos \\alpha = \\pm %s$. \\\\
            %s. \\\\
            Vậy: $\\cos \\left( \\alpha - \\frac{%s\\pi}{4} \\right) = \\cos \\alpha \\cos \\frac{%s\\pi}{4} + \\sin \\alpha \\sin \\frac{%s\\pi}{4}$ \\\\
            = $%s \\cdot %s + %s \\cdot %s = %s$.'''
                           % (cos_alpha_binh, cos_tuyet_doi, str_cos_giai_thich, 
                              latex(k_le), latex(k_le), latex(k_le),
                              format_parentheses(cos_alpha), format_parentheses(cos_phi_val),
                              format_parentheses(sin_alpha), format_parentheses(sin_phi_val),
                              da_dung_str))

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

