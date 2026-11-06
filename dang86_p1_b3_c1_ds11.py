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


def bt_dang86_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo ngẫu nhiên các hệ số đảm bảo mẫu số vô nghiệm (a2^2 + b2^2 < c2^2)
                # y = (1*sin(x) + b1*cos(x)) / (1*sin(x) + b2*cos(x) + c2)
                # Bài gốc: b1 = -2, b2 = 1, c2 = 3
                b1 = randint(-3, -1)
                b2 = randint(1, 2)
                c2 = randint(3, 4)

                # Biến đổi phương trình bậc nhất theo sin và cos:
                # (y - 1)sin x + (b2*y - b1)cos x = -c2*y
                # Điều kiện có nghiệm: (y - 1)^2 + (b2*y - b1)^2 >= (-c2*y)^2
                # <=> (1 + b2^2 - c2^2)y^2 - 2(1 + b1*b2)y + (1 + b1^2) <= 0
                A_coeff = 1 + b2**2 - c2**2
                B_coeff = -2 * (1 + b1 * b2)
                C_coeff = 1 + b1**2

                # Giải tìm nghiệm của phương trình biên bằng SymPy để lấy cận chính xác dưới dạng phân số/căn thức
                y_sym = symbols('y')
                pt_bien = A_coeff * y_sym**2 + B_coeff * y_sym + C_coeff
                nghiem_bien = solve(pt_bien, y_sym)

                # Sắp xếp nghiệm để xác định chính xác cận dưới và cận trên
                nghiem_bien = sorted(nghiem_bien, key=lambda val: float(val))
                can_duoi = nghiem_bien[0]
                can_tren = nghiem_bien[1]

                can_duoi_latex = latex(can_duoi)
                can_tren_latex = latex(can_tren)

                # Đếm số giá trị nguyên thuộc đoạn [can_duoi, can_tren] bằng số thực (float)
                min_float = float(can_duoi)
                max_float = float(can_tren)

                cac_gia_tri_nguyen = []
                for v in range(math.ceil(min_float), math.floor(max_float) + 1):
                    cac_gia_tri_nguyen.append(v)

                kq_val = len(cac_gia_tri_nguyen)

                # Định dạng chuỗi hàm số cho đề bài
                tu_str = '\\sin x %s \\cos x' % ('- %s' % abs(b1) if b1 < 0 else '+ %s' % b1)
                mau_str = '\\sin x + %s\\cos x + %s' % (latex(b2) if b2 != 1 else '', latex(c2))

                # Định dạng các hệ số biến đổi trong lời giải
                b2y_b1_str = '%sy %s' % (latex(b2) if b2 != 1 else '', '+ %s' % abs(b1) if b1 < 0 else '- %s' % b1)
                b2y_b1_sq_str = '\\left(%sy %s\\right)^2' % (latex(b2) if b2 != 1 else '', '+ %s' % abs(b1) if b1 < 0 else '- %s' % b1)

                # Chuỗi tập hợp giá trị nguyên
                taphop_str = '{' + ';'.join(str(v) for v in cac_gia_tri_nguyen) + '}'

                da = '%s' % (latex(kq_val))
                du = ['$%s$' % (da)]
                da_choice = random.choice(du)

                # Tạo các phương án nhiễu (đảm bảo không trùng với đáp án đúng)
                s_nhieu = ['0', '1', '2', '3', '4', '5', '6']
                if da in s_nhieu:
                    s_nhieu.remove(da)
                random.shuffle(s_nhieu)
                das1 = '$%s$' % (s_nhieu[0])
                das2 = '$%s$' % (s_nhieu[1])
                das3 = '$%s$' % (s_nhieu[2])

                # Câu hỏi
                noidungcauhoi = ('''Hàm số $y = \\frac{%s}{%s}$ có bao nhiêu giá trị nguyên?''' % (tu_str, mau_str))

                # Các đáp án
                da_d = ('\\True ' + str(da_choice))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết trình bày rõ ràng từng bước như nội dung gốc
                loigiai = ('''Ta có $y = \\frac{%s}{%s} \\Leftrightarrow (y - 1)\\sin x + \\left(%s\\right)\\cos x = -%sy$\\\\
                           Phương trình có nghiệm $\\Leftrightarrow (y - 1)^2 + %s \\ge (-%sy)^2 \\Leftrightarrow %sy^2 %sy %s \\le 0 \\Leftrightarrow %s \\le y \\le %s$\\\\
                           $\\xrightarrow{y \\in \\mathbb{Z}} y \\in %s$.\\\\
                           Vậy hàm số đã cho có $%s$ giá trị nguyên.'''
                           % (tu_str, mau_str, b2y_b1_str, latex(c2),
                              b2y_b1_sq_str, latex(c2),
                              latex(A_coeff), '+ %s' % latex(B_coeff) if B_coeff > 0 else '- %s' % latex(abs(B_coeff)), '+ %s' % latex(C_coeff) if C_coeff > 0 else '- %s' % latex(abs(C_coeff)),
                              can_duoi_latex, can_tren_latex,
                              taphop_str, latex(kq_val)))

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

