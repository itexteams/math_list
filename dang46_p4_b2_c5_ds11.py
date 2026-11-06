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


def bt_dang46_p4_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':


                k = random.randint(1, 5) # Giá trị của P
                c1 = 4 * k               # Hệ số của log_a(b)
                c2 = k - 1               # Hệ số của log_b(c)

                # Đáp án đúng
                kq = k

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    val = random.choice([k+1, k+2, k-1, k+3, 7, 9, 5, 10])
                    if val != kq and val > 0 and val not in s:
                        s.append(val)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq))
                das1 = '$%s$' % (latex(s[0]))
                das2 = '$%s$' % (latex(s[1]))
                das3 = '$%s$' % (latex(s[2]))

                # Xử lý hiển thị vế phải (RHS)
                # Nếu k=1 thì (k-1) = 0, vế phải chỉ có 4log_a(b)
                if c2 == 0:
                    rhs = '%s \\log_a b' % (latex(c1))
                else:
                    rhs = '%s \\log_a b + %s \\log_b c' % (latex(c1), latex(c2))

                # Câu hỏi
                noidungcauhoi = ('''Cho các số thực $a,b,c$ thuộc khoảng $(1;+\\infty)$ và $\\log_{\\sqrt{a}}^2 b + \\log_b c \\cdot \\log_b \\left( \\frac{c^2}{b} \\right) + 9\\log_a c = %s$. Tính $P = \\log_a b + \\log_b c^2$.'''
                                 % (rhs))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đặt $\\log_a b = x, \\log_b c = y \\Rightarrow \\log_a c = xy$. Điều kiện: $x, y > 0$. \\\\
                             Biến đổi giả thiết ta có: $4x^2 + y(2y-1) + 9xy = %s x + %s y$ \\\\
                             $\\Leftrightarrow 4x^2 + (9y - %s)x + 2y^2 - %s y = 0$. \\\\
                             Tính $P = x + 2y$. Rút $x = P - 2y$ thay vào phương trình trên, ta có: \\\\
                             $4(P - 2y)^2 + (9y - %s)(P - 2y) + 2y^2 - %s y = 0$ \\\\
                             $\\Leftrightarrow 4P^2 - 16Py + 16y^2 + 9Py - 18y^2 - %s P + %s y + 2y^2 - %s y = 0$ \\\\
                             $\\Leftrightarrow 4P^2 - 7Py - %s P + %s y = 0$ \\\\
                             $\\Leftrightarrow (P - %s)(4P - 7y) = 0$ \\\\
                             $\\Leftrightarrow \\left[ \\begin{aligned} & P = %s \\\\ & 4P - 7y = 0 \\end{aligned} \\right.$ \\\\
                             Xét TH: $4P - 7y = 0 \\Leftrightarrow 4(x+2y) - 7y = 0 \\Leftrightarrow 4x + y = 0$, loại vì $x, y > 0$. \\\\
                             Vậy $P = %s$.'''
                           % (latex(c1), latex(c2), latex(c1), latex(k), 
                              latex(c1), latex(k), latex(c1), latex(2*c1), latex(k),
                              latex(c1), latex(2*c1), latex(k), latex(k), latex(k)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

