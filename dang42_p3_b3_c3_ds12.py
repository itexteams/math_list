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


def bt_dang42_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chiều cao h (m), Chiều dài l (m), Cơ số b
                h_val = random.randint(2, 3)
                l_val = random.randint(4, 6)
                b_val = random.choice([0.4, 0.5, 0.6, 0.8])
                b_latex = str(b_val).replace('.', ',')

                # Tính toán thể tích bằng tích phân: V = Integrate(l * b^x, (x, 0, h))
                # Công thức: V = l * (b^h - 1) / ln(b)
                expr = l_val * (b_val**x)
                v_exact = integrate(expr, (x, 0, h_val))
                v_float = float(v_exact)

                # Làm tròn đến hàng phần mười theo quy tắc ROUND_HALF_UP
                kq_decimal = Decimal(str(v_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                # Tạo các đáp án nhiễu
                s = []
                while len(s) < 3:
                    nhieu = float(kq_decimal) + random.choice([-1.5, -1.2, -0.8, 0.5, 1.1, 1.4, 2.2])
                    if nhieu > 0:
                        nhieu_dec = Decimal(str(nhieu)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                        nhieu_str = str(nhieu_dec).replace('.', ',')
                        if nhieu_str != kq_str and nhieu_str not in s:
                            s.append('$%s$' % nhieu_str)

                da_d = ('\\True $%s$' % kq_str)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại nội dung bài toán (không dùng raw string r)
                noidungcauhoi = (
                    '\\immini{Một khối bê tông có chiều cao ' + str(h_val) + ' mét được đặt trên mặt đất. '
                    'Nếu cắt khối bê tông bởi một mặt phẳng nằm ngang và cách mặt đất $x$ mét ($0 \\le x \\le ' + str(h_val) + '$) '
                    'thì được mặt cắt là một hình chữ nhật có chiều dài ' + str(l_val) + ' mét và chiều rộng bằng $(' + b_latex + ')^x$ mét (xem hình). '
                    'Thể tích của khối bê tông đó bằng bao nhiêu mét khối? (Kết quả làm tròn đến hàng phần mười).}'
                    r'''{\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][line width=1]  (192.21,192.12) .. controls (174.58,180.21) and (162.09,152.99) .. (161.47,121.07) -- (212.18,118.55) -- cycle ; \draw  [line width=1]  (192.21,192.12) .. controls (174.58,180.21) and (162.09,152.99) .. (161.47,121.07) ;  
            	\draw  [draw opacity=0][line width=1]  (252.21,152.12) .. controls (234.58,140.21) and (222.09,112.99) .. (221.47,81.07) -- (272.18,78.55) -- cycle ; \draw  [line width=1]  (252.21,152.12) .. controls (234.58,140.21) and (222.09,112.99) .. (221.47,81.07) ;  
            	\draw  [draw opacity=0][line width=1]  (91.88,191.89) .. controls (108.88,179.83) and (120.88,152.76) .. (121.47,121.07) -- (72,118.61) -- cycle ; \draw  [line width=1]  (91.88,191.89) .. controls (108.88,179.83) and (120.88,152.76) .. (121.47,121.07) ;  
            	\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (151.88,151.89) .. controls (168.88,139.83) and (180.88,112.76) .. (181.47,81.07) -- (132,78.61) -- cycle ; \draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (151.88,151.89) .. controls (168.88,139.83) and (180.88,112.76) .. (181.47,81.07) ;  
            	\draw [line width=1]    (121.47,121.07) -- (181.47,81.07) ;
            	\draw [line width=1]    (161.47,121.07) -- (221.47,81.07) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (91.88,191.89) -- (151.88,151.89) ;
            	\draw [line width=1]    (192.21,192.12) -- (252.21,152.12) ;
            	\draw [line width=1]    (91.88,191.89) -- (192.21,192.12) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (151.88,151.89) -- (252.21,152.12) ;
            	\draw [line width=1]    (121.47,121.07) -- (161.47,121.07) ;
            	\draw [line width=1]    (181.47,81.07) -- (221.47,81.07) ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.49 ][line width=1]  (174.08,121.65) -- (230.67,121.65) -- (169.85,162.07) -- (113.26,162.07) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (174.08,121.65) -- (229.08,121.65) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (113.26,162.07) -- (173.26,122.07) ;
            	\draw [line width=1]    (169.85,162.07) -- (229.85,122.07) ; 
            	\draw [line width=1]    (113.26,162.07) -- (169.85,162.07) ;
            \end{tikzpicture}}'''
                )

                # Bước 1: Nghiên cứu đề bài và lời giải chi tiết
                loigiai = (
                    'Diện tích mặt cắt của khối bê tông tại độ cao $x$ là một hình chữ nhật có diện tích là:\\\\\n'
                    '$S(x) = ' + str(l_val) + ' \\cdot (' + b_latex + ')^x$ (m$^2$).\\\\\n'
                    'Thể tích của khối bê tông là tích phân của diện tích mặt cắt từ $0$ đến $'+ str(h_val) +'$ (độ cao của khối bê tông):\\\\\n'
                    '$V = \\int\\limits_{0}^{' + str(h_val) + '} S(x) \\text{d}x = \\int\\limits_{0}^{' + str(h_val) + '} ' + str(l_val) + ' \\cdot (' + b_latex + ')^x \\text{d}x$.\\\\\n'
                    'Áp dụng công thức nguyên hàm hàm số mũ $\\int a^x \\text{d}x = \\frac{a^x}{\\ln a} + C$, ta có:\\\\\n'
                    '$V = ' + str(l_val) + ' \\cdot \\left. \\frac{(' + b_latex + ')^x}{\\ln ' + b_latex + '} \\right|_{0}^{' + str(h_val) + '} '
                    '= ' + str(l_val) + ' \\cdot \\left( \\frac{(' + b_latex + ')^{' + str(h_val) + '}}{\\ln ' + b_latex + '} - \\frac{(' + b_latex + ')^0}{\\ln ' + b_latex + '} \\right)$.\\\\\n'
                    '$V = \\frac{' + str(l_val) + '}{\\ln ' + b_latex + '} \\cdot \\left( ' + str(round(b_val**h_val, 4)).replace('.', ',') + ' - 1 \\right) '
                    '\\approx ' + kq_str + '$ (m$^3$).'
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

