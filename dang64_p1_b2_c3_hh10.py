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


def bt_dang64_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random điểm M(xm, ym) 
                xm = randint(1, 5)
                ym = randint(1, 5)

                # Chọn VTPT (a, b) trước
                a_val = randint(1, 4)
                b_val = randint(1, 4)
                while math.gcd(a_val, b_val) != 1:
                    a_val = randint(1, 4)
                    b_val = randint(1, 4)

                # Tính k1, k2 sao cho dấu bằng xảy ra tại a, b: k2*xm*a^2 = k1*ym*b^2
                k1_raw = xm * (a_val**2)
                k2_raw = ym * (b_val**2)
                common = math.gcd(k1_raw, k2_raw)
                k1 = k1_raw // common
                k2 = k2_raw // common

                # Phương trình d: ax + by - c = 0
                c_val = a_val * xm + b_val * ym

                # --- XỬ LÝ HIỂN THỊ HỆ SỐ 1 ---
                # Hàm ẩn số 1: Nếu n=1 trả về rỗng, ngược lại trả về giá trị n
                def h(n):
                    return "" if n == 1 else latex(n)

                # Định dạng phương trình đúng (ẩn số 1)
                pt_dung = "$%sx + %sy - %s = 0$" % (h(a_val), h(b_val), latex(c_val))
                da_dung = pt_dung

                # Tính toán các giá trị cho lời giải
                const_part = k1 * xm + k2 * ym
                coeff_ba = k1 * ym
                coeff_ab = k2 * xm
                min_val = const_part + 2 * int(math.sqrt(coeff_ba * coeff_ab))

                # Tạo đáp án sai (cũng xử lý ẩn số 1 để đồng bộ)
                s = [
                    '$%sx + %sy - %s = 0$' % (h(b_val), h(a_val), latex(b_val * xm + a_val * ym)),
                    '$%sx + %sy + %s = 0$' % (h(a_val), h(b_val), latex(c_val)),
                    '$%sx - %sy - %s = 0$' % (h(a_val), h(b_val), latex(abs(a_val * xm - b_val * ym))),
                    '$%sx + %sy - %s = 0$' % (h(a_val + 1), h(b_val), latex((a_val + 1) * xm + b_val * ym))
                ]
                s = [i for i in s if i != da_dung]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi (Sử dụng h(k1), h(k2) để ẩn số 1 trước OA, OB)
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, phương trình đường thẳng $d$ đi qua $M(%s;%s)$ và cắt chiều dương các trục $Ox, Oy$ lần lượt tại $A$ và $B$ sao cho $%sOA + %sOB$ nhỏ nhất là'''
                                 %(latex(xm), latex(ym), h(k1), h(k2)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết - Sử dụng h(a_val), h(b_val) để loại bỏ "1x", "1y"
                loigiai = ('''Giả sử đường thẳng $d$ có vectơ pháp tuyến $\\vec{n} = (a;b)$ với $a^2 + b^2 \\neq 0$ nên có phương trình \\\\
            $d: a(x - %s) + b(y - %s) = 0$ hay $ax + by - %sa - %sb = 0$. \\\\
            Khi đó $d \\cap Ox = A\\left(\\frac{%sa + %sb}{a}; 0\\right)$ và $d \\cap Oy = B\\left(0; \\frac{%sa + %sb}{b}\\right)$. \\\\
            Điều kiện $\\frac{%sa + %sb}{a} > 0; \\frac{%sa + %sb}{b} > 0$. \\\\
            Ta có: \\\\
            $%sOA + %sOB = %s \\left| \\frac{%sa + %sb}{a} \\right| + %s \\left| \\frac{%sa + %sb}{b} \\right| = %s \\cdot \\frac{%sa + %sb}{a} + %s \\cdot \\frac{%sa + %sb}{b}$ \\\\
            $= %s + \\frac{%sb}{a} + \\frac{%sa}{b} + %s = %s + \\frac{%sb}{a} + \\frac{%sa}{b}$ \\\\
            $\\geq %s + 2\\sqrt{\\frac{%sb}{a} \\cdot \\frac{%sa}{b}} = %s$. \\\\
            Dấu "$=$" xảy ra khi và chỉ khi $\\frac{%sb}{a} = \\frac{%sa}{b} \\Leftrightarrow %sb^2 = %sa^2$. \\\\
            Ta chọn $a = %s$, suy ra $b = %s$. \\\\
            Vậy đường thẳng cần tìm có phương trình $d: %s$.'''
                % (latex(xm), latex(ym), latex(xm), latex(ym),
                   latex(xm), latex(ym), latex(xm), latex(ym),
                   latex(xm), latex(ym), latex(xm), latex(ym),
                   h(k1), h(k2), latex(k1), latex(xm), latex(ym), 
                   latex(k2), latex(xm), latex(ym),
                   latex(k1), latex(xm), latex(ym), latex(k2), latex(xm), latex(ym),
                   latex(k1*xm), latex(k1*ym), latex(k2*xm), latex(k2*ym),
                   latex(const_part), latex(coeff_ba), latex(coeff_ab),
                   latex(const_part), latex(coeff_ba), latex(coeff_ab), latex(min_val),
                   latex(coeff_ba), latex(coeff_ab), latex(coeff_ba), latex(coeff_ab),
                   latex(a_val), latex(b_val), pt_dung.replace('$', '')
                ))

            # Xuất câu trắc nghiệm
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

