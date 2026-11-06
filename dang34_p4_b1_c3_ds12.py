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


def bt_dang34_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Chọn các bộ số (a, b, x0, x1) để căn bậc hai là số nguyên
                # Bộ (a, b, x0, x1, m, n) với m = sqrt(ax0+b), n = sqrt(ax1+b)
                sets = [
                    (3, 1, 1, 5, 2, 4),    # 3*1+1=4, 3*5+1=16
                    (3, 1, 1, 8, 2, 5),    # 3*1+1=4, 3*8+1=25
                    (5, 4, 1, 6, 3, 5),    # 5*1+4=9, 5*6+4=34 (không được), chọn lại:
                    (2, 7, 1, 9, 3, 5),    # 2*1+7=9, 2*9+7=25
                    (1, 3, 1, 6, 2, 3),    # 1*1+3=4, 1*6+3=9
                    (8, 1, 1, 3, 3, 5),    # 8*1+1=9, 8*3+1=25
                ]

                a, b, x0, x1, m, n = random.choice(sets)
                k = random.randint(1, 2) # f(x0) = e^k


                he_so_truoc_can = Rational(2, a)
                gia_tri_tai_x0 = he_so_truoc_can * m
                C = k - gia_tri_tai_x0

                # Tính f(x1)
                so_mu_tai_x1 = he_so_truoc_can * n + C

                # Đáp án đúng
                if so_mu_tai_x1.denominator == 1:
                    kq_chuan = "e^{%s}" % (latex(so_mu_tai_x1))
                else:
                    kq_chuan = "e^{\\frac{%s}{%s}}" % (latex(so_mu_tai_x1.numerator), latex(so_mu_tai_x1.denominator))

                val_approx = float(exp(so_mu_tai_x1))
                kq_approx = str(Decimal(str(val_approx)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Tạo các đáp án sai (đảm bảo không trùng)
                da_dung = "$%s$" % kq_chuan
                s = set()
                while len(s) < 3:
                    sai_mu = so_mu_tai_x1 + random.choice([Rational(1, 2), Rational(-1, 2), 1, -1, Rational(2, 3)])
                    if sai_mu != so_mu_tai_x1:
                        if sai_mu.denominator == 1:
                            txt = "$e^{%s}$" % (latex(sai_mu))
                        else:
                            txt = "$e^{\\frac{%s}{%s}}$" % (latex(sai_mu.numerator), latex(sai_mu.denominator))
                        s.add(txt)

                list_sai = list(s)

                # Câu hỏi
                f_x0_tex = "e" if k == 1 else "e^%s" % k
                bieu_thuc_can = latex(sqrt(a*symbols('x') + b))

                noidungcauhoi = (r"Giả sử hàm số $y=f(x)$ liên tục, nhận giá trị dương trên $(0;+\infty)$ và thỏa mãn $f(%s)=%s$, "
                                 r"$f(x)=f'(x) \cdot %s$, với mọi $x>0$. Tính $f(%s)$."
                                 % (x0, f_x0_tex, bieu_thuc_can, x1))

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d] + list_sai
                random.shuffle(list_1)

                # Lời giải
                loigiai = (r"Do hàm số $y=f(x)$ liên tục, nhận giá trị dương nên $f(x)=f'(x)\sqrt{%sx+%s}$ \\"
                           r"$\Leftrightarrow \frac{f'(x)}{f(x)} = \frac{1}{\sqrt{%sx+%s}} \Leftrightarrow \int \frac{f'(x)}{f(x)} dx = \int \frac{1}{\sqrt{%sx+%s}} dx$ \\"
                           r"$\Leftrightarrow \ln f(x) = %s\sqrt{%sx+%s} + C \quad (*)$ \\"
                           r"Ta có: $f(%s)=%s$ nên $(*)\Leftrightarrow %s = %s \cdot %s + C \Leftrightarrow C = %s \quad (**)$ \\"
                           r"Từ $(*)$ và $(**)$ suy ra $f(x) = e^{%s\sqrt{%sx+%s} %s} \Rightarrow f(%s) = %s \approx %s$."
                           % (a, b, a, b, a, b, 
                              latex(he_so_truoc_can), a, b, 
                              x0, f_x0_tex, k, latex(he_so_truoc_can), m, latex(C),
                              latex(he_so_truoc_can), a, b, ("+" + latex(C) if C > 0 else latex(C)),
                              x1, kq_chuan, kq_approx))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

