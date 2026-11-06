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


def bt_dang45_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của cấp số cộng
                u1 = randint(2, 9)
                d = randint(2, 6)
                n = random.choice([20, 30, 40, 50, 60])

                # Tính tổng Sn
                Sn = (n * (2 * u1 + (n - 1) * d)) // 2

                # Tính các hệ số a, b của số hạng tổng quát u_n = a + bn
                a_true = u1 - d
                b_true = d

                # Hàm hỗ trợ định dạng chuỗi u_n
                def format_un(a, b):
                    if a == 0:
                        return '%sn' % (b)
                    elif a > 0:
                        return '%s + %sn' % (a, b)
                    else:
                        return '%sn - %s' % (b, abs(a))

                kq = format_un(a_true, b_true)

                # Các đáp án trắc nghiệm
                du = ['u_n = %s'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (distractors) đảm bảo không trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    da_val = a_true + randint(-3, 3)
                    db_val = b_true + randint(-2, 2)
                    # Đảm bảo hệ số của n dương và (da_val, db_val) khác (a_true, b_true)
                    if db_val > 0 and (da_val, db_val) != (a_true, b_true):
                        distractor = 'u_n = %s' % (format_un(da_val, db_val))
                        if distractor not in s and distractor != da:
                            s.append(distractor)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho một cấp số cộng $(u_n)$ có $u_1 = %s$ và tổng của $%s$ số hạng đầu bằng $%s$. Công thức của số hạng tổng quát $u_n$ là'''
                                 %(latex(u1), latex(n), latex(Sn)))

                # Các đáp án
                da_d = ('\\True $%s$' % (da))
                da_s1 = '$%s$' % (das1)
                da_s2 = '$%s$' % (das2) 
                da_s3 = '$%s$' % (das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Tính toán trước các giá trị để điền vào lời giải
                n_half = n // 2
                two_u1 = 2 * u1
                n_minus_1 = n - 1
                step1_val = Sn // n_half
                step2_val = step1_val - two_u1

                # Nội dung lời giải
                loigiai = ('''Gọi $d$ là công sai của cấp số cộng. \\\\
                         Theo giả thiết, ta có tổng của $%s$ số hạng đầu là: \\\\
                         $S_{%s} = \\frac{%s}{2} \\left[ 2u_1 + (%s - 1)d \\right]$ \\\\
                         $\\Leftrightarrow %s = %s \\left( 2 \\cdot %s + %s d \\right)$ \\\\
                         $\\Leftrightarrow %s = %s + %s d$ \\\\
                         $\\Leftrightarrow %s d = %s$ \\\\
                         $\\Leftrightarrow d = %s$. \\\\
                         Công thức của số hạng tổng quát là: $u_n = u_1 + (n - 1)d = %s + (n - 1) \\cdot %s = %s$.'''
                         %(latex(n), latex(n), latex(n), latex(n),
                           latex(Sn), latex(n_half), latex(u1), latex(n_minus_1),
                           latex(step1_val), latex(two_u1), latex(n_minus_1),
                           latex(n_minus_1), latex(step2_val), latex(d),
                           latex(u1), latex(d), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

