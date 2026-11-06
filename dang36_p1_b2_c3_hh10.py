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


def bt_dang36_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu cho Sympy
            x, y = symbols('x y')

            def format_line_equation(A, B, C):
                """Hàm bổ trợ để viết phương trình đường thẳng Ax + By + C = 0 đẹp hơn"""
                expr = A*x + B*y + C
                return latex(expr) + " = 0"

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Cách làm: Chọn 3 điểm A, B, C có tọa độ nguyên sao cho không thẳng hàng.
            # Từ đó tính phương trình BC, đường cao d1 (qua B, vuông AC), d2 (qua C, vuông AB).

            while True:
                xa, ya = randint(-5, 5), randint(-5, 5)
                xb, yb = randint(-5, 10), randint(-5, 10)
                xc, yc = randint(-5, 10), randint(-5, 10)

                # Kiểm tra không thẳng hàng (diện tích tam giác khác 0)
                area = abs(xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb))
                if area > 2 and xa != xb and xb != xc: # Đảm bảo tam giác rõ ràng và không quá đặc biệt
                    break

            # 1. Phương trình cạnh BC: (yb-yc)x + (xc-xb)y + xb*yc - xc*yb = 0
            a_bc, b_bc, c_bc = yb - yc, xc - xb, xb*yc - xc*yb
            # Rút gọn hệ số
            gcd_bc = sp.gcd(sp.gcd(a_bc, b_bc), c_bc)
            a_bc, b_bc, c_bc = a_bc//gcd_bc, b_bc//gcd_bc, c_bc//gcd_bc
            if a_bc < 0: a_bc, b_bc, c_bc = -a_bc, -b_bc, -c_bc
            pt_bc = format_line_equation(a_bc, b_bc, c_bc)

            # 2. Đường cao d1 qua B(xb, yb) và vuông góc AC. Véctơ AC = (xc-xa, yc-ya)
            # PT: (xc-xa)(x - xb) + (yc-ya)(y - yb) = 0
            a1, b1, c1 = xc - xa, yc - ya, -(xc - xa)*xb - (yc - ya)*yb
            gcd1 = sp.gcd(sp.gcd(a1, b1), c1)
            a1, b1, c1 = a1//gcd1, b1//gcd1, c1//gcd1
            if a1 < 0: a1, b1, c1 = -a1, -b1, -c1
            pt_d1 = format_line_equation(a1, b1, c1)

            # 3. Đường cao d2 qua C(xc, yc) và vuông góc AB. Véctơ AB = (xb-xa, yb-ya)
            # PT: (xb-xa)(x - xc) + (yb-ya)(y - yc) = 0
            a2, b2, c2 = xb - xa, yb - ya, -(xb - xa)*xc - (yb - ya)*yc
            gcd2 = sp.gcd(sp.gcd(a2, b2), c2)
            a2, b2, c2 = a2//gcd2, b2//gcd2, c2//gcd2
            if a2 < 0: a2, b2, c2 = -a2, -b2, -c2
            pt_d2 = format_line_equation(a2, b2, c2)

            # --- B4: Điều chỉnh phương án sai ---
            kq_dung = '(%s;%s)' % (xa, ya)
            s = set()
            while len(s) < 3:
                xi, yi = xa + randint(-3, 3), ya + randint(-3, 3)
                distractor = '(%s;%s)' % (xi, yi)
                if distractor != kq_dung:
                    s.add(distractor)

            list_sai = list(s)
            da_d = '\\True $%s$' % kq_dung
            da_s1 = '$%s$' % list_sai[0]
            da_s2 = '$%s$' % list_sai[1]
            da_s3 = '$%s$' % list_sai[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- B2: Viết lại nội dung bài toán ---
            noidungcauhoi = (
                'Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có phương trình cạnh $BC: %s$, '
                'đường cao qua đỉnh $B$ và $C$ lần lượt có phương trình $d_1: %s$; $d_2: %s$. '
                'Tọa độ đỉnh $A$ là' % (pt_bc, pt_d1, pt_d2)
            )

            # PT AC: đi qua C, vuông góc d1. Véctơ pháp tuyến d1 là (a1, b1) => Véctơ chỉ phương AC là (a1, b1)
            # => Véctơ pháp tuyến AC là (b1, -a1). PT: b1(x-xc) - a1(y-yc) = 0
            a_ac, b_ac, c_ac = b1, -a1, -b1*xc + a1*yc
            pt_ac = format_line_equation(a_ac, b_ac, c_ac)

            # PT AB: đi qua B, vuông góc d2. Véctơ pháp tuyến d2 là (a2, b2) => Véctơ pháp tuyến AB là (b2, -a2)
            a_ab, b_ab, c_ab = b2, -a2, -b2*xb + a2*yb
            pt_ab = format_line_equation(a_ab, b_ab, c_ab)

            loigiai = (
                'Do $B = d_1 \\cap BC$ nên tọa độ của $B$ là nghiệm của hệ: \\\\'
                '$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$, ta được $B(%s; %s)$. \\\\'
                'Do $C = d_2 \\cap BC$ nên tọa độ của $C$ là nghiệm của hệ: \\\\'
                '$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$, ta được $C(%s; %s)$. \\\\'
                'Cạnh $AC$ đi qua $C$ và vuông góc với $d_1$ nên $AC$ có phương trình: $%s$. \\\\'
                'Cạnh $AB$ đi qua $B$ và vuông góc với $d_2$ nên $AB$ có phương trình: $%s$. \\\\'
                'Do $A = AB \\cap AC$ nên tọa độ $A$ là nghiệm của hệ: \\\\'
                '$\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\'
                'Vậy $A(%s; %s)$.' 
                % (pt_d1, pt_bc, xb, yb, xb, yb, 
                   pt_d2, pt_bc, xc, yc, xc, yc,
                   pt_ac, pt_ab,
                   pt_ac, pt_ab, xa, ya, xa, ya)
            )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

