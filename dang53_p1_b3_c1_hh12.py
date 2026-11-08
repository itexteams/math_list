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


def bt_dang53_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random hệ số tạo ra 3 vectơ theo mẫu
        # a = (-m; m; 0), b = (m; m; 0) để a vuông góc b, c = (m; m; p) với p != 0 để c không vuông góc b
        m = random.choice([1, 2, 3])
        p = random.choice([1, 2, 3])
    
        a1, a2, a3 = -m, m, 0
        b1, b2, b3 = m, m, 0
        c1, c2, c3 = m, m, p
    
        # Độ dài |a|, |c|
        len_a = sp.sqrt(a1**2 + a2**2 + a3**2)
        len_c = sp.sqrt(c1**2 + c2**2 + c3**2)
    
        # Tích vô hướng c.b
        cb = c1 * b1 + c2 * b2 + c3 * b3
    
        # Mệnh đề sai (đáp án cần chọn cho câu hỏi: "Mệnh đề nào dưới đây sai?")
        da = '$\\vec{c} \\perp \\vec{b}$'
    
        # Ba mệnh đề đúng
        s = [
            '$\\vec{a} \\perp \\vec{b}$',
            '$|\\vec{a}| = %s$' % latex(len_a),
            '$|\\vec{c}| = %s$' % latex(len_c)
        ]
    
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]
    
        # Câu hỏi[cite: 10]
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho các vec tơ $\\vec{a}=(%s;%s;%s)$; $\\vec{b}=(%s;%s;%s)$ và $\\vec{c}=(%s;%s;%s)$. Mệnh đề nào dưới đây sai?'''
                         % (a1, a2, a3, b1, b2, b3, c1, c2, c3)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Định dạng dấu số cho phép tính tích vô hướng
        term_a1 = '(%s) \\cdot %s' % (a1, b1) if a1 < 0 else '%s \\cdot %s' % (a1, b1)
        term_a2 = '%s \\cdot %s' % (a2, b2)
        term_a3 = '%s \\cdot %s' % (a3, b3)
    
        term_c1 = '%s \\cdot %s' % (c1, b1)
        term_c2 = '%s \\cdot %s' % (c2, b2)
        term_c3 = '%s \\cdot %s' % (c3, b3)
    
        term_sq_a1 = '(%s)^2' % a1 if a1 < 0 else '%s^2' % a1
    
        # Nội dung lời giải chi tiết[cite: 10]
        loigiai = ('''Ta kiểm tra từng mệnh đề:\\\\
    - Xét tích vô hướng $\\vec{a} \\cdot \\vec{b} = %s + %s + %s = 0 \\Rightarrow \\vec{a} \\perp \\vec{b}$. Mệnh đề này đúng.\\\\
    - Xét độ dài $|\\vec{a}| = \\sqrt{%s + %s^2 + %s^2} = %s$. Mệnh đề này đúng.\\\\
    - Xét độ dài $|\\vec{c}| = \\sqrt{%s^2 + %s^2 + %s^2} = %s$. Mệnh đề này đúng.\\\\
    - Xét tích vô hướng $\\vec{c} \\cdot \\vec{b} = %s + %s + %s = %s \\neq 0 \\Rightarrow \\vec{c}$ không vuông góc với $\\vec{b}$.\\\\
    Do đó mệnh đề \"$\\vec{c} \\perp \\vec{b}$\" là mệnh đề sai.'''
                   % (term_a1, term_a2, term_a3,
                      term_sq_a1, a2, a3, latex(len_a),
                      c1, c2, c3, latex(len_c),
                      term_c1, term_c2, term_c3, cb)
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
    