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


def bt_dang54_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Random tọa độ ba điểm A, B, C không trùng nhau
        while True:
            xA, yA, zA = [random.randint(-4, 5) for _ in range(3)]
            xB, yB, zB = [random.randint(-4, 5) for _ in range(3)]
            xC, yC, zC = [random.randint(-4, 5) for _ in range(3)]
    
            # Tọa độ vectơ AB và BC
            x_AB = xB - xA
            y_AB = yB - yA
            z_AB = zB - zA
    
            x_BC = xC - xB
            y_BC = yC - yB
            z_BC = zC - zB
    
            # Tính tích vô hướng AB.BC
            tich_dung = x_AB * x_BC + y_AB * y_BC + z_AB * z_BC
    
            # Tránh vectơ không và tích bằng 0 để các đáp án đa dạng, rõ ràng
            if (x_AB, y_AB, z_AB) != (0, 0, 0) and (x_BC, y_BC, z_BC) != (0, 0, 0) and tich_dung != 0:
                break
    
        # Đáp án đúng[cite: 11]
        da = '$\\vec{AB} \\cdot \\vec{BC} = %s$' % tich_dung
    
        # Các đáp án nhiễu (ngược dấu, tính nhầm vectơ BA.BC, nhầm thành tích độ dài, sai lệch hệ số)[cite: 11]
        tich_BA_BC = (-x_AB) * x_BC + (-y_AB) * y_BC + (-z_AB) * z_BC
        tich_AB_CB = x_AB * (-x_BC) + y_AB * (-y_BC) + z_AB * (-z_BC)
    
        candidates = [
            -tich_dung,
            tich_BA_BC,
            -tich_BA_BC,
            tich_dung + 4,
            tich_dung - 4,
            -(tich_dung + 4),
            -(tich_dung - 4)
        ]
    
        s = []
        for val in candidates:
            ans_str = '$\\vec{AB} \\cdot \\vec{BC} = %s$' % val
            if ans_str != da and ans_str not in s:
                s.append(ans_str)
    
        delta = 1
        while len(s) < 3:
            ans_str = '$\\vec{AB} \\cdot \\vec{BC} = %s$' % (tich_dung + delta * 2)
            if ans_str != da and ans_str not in s:
                s.append(ans_str)
            delta += 1
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho biểu thức tọa độ vectơ trong lời giải
        sign_xA = '- (%s)' % xA if xA < 0 else '- %s' % xA
        sign_yA = '- (%s)' % yA if yA < 0 else '- %s' % yA
        sign_zA = '- (%s)' % zA if zA < 0 else '- %s' % zA
    
        sign_xB = '- (%s)' % xB if xB < 0 else '- %s' % xB
        sign_yB = '- (%s)' % yB if yB < 0 else '- %s' % yB
        sign_zB = '- (%s)' % zB if zB < 0 else '- %s' % zB
    
        # Định dạng dấu ngoặc cho các số khi nhân
        str_x_AB = '(%s)' % x_AB if x_AB < 0 else '%s' % x_AB
        str_y_AB = '(%s)' % y_AB if y_AB < 0 else '%s' % y_AB
        str_z_AB = '(%s)' % z_AB if z_AB < 0 else '%s' % z_AB
    
        str_x_BC = '(%s)' % x_BC if x_BC < 0 else '%s' % x_BC
        str_y_BC = '(%s)' % y_BC if y_BC < 0 else '%s' % y_BC
        str_z_BC = '(%s)' % z_BC if z_BC < 0 else '%s' % z_BC
    
        # Câu hỏi[cite: 11]
        noidungcauhoi = ('''Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$. Tích vô hướng hai vectơ $\\vec{AB} \\cdot \\vec{BC}$ bằng'''
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
    
        # Nội dung lời giải chi tiết[cite: 11]
        loigiai = ('''Ta có:\\\\
    $\\vec{AB} = (%s %s; %s %s; %s %s) = (%s;%s;%s)$\\\\
    $\\vec{BC} = (%s %s; %s %s; %s %s) = (%s;%s;%s)$.\\\\
    Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{BC}$ là:\\\\
    $\\vec{AB} \\cdot \\vec{BC} = %s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$.'''
                   % (xB, sign_xA, yB, sign_yA, zB, sign_zA, x_AB, y_AB, z_AB,
                      xC, sign_xB, yC, sign_yB, zC, sign_zB, x_BC, y_BC, z_BC,
                      str_x_AB, str_x_BC, str_y_AB, str_y_BC, str_z_AB, str_z_BC, tich_dung)
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
    