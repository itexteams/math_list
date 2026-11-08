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


def bt_dang51_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random tọa độ điểm A, B, C sao cho tạo thành tam giác và độ dài có căn thức đẹp
        while True:
            xA, yA, zA = [random.randint(-3, 3) for _ in range(3)]
            xB, yB, zB = [random.randint(-3, 3) for _ in range(3)]
            xC, yC, zC = [random.randint(-3, 3) for _ in range(3)]
    
            # Vectơ AB, AC
            vAB = (xB - xA, yB - yA, zB - zA)
            vAC = (xC - xA, yC - yA, zC - zA)
    
            # Tích có hướng để kiểm tra không thẳng hàng
            cross_prod = (
                vAB[1] * vAC[2] - vAB[2] * vAC[1],
                vAB[2] * vAC[0] - vAB[0] * vAC[2],
                vAB[0] * vAC[1] - vAB[1] * vAC[0]
            )
            if cross_prod == (0, 0, 0):
                continue
    
            d2_AB = (xB - xA)**2 + (yB - yA)**2 + (zB - zA)**2
            d2_BC = (xC - xB)**2 + (yC - yB)**2 + (zC - zB)**2
            d2_CA = (xA - xC)**2 + (yA - yC)**2 + (zA - zC)**2
    
            len_AB = sp.sqrt(d2_AB)
            len_BC = sp.sqrt(d2_BC)
            len_CA = sp.sqrt(d2_CA)
    
            chu_vi = len_AB + len_BC + len_CA
    
            # Chọn trường hợp có 2 cạnh cùng căn hoặc chu vi gọn gàng tương tự mẫu
            if d2_AB <= 30 and d2_BC <= 30 and d2_CA <= 30:
                break
    
        # Đáp án đúng
        da = '$%s$' % latex(chu_vi)
    
        # Sinh các đáp án nhiễu theo các lỗi sai thường gặp (cộng nhầm 2 cạnh, nhân hệ số)
        s = [
            '$%s$' % latex(len_AB + len_BC),
            '$%s$' % latex(len_BC + len_CA),
            '$%s$' % latex(len_AB + len_CA),
            '$%s$' % latex(2 * len_AB + len_BC),
            '$%s$' % latex(len_AB + 2 * len_BC),
            '$%s$' % latex(len_BC + 2 * len_CA),
            '$%s$' % latex(2 * chu_vi),
            '$%s$' % latex(sp.sqrt(d2_AB + d2_BC + d2_CA))
        ]
    
        # Lọc bỏ đáp án trùng với đáp án đúng
        s = list(set([item for item in s if item != da]))
    
        # Bổ sung nếu chưa đủ 3 đáp án sai
        k = 1
        while len(s) < 3:
            alt = '$%s$' % latex(chu_vi + k)
            if alt != da and alt not in s:
                s.append(alt)
            k += 1
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho công thức tính độ dài
        sign_xB = '- (%s)' % xB if xB < 0 else '- %s' % xB
        sign_yB = '- (%s)' % yB if yB < 0 else '- %s' % yB
        sign_zB = '- (%s)' % zB if zB < 0 else '- %s' % zB
    
        sign_xC = '- (%s)' % xC if xC < 0 else '- %s' % xC
        sign_yC = '- (%s)' % yC if yC < 0 else '- %s' % yC
        sign_zC = '- (%s)' % zC if zC < 0 else '- %s' % zC
    
        sign_xA = '- (%s)' % xA if xA < 0 else '- %s' % xA
        sign_yA = '- (%s)' % yA if yA < 0 else '- %s' % yA
        sign_zA = '- (%s)' % zA if zA < 0 else '- %s' % zA
    
        # Câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Chu vi của tam giác $ABC$ bằng'''
                         % (xA, yA, zA, xB, yB, zB, xC, yC, zC)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Lời giải chi tiết
        loigiai = ('''Ta có độ dài các cạnh của tam giác $ABC$ là:\\\\
    $AB = \\sqrt{(%s %s)^2 + (%s %s)^2 + (%s %s)^2} = \\sqrt{%s} = %s$.\\\\
    $BC = \\sqrt{(%s %s)^2 + (%s %s)^2 + (%s %s)^2} = \\sqrt{%s} = %s$.\\\\
    $CA = \\sqrt{(%s %s)^2 + (%s %s)^2 + (%s %s)^2} = \\sqrt{%s} = %s$.\\\\
    Chu vi của tam giác $ABC$ là:\\\\
    $P = AB + BC + CA = %s + %s + %s = %s$.'''
                   % (xB, sign_xA, yB, sign_yA, zB, sign_zA, d2_AB, latex(len_AB),
                      xC, sign_xB, yC, sign_yB, zC, sign_zB, d2_BC, latex(len_BC),
                      xA, sign_xC, yA, sign_yC, zA, sign_zC, d2_CA, latex(len_CA),
                      latex(len_AB), latex(len_BC), latex(len_CA), latex(chu_vi))
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
    