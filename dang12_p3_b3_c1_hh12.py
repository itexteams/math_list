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


def bt_dang12_p3_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            xa = 0
            ya = randint(33, 36)
            za = randint(8, 13)

            xb = randint(28, 33)
            yb = randint(8, 13)
            zb = randint(8, 13)

            x1 = 3
            y1 = 4
            z1 = 0

            x2 = 5
            y2 = 12
            z2 = 0

            v1 = 900
            v2 = 910

            h = Rational(93, 10)  # 9.3 km dùng Rational để giữ chính xác đại số
            a = symbols('a')
            b = symbols('b')
            t = symbols('t')

            xa1 = x1 * a + xa
            ya1 = y1 * a + ya
            za1 = z1 * a + za

            xa1a = xa - xa1
            ya1a = ya - ya1
            za1a = za - za1

            a1 = Rational(v1, int(math.isqrt(x1**2 + y1**2 + z1**2)))  # 900 / 5 = 180

            xa10 = x1 * a1 * t + xa
            ya10 = y1 * a1 * t + ya
            za10 = z1 * a1 * t + za

            xb1 = x2 * b + xb
            yb1 = y2 * b + yb
            zb1 = z2 * b + zb

            xb1b = xb - xb1
            yb1b = yb - yb1
            zb1b = zb - zb1

            b1 = Rational(v2, int(math.isqrt(x2**2 + y2**2 + z2**2)))  # 910 / 13 = 70

            xb10 = x2 * b1 * t + xb
            yb10 = y2 * b1 * t + yb
            zb10 = z2 * b1 * t + zb

            x0 = xb10 - xa10
            y0 = yb10 - ya10
            z0 = zb10 - za10

            f = expand(x0**2 + y0**2 + z0**2 - h**2, t)

            # Giải phương trình bậc 2 trực tiếp qua Sympy Poly để tránh xung đột hàm solve
            poly_f = Poly(f, t)
            coeffs = poly_f.all_coeffs()
            A, B, C = coeffs[0], coeffs[1], coeffs[2]
            delta = B**2 - 4 * A * C

            # Điều kiện có 2 nghiệm thực dương phân biệt
            if delta > 0:
                t1_val = (-B - sqrt(delta)) / (2 * A)
                t2_val = (-B + sqrt(delta)) / (2 * A)
                if t1_val > 0 and t2_val > 0:
                    tmin = min(t1_val, t2_val)
                    tmax = max(t1_val, t2_val)
                    break

        h1 = tmin * 60
        number = Decimal(str(float(N(h1))))  # Số cần làm tròn
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = (
            '''Trạm kiểm soát không lưu đang theo dõi hai máy bayzz Giả sử trong không gian với hệ trục tọa độ $Oxyz$, đơn vị đo lấy theo kilômét, tại cùng một thời điểm theo dõi ban đầu: Máy bay thứ nhất ở tọa độ $A(%s;%s;%s)$, bay theo hướng vectơ $\\vec{v}_1=(%s;%s;%s)$ với tốc độ không đổi $%s$ km/h và máy bay thứ hai ở tọa độ $B(%s;%s;%s)$, bay theo hướng vectơ $\\vec{v}_2=(%s;%s;%s)$ với tốc độ không đổi $%s$ km/hzz Biết rằng khoảng cách an toàn tối thiểu giữa hai máy bay là $%s$ kmzz Nếu hai máy bay tiếp tục duy trì hướng và tốc độ bay như trên thì sau ít nhất bao nhiêu phút (kể từ thời điểm theo dõi ban đầu) hai máy bay vi phạm khoảng cách an toàn? (kết quả làm tròn đến hàng phần trăm)zz'''
            % (
                latex(xa), latex(ya), latex(za),
                latex(x1), latex(y1), latex(z1),
                latex(v1),
                latex(xb), latex(yb), latex(zb),
                latex(x2), latex(y2), latex(z2),
                latex(v2),
                latex(9.3),
            )
        )

        # Nội dung lời giải
        loigiai = (
            '''Đặt $A'(%s;%s;%s)$ là điểm di chuyển của máy bay thứ nhấtzz \\\\
            Gọi $t$ (giờ) là thời gian hai máy bay bay kể từ thời điểm ban đầu ($t \\ge 0$)zz \\\\
            Ta có khoảng cách máy bay thứ nhất so với điểm ban đầu là \\\\
            $A'A=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s t \\Leftrightarrow a=%s t \\Rightarrow A'(%s;%s;%s)$zz \\\\
            Đặt $B'(%s;%s;%s)$ là điểm di chuyển của máy bay thứ haizz \\\\
            Ta có khoảng cách máy bay thứ hai so với điểm ban đầu là \\\\
            $B'B=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s t \\Leftrightarrow b=%s t \\Rightarrow B'(%s;%s;%s)$zz \\\\
            Vì khoảng cách tối thiểu để hai máy bay an toàn là $%s$ km nên hai máy bay vi phạm khoảng cách an toàn khi $A'B' \\le %s$ hay \\\\
            $(%s)^2+(%s)^2+(%s)^2 \\le (%s)^2 \\Leftrightarrow %s \\le 0$ \\\\
            $\\Leftrightarrow %s \\le t \\le %s$ (giờ)zz \\\\
            Vậy sau ít nhất khoảng $%s$ phút thì hai máy bay vi phạm khoảng cách an toànzz'''
            % (
                latex(xa1), latex(ya1), latex(za1),
                latex(xa1a), latex(ya1a), latex(za1a), latex(v1), latex(a1),
                latex(xa10), latex(ya10), latex(za10),
                latex(xb1), latex(yb1), latex(zb1),
                latex(xb1b), latex(yb1b), latex(zb1b), latex(v2), latex(b1),
                latex(xb10), latex(yb10), latex(zb10),
                latex(9.3), latex(9.3),
                latex(x0), latex(y0), latex(z0), latex(9.3),
                latex(f),
                latex(round(float(N(tmin)), 4)), latex(round(float(N(tmax)), 4)),
                str(kq_str),
            )
        )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xử lý dấu phẩy
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n'
        + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.')
    return content

