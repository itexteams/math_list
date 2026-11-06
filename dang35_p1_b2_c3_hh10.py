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


def bt_dang35_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random tọa độ 3 đỉnh để đảm bảo lời giải luôn ra số nguyên đẹp
                # Chọn A, B, C sao cho không thẳng hàng
                while True:
                    xA, yA = random.randint(-5, 5), random.randint(-5, 5)
                    xB, yB = random.randint(-7, 7), random.randint(-7, 7)
                    xC, yC = random.randint(-7, 7), random.randint(-7, 7)
                    # Kiểm tra không thẳng hàng (diện tích tam giác != 0)
                    area = abs(xA*(yB - yC) + xB*(yC - yA) + xC*(yA - yB))
                    if area > 0 and (xB, yB) != (xA, yA) and (xC, yC) != (xA, yA):
                        break

                # Bước 2: Tìm phương trình đường cao d1 (từ B, vuông góc AC)
                # Vec-tơ AC = (xC-xA, yC-yA) là vec-tơ pháp tuyến của d1
                a1, b1 = xC - xA, yC - yA
                # Rút gọn hệ số pháp tuyến
                common1 = gcd(a1, b1)
                a1, b1 = a1 // common1, b1 // common1
                if a1 < 0 or (a1 == 0 and b1 < 0): # Chuẩn hóa hệ số dương
                    a1, b1 = -a1, -b1
                c1 = -(a1 * xB + b1 * yB)

                # Bước 3: Tìm phương trình đường cao d2 (từ C, vuông góc AB)
                # Vec-tơ AB = (xB-xA, yB-yA) là vec-tơ pháp tuyến của d2
                a2, b2 = xB - xA, yB - yA
                common2 = gcd(a2, b2)
                a2, b2 = a2 // common2, b2 // common2
                if a2 < 0 or (a2 == 0 and b2 < 0):
                    a2, b2 = -a2, -b2
                c2 = -(a2 * xC + b2 * yC)

                # Hàm hiển thị phương trình đường thẳng ax + by + c = 0
                def format_line(a, b, c):
                    res = ""
                    if a == 1: res += "x"
                    elif a == -1: res += "-x"
                    elif a != 0: res += str(a) + "x"

                    if b > 0:
                        res += ("+" if a != 0 else "") + (str(b) if b != 1 else "") + "y"
                    elif b < 0:
                        res += ("-" if b == -1 else str(b)) + "y"

                    if c > 0: res += "+" + str(c)
                    elif c < 0: res += str(c)
                    return res + "=0"

                eq_d1 = format_line(a1, b1, c1)
                eq_d2 = format_line(a2, b2, c2)

                # Phương trình AC: b1*x - a1*y + ... = 0 (vuông góc d1)
                # Phương trình AB: b2*x - a2*y + ... = 0 (vuông góc d2)
                c_ac = -(b1 * xA - a1 * yA)
                eq_ac = format_line(b1, -a1, c_ac)
                c_ab = -(b2 * xA - a2 * yA)
                eq_ab = format_line(b2, -a2, c_ab)

                # Đáp án đúng
                da = "$B(%s;%s), C(%s;%s)$" % (xB, yB, xC, yC)

                # Tạo các phương án sai (nhiễu)
                s = [
                    "$B(%s;%s), C(%s;%s)$" % (yB, xB, yC, xC),
                    "$B(%s;%s), C(%s;%s)$" % (xB+1, yB-1, xC-1, yC+1),
                    "$B(%s;%s), C(%s;%s)$" % (-xB, -yB, -xC, -yC),
                    "$B(%s;%s), C(%s;%s)$" % (xB, yB, xA, yA),
                    "$B(%s;%s), C(%s;%s)$" % (xC, yC, xB, yB)
                ]

                # Lọc bỏ nếu trùng đáp án đúng
                s = [i for i in s if i != da]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có tọa độ đỉnh $A(%s;%s)$ và hai đường thẳng chứa các đường cao kẻ từ $B, C$ có phương trình lần lượt là $d_1: %s$ và $d_2: %s$. Tọa độ đỉnh $B$ và $C$ là"
                                 %(xA, yA, eq_d1, eq_d2))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ("Đường thẳng $AC$ đi qua $A(%s;%s)$ và vuông góc với $d_1$ nên $AC$ có phương trình: $%s$. \\\\"
                           "Tương tự, $AB$ đi qua $A(%s;%s)$ và vuông góc với $d_2$ nên $AB$ có phương trình: $%s$. \\\\"
                           "Do $B = d_1 \\cap AB$ nên tọa độ điểm $B$ là nghiệm của hệ: \\\\$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$, ta được $B(%s;%s)$. \\\\"
                           "Tương tự $C = d_2 \\cap AC$ nên tọa độ điểm $C$ là nghiệm của hệ: \\\\$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$, ta được $C(%s;%s)$. \\\\"
                           "Vậy $B(%s;%s), C(%s;%s)$."
                           %(xA, yA, eq_ac, xA, yA, eq_ab, eq_d1, eq_ab, xB, yB, xB, yB, eq_d2, eq_ac, xC, yC, xC, yC, xB, yB, xC, yC))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

