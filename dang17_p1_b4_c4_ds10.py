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


def bt_dang17_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')
            t = symbols('t')

            # B3: Suy nghĩ tìm cách random bài toán
            # Phương trình dạng: x(x + a) = c*cbrt(x^2 + ax + d) + e
            # Đặt t = cbrt(x^2 + ax + d) => x^2 + ax = t^3 - d
            # Thay vào PT: t^3 - d = c*t + e <=> t^3 - c*t - (d + e) = 0
            # Ta chọn t0 là nghiệm nguyên của PT bậc 3 này.

            def generate_data():
                while True:
                    a = random.randint(2, 8)
                    c = random.randint(2, 5)
                    t0 = random.randint(-4, 4)
                    if t0 == 0: continue

                    # Tính tổng d + e từ nghiệm t0: t0^3 - c*t0 - (d + e) = 0
                    sum_de = t0**3 - c*t0
                    # Để d và e đẹp, ta chọn d = e = sum_de / 2 (nếu sum_de chẵn)
                    if sum_de % 2 != 0: continue
                    d = sum_de // 2
                    e = d

                    # Kiểm tra phương trình x^2 + ax + d = t0^3 có bao nhiêu nghiệm nguyên
                    # x^2 + ax + (d - t0^3) = 0
                    const_quad = d - t0**3
                    delta = a**2 - 4 * const_quad

                    if delta >= 0:
                        sqrt_delta = int(delta**0.5)
                        if sqrt_delta**2 == delta:
                            # Nghiệm x = (-a +/- sqrt_delta) / 2
                            if (-a + sqrt_delta) % 2 == 0:
                                x1 = (-a + sqrt_delta) // 2
                                x2 = (-a - sqrt_delta) // 2

                                # Kiểm tra phần còn lại của PT bậc 3: t^2 + t0*t + (t0^2 - c) = 0
                                # Để bài toán giống mẫu, ta ưu tiên phần này vô nghiệm hoặc không tạo thêm nghiệm nguyên x
                                delta_t = t0**2 - 4*(t0**2 - c)

                                # Số nghiệm nguyên tìm được
                                roots_x = set([x1, x2])
                                count_roots = len(roots_x)

                                # Biểu thức bậc 2 của t để viết lời giải: t^2 + t0*t + (t0^2 - c)
                                b_t = t0
                                c_t = t0**2 - c

                                return a, c, d, e, t0, count_roots, x1, x2, b_t, c_t, sum_de

            a, c, d, e, t0, count_roots, x1, x2, b_t, c_t, sum_de = generate_data()

            # B4: Điều chỉnh các phương án sai
            kq = count_roots
            s = [0, 1, 2, 3, 4]
            if kq in s:
                s.remove(kq)
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Số các nghiệm nguyên của phương trình $x(x + %s) = %s\\sqrt[3]{x^2 + %s x %s} %s$ là'''
                            % (latex(a), latex(c), latex(a), latex(d) if d < 0 else '+ ' + latex(d), latex(e) if e < 0 else '+ ' + latex(e)))

            # Nội dung lời giải chi tiết (B2: Viết lại y hệt cấu trúc mẫu)
            # Chuyển đổi dấu cho lời giải
            sign_d = '-' + str(abs(d)) if d < 0 else '+ ' + str(d)
            sign_e = '-' + str(abs(e)) if e < 0 else '+ ' + str(e)
            sign_bt = '+' + str(b_t) if b_t > 0 else '-' + str(abs(b_t))
            sign_ct = '+' + str(c_t) if c_t > 0 else '-' + str(abs(c_t))

            loigiai = ('''Đặt $t = \\sqrt[3]{x^2 + %sx %s} \\Leftrightarrow x(x + %s) = t^3 %s$. Phương trình đã cho trở thành \\\\
                         $t^3 %s - %st - %s = 0 \\Leftrightarrow (t %s)(t^2 %s t %s) = 0 \\Leftrightarrow t = %s$. \\\\
                         Với $t = %s$: $x^2 + %sx %s = %s \\Leftrightarrow x^2 + %sx %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$ \\\\
                         Vậy phương trình có %s nghiệm nguyên.'''
                         % (latex(a), sign_d, latex(a), latex(-d) if -d < 0 else '+ ' + latex(-d),
                            latex(-d) if -d < 0 else '+ ' + latex(-d), latex(c), latex(e), 
                            '+ ' + str(-t0) if -t0 > 0 else '- ' + str(abs(t0)),
                            sign_bt, sign_ct, latex(t0),
                            latex(t0), latex(a), sign_d, latex(t0**3),
                            latex(a), latex(d - t0**3) if d - t0**3 < 0 else '+ ' + latex(d - t0**3),
                            latex(x1), latex(x2), latex(count_roots)))

            # Các đáp án
            da_d = '\\True $' + str(kq) + '$'
            da_s1 = '$' + str(das1) + '$'
            da_s2 = '$' + str(das2) + '$'
            da_s3 = '$' + str(das3) + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

