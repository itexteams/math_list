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


def bt_dang32_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Định nghĩa các góc và giá trị cosin tương ứng
                angles = [150, 120, 60, 30]
                C_deg = random.choice(angles)

                if C_deg == 150:
                    cos_C = -sp.sqrt(3)/2
                    cos_val_str = '-\\frac{\\sqrt{3}}{2}'
                    BC = sp.sqrt(3)
                    AC = random.choice([2, 4])
                elif C_deg == 120:
                    cos_C = Rational(-1, 2)
                    cos_val_str = '-\\frac{1}{2}'
                    BC = random.randint(2, 5)
                    AC = random.randint(3, 6)
                    while BC == AC:
                        AC = random.randint(3, 6)
                elif C_deg == 60:
                    cos_C = Rational(1, 2)
                    cos_val_str = '\\frac{1}{2}'
                    BC = random.randint(3, 7)
                    AC = random.randint(4, 8)
                    while BC == AC:
                        AC = random.randint(4, 8)
                else: # C_deg == 30
                    cos_C = sp.sqrt(3)/2
                    cos_val_str = '\\frac{\\sqrt{3}}{2}'
                    BC = sp.sqrt(3)
                    AC = random.choice([2, 4])

                # Tính cạnh AB
                AB_sq = sp.simplify(BC**2 + AC**2 - 2*BC*AC*cos_C)
                AB = sp.simplify(sp.sqrt(AB_sq))

                kq = latex(AB)

                # Tạo các đáp án sai (distractors)
                # Sai lầm 1: Pytago AB^2 = BC^2 + AC^2
                fake1 = sp.simplify(sp.sqrt(BC**2 + AC**2))

                # Sai lầm 2: Sai dấu cộng thành trừ trong định lý cosin
                fake2 = sp.simplify(sp.sqrt(BC**2 + AC**2 + 2*BC*AC*cos_C))

                # Sai lầm 3: Quên lấy căn bậc 2 của kết quả
                fake3 = AB_sq

                # Sai lầm 4: AB = BC + AC (Bất đẳng thức tam giác, học sinh lấy nhầm)
                fake4 = BC + AC

                s_cands = [fake1, fake2, fake3, fake4, sp.sqrt(10), sp.sqrt(13), 1]

                # Lọc bỏ các đáp án sai trùng với đáp án đúng hoặc trùng nhau
                unique_s_cands = []
                for cand in s_cands:
                    if cand != AB and cand not in unique_s_cands:
                        unique_s_cands.append(cand)

                random.shuffle(unique_s_cands)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                s = ['$%s$'%(latex(unique_s_cands[0])),
                     '$%s$'%(latex(unique_s_cands[1])),
                     '$%s$'%(latex(unique_s_cands[2]))]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tam giác $ABC$ có $C = %s^\\circ, BC = %s, AC = %s$. Tính độ dài cạnh $AB$.'''
                                 %(C_deg, latex(BC), latex(AC)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Tính các thành phần trong lời giải
                bc_sq = latex(sp.simplify(BC**2))
                ac_sq = latex(sp.simplify(AC**2))
                term3 = latex(sp.simplify(2*BC*AC))

                # Nội dung lời giải
                loigiai = ('''Áp dụng định lí côsin trong tam giác $ABC$, ta có: \\\\
                             $AB^2 = BC^2 + AC^2 - 2 \\cdot BC \\cdot AC \\cdot \\cos C$ \\\\
                             $\\Rightarrow AB^2 = \\left(%s\\right)^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ$ \\\\
                             $\\Rightarrow AB^2 = %s + %s - %s \\cdot \\left(%s\\right) = %s$. \\\\
                             Vậy $AB = %s$.'''
                           %(latex(BC), latex(AC), latex(BC), latex(AC), C_deg, bc_sq, ac_sq, term3, cos_val_str, latex(AB_sq), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

