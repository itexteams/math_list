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


def bt_dang60_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của hàm logistic N(t) = C / (1 + A * e^(-kt))
                C = random.choice([5000, 8000, 10000, 12000, 15000, 20000])
                A = random.randint(50, 150)
                k_int = random.randint(30, 80) 
                k = k_int / 100.0

                # Chuẩn bị chuỗi số thập phân có dấu phẩy thay cho dấu chấm
                k_str = str(k).replace('.', ',')

                # Tính toán kết quả
                exact_t = math.log(A) / k
                ans = round(exact_t)
                exact_str = str(round(exact_t, 2)).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(ans))]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng đáp án đúng)
                options = [ans - 2, ans - 1, ans + 1, ans + 2, ans + 3]
                random.shuffle(options)

                s = ['$%s$' % (latex(opt)) for opt in options]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Sau khi phát hiện một dịch bệnh, các chuyên gia y tế ước tính số người nhiễm bệnh theo thời gian $t$ (tính bằng tuần) được cho bởi hàm số $N(t)=\\frac{%s}{1+%se^{-%st}}$ với $t \\ge 0$. Hàm số $N'(t)$ biểu thị tốc độ lây lan của dịch bệnh tại thời điểm $t$. Hỏi vào khoảng tuần thứ mấy (làm tròn đến hàng đơn vị) thì tốc độ lây lan của dịch bệnh là lớn nhất?'''
                                 % (latex(C), latex(A), k_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Giải bằng cách xét hàm số, lập bảng biến thiên)
                loigiai = ('''Ta có hàm số biểu thị tốc độ lây lan của dịch bệnh tại thời điểm $t$ là $f(t) = N'(t) = \\frac{%s \\cdot %s \\cdot %s e^{-%st}}{(1 + %s e^{-%st})^2}$. \\\\
                Đạo hàm $f'(t) = \\frac{%s \\cdot %s \\cdot %s^2 e^{-%st} (%s e^{-%st} - 1)}{(1 + %s e^{-%st})^3}$. \\\\
                Xét $f'(t) = 0 \\Leftrightarrow %s e^{-%st} - 1 = 0 \\Leftrightarrow e^{-%st} = \\frac{1}{%s} \\Leftrightarrow -%st = -\\ln %s \\Leftrightarrow t = \\frac{\\ln %s}{%s} \\approx %s$. \\\\
                Ta có bảng biến thiên: \\\\
                \\begin{center}
                \\begin{tikzpicture}
                \\tkzTabInit[nocadre=false,lgt=2,espcl=3.5]{$t$ /1, $f'(t)$ /1, $f(t)$ /2.5}{$0$, $\\frac{\\ln %s}{%s}$, $+\\infty$}
                \\tkzTabLine{,+,0,-,}
                \\tkzTabVar{-/ , +/ $f\\left(\\frac{\\ln %s}{%s}\\right)$, -/ }
                \\end{tikzpicture}
                \\end{center}
                Từ bảng biến thiên, ta thấy $f(t)$ đạt giá trị lớn nhất tại $t = \\frac{\\ln %s}{%s} \\approx %s$. \\\\
                Làm tròn đến hàng đơn vị, ta được $t \\approx %s$. Vậy vào khoảng tuần thứ $%s$, tốc độ lây lan của dịch bệnh là lớn nhất.'''
                           % (
                              # f(t)
                              latex(C), latex(A), k_str, k_str, latex(A), k_str,
                              # f'(t)
                              latex(C), latex(A), k_str, k_str, latex(A), k_str, latex(A), k_str,
                              # f'(t) = 0
                              latex(A), k_str, k_str, latex(A), k_str, latex(A), latex(A), k_str, exact_str,
                              # tab init
                              latex(A), k_str,
                              # tab var
                              latex(A), k_str,
                              # kết luận
                              latex(A), k_str, exact_str,
                              # làm tròn
                              latex(ans), latex(ans)
                             ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(ans))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

