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


def bt_dang22_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên
                # b là số hạng thứ hai trong nhị thức (xy + b)^n
                b = random.randint(2, 5)
                # n là số mũ
                n = 5 # Giữ nguyên bậc 5 như đề bài mẫu để đảm bảo độ phức tạp

                x, y = symbols('x y')

                # Biểu thức gốc: (xy + b)^n
                bieu_thuc = (x*y + b)**n

                # Hàm để tạo chuỗi LaTeX cho khai triển theo thứ tự giảm dần của số mũ xy
                def lay_khai_trien(n_val, b_val, dau=1):
                    term_list = []
                    for k in range(n_val + 1):
                        # Công thức: C(n, k) * (xy)^(n-k) * (dau * b)^k
                        he_so = binomial(n_val, k) * ((dau * b_val)**k)
                        mu = n_val - k

                        if mu == 0:
                            phan_bien = ""
                        elif mu == 1:
                            phan_bien = "xy"
                        else:
                            phan_bien = "x^{%s}y^{%s}" % (mu, mu)

                        if he_so == 1 and mu > 0:
                            term = phan_bien
                        elif he_so == -1 and mu > 0:
                            term = "-" + phan_bien
                        else:
                            term = str(he_so) + phan_bien
                        term_list.append(term)

                    # Nối các hạng tử, xử lý dấu cộng trừ
                    ket_qua = term_list[0]
                    for i in range(1, len(term_list)):
                        if term_list[i].startswith("-"):
                            ket_qua += term_list[i]
                        else:
                            ket_qua += " + " + term_list[i]
                    return ket_qua

                # Đáp án đúng
                kq_dung = lay_khai_trien(n, b)

                # Tạo các phương án sai
                # Sai 1: Khai triển của (xy - b)^n (đan dấu)
                kq_sai1 = lay_khai_trien(n, b, dau=-1)

                # Sai 2: Sai hệ số đầu tiên (thêm n vào trước)
                kq_sai2 = str(n) + kq_dung

                # Sai 3: Sai hệ số các hạng tử giữa (nhân hệ số với 10)
                term_list_sai3 = []
                for k in range(n + 1):
                    he_so = binomial(n, k) * (b**k)
                    if 0 < k < n:
                        he_so = he_so * 10
                    mu = n - k
                    phan_bien = "x^{%s}y^{%s}" % (mu, mu) if mu > 1 else ("xy" if mu == 1 else "")
                    term = (str(he_so) if he_so != 1 or mu == 0 else "") + phan_bien
                    term_list_sai3.append(term)
                kq_sai3 = " + ".join(term_list_sai3)

                # Các đáp án trắc nghiệm
                da = "$%s$" % (kq_dung)

                s = ["$%s$" % (kq_sai1),
                     "$%s$" % (kq_sai2),
                     "$%s$" % (kq_sai3)]

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Khai triển của nhị thức $\\left(xy + %s\\right)^{%s}$ là'''
                                 % (latex(b), latex(n)))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng nội dung lời giải chi tiết
                buoc_khai_trien = ""
                for k in range(n + 1):
                    c_nk = "C_{%s}^{%s}" % (n, k)
                    term_xy = "\\left(xy\\right)^{%s}" % (n - k) if (n - k) > 0 else ""
                    term_b = "\\cdot %s^{%s}" % (b, k) if k > 0 else ""

                    buoc_khai_trien += c_nk + term_xy + term_b
                    if k < n:
                        buoc_khai_trien += " + "

                loigiai = ('''$\\left(xy + %s\\right)^{%s} = %s$ \\\\
                             $= %s$.'''
                           % (latex(b), latex(n), buoc_khai_trien, kq_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

