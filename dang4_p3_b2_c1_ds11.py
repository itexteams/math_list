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


def bt_dang4_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tử số mẫu số sao cho mẫu số của alpha và beta bằng nhau (để dễ rút gọn mẫu chung như đề gốc)
                # sin(alpha) = m/n, cos(beta) = -p/n với pi/2 < alpha, beta < pi
                while True:
                    n = randint(3, 6) # Mẫu số
                    m = randint(1, n-1) # Tử số sin(alpha)
                    p = randint(1, n-1) # Tử số trị tuyệt đối cos(beta)

                    # Đảm bảo các căn thức không bị biến thành số nguyên để giữ nguyên dạng thức của bài toán gốc
                    if not math.isqrt(n**2 - m**2)**2 == (n**2 - m**2) and not math.isqrt(n**2 - p**2)**2 == (n**2 - p**2):
                        if math.gcd(m, n) == 1 and math.gcd(p, n) == 1:
                            break



                tich_so_hoc = m * p
                can_thuc = (n**2 - m**2) * (n**2 - p**2)
                mau_so = n**2


                # Phân tích căn thức lớn can_thuc thành k^2 * d
                d_trong_can = can_thuc
                k_ngoai_can = 1
                for i in range(2, int(math.sqrt(can_thuc)) + 1):
                    while d_trong_can % (i**2) == 0:
                        k_ngoai_can *= i
                        d_trong_can //= i**2

                # Tử số lúc này có dạng: tich_so_hoc + k_ngoai_can * sqrt(d_trong_can)
                # Ta đặt nhân tử chung lớn nhất của tich_so_hoc và k_ngoai_can ra ngoài, gọi là `a_tam`
                a_tam = math.gcd(tich_so_hoc, k_ngoai_can)

                c_trong_ngoac = tich_so_hoc // a_tam
                he_so_can_trong_ngoac = k_ngoai_can // a_tam

                # Biểu diễn tử số: a_tam * (c_trong_ngoac + he_so_can_trong_ngoac * sqrt(d_trong_can))
                # Bây giờ rút gọn phân số giữa a_tam và mau_so (n^2)
                phan_so_rut_gon = Rational(a_tam, mau_so)
                a = phan_so_rut_gon.p
                b = phan_so_rut_gon.q

                # Kết quả cuối cùng là tổng a + b
                kq_dung = a + b

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(kq_dung))]
                da = random.choice(du)

                # Tạo các phương án nhiễu không trùng đáp án đúng
                s = []
                for sai in [a * b, b - a, a + b + 2, a + b - 2, a + b + 4, a + b - 4]:
                    val_sai = '$%s$'%(latex(sai))
                    if val_sai != da and val_sai not in s:
                        s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Xử lý chuỗi hiển thị biểu thức trong dấu ngoặc tử số cho câu hỏi và lời giải
                if he_so_can_trong_ngoac == 1:
                    chuoi_tu_so_rut_gon = '%s + \\sqrt{%s}' % (latex(c_trong_ngoac), latex(d_trong_can))
                    chuoi_tu_so_chua_rut_gon = '%s + \\sqrt{%s}' % (latex(tich_so_hoc), latex(can_thuc))
                else:
                    chuoi_tu_so_rut_gon = '%s + %s\\sqrt{%s}' % (latex(c_trong_ngoac), latex(he_so_can_trong_ngoac), latex(d_trong_can))
                    chuoi_tu_so_chua_rut_gon = '%s + %s\\sqrt{%s}' % (latex(tich_so_hoc), latex(k_ngoai_can), latex(d_trong_can))

                # Câu hỏi
                if a == 1:
                    bieu_thuc_sin = '-\\frac{%s}{%s}' % (chuoi_tu_so_rut_gon, latex(b))
                else:
                    bieu_thuc_sin = '-\\frac{%s\\left(%s\\right)}{%s}' % (latex(a), chuoi_tu_so_rut_gon, latex(b))

                noidungcauhoi = ('''Cho các góc $\\alpha, \\beta$ thỏa mãn $\\frac{\\pi}{2} < \\alpha, \\beta < \\pi, \\sin \\alpha = \\frac{%s}{%s}, \\cos \\beta = -\\frac{%s}{%s}$. Biết $\\sin(\\alpha + \\beta) = %s$ với $\\frac{a}{b}$ là phân số tối giản và $b>0$. Tổng $a+b$ bằng bao nhiêu?'''
                                 %(latex(m), latex(n), latex(p), latex(n), bieu_thuc_sin))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các giá trị trung gian hiển thị trong lời giải
                cos_alpha_tu = n**2 - m**2
                sin_beta_tu = n**2 - p**2

                # Lời giải chi tiết theo các bước của ảnh mẫu
                loigiai = ('''Do $\\frac{\\pi}{2} < \\alpha, \\beta < \\pi \\Rightarrow \\begin{cases} \\cos \\alpha < 0 \\\\ \\sin \\beta > 0 \\end{cases}$. \\\\
                           Ta có $\\cos \\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\frac{%s}{%s}} = -\\frac{\\sqrt{%s}}{%s}$; $\\sin \\beta = \\sqrt{1 - \\cos^2 \\beta} = \\sqrt{1 - \\frac{%s}{%s}} = \\frac{\\sqrt{%s}}{%s}$. \\\\
                           Suy ra $\\sin(\\alpha + \\beta) = \\sin \\alpha \\cdot \\cos \\beta + \\cos \\alpha \\cdot \\sin \\beta = \\frac{%s}{%s} \\cdot \\left(-\\frac{%s}{%s}\\right) + \\left(-\\frac{\\sqrt{%s}}{%s}\\right) \\cdot \\frac{\\sqrt{%s}}{%s} = -\\frac{%s}{%s}$. \\\\
                           Suy ra $\\sin(\\alpha + \\beta) = -\\frac{%s}{%s} = %s$. \\\\
                           Vậy $a+b = %s + %s = %s$.'''
                           %(latex(m**2), latex(n**2), latex(cos_alpha_tu), latex(n),
                             latex(p**2), latex(n**2), latex(sin_beta_tu), latex(n),
                             latex(m), latex(n), latex(p), latex(n), latex(cos_alpha_tu), latex(n), latex(sin_beta_tu), latex(n),
                             chuoi_tu_so_chua_rut_gon, latex(mau_so),
                             chuoi_tu_so_chua_rut_gon, latex(mau_so), bieu_thuc_sin,
                             latex(a), latex(b), latex(kq_dung)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

