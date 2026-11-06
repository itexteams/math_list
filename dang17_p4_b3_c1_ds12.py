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


def bt_dang17_p4_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm bộ số thỏa mãn kết quả cuối cùng là số nguyên
                while True:
                    K = randint(5, 25)          # Kết quả mong muốn (số nguyên)
                    delta = randint(1, 10)      # Độ lệch để tìm nồng độ c
                    A = K + delta               # Nồng độ muối c của nước bơm vào
                    V0m = randint(1, 5)         # Thể tích ban đầu tính theo m3
                    th = randint(1, 3)          # Thời gian tính theo giờ
                    t1 = th * 60                # Thời gian tính theo phút
                    V0 = V0m * 1000             # Thể tích ban đầu tính theo lít

                    # Điều kiện để tốc độ r là số nguyên và có giá trị thực tế hợp lý
                    numerator = K * V0
                    denominator = delta * t1
                    if numerator % denominator == 0:
                        r = numerator // denominator
                        if 10 <= r <= 100:      # Giới hạn tốc độ bơm hợp lý từ 10 đến 100 lít/phút
                            break

                # Tính toán nồng độ thực tế để đồng bộ với cấu trúc mẫu
                c = A
                M = c * r * t1
                V = V0 + r * t1
                kq_sym = Rational(M, V)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq_sym))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu
                s = [
                    '$%s$' % (latex(Rational(M, V0))),
                    '$%s$' % (latex(Rational(c * r * t1, r * t1))),
                    '$%s$' % (latex(Rational(c * t1, V0 + r * t1))),
                    '$%s$' % (latex(Rational(M + 100, V))),
                    '$%s$' % (latex(Rational(M, V + 100))),
                    '$%s$' % (latex(kq_sym + Rational(1,2))),
                    '$%s$' % (latex(kq_sym - Rational(1,2))),
                    '$%s$' % (latex(kq_sym + 1)),
                    '$%s$' % (latex(kq_sym - 1))
                ]

                # Xóa trùng và xóa đáp án đúng ra khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một bể chứa $%s m^3$ nước tinh khiết. Người ta bơm vào bể đó nước muối có nồng độ không đổi với tốc độ $%s$ lít/phút. Nồng độ muối trong bể sau $t$ phút (tính bằng tỉ số của khối lượng muối có trong bể và thể tích nước trong bể, đơn vị gam/lít) là một hàm số $f(t)$, thời gian tính bằng phút. Biết rằng tiệm cận ngang của đồ thị hàm số $f(t)$ là $y=%s$. Tính nồng độ muối trong bể sau khi bơm được $%s$ giờ.'''
                                 % (latex(V0m), latex(r), latex(A), latex(th)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đổi $%s m^3 = %s$ lít; $%s$ giờ $= %s$ phút.\\\\
            Gọi nồng độ muối của nước bơm vào bể là $c$ (gam/lít).\\\\
            Sau $t$ phút ($t > 0$), thể tích nước trong bể là: $V(t) = %s + %st$ (lít).\\\\
            Khối lượng muối trong bể sau $t$ phút là: $m(t) = c \\cdot %s \\cdot t = %sc \\cdot t$ (gam).\\\\
            Nồng độ muối trong bể sau $t$ phút là: $f(t) = \\frac{m(t)}{V(t)} = \\frac{%sc \\cdot t}{%s + %st}$ (gam/lít).\\\\
            Ta có $\\lim_{t \\to +\\infty} f(t) = \\lim_{t \\to +\\infty} \\frac{%sc \\cdot t}{%st + %s} = c$.\\\\
            Suy ra đường thẳng $y = c$ là tiệm cận ngang của đồ thị hàm số $f(t)$.\\\\
            Theo giả thiết, tiệm cận ngang của đồ thị hàm số $f(t)$ là $y = %s$, do đó $c = %s$.\\\\
            Khi đó $f(t) = \\frac{%s \\cdot %s \\cdot t}{%s + %st} = \\frac{%st}{%s + %st}$.\\\\
            Nồng độ muối trong bể sau khi bơm được $%s$ giờ ($t = %s$) là:
            $$f(%s) = \\frac{%s \\cdot %s}{%s + %s \\cdot %s} = %s \\text{ (gam/lít)}.$$'''
                           % (latex(V0m), latex(V0), latex(th), latex(t1),
                              latex(V0), latex(r),
                              latex(r), latex(r),
                              latex(r), latex(V0), latex(r),
                              latex(r), latex(r), latex(V0),
                              latex(A), latex(A),
                              latex(A), latex(r), latex(V0), latex(r), latex(A*r), latex(V0), latex(r),
                              latex(th), latex(t1),
                              latex(t1), latex(A*r), latex(t1), latex(V0), latex(r), latex(t1), latex(kq_sym)))



            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

