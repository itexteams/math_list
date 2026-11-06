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


def bt_dang67_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 1: RANDOM THÔNG SỐ ---
                # Parabol (P): y = x^2 - bx + c. Trong hình b=4, c=3.
                # Ta giữ c=3 để A luôn nằm trên Oy: A(0,3) => OA = 3
                c = 3
                b = randint(2, 6) # Hệ số b trong x^2 - bx

                # Random diện tích S sao cho |b+m| là số nguyên cho đẹp
                # S = 1/2 * OA * |b+m| = 1/2 * 3 * k => S nên là bội của 1.5
                k = randint(2, 5) # k chính là trị tuyệt đối |b+m|
                S_val = Rational(3 * k, 2)
                S_tex = latex(S_val)

                # --- BƯỚC 2: TÍNH TOÁN ĐÁP ÁN ---
                # |b + m| = k  => m + b = k hoặc m + b = -k
                m1 = k - b
                m2 = -k - b
                tong_m = m1 + m2

                # Đáp án đúng
                kq = tong_m
                da = '$%s$' % (latex(kq))

                # --- BƯỚC 3: TẠO CÁC PHƯƠNG ÁN SAI (Không trùng đáp án đúng) ---
                s = set()
                while len(s) < 3:
                    sai = kq + randint(-5, 5)
                    if sai != kq:
                        s.add('$%s$' % (latex(sai)))

                das1, das2, das3 = list(s)

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''Cho parabol $(P): y = x^2 - %sx + %s$ và đường thẳng $d: y = mx + %s$. Tổng các giá trị của $m$ để $d$ và $(P)$ tại hai điểm phân biệt $A, B$ sao cho diện tích tam giác $OAB$ bằng $%s$ là'''
                                 % (latex(b), latex(c), latex(c), S_tex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # --- BƯỚC 5: NỘI DUNG LỜI GIẢI (Chi tiết theo ảnh) ---
                loigiai = ('''Phương trình hoành độ giao điểm của $(P)$ và $d$ là $x^2 - %sx + %s = mx + %s$ \\\\
                             $\\Leftrightarrow x^2 - (%s + m)x = 0 \\Leftrightarrow \\left[ \\begin{aligned} & x = 0 \\\\ & x = %s + m \\end{aligned} \\right.$ \\\\
                             $d$ cắt $(P)$ tại hai điểm phân biệt $A, B$ khi $%s + m \\neq 0 \\Leftrightarrow m \\neq -%s$. \\\\
                             Với $x = 0$ thì $y = %s$ suy ra $A(0; %s) \\in Oy$. Với $x = %s + m$ thì $y = m^2 + %sm + %s$ suy ra $B(%s + m; m^2 + %sm + %s)$. \\\\
                             Gọi $H$ là hình chiếu của $B$ lên $OA$. Suy ra $BH = |x_B| = |%s + m|$. \\\\
                             Theo giả thiết bài toán, ta có: \\\\
                             $S_{\\Delta OAB} = %s \\Leftrightarrow \\frac{1}{2} OA \\cdot BH = %s \\Leftrightarrow \\frac{1}{2} \\cdot %s \\cdot |m + %s| = %s \\Leftrightarrow |m + %s| = %s \\Leftrightarrow \\left[ \\begin{aligned} & m = %s \\\\ & m = %s \\end{aligned} \\right.$ \\\\
                             Vậy tổng các giá trị của $m$ là $%s$.'''
                           % (latex(b), latex(c), latex(c), latex(b), latex(b), latex(b), latex(b), 
                              latex(c), latex(c), latex(b), latex(b), latex(c), latex(b), latex(b), latex(c),
                              latex(b), S_tex, S_tex, latex(c), latex(b), S_tex, latex(b), latex(k), 
                              latex(m1), latex(m2), latex(kq)
                           ))

            # --- XUẤT KẾT QUẢ ---
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

