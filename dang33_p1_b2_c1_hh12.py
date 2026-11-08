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


def bt_dang33_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random tọa độ điểm A(xA; yA; zA) và trung điểm M(xM; yM; zM)
        while True:
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)
            zA = random.randint(-5, 5)
    
            xM = random.randint(-5, 5)
            yM = random.randint(-5, 5)
            zM = random.randint(-5, 5)
    
            # Đảm bảo điểm A và M phân biệt
            if (xA, yA, zA) != (xM, yM, zM):
                break
    
        # Tọa độ điểm B = 2*M - A
        xB = 2 * xM - xA
        yB = 2 * yM - yA
        zB = 2 * zM - zA
    
        # Đáp án đúng
        da = '$B(%s;%s;%s)$' % (xB, yB, zB)
    
        # Biểu diễn tọa độ dưới dạng phân số tối giản LaTeX
        def format_coord(num, den=2):
            if num % den == 0:
                return '%s' % (num // den)
            f = frac(num, den)
            return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)
    
        # Đáp án nhiễu: Trung điểm của AM, nhầm dấu phép trừ 2*M - A, đảo vai trò 2*A - M
        mid_AM = '$B\\left(%s;%s;%s\\right)$' % (format_coord(xA + xM), format_coord(yA + yM), format_coord(zA + zM))
        wrong_sub1 = '$B(%s;%s;%s)$' % (xB, -yB, zB)
        wrong_sub2 = '$B(%s;%s;%s)$' % (2 * xA - xM, 2 * yA - yM, 2 * zA - zM)
        wrong_sub3 = '$B(%s;%s;%s)$' % (-xB, yB, zB)
        wrong_sub4 = '$B(%s;%s;%s)$' % (xB, yB, -zB)
        wrong_sum = '$B(%s;%s;%s)$' % (2 * xM + xA, 2 * yM + yA, 2 * zM + zA)
    
        s = [mid_AM, wrong_sub1, wrong_sub2, wrong_sub3, wrong_sub4, wrong_sum]
        s = list(set([item for item in s if item != da]))
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho lời giải
        sign_xA = '- (%s)' % xA if xA < 0 else '- %s' % xA
        sign_yA = '- (%s)' % yA if yA < 0 else '- %s' % yA
        sign_zA = '- (%s)' % zA if zA < 0 else '- %s' % zA
    
        term_xM = '2 \\cdot (%s)' % xM if xM < 0 else '2 \\cdot %s' % xM
        term_yM = '2 \\cdot (%s)' % yM if yM < 0 else '2 \\cdot %s' % yM
        term_zM = '2 \\cdot (%s)' % zM if zM < 0 else '2 \\cdot %s' % zM
    
        # Câu hỏi[cite: 6]
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s)$ và $M(%s;%s;%s)$. Tọa độ điểm $B$ biết $M$ là trung điểm của đoạn $AB$ là'''
                         % (xA, yA, zA, xM, yM, zM)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải chi tiết[cite: 6]
        loigiai = ('''Vì $M$ là trung điểm của đoạn thẳng $AB$ nên ta có:\\\\
    $\\begin{cases} x_M = \\dfrac{x_A + x_B}{2} \\\\ y_M = \\dfrac{y_A + y_B}{2} \\\\ z_M = \\dfrac{z_A + z_B}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x_B = 2x_M - x_A = %s %s = %s \\\\ y_B = 2y_M - y_A = %s %s = %s \\\\ z_B = 2z_M - z_A = %s %s = %s. \\end{cases}$\\\\
    Vậy tọa độ của điểm $B$ là $B(%s;%s;%s)$.'''
                   % (term_xM, sign_xA, xB, term_yM, sign_yA, yB, term_zM, sign_zA, zB, xB, yB, zB)
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
    