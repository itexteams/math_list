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


def bt_dang27_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['3'] 
            dang=random.choice(lisdang)

            if dang=='3':
                # --- Random hóa các tham số cơ sở ---
                # Random u1 (Số chỗ ngồi hàng đầu): [5, 20]
                u1 = randint(5, 20)      
                # Random d (Công sai): [2, 5]
                d = randint(2, 5)        
                # Random n_val (Số hàng ghế - Đáp án): [15, 40]
                n_val = randint(15, 40)  

                # --- Tính toán S_n (Tổng chỗ ngồi) từ các tham số đã random ---
                # Công thức: S_n = n/2 * [2*u1 + (n-1)*d]
                S_n = (n_val / 2) * (2 * u1 + (n_val - 1) * d)
                S_n_random = int(S_n) # Tổng số chỗ ngồi (luôn là số nguyên)

                # --- Giải phương trình tìm n (Mặc dù đã biết, nhưng cần để chứng minh trong lời giải) ---
                n_sym = symbols('n')
                eq = Eq(S_n_random, n_sym/2 * (2*u1 + (n_sym-1)*d))
                n_solutions = solve(eq, n_sym)

                # Lấy nghiệm nguyên dương
                n_ans_val = [s for s in n_solutions if s > 0 and s.is_integer][0]

                # --- Chuẩn bị đáp án trắc nghiệm ---
                kq = '$%s$'%(latex(n_ans_val))

                # Tạo các đáp án sai xung quanh đáp án đúng
                n_int = int(n_ans_val)
                # Chọn các giá trị sai trong khoảng [-3, -2, -1, 1, 2, 3] xung quanh đáp án đúng
                s_int = [n_int + i for i in [-3, -2, -1, 1, 2, 3] if n_int + i > 0]
                s_options = ['$%s$'%(latex(i)) for i in s_int]

                du = [kq]
                da = random.choice(du)

                random.shuffle(s_options)
                # Lấy 3 đáp án sai
                das1 = s_options.pop()
                das2 = s_options.pop()
                das3 = s_options.pop()

                # --- Nội dung câu hỏi ---
                noidungcauhoi = ('''Có bao nhiêu hàng ghế trong một góc khán đài của một sân vận động, biết tổng số chỗ ngồi là $%s$ chỗ, hàng ghế đầu tiên có $%s$ chỗ và mỗi hàng ghế sau có thêm $%s$ chỗ ngồi so với hàng ghế ngay trước nó?'''
                                 %(latex(S_n_random), latex(u1), latex(d)
                                 ))

                # --- Sắp xếp đáp án (bao gồm đáp án đúng \True) ---
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = ('''Áp dụng công thức tính tổng $n$ số hạng đầu của cấp số cộng với $S_n = %s, u_1 = %s, d = %s$ để tìm $n$, ta được \\\\
                              $$%s = S_n = \\frac{n}{2} \\left[2 \\cdot %s + (n-1)%s\\right]$$ \\\\
                              Giải phương trình bậc hai theo $n$ ta được $n = %s$, tức là góc khán đài đó có $%s$ hàng ghế.'''
                          %(latex(S_n_random), latex(u1), latex(d),
                            latex(S_n_random), latex(u1), latex(d),
                            latex(n_ans_val), latex(n_ans_val)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(n_ans_val))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

