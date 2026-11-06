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


def bt_dang18_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1', '2']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dạng 1: Kết quả có 1 điểm C nguyên (Dựa trên hình ảnh mẫu)
                k = 3 
                xA, yA = 0, 2
                xB, yB = 4, 3

            elif dang=='2':
                # Dạng 2: Kết quả có 2 điểm C nguyên
                # Chọn A(1, 3), B(3, 1) và đường thẳng x - y = 0
                k = 1
                xA, yA = 1, 3
                xB, yB = 3, 1

            # --- Phần xử lý chung cho cả hai dạng ---
            t = symbols('t')
            # I thuộc Delta: x - ky = 0 => I(kt, t)
            # Vì ABCD là hình thoi nên IA vuông góc IB => tích vô hướng = 0
            expr = (xA - k*t)*(xB - k*t) + (yA - t)*(yB - t)
            f_expanded = expand(expr)

            # Lấy các hệ số của phương trình bậc 2: at^2 + bt + c = 0
            coeff_a = f_expanded.coeff(t, 2)
            coeff_b = f_expanded.coeff(t, 1)
            coeff_c = f_expanded.coeff(t, 0)

            # Giải tìm t
            sol_t = solve(expr, t)

            count_integer_C = 0
            loigiai_t_cases = ""

            for val_t in sol_t:
                # Tọa độ I
                xI, yI = k*val_t, val_t
                # Tọa độ C: I là trung điểm AC => C = 2I - A
                xC = 2*xI - xA
                yC = 2*yI - yA

                # Kiểm tra tọa độ nguyên
                if float(xC).is_integer() and float(yC).is_integer():
                    count_integer_C += 1
                    check_note = "(nhận)"
                else:
                    check_note = "(loại)"

                loigiai_t_cases += ('''Với $t = %s$ ta có: $\\begin{cases} I \\left( %s; %s \\right) \\\\ A(%s; %s) \\end{cases} \\Rightarrow C(%s; %s)$ %s \\\\ ''' 
                                    %(latex(val_t), latex(xI), latex(yI), latex(xA), latex(yA), latex(int(xC)), latex(int(yC)), check_note))

            # Đáp án đúng
            kq = count_integer_C

            # Các đáp án trắc nghiệm
            du = ['$%s$'%(kq)]
            da = random.choice(du)

            # Tạo các phương án sai (không trùng đáp án đúng)
            s = []
            for i in range(5):
                if str(i) != str(kq):
                    s.append('$%s$' % i)

            random.shuffle(s)
            das1 = s.pop()
            das2 = s.pop()
            das3 = s.pop()

            # Câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho hình thoi $ABCD$ có $A(%s;%s), B(%s;%s)$, giao điểm hai đường chéo nằm trên đường thẳng $\\Delta : x - %sy = 0$. Khi đó có bao nhiêu điểm $C$ có tọa độ nguyên?'''
                             %(latex(xA), latex(yA), latex(xB), latex(yB), latex(k) if k != 1 else ""))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Gọi $I$ là giao điểm của hai đường chéo. \\\\
                         Vì $I$ thuộc $\\Delta$ nên giả sử $I(%st; t)$. \\\\
                         Khi đó $\\vec{IA} = (%s - %st; %s - t), \\vec{IB} = (%s - %st; %s - t)$. \\\\
                         Vì tứ giác $ABCD$ là hình thoi nên $AC \\perp BD$ tại $I$, do đó $\\vec{IA} \\cdot \\vec{IB} = 0$. \\\\
                         $\\Leftrightarrow (%s - %st)(%s - %st) + (%s - t)(%s - t) = 0$ \\\\
                         $\\Leftrightarrow %st^2 %st + %s = 0$ \\\\
                         Suy ra $t = %s$ hoặc $t = %s$. \\\\
                         %s
                         Vậy có %s điểm $C$ có tọa độ nguyên.'''
                       %(latex(k) if k != 1 else "", 
                         latex(xA), latex(k) if k != 1 else "", latex(yA), latex(xB), latex(k) if k != 1 else "", latex(yB),
                         latex(xA), latex(k) if k != 1 else "", latex(xB), latex(k) if k != 1 else "", latex(yA), latex(yB),
                         latex(coeff_a), ('+' + latex(coeff_b) if coeff_b > 0 else latex(coeff_b)), latex(coeff_c),
                         latex(sol_t[0]), latex(sol_t[1] if len(sol_t) > 1 else sol_t[0]),
                         loigiai_t_cases,
                         latex(kq)
                       ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

