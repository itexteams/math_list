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


def bt_dang8_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các tham số sao cho điểm P(a, b) có tọa độ nguyên
                # Đường thẳng Delta: x - y + c = 0 => y = x + c
                # Giả sử P(a, a + c)
                a_real = randint(-5, 5)
                c = randint(-5, 5)
                b_real = a_real + c

                # Để tam giác MNP vuông tại P, ta chọn vector PM và PN sao cho PM.PN = 0
                # Gọi PM = (h, k), PN = (-m*k, m*h) với m là hệ số tỉ lệ
                h = randint(-4, 4)
                k = randint(-4, 4)
                if h == 0 and k == 0: h = 1 # Tránh vector không
                m = random.choice([-2, -1, 1, 2])

                # Tọa độ M = P + PM, N = P + PN
                xm, ym = a_real + h, b_real + k
                xn, yn = a_real - m*k, b_real + m*h

                # Tính T = 2a + 3b
                kq_num = 2 * a_real + 3 * b_real
                da = '$%s$' % (latex(kq_num))

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = kq_num + randint(-10, 10)
                    if sai != kq_num:
                        s.add('$%s$' % (latex(sai)))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                # Delta: x - y + c = 0 <=> x - y + (c) = 0
                sign_c = "+" if c >= 0 else ""
                equation_delta = "x - y %s %s = 0" % (sign_c, c)

                noidungcauhoi = ('''Trong mặt phẳng $Oxy$, cho đường thẳng $\\Delta : %s$ và hai điểm $M(%s;%s)$, $N(%s;%s)$. Giả sử $P(a,b)$ với $(a, b \\in \\mathbb{Z})$ thuộc đường thẳng $\\Delta$ sao cho tam giác $MNP$ vuông tại $P$. Giá trị $T = 2a + 3b$ bằng bao nhiêu?'''
                                 % (equation_delta, xm, ym, xn, yn))

                # Xây dựng lời giải chi tiết
                # P thuộc Delta => P(a, a + c)
                # PM = (xm - a, ym - (a+c)) = (xm - a, (ym-c) - a)
                # PN = (xn - a, yn - (a+c)) = (xn - a, (yn-c) - a)

                y_minus_c_m = ym - c
                y_minus_c_n = yn - c

                # Phương trình: (xm-a)(xn-a) + (ym-c-a)(yn-c-a) = 0
                # Khai triển: a^2 - (xm+xn)a + xm*xn + a^2 - (ym-c + yn-c)a + (ym-c)(yn-c) = 0
                # <=> 2a^2 - (xm+xn + ym-c + yn-c)a + (xm*xn + (ym-c)*(yn-c)) = 0

                coeff_A = 2
                coeff_B = -(xm + xn + y_minus_c_m + y_minus_c_n)
                coeff_C = xm * xn + y_minus_c_m * y_minus_c_n

                # Giải phương trình 2a^2 + Ba + C = 0
                a_sym = symbols('a')
                roots = solve(coeff_A * a_sym**2 + coeff_B * a_sym + coeff_C, a_sym)

                # Chuẩn bị chuỗi cho lời giải
                pm_vec = "(%s - a; %s - a)" % (xm, y_minus_c_m)
                pn_vec = "(%s - a; %s - a)" % (xn, y_minus_c_n)

                sign_B = "+" if coeff_B >= 0 else ""
                sign_C = "+" if coeff_C >= 0 else ""

                # Tìm nghiệm nguyên
                nghiem_day_du = ""
                if len(roots) == 1:
                    nghiem_day_du = "a = %s" % (latex(roots[0]))
                else:
                    nghiem_day_du = " \\left[ \\begin{aligned} & a = %s \\\\ & a = %s \\end{aligned} \\right." % (latex(roots[0]), latex(roots[1]))

                loigiai = ('''Vì $P \\in \\Delta$ nên $P(a; a %s %s)$. Ta có\\\\
                             $\\vec{PM} = %s; \\vec{PN} = %s$.\\\\
                             Do tam giác $MNP$ vuông tại $P$ nên $\\vec{PM} \\cdot \\vec{PN} = 0$\\\\
                             $\\Leftrightarrow (%s - a)(%s - a) + (%s - a)(%s - a) = 0$\\\\
                             $\\Leftrightarrow 2a^2 %s %s a %s %s = 0 \\Leftrightarrow %s$\\\\
                             Vì $a \\in \\mathbb{Z}$ nên $a = %s \\Rightarrow b = %s$.\\\\
                             Vậy $T = 2a + 3b = 2(%s) + 3(%s) = %s$.'''
                           % (sign_c, abs(c), pm_vec, pn_vec,
                              xm, xn, y_minus_c_m, y_minus_c_n,
                              sign_B, coeff_B, sign_C, coeff_C, nghiem_day_du,
                              a_real, b_real, a_real, b_real, kq_num))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

