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


def bt_dang22_p4_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của x trong biểu thức (ax + b) và (cx + d)
                # Để giữ nguyên dạng của bài toán mẫu: a = 2, c = 1
                a = 2
                c = 1

                # Để tránh việc trùng lặp mẫu số hoặc tính toán quá phức tạp, chọn bộ số đẹp ngẫu nhiên cho các pha
                # Mẫu số chung thường là 4 để giống bài gốc
                list_pha = [
                    (-1, 3),  # -pi/4 và 3pi/4 (bài gốc)
                    (1, -3),  # pi/4 và -3pi/4
                    (-3, 1),  # -3pi/4 và pi/4
                    (3, -1)   # 3pi/4 và -pi/4
                ]
                p1, p2 = random.choice(list_pha)

                # Biểu diễn phân số pha dưới dạng Rational
                pha1 = Rational(p1, 4)
                pha2 = Rational(p2, 4)

                # Nghiệm họ 1: (a-c)x = pha2 - pha1 + k2pi => x = (p2 - p1)/4 * pi + k2pi
                # Với bài gốc: 2x - pi/4 = x + 3pi/4 => x = pi + k2pi
                tu_ho1 = p2 - p1
                mau_ho1 = 4
                kq_ho1 = Rational(tu_ho1, mau_ho1) # Hệ số của pi trong họ nghiệm 1

                # Nghiệm họ 2: (a+c)x = pi - pha2 - pha1 + k2pi => 3x = pi - (p1+p2)pi/4 + k2pi
                # Với bài gốc: 3x = pi - 2pi/4 = pi/2 => x = pi/6 + k2pi/3
                tu_ho2 = 4 - (p1 + p2)
                mau_ho2 = 12 # Vì chia cho (a+c) = 3 nên mẫu số nhân 3
                kq_ho2 = Rational(tu_ho2, mau_ho2) # Hệ số của pi trong họ nghiệm 2

                # Xét các giá trị k để nghiệm thuộc khoảng (0; pi)
                nghiem_list = []

                # Họ 1: x = kq_ho1*pi + k*2*pi => 0 < kq_ho1 + 2k < 1
                # Bài gốc kq_ho1 = 1 => 0 < 1 + 2k < 1 => -1/2 < k < 0 => Không có k nguyên
                k1_min = math.ceil((-kq_ho1) / 2)
                k2_max = math.floor((1 - kq_ho1) / 2)
                for k in range(k1_min, k2_max + 1):
                    nghiem_list.append(kq_ho1 + 2*k)

                # Họ 2: x = kq_ho2*pi + k*2*pi/3 => 0 < kq_ho2 + 2k/3 < 1
                # Bài gốc kq_ho2 = 1/6 => 0 < 1/6 + 2k/3 < 1 => -1/4 < k < 5/4 => k = 0, k = 1
                k2_min = math.ceil((-kq_ho2) * 3 / 2)
                k2_max = math.floor((1 - kq_ho2) * 3 / 2)
                for k in range(k2_min, k2_max + 1):
                    nghiem_list.append(kq_ho2 + Rational(2*k, 3))

                # Tính tổng các nghiệm (hệ số nhân với pi)
                tong_he_so = sum(nghiem_list)
                tong_nghiem_latex = latex(tong_he_so * pi)
                if tong_he_so == 1:
                    tong_nghiem_latex = '\\pi'
                elif tong_he_so == 0:
                    tong_nghiem_latex = '0'

                da = '$%s$' % tong_nghiem_latex

                # Tạo các phương án sai ngẫu nhiên và không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_he_so = random.choice([Rational(1, 4), Rational(1, 2), Rational(3, 4), Rational(3, 2), Rational(5, 4), Rational(7, 4), Rational(2, 1), Rational(5, 2)])
                    if sai_he_so != tong_he_so:
                        if sai_he_so == 1:
                            s.add('$\\pi$')
                        else:
                            s.add('$%s$' % latex(sai_he_so * pi))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Định dạng chuỗi phương trình bài toán lượng giác ban đầu
                pt_ve_trai = latex(a*x + pha1*pi)
                pt_ve_phai = latex(c*x + pha2*pi)

                noidungcauhoi = ('''Cho phương trình $\\sin \\left( %s \\right) = \\sin \\left( %s \\right)$. Tìm tổng các nghiệm thuộc khoảng $(0;\\pi)$ của phương trình.'''
                                 % (pt_ve_trai, pt_ve_phai))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuẩn bị chuỗi hiển thị cho lời giải chi tiết
                b1_vt = latex(a*x + pha1*pi)
                b1_vp = latex(c*x + pha2*pi)

                # Lời giải chi tiết động theo hệ số đã bốc thăm
                loigiai = ('''Ta có: $\\sin \\left( %s \\right) = \\sin \\left( %s \\right) \\Leftrightarrow \\left[ \\begin{aligned} & %s = %s + k2\\pi \\\\ & %s = \\pi - \\left( %s \\right) + k2\\pi \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x = %s + k2\\pi \\\\ & x = %s + k\\frac{2\\pi}{3} \\end{aligned} \\right. \\quad (k \\in \\mathbb{Z})$. \\\\
            + Xét họ nghiệm $x = %s + k2\\pi \\quad (k \\in \\mathbb{Z})$. \\\\
            Do $0 < x < \\pi \\Leftrightarrow 0 < %s + k2\\pi < \\pi \\Leftrightarrow %s < k < %s$. Vì $k \\in \\mathbb{Z}$ nên họ này đóng góp các nghiệm có hệ số $\\pi$ là: %s. \\\\
            + Xét họ nghiệm $x = %s + k\\frac{2\\pi}{3} \\quad (k \\in \\mathbb{Z})$. \\\\
            Do $0 < x < \\pi \\Leftrightarrow 0 < %s + k\\frac{2\\pi}{3} < \\pi \\Leftrightarrow %s < k < %s$. Vì $k \\in \\mathbb{Z}$ nên ta tìm được các giá trị nghiệm cụ thể. \\\\
            Do đó trên khoảng $(0;\\pi)$ phương trình đã cho có tổng các nghiệm thu được là: $%s$.'''
                           % (b1_vt, b1_vp, b1_vt, b1_vp, b1_vt, b1_vp, 
                              latex(kq_ho1*pi) if kq_ho1 != 1 else '\\pi', latex(kq_ho2*pi),
                              latex(kq_ho1*pi) if kq_ho1 != 1 else '\\pi',
                              latex(kq_ho1*pi) if kq_ho1 != 1 else '\\pi',
                              latex(Rational(-tu_ho1, 2*mau_ho1)), latex(Rational(4-tu_ho1, 2*mau_ho1)),
                              ', '.join(['$%s\\pi$' % latex(v) for v in nghiem_list if (v - kq_ho1) % 2 == 0]) if len([v for v in nghiem_list if (v - kq_ho1) % 2 == 0]) > 0 else "không có giá trị k thỏa mãn",
                              latex(kq_ho2*pi), latex(kq_ho2*pi),
                              latex(Rational(-3*tu_ho2, 2*mau_ho2)), latex(Rational(3*(12-tu_ho2), 2*mau_ho2)),
                              tong_nghiem_latex
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

