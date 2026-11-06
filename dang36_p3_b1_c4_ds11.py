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


def bt_dang36_p3_b1_c4_ds11(self):
            # Khai báo biến
            # --- Cấu hình random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số mũ k (Bài gốc là k=3, code random 3 hoặc 4)
                k_val = random.randint(3, 4) 

                # 1. TÍNH TOÁN CÁC THAM SỐ TOÁN HỌC
                # Tính giai thừa k! (biến tu_so_goc)
                tu_so_goc = 1
                for i in range(1, k_val + 1):
                    tu_so_goc *= i

                # Hệ số tách (k-1)
                he_so_tach = k_val - 1

                # Giai thừa (k-1)! (dùng cho kết quả cuối)
                gt_mau = 1
                for i in range(1, k_val):
                    gt_mau *= i

                # Kết quả giới hạn: k/(k-1)
                kq_fraction = Rational(k_val, k_val - 1)
                h1=round(kq_fraction,9)
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kqz).replace('.', ',')

                # Hệ số M = k! / (k-1)
                M = Rational(tu_so_goc, he_so_tach)

                # 2. CHUẨN BỊ CÁC CHUỖI LATEX
                mau_C1 = "C_{%s}^{%s}" % (k_val, k_val)
                mau_C2 = "C_{%s}^{%s}" % (k_val + 1, k_val)
                mau_C3 = "C_{%s}^{%s}" % (k_val + 2, k_val)
                mau_Cn = "C_{n}^{%s}" % (k_val)

                # Chuỗi tích n: n(n-1)(n-2)...
                list_n = []
                for i in range(k_val):
                    if i == 0: list_n.append("n")
                    else: list_n.append("(n-%s)" % i)
                str_tich_n = "".join(list_n) 

                # Chuỗi tích đảo ngược (n-2)(n-1)n
                list_n_rev = list_n[:]
                list_n_rev.reverse()
                str_tich_n_rev = "".join(list_n_rev) 

                # Chuỗi số: 1.2.3, 2.3.4...
                def gen_num_str(start_num, count):
                    nums = []
                    for i in range(count):
                        nums.append(str(start_num + i))
                    return ".".join(nums)

                str_so_1 = gen_num_str(1, k_val) 
                str_so_2 = gen_num_str(2, k_val) 
                str_so_3 = gen_num_str(3, k_val) 

                # Chuỗi tách phân số
                str_mau_tach_1 = "".join(list_n_rev[:-1]) # Bỏ n cuối
                str_mau_tach_2 = "".join(list_n_rev[1:])  # Bỏ phần tử đầu

                # Chuỗi số cho phần tách
                str_so_tach_1 = gen_num_str(1, k_val - 1) 
                str_so_tach_2 = gen_num_str(2, k_val - 1) 

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (
                    'Với $n$ là số tự nhiên lớn hơn %s, đặt $S_n = \\frac{1}{%s} + \\frac{1}{%s} + \\frac{1}{%s} + ... + \\frac{1}{%s}$. Tính giới hạn của $S_n$.' 
                    % (k_val - 1, mau_C1, mau_C2, mau_C3, mau_Cn)
                )

                # --- CÁC ĐÁP ÁN ---
                da_dung = '$%s$' % latex(kq_fraction)
                da_sai1 = '$%s$' % latex(kq_fraction + 1)
                da_sai2 = '$%s$' % latex(Rational(1, k_val))
                da_sai3 = '$%s$' % latex(Rational(k_val + 1, k_val))

                list_da = [da_dung, da_sai1, da_sai2, da_sai3]
                random.shuffle(list_da)

                # --- LỜI GIẢI CHI TIẾT ---
                loigiai = (
                    '''Ta có \\\\
                    $C_{n}^{%s} = \\frac{n!}{%s!(n-%s)!} = \\frac{(n-%s)!%s}{(n-%s)! \\cdot %s} = \\frac{%s}{%s}. \\\\
                    \\Rightarrow \\frac{1}{C_{n}^{%s}} = \\frac{%s}{%s}.$\\\\
                    Vậy ta có $S_n = \\frac{%s}{%s} + \\frac{%s}{%s} + \\frac{%s}{%s} + ... + \\frac{%s}{%s}$. \\\\
                    Nhận xét: \\\\
                    $\\frac{%s}{%s} = \\frac{1}{%s} - \\frac{1}{%s}$.\\\\
                    $ \\Rightarrow S_n = %s \\left( \\frac{1}{%s} - \\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} + ... + \\frac{1}{%s} - \\frac{1}{%s} \\right) \\\\
                    = %s \\left( \\frac{1}{%s} - \\frac{1}{%s} \\right)$.\\\\
                    Vậy $\\lim_{n \\to +\\infty} S_n = \\lim_{n \\to +\\infty} %s \\left( \\frac{1}{%s} - \\frac{1}{%s} \\right) = %s \\cdot \\frac{1}{%s} = %s \\approx %s$.'''
                    % (
                        # Dòng 1: Khai triển C_n^k
                        k_val, k_val, k_val, k_val, str_tich_n_rev, k_val, tu_so_goc, str_tich_n, tu_so_goc, k_val, tu_so_goc, str_tich_n,
                        # Dòng 2: Viết lại Sn
                        tu_so_goc, str_so_1, tu_so_goc, str_so_2, tu_so_goc, str_so_3, tu_so_goc, str_tich_n,
                        # Dòng 3: Nhận xét - ĐÃ SỬA (Chỉ còn công thức tổng quát)
                        he_so_tach, str_tich_n_rev, str_mau_tach_1, str_mau_tach_2,
                        # Dòng 4: Tổng Sn
                        latex(M), str_so_tach_1, str_so_tach_2, str_so_tach_2, gen_num_str(3, k_val-1), str_mau_tach_1, str_mau_tach_2, latex(M), str_so_tach_1, str_mau_tach_2,
                        # Dòng 5: Limit
                        latex(M), latex(Rational(1, gt_mau)), str_mau_tach_2, latex(M), latex(Rational(1, gt_mau)), latex(kq_fraction),str(kq1)
                    )
                )

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

