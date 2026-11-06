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


def bt_dang44_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các đỉnh A, B, C sao cho tọa độ nguyên và đẹp
                xa = random.randint(-5, 5)
                ya = random.randint(-5, 5)

                xb = random.randint(-5, 5)
                if (xa + xb) % 2 != 0: xb += 1
                yb = random.randint(-5, 5)
                if (ya + yb) % 2 != 0: yb += 1

                while True:
                    xc = random.randint(-5, 5)
                    yc = random.randint(-5, 5)
                    if (xc - xa) * (yb - ya) != (yc - ya) * (xb - xa) and (xc, yc) != (xb, yb):
                        break

                # Bước 2: Lập phương trình d1 (đường cao qua B)
                n1_a = xc - xa
                n1_b = yc - ya
                u_gcd = gcd(n1_a, n1_b)
                n1_a //= u_gcd
                n1_b //= u_gcd
                n1_c = -(n1_a * xb + n1_b * yb)

                # Bước 3: Lập phương trình d2 (trung tuyến qua C)
                xm = (xa + xb) // 2
                ym = (ya + yb) // 2
                n2_a = yc - ym
                n2_b = -(xc - xm)
                u_gcd2 = gcd(n2_a, n2_b)
                n2_a //= u_gcd2
                n2_b //= u_gcd2
                n2_c = -(n2_a * xc + n2_b * yc)

                if n1_a * n2_b == n1_b * n2_a:
                    xa, ya = 2, 1
                    xb, yb = -2, -3
                    xc, yc = 4, -5
                    n1_a, n1_b, n1_c = 1, -3, -7
                    n2_a, n2_b, n2_c = 1, 1, 1
                    xm, ym = 0, -1

                def format_line(a, b, c):
                    res = ""
                    if a == 1: res += "x"
                    elif a == -1: res += "-x"
                    elif a != 0: res += str(a) + "x"

                    if b > 0:
                        res += "+" + (str(b) if b != 1 else "") + "y"
                    elif b < 0:
                        res += "-" + (str(abs(b)) if b != 1 else "") + "y"

                    if c > 0: res += "+" + str(c)
                    elif c < 0: res += "-" + str(abs(c))
                    return res + "=0"

                str_d1 = format_line(n1_a, n1_b, n1_c)
                str_d2 = format_line(n2_a, n2_b, n2_c)

                # Các đáp án với \left( và \right)
                da_dung = "$B\\left(%s;%s\\right)$ và $C\\left(%s;%s\\right)$" % (xb, yb, xc, yc)
                da_sai1 = "$B\\left(%s;%s\\right)$ và $C\\left(%s;%s\\right)$" % (xc, yc, xb, yb)
                da_sai2 = "$B\\left(%s;%s\\right)$ và $C\\left(%s;%s\\right)$" % (xb + 1, yb, xc - 1, yc)
                da_sai3 = "$B\\left(%s;%s\\right)$ và $C\\left(%s;%s\\right)$" % (xb, yb - 2, xc, yc + 2)

                list_1 = ["\\True " + da_dung, da_sai1, da_sai2, da_sai3]
                random.shuffle(list_1)

                # Nội dung câu hỏi
                noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $A\\left(%s;%s\\right)$, đường cao qua đỉnh $B$ và đường trung tuyến qua đỉnh $C$ lần lượt có phương trình $d_1:%s, d_2:%s$. Tìm tọa độ các đỉnh $B$ và $C$."
                                 % (xa, ya, str_d1, str_d2))

                # Lời giải chi tiết
                tu_x = ""
                if n1_b != 0: tu_x += f"{-n1_b}b"
                if n1_c != 0: tu_x += f"{'-' if n1_c > 0 else '+'}{abs(n1_c)}"

                loigiai = ("Điểm $B \\in d_1$ nên tọa độ của $B$ có dạng $\\left(\\frac{%s}{%s}; b\\right)$. \\\\"
                           "Gọi $M$ là trung điểm $AB$, suy ra $M\\left(\\frac{\\frac{%s}{%s} + %s}{2}; \\frac{b + %s}{2}\\right)$. \\\\"
                           "Mặt khác, $M \\in d_2$, thay tọa độ $M$ vào phương trình $d_2$ ta tìm được $b = %s$. \\\\"
                           "Suy ra $B\\left(%s; %s\\right)$. \\\\"
                           "Đường thẳng $AC$ đi qua $A$ và vuông góc với $d_1$, nên có phương trình: $%s\\left(x - %s\\right) + %s\\left(y - %s\\right) = 0 \\Leftrightarrow %s$. \\\\"
                           "Ta có $C = AC \\cap d_2$, nên tọa độ điểm $C$ là nghiệm của hệ $\\begin{cases} %s \\\\ %s \\end{cases}$, ta được $C\\left(%s; %s\\right)$. \\\\"
                           "Vậy $B\\left(%s; %s\\right)$ và $C\\left(%s; %s\\right)$."
                           % (tu_x, n1_a, tu_x, n1_a, xa, ya, yb, xb, yb, n1_a, xa, n1_b, ya, format_line(n1_a, n1_b, -(n1_a*xa + n1_b*ya)), format_line(n1_a, n1_b, -(n1_a*xa + n1_b*ya)), str_d2, xc, yc, xb, yb, xc, yc))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content 

