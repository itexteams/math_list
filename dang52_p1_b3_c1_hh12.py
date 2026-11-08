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


def bt_dang52_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Hàm biểu diễn vectơ dạng tổ hợp i, j, k
        def format_vector(vx, vy, vz):
            terms = []
            # Hệ số của i
            if vx == 1:
                terms.append('\\vec{i}')
            elif vx == -1:
                terms.append('-\\vec{i}')
            elif vx != 0:
                terms.append('%s\\vec{i}' % vx)
    
            # Hệ số của j
            if vy == 1:
                terms.append('+ \\vec{j}' if len(terms) > 0 else '\\vec{j}')
            elif vy == -1:
                terms.append('- \\vec{j}' if len(terms) > 0 else '-\\vec{j}')
            elif vy > 0:
                terms.append('+ %s\\vec{j}' % vy if len(terms) > 0 else '%s\\vec{j}' % vy)
            elif vy < 0:
                terms.append('- %s\\vec{j}' % (-vy) if len(terms) > 0 else '%s\\vec{j}' % vy)
    
            # Hệ số của k
            if vz == 1:
                terms.append('+ \\vec{k}' if len(terms) > 0 else '\\vec{k}')
            elif vz == -1:
                terms.append('- \\vec{k}' if len(terms) > 0 else '-\\vec{k}')
            elif vz > 0:
                terms.append('+ %s\\vec{k}' % vz if len(terms) > 0 else '%s\\vec{k}' % vz)
            elif vz < 0:
                terms.append('- %s\\vec{k}' % (-vz) if len(terms) > 0 else '%s\\vec{k}' % vz)
    
            return ' '.join(terms)
    
        # Random vectơ a(a1; a2; a3)
        a1 = random.choice([i for i in range(-5, 6) if i != 0])
        a2 = random.choice([i for i in range(-5, 6) if i != 0])
        a3 = random.choice([i for i in range(-5, 6) if i != 0])
    
        # Vectơ b khuyết tung độ j (b2 = 0) giống mẫu b = i - 3k
        b1 = random.choice([i for i in range(-4, 5) if i != 0])
        b2 = 0
        b3 = random.choice([i for i in range(-4, 5) if i != 0])
    
        bieu_thuc_b = format_vector(b1, b2, b3)
    
        # Tích vô hướng đúng: a.b = a1*b1 + a2*b2 + a3*b3
        tich_dung = a1 * b1 + a2 * b2 + a3 * b3
        da = '$\\vec{a} \\cdot \\vec{b} = %s$' % tich_dung
    
        # Các đáp án nhiễu theo bẫy thường gặp của học sinh:
        # 1. Nhầm b = (b1; b3; 0) thay vì (b1; 0; b3) dẫn đến nhân nhầm a2 với b3
        tich_nham_1 = a1 * b1 + a2 * b3
        # 2. Sai dấu ở một thành phần
        tich_nham_2 = a1 * b1 - a3 * b3
        # 3. Quên nhân thành phần thứ ba hoặc sai lệch kết quả
        tich_nham_3 = -tich_dung
        tich_nham_4 = tich_dung + random.choice([-3, -2, -1, 1, 2, 3])
        tich_nham_5 = tich_dung + random.choice([-5, 5])
    
        candidates = [tich_nham_1, tich_nham_2, tich_nham_3, tich_nham_4, tich_nham_5]
    
        s = []
        for cand in candidates:
            ans_str = '$\\vec{a} \\cdot \\vec{b} = %s$' % cand
            if ans_str != da and ans_str not in s:
                s.append(ans_str)
    
        delta = 1
        while len(s) < 3:
            alt_str = '$\\vec{a} \\cdot \\vec{b} = %s$' % (tich_dung + delta)
            if alt_str != da and alt_str not in s:
                s.append(alt_str)
            delta += 1
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho lời giải
        sign_a1 = '(%s)' % a1 if a1 < 0 else '%s' % a1
        sign_b1 = '(%s)' % b1 if b1 < 0 else '%s' % b1
    
        sign_a2 = '(%s)' % a2 if a2 < 0 else '%s' % a2
        sign_b2 = '(%s)' % b2 if b2 < 0 else '%s' % b2
    
        sign_a3 = '(%s)' % a3 if a3 < 0 else '%s' % a3
        sign_b3 = '(%s)' % b3 if b3 < 0 else '%s' % b3
    
        # Câu hỏi[cite: 9]
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $(O;\\vec{i};\\vec{j};\\vec{k})$, cho hai vectơ $\\vec{a}=(%s;%s;%s)$ và $\\vec{b} = %s$. Tích $\\vec{a} \\cdot \\vec{b}$ bằng'''
                         % (a1, a2, a3, bieu_thuc_b)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải chi tiết[cite: 9]
        loigiai = ('''Từ giả thiết $\\vec{b} = %s$, suy ra tọa độ của vectơ $\\vec{b}$ là $\\vec{b} = (%s;%s;%s)$.\\\\
    Tích vô hướng của hai vectơ $\\vec{a}$ và $\\vec{b}$ là:\\\\
    $\\vec{a} \\cdot \\vec{b} = %s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$.'''
                   % (bieu_thuc_b, b1, b2, b3, sign_a1, sign_b1, sign_a2, sign_b2, sign_a3, sign_b3, tich_dung)
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    