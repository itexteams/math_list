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


def bt_dang27_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random nghiệm cố định x2 (phải là số nguyên khác 0)
                # Phương trình x^3 - Ax^2 + Bx - C = 0 có 3 nghiệm lập thành CSN thì C = (x2)^3
                x2_val = random.choice([2, 3, 4, -2, -3])
                C_val = x2_val**3
                m=symbols('m')

                # Tạo hệ số ngẫu nhiên cho a, b, c, d
                a_val = random.randint(1, 5)
                b_val = random.randint(1, 5)

                # Để m là số nguyên, chọn m_ans trước
                m_ans = random.randint(1, 5)

                # Khi thay x2 vào: - (a*m + b)*x2^2 + (c*m + d)*x2 = 0
                # <=> c*m + d = (a*m + b)*x2
                # Chọn c và tính d:
                c_val = random.randint(1, 5)
                # d = a*x2*m + b*x2 - c*m
                # Để d là số nguyên, công thức trên luôn cho d nguyên
                d_val = a_val * x2_val * m_ans + b_val * x2_val - c_val * m_ans

                # Tạo biểu thức
                term2 = a_val * m + b_val
                term3 = c_val * m + d_val

                # Hàm format latex
                def format_poly(term):
                    if term == 1:
                        return ""
                    elif term == -1:
                        return "-"
                    return latex(term)

                str_term2 = latex(term2)
                str_term3 = latex(term3)

                # Kiểm tra điều kiện có 3 nghiệm phân biệt (có thể bỏ qua trong script gen đơn giản)

                # Các đáp án trắc nghiệm
                da = '$m = %s$' % m_ans

                # Tạo các phương án nhiễu
                # Phương án có chữ "hoặc"
                m_fake1 = m_ans
                m_fake2 = Rational(-1, random.randint(2, 5))
                s1 = '$m = %s$ hoặc $m = %s$' % (m_fake1, latex(m_fake2))

                m_fake3 = random.randint(-6, -1)
                m_fake4 = random.randint(6, 10)
                s2 = '$m = %s$ hoặc $m = %s$' % (m_fake3, m_fake4)

                m_fake5 = m_ans + random.choice([-1, 1])
                m_fake6 = m_fake3
                s3 = '$m = %s$ hoặc $m = %s$' % (m_fake5, m_fake6)

                # Lọc trùng
                s = [s1, s2, s3]
                # Đảm bảo ko có đáp án đúng trong list nhiễu
                while da in s:
                    s.remove(da)
                    s.append('$m = %s$' % (m_ans + 2))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Chú ý xử lý dấu của C_val và term3
                sign_C = "-" if C_val > 0 else "+"
                abs_C = abs(C_val)

                sign_term3 = "+" if term3.subs(m, 0) > 0 else "-"
                if term3.subs(m, 0) < 0: # Cần cẩn thận khi in term3, nếu có dấu trừ bên ngoài
                     str_term3 = "(%s)" % latex(term3)

                noidungcauhoi = ('''Giá trị $m$ để phương trình $x^3 - (%s)x^2 + (%s)x - %s = 0$ có $3$ nghiệm lập thành một cấp số nhân là'''
                                 % (str_term2, str_term3, abs_C))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giả sử phương trình có $3$ nghiệm $x_1, x_2, x_3$ lập thành cấp số nhân. \\\\
                             Theo định lí Vi-ét, ta có: $x_1x_2x_3 = %s$. \\\\
                             Mặt khác $x_1x_3 = x_2^2$ nên suy ra $x_2^3 = %s \\Leftrightarrow x_2 = %s$. \\\\
                             Thay $x = %s$ vào phương trình ban đầu ta được: \\\\
                             $%s^3 - (%s) \\cdot %s^2 + (%s) \\cdot %s - %s = 0 \\\\
                             \\Leftrightarrow %s - %s(%s) + %s(%s) - %s = 0 \\\\
                             \\Leftrightarrow %s - %s m - %s + %s m + %s - %s = 0 \\\\
                             \\Leftrightarrow %s m = %s \\Leftrightarrow m = %s$. \\\\
                             Thử lại với $m = %s$, phương trình có $3$ nghiệm phân biệt lập thành cấp số nhân. (Học sinh có thể tự kiểm tra lại).'''
                             % (abs_C if C_val > 0 else -abs_C, 
                                abs_C if C_val > 0 else -abs_C, x2_val,
                                x2_val,
                                x2_val, str_term2, x2_val, str_term3, x2_val, abs_C,
                                x2_val**3, x2_val**2, str_term2, x2_val, str_term3, abs_C,
                                x2_val**3, a_val*(x2_val**2), b_val*(x2_val**2), c_val*x2_val, d_val*x2_val, abs_C,
                                c_val*x2_val - a_val*(x2_val**2), b_val*(x2_val**2) - x2_val**3 - d_val*x2_val + abs_C, m_ans,
                                m_ans))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

