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


def bt_dang57_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ điểm A, B và hệ số đường thẳng d: x + ay + c = 0
                # Để đơn giản và giống mẫu, ta fix hệ số của x là 1
                m=symbols('m')
                a_d = randint(1, 3) 
                c_d = randint(-10, 10)

                xA = randint(-5, 5)
                yA = randint(-5, 5)
                xB = randint(-5, 10)
                yB = randint(-5, 10)
                k = randint(2, 4) # Hệ số k trong |MA + kMB|

                # Điểm M thuộc d: x + ay + c = 0 => x = -ay - c. Đặt y = m => M(-a*m - c, m)
                # Trong ảnh mẫu: x + 2y - 4 = 0 => x = 4 - 2m, y = m. Tương ứng c = -4, a = 2.

                # Biểu diễn các vector theo m
                # MA = (xA - (-a_d*m - c_d), yA - m) = (a_d*m + xA + c_d, yA - m)
                vMA_x = Poly(a_d*m + xA + c_d, m)
                vMA_y = Poly(-1*m + yA, m)

                # MB = (xB - (-a_d*m - c_d), yB - m) = (a_d*m + xB + c_d, yB - m)
                vMB_x = Poly(a_d*m + xB + c_d, m)
                vMB_y = Poly(-1*m + yB, m)

                # u = MA + k*MB
                u_x = vMA_x + k * vMB_x
                u_y = vMA_y + k * vMB_y

                # Bình phương độ dài: |u|^2 = u_x^2 + u_y^2
                f_m = expand(u_x.as_expr()**2 + u_y.as_expr()**2)
                poly_f = Poly(f_m, m)
                coeffs = poly_f.all_coeffs() # [A, B, C] của Am^2 + Bm + C
                A_f, B_f, C_f = coeffs[0], coeffs[1], coeffs[2]

                # Tìm giá trị nhỏ nhất của căn bậc hai của tam thức bậc hai
                # f(m) = A_f(m + B_f/2A_f)^2 + (C_f - B_f^2/4A_f)
                m_min = Rational(-B_f, 2*A_f)
                val_min_sq = f_m.subs(m, m_min)
                kq_chuan = sqrt(val_min_sq)

                # Đáp án đúng
                da = '$%s$' % (latex(kq_chuan))

                # Tạo các đáp án sai
                s = []
                while len(s) < 3:
                    sai = random.choice([sqrt(val_min_sq + randint(1, 10)), 
                                         sqrt(abs(val_min_sq - randint(1, 5))),
                                         randint(2, 10) * sqrt(randint(2, 5))])
                    if sai != kq_chuan:
                        s_str = '$%s$' % (latex(sai))
                        if s_str not in s:
                            s.append(s_str)

                # Câu hỏi
                line_eq = 'x + %sy %s = 0' % (a_d, '+ ' + str(c_d) if c_d > 0 else '- ' + str(abs(c_d)))
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d:%s$ và hai điểm $A(%s;%s)$, $B(%s;%s)$. Điểm $M$ thuộc $d$ sao cho $|\\overrightarrow{MA} + %s\\overrightarrow{MB}|$ nhỏ nhất. Tính giá trị nhỏ nhất đó.'''
                                %(line_eq, xA, yA, xB, yB, k))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d] + s
                random.shuffle(list_1)

                # Lời giải chi tiết
                expr_M = '(%s - %sm; m)' % (latex(-c_d), latex(a_d))

                # MA vector
                ma_x_expr = simplify(xA - (-a_d*m - c_d))
                ma_y_expr = simplify(yA - m)

                # MB vector
                mb_x_expr = simplify(xB - (-a_d*m - c_d))
                mb_y_expr = simplify(yB - m)

                # u vector
                ux_expr = expand(ma_x_expr + k*mb_x_expr)
                uy_expr = expand(ma_y_expr + k*mb_y_expr)

                # Phân tích hằng đẳng thức cho f(m)
                # f(m) = A_f * (m^2 + (B_f/A_f)m + C_f/A_f)
                loigiai = ('''Điểm $M \\in d$ nên có tọa độ dạng $M%s$.\\\\
                            Ta có $\\overrightarrow{MA} = (%s; %s)$; $\\overrightarrow{MB} = (%s; %s)$, suy ra $%s\\overrightarrow{MB} = (%s; %s)$.\\\\
                            Do đó $\\overrightarrow{MA} + %s\\overrightarrow{MB} = (%s; %s)$. Ta có:\\\\
                            $|\\overrightarrow{MA} + %s\\overrightarrow{MB}| = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$.\\\\
                            $= \\sqrt{%s(m^2 + %sm + %s)} = \\sqrt{%s \\left[ \\left(m %s \\right)^2 + %s \\right]} \\ge %s$.'''
                            %(expr_M, latex(ma_x_expr), latex(ma_y_expr), latex(mb_x_expr), latex(mb_y_expr), 
                              k, latex(expand(k*mb_x_expr)), latex(expand(k*mb_y_expr)),
                              k, latex(ux_expr), latex(uy_expr),
                              k, latex(ux_expr), latex(uy_expr), latex(f_m),
                              A_f, Rational(B_f, A_f), Rational(C_f, A_f), A_f, 
                              '+ ' + latex(-m_min) if -m_min > 0 else latex(-m_min),
                              latex(Rational(val_min_sq, A_f)), latex(kq_chuan)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-')
            return content 

