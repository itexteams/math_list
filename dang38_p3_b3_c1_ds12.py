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


def bt_dang38_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp sinh số ngẫu nhiên cho bài toán
                while True:
                    b_val = randint(1, 4)
                    x0 = random.choice([1, 2, 3, -1, -2])
                    D_val = b_val * x0
                    if D_val == 0: continue

                    y0 = random.choice([Rational(1, 2), Rational(1, 3), Rational(2, 3), Rational(3, 2), Rational(1, 4), Rational(3, 4), 2, 3])
                    C_val = random.choice([1, 2, 3, -1, -2])

                    a_val = b_val * y0

                    # Kiểm tra tử số tại x0 phải khác 0 để x0 thực sự là tiệm cận đứng
                    if a_val * x0 + C_val != 0:
                        break

                # Kết quả tính a + b
                kq = a_val + b_val

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu
                s = [
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq - 2)),
                    '$%s$' % (latex(a_val - b_val)),
                    '$%s$' % (latex(b_val - a_val)),
                    '$%s$' % (latex(a_val * b_val)),
                    '$%s$' % (latex(kq + Rational(1, 2)))
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

                # Định dạng chuỗi tử số và mẫu số
                if C_val > 0:
                    tu_str = "ax + %s" % C_val
                else:
                    tu_str = "ax - %s" % abs(C_val)

                if D_val > 0:
                    mau_str = "bx - %s" % D_val
                    pt_mau = "b \\cdot (%s) - %s = 0" % (latex(x0), D_val)
                else:
                    mau_str = "bx + %s" % abs(D_val)
                    pt_mau = "b \\cdot (%s) + %s = 0" % (latex(x0), abs(D_val))

                tu_val_at_x0 = a_val * x0 + C_val

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = \\frac{%s}{%s}$. Để đồ thị hàm số có $x = %s$ là tiệm cận đứng và $y = %s$ là tiệm cận ngang thì giá trị $a + b$ bằng bao nhiêu?'''
                                 % (tu_str, mau_str, latex(x0), latex(y0)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Đồ thị hàm số $y = \\frac{%s}{%s}$ có:\\\\
            - Tiệm cận đứng $x = %s$: Mẫu số bằng $0$ tại $x = %s$ và tử số khác $0$ tại $x = %s$.\\\\
            Cho mẫu số bằng $0$ tại $x = %s$ ta có:\\\\
            $$%s \\iff b = %s.$$\\\\
            - Tiệm cận ngang $y = %s$: Giới hạn của hàm số khi $x \\to \\pm\\infty$ là $\\frac{a}{b}$. Do đó:\\\\
            $$\\frac{a}{b} = %s \\iff a = %s \\cdot b = %s \\cdot %s = %s.$$\\\\
            Thử lại với $a = %s$ và $b = %s$, tại $x = %s$ tử số bằng $%s \\cdot (%s) + (%s) = %s \\ne 0$ (thỏa mãn).\\\\
            Vậy giá trị $a + b = %s + %s = %s$.'''
                           % (tu_str, mau_str, latex(x0), latex(x0), latex(x0),
                              latex(x0), pt_mau, latex(b_val),
                              latex(y0), latex(y0), latex(y0), latex(y0), latex(b_val), latex(a_val),
                              latex(a_val), latex(b_val), latex(x0), latex(a_val), latex(x0), latex(C_val), latex(tu_val_at_x0),
                              latex(a_val), latex(b_val), latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     
