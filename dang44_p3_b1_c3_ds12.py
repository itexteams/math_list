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


def bt_dang44_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random các thông số để f'(x) = Ax^2 + B
                # Để f(x) có hệ số nguyên, chọn A là bội số của 3
                A = 3 * random.randint(1, 3) 
                B = random.randint(1, 4)

                # Biểu thức đề bài dựa trên mẫu: (1+x^2)f'(x) - B = Ax^4 + (A+B)x^2
                h_so_tu = B
                h_so_x4 = A
                h_so_x2 = A + B

                # f(1) = 0
                x0 = 1
                y0 = 0

                # Tính f(x) = tích phân (Ax^2 + B)dx
                f_prime = A*x**2 + B
                f_nguyen_ham_temp = integrate(f_prime, x) 
                # Tìm hằng số C từ f(1) = 0
                C_val = solve(f_nguyen_ham_temp.subs(x, x0) + symbols('C') - y0, symbols('C'))[0]
                f_x = f_nguyen_ham_temp + C_val

                # Tính f(x^2)
                f_x2 = f_x.subs(x, x**2)

                # F(x) là nguyên hàm của M * f(x^2)
                # Để F(x) có hệ số nguyên, chọn M là bội của 21 (vì có x^7/7 và x^3/3)
                M = 21 * random.randint(1, 2)
                F_nguyen_ham_temp = integrate(M * f_x2, x)

                # F(0) = D_fix
                D_fix = random.randint(5, 15)
                D_val = solve(F_nguyen_ham_temp.subs(x, 0) + symbols('D') - D_fix, symbols('D'))[0]
                F_x = F_nguyen_ham_temp + D_val

                # Tính giá trị F(2) - Kết quả là số nguyên
                target = 2
                kq_final = int(F_x.subs(x, target))

                # Đáp án đúng
                da = '$%s$' % (kq_final)

                # Tạo các đáp án sai (là các số nguyên lân cận)
                s = []
                while len(s) < 3:
                    sai = kq_final + random.choice([-20, -10, 10, 20, 30, -30]) + random.randint(1, 9)
                    sai_str = '$%s$' % (sai)
                    if sai != kq_final and sai_str not in s:
                        s.append(sai_str)

                das1, das2, das3 = s

                # Câu hỏi (Bỏ phần yêu cầu làm tròn)
                noidungcauhoi = ('''Cho hàm số $y = f(x)$ có đạo hàm $f'(x)$ thỏa mãn $(1+x^2)f'(x)-%s = %sx^4 + %sx^2, \\forall x \\in \\mathbb{R}$ và $f(%s)=%s$. Biết $F(x)$ là một nguyên hàm của hàm số $%s \\cdot f(x^2)$ và $F(0)=%s$. Giá trị $F(%s)$ bằng bao nhiêu?'''
                                 %(latex(h_so_tu), latex(h_so_x4), latex(h_so_x2), latex(x0), latex(y0), latex(M), latex(D_fix), latex(target)
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai=('''Ta có $(1+x^2)f'(x)-%s = %sx^4 + %sx^2 \\Leftrightarrow f'(x) = \\frac{%sx^4 + %sx^2 + %s}{1+x^2} = %s x^2 + %s$. \\\\
                          Suy ra $f(x) = \\int (%s x^2 + %s) \\text{d}x = %s + C$. \\\\
                          Do $f(%s)=%s \\Rightarrow %s + C = %s \\Rightarrow C = %s$. \\\\
                          Vậy $f(x) = %s$. Suy ra $f(x^2) = %s$. \\\\
                          Ta có $F(x) = \\int %s \\cdot f(x^2) \\text{d}x = %s \\int (%s) \\text{d}x = %s + D$. \\\\
                          Vì $F(0)=%s \\Rightarrow D=%s$. \\\\
                          Suy ra $F(x) = %s$. \\\\
                          Vậy $F(%s) = %s$.'''
                         %(latex(h_so_tu), latex(h_so_x4), latex(h_so_x2), latex(h_so_x4), latex(h_so_x2), latex(h_so_tu), latex(A), latex(B),
                           latex(A), latex(B), latex(f_nguyen_ham_temp), 
                           latex(x0), latex(y0), latex(f_nguyen_ham_temp.subs(x, x0)), latex(y0), latex(C_val),
                           latex(f_x), latex(f_x2),
                           latex(M), latex(M), latex(f_x2), latex(F_nguyen_ham_temp),
                           latex(D_fix), latex(D_val),
                           latex(F_x),
                           latex(target), latex(kq_final)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_final)) 

            # Xuất câu trắc nghiệm ra định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

