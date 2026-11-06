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


def bt_dang36_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước random thông số: Chọn x1 và x2 sao cho x0 = sqrt(x1*x2) là số nguyên
                # Cặp (x1, x2, x0)
                pairs = [(1, 4, 2), (1, 9, 3), (2, 8, 4), (4, 16, 8), (1, 16, 4)]
                x1, x2, x0 = random.choice(pairs)

                C_val = Rational(x1 * x2, 2)

                # Tính ln(f(x0)) = (x0^2/2 + C) / x0
                ln_f_x0 = Rational(x0**2 + 2*C_val, 2*x0)
                k = int(ln_f_x0) # Số mũ của e

                # Đáp án đúng
                kq_exact = E**k
                kq_approx = Decimal(float(math.exp(k))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                da_dung = '$f(%s) = e^{%s} \\approx %s$' % (x0, k, str(kq_approx).replace('.', ','))

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    sai_k = random.choice([k-1, k+1, k+2, 2*k, k+3])
                    if sai_k <= 0: sai_k = k + random.randint(1,3)
                    val_approx = Decimal(float(math.exp(sai_k))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    option = '$f(%s) = e^{%s} \\approx %s$' % (x0, sai_k, str(val_approx).replace('.', ','))
                    if option != da_dung and option not in s:
                        s.append(option)

                # Câu hỏi
                noidungcauhoi = (r'''Cho hàm số $f(x)$ nhận giá trị dương trên khoảng $(0;+\infty)$, có đạo hàm trên khoảng đó và thỏa mãn 
                                 $f(x)\ln f(x) = x(f(x) - f'(x)), \forall x \in (0;+\infty)$. 
                                 Biết $f(%s) = f(%s)$, tìm giá trị $f(%s)$.'''
                                 %(latex(x1), latex(x2), latex(x0)))

                # Các đáp án
                da_d = ('\\True ' + da_dung)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có: 
                           $$f(x)\ln f(x) = x(f(x) - f'(x)) \Leftrightarrow f(x)\ln f(x) + xf'(x) = xf(x)$$
                           Chia cả hai vế cho $f(x) > 0$, ta được: 
                           $$\ln f(x) + x\frac{f'(x)}{f(x)} = x \Leftrightarrow [x\ln f(x)]' = x$$
                           Suy ra: $x\ln f(x) = \int x \text{d}x = \frac{x^2}{2} + C$.
                           \\ Với $x=%s \Rightarrow %s \ln f(%s) = \frac{%s^2}{2} + C \Rightarrow \ln f(%s) = \frac{%s}{2} + \frac{C}{%s}$.
                           \\ Với $x=%s \Rightarrow %s \ln f(%s) = \frac{%s^2}{2} + C \Rightarrow \ln f(%s) = \frac{%s}{2} + \frac{C}{%s}$.
                           \\ Vì $f(%s) = f(%s)$ nên: $\frac{%s}{2} + \frac{C}{%s} = \frac{%s}{2} + \frac{C}{%s} \Leftrightarrow C = %s$.
                           \\ Khi đó: $x\ln f(x) = \frac{x^2}{2} + %s$.
                           \\ Với $x=%s \Rightarrow %s \ln f(%s) = \frac{%s^2}{2} + %s \Leftrightarrow %s \ln f(%s) = %s \Leftrightarrow \ln f(%s) = %s$.
                           \\ Vậy $f(%s) = e^{%s} \approx %s$.'''
                           %(x1, x1, x1, x1, x1, x1, x1,
                             x2, x2, x2, x2, x2, x2, x2,
                             x1, x2, x1, x1, x2, x2, latex(C_val),
                             latex(C_val), x0, x0, x0, x0, latex(C_val), x0, x0, x0**2//2 + C_val, x0, k,
                             x0, k, str(kq_approx).replace('.', ',')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

