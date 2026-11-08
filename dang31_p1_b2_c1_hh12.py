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


def bt_dang31_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random tọa độ điểm M(xM; yM; zM) và vectơ MN(u1; u2; u3)
        # Giữ dạng có thành phần bằng 0 tương tự như đề gốc
        xM = random.choice([i for i in range(-5, 6) if i != 0])
        yM = random.choice([i for i in range(-5, 6) if i != 0])
        zM = 0
    
        u1 = random.choice([i for i in range(-4, 5) if i != 0])
        u2 = random.choice([i for i in range(-4, 5) if i != 0])
        u3 = 0
    
        # Tọa độ đúng của N = M + MN
        xN = xM + u1
        yN = yM + u2
        zN = zM + u3
    
        # Đáp án đúng
        da = '$N(%s;%s;%s)$' % (xN, yN, zN)
    
        # Các đáp án nhiễu (lỗi lấy M - MN, đổi dấu, sai dấu)
        s = [
            '$N(%s;%s;%s)$' % (-xN, yN, zN),
            '$N(%s;%s;%s)$' % (xM - u1, yM - u2, zM - u3),
            '$N(%s;%s;%s)$' % (-(xM - u1), -(yM - u2), zM - u3),
            '$N(%s;%s;%s)$' % (xN, -yN, zN),
            '$N(%s;%s;%s)$' % (-xN, -yN, zN),
            '$N(%s;%s;%s)$' % (u1 - xM, u2 - yM, u3 - zM)
        ]
    
        # Loại bỏ đáp án trùng với đáp án đúng
        s = list(set([item for item in s if item != da]))
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho điểm $M(%s;%s;%s)$ và $\\vec{MN} = (%s;%s;%s)$. Tọa độ của điểm $N$ là'''
                         % (xM, yM, zM, u1, u2, u3)
                         )
    
        # Các đáp án (không có dấu chấm ở cuối)
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Trình bày dấu trong lời giải
        dau_u1 = '+ (%s)' % u1 if u1 < 0 else '+ %s' % u1
        dau_u2 = '+ (%s)' % u2 if u2 < 0 else '+ %s' % u2
        dau_u3 = '+ (%s)' % u3 if u3 < 0 else '+ %s' % u3
    
        # Nội dung lời giải chi tiết
        loigiai = ('''Gọi $N(x_N;y_N;z_N)$ là tọa độ của điểm $N$.\\\\
    Ta có $\\vec{MN} = (x_N - x_M; y_N - y_M; z_N - z_M)$.\\\\
    Theo giả thiết, ta có hệ phương trình:\\\\
    $\\begin{cases} x_N - %s = %s \\\\ y_N - %s = %s \\\\ z_N - %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_N = %s %s = %s \\\\ y_N = %s %s = %s \\\\ z_N = %s %s = %s. \\end{cases}$\\\\
    Vậy tọa độ của điểm $N$ là $N(%s;%s;%s)$.'''
                   % (xM, u1, yM, u2, zM, u3, xM, dau_u1, xN, yM, dau_u2, yN, zM, dau_u3, zN, xN, yN, zN)
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
    