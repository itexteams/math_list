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


def bt_dang23_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # h'(t) = a*t + b
                # Chọn a sao cho a/2 là số đẹp (ví dụ a là số chẵn hoặc đuôi .5)
                a = random.choice([1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2])
                b = random.randint(3, 8)
                h0 = random.randint(10, 25) # Chiều cao ban đầu
                t_sell = random.randint(5, 10) # Số năm trồng

                # Tính toán kết quả
                # H(t) = (a/2)*t^2 + b*t + C
                # H(0) = h0 => C = h0
                a_half = Rational(str(a))/2
                kq_val = a_half * (t_sell**2) + b * t_sell + h0

                # Định dạng số theo kiểu VN (dùng dấu phẩy cho số thập phân)
                def format_vn(num):
                    return str(num).replace('.', ',')

                kq = format_vn(float(kq_val))

                # --- BƯỚC 4: ĐIỀU CHỈNH PHƯƠNG ÁN SAI ---
                # Tạo các đáp án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = float(kq_val) + random.choice([-5, -10, 5, 10, 15, -3, 3])
                    if sai > 0 and sai != float(kq_val):
                        s.add(format_vn(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Một vườn ươm cây cảnh bán một cây sau $%s$ năm trồng và uốn tạo dáng. Tốc độ tăng trưởng trong suốt $%s$ năm được tính xấp xỉ bởi công thức $h'(t) = %s t + %s$, trong đó $h(t)$ (cm) là chiều cao của cây khi kết thúc $t$ (năm). Cây con khi được trồng cao $%s$ cm. Tính chiều cao của cây khi được bán.'''
                                 %(latex(t_sell), latex(t_sell), format_vn(a), latex(b), latex(h0)))

                # Đáp án
                da_d = ('\\True $%s$ cm' % (kq))
                da_s1 = ('$%s$ cm' % (das1))
                da_s2 = ('$%s$ cm' % (das2)) 
                da_s3 = ('$%s$ cm' % (das3)) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $H(t) = \\int h'(t) \\text{d}t = \\int (%s t + %s) \\text{d}t = %s t^2 + %s t + C$. \\\\
                           Tại thời điểm $t=0$ (khi mới trồng), cây cao $%s$ cm nên: \\\\
                           $H(0) = %s \\cdot 0^2 + %s \\cdot 0 + C = %s \\Rightarrow C = %s$. \\\\
                           Vậy công thức chiều cao là $H(t) = %s t^2 + %s t + %s$. \\\\
                           Khi được bán ($t = %s$), chiều cao của cây là: \\\\
                           $H(%s) = %s \\cdot (%s)^2 + %s \\cdot %s + %s = %s$ cm.'''
                           %(format_vn(a), latex(b), format_vn(float(a_half)), latex(b), 
                             latex(h0), format_vn(float(a_half)), latex(b), latex(h0), latex(h0),
                             format_vn(float(a_half)), latex(b), latex(h0),
                             latex(t_sell), latex(t_sell), format_vn(float(a_half)), latex(t_sell), latex(b), latex(t_sell), latex(h0), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

