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


def bt_dang6_p1_b3_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
    
        goc_dep = [30, 45, 60, 90]
        goc_chinh = random.choice(goc_dep)
        
        sign = random.choice([-1, 1])
        d_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        
        if goc_chinh == 45:
            # cos = 1/sqrt(2) => |C| / sqrt(A^2 + B^2 + C^2) = 1/sqrt(2)
            # Giống đề gốc: x + z + 1 = 0 (A=1, B=0, C=1) hoặc y + z + d = 0, hoặc có dấu trừ
            truc = random.choice(['x', 'y'])
            if truc == 'x':
                a_val = random.choice([-1, 1])
                b_val = 0
                c_val = random.choice([-1, 1]) * abs(a_val)
            else:
                a_val = 0
                b_val = random.choice([-1, 1])
                c_val = random.choice([-1, 1]) * abs(b_val)
        elif goc_chinh == 60:
            # cos = 1/2 => A^2 + B^2 = 3*C^2
            truc = random.choice(['x', 'y'])
            c_val = random.choice([-1, 1])
            pass
    
        # Để đảm bảo hệ số A, B, C nguyên đẹp, ta định nghĩa danh sách các cấu hình (A, B, C, goc):
        cau_hinh = [
            (1, 0, 1, 45),
            (1, 0, -1, 45),
            (-1, 0, 1, 45),
            (0, 1, 1, 45),
            (0, 1, -1, 45),
            (1, 1, 0, 90),
            (2, -1, 0, 90),
            (1, -2, 0, 90),
            (0, 1, 0, 90),
            (1, 0, 0, 90)
        ]
        ch = random.choice(cau_hinh)
        a_val, b_val, c_val, goc_chinh = ch
        k_mult = random.choice([1, 2, 3])
        a_val *= k_mult
        b_val *= k_mult
        c_val *= k_mult
        d_val = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        
        # Tạo chuỗi phương trình mặt phẳng (P)
        terms = []
        if a_val != 0:
            if a_val == 1:
                terms.append("x")
            elif a_val == -1:
                terms.append("-x")
            else:
                terms.append("%s x" % a_val)
                
        if b_val != 0:
            if b_val == 1:
                terms.append("+ y" if terms else "y")
            elif b_val == -1:
                terms.append("- y" if terms else "-y")
            elif b_val > 0:
                terms.append("+ %s y" % b_val if terms else "%s y" % b_val)
            else:
                terms.append("- %s y" % abs(b_val) if terms else "-%s y" % abs(b_val))
                
        if c_val != 0:
            if c_val == 1:
                terms.append("+ z" if terms else "z")
            elif c_val == -1:
                terms.append("- z" if terms else "-z")
            elif c_val > 0:
                terms.append("+ %s z" % c_val if terms else "%s z" % c_val)
            else:
                terms.append("- %s z" % abs(c_val) if terms else "-%s z" % abs(c_val))
                
        if d_val > 0:
            terms.append("+ %s" % d_val)
        else:
            terms.append("- %s" % abs(d_val))
            
        pt_p = " ".join(terms) + " = 0"
    
        # Đáp án đúng
        da = "$%s^\\circ$" % goc_chinh
        
        # Tập hợp các đáp án nhiễu
        tap_goc = [30, 45, 60, 90]
        tap_goc.remove(goc_chinh)
        
        das1 = "$%s^\\circ$" % tap_goc[0]
        das2 = "$%s^\\circ$" % tap_goc[1]
        das3 = "$%s^\\circ$" % tap_goc[2]
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$, góc giữa mặt phẳng $(Oxy)$ và mặt phẳng $(P)$ có phương trình $(P): %s$ là'''
                         % (pt_p))
                         
        # Chuẩn bị nội dung tính toán cho lời giải
        do_dai_np = "sqrt((%s)^2 + (%s)^2 + (%s)^2)" % (a_val, b_val, c_val)
        tong_binh = a_val**2 + b_val**2 + c_val**2
        tich_vo_huong = abs(c_val)
        
        loigiai = ('''Mặt phẳng $(Oxy)$ có một vectơ pháp tuyến là $\\vec{k} = (0; 0; 1)$.\\\\
    Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\\vec{n}_{(P)} = (%s; %s; %s)$.\\\\
    Gọi $\\alpha$ là góc giữa mặt phẳng $(Oxy)$ và mặt phẳng $(P)$, ta có: \\\\
    $\\cos \\alpha = \\frac{|\\vec{k} \\cdot \\vec{n}_{(P)}}{|\\vec{k}| \\cdot |\\vec{n}_{(P)}|} $ \\\\
    $=\\frac{|0 \\cdot (%s) + 0 \\cdot (%s) + 1 \\cdot (%s)|}{\\sqrt{0^2 + 0^2 + 1^2} \\cdot \\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} $ \\\\
    $=\\frac{%s}{\\sqrt{%s}} = \\frac{%s}{%s}$. \\\\
    Suy ra góc giữa hai mặt phẳng là $\\alpha = %s^\\circ$.'''
                   % (a_val, b_val, c_val,
                      a_val, b_val, c_val,
                      a_val, b_val, c_val,
                      tich_vo_huong, tong_binh,
                      latex(Rational(tich_vo_huong, 1)), latex(sqrt(tong_binh)),
                      goc_chinh))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content
    