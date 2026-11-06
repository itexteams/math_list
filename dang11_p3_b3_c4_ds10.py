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


def bt_dang11_p3_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số của tử thức: x^2 + (m + a)x + b
                # Để đơn giản và giống mẫu, ta giữ hệ số x^2 là 1
                # Chọn b dương để có khả năng delta <= 0
                b = random.randint(1, 4) 
                a = random.randint(1, 5)

                # Mẫu thức: x^2 + cx + d luôn dương
                # Điều kiện: c^2 - 4d < 0. Chọn c chẵn để chia 2 dễ dàng.
                c = random.choice([2, 4])
                d = random.randint(c**2 // 4 + 1, c**2 // 4 + 5)

                # Giải bất phương trình (m+a)^2 - 4*1*b <= 0
                # <=> |m + a| <= sqrt(4b) <=> -sqrt(4b) - a <= m <= sqrt(4b) - a
                m_min = -2 * sqrt(b) - a
                m_max = 2 * sqrt(b) - a

                # Tìm các giá trị nguyên của m
                val_m = []
                for i in range(math.ceil(m_min), math.floor(m_max) + 1):
                    val_m.append(i)

                kq_num = len(val_m) # Số lượng giá trị nguyên (Đáp án đúng)
                da = '$' + str(kq_num) + '$'

                # Tạo danh sách đáp án nhiễu
                s_set = {kq_num + 1, kq_num + 2, kq_num - 1, kq_num - 2, 0}
                s_set.discard(kq_num) # Đảm bảo không trùng đáp án đúng
                s_list = list(s_set)
                random.shuffle(s_list)

                das1 = '$' + str(s_list[0]) + '$'
                das2 = '$' + str(s_list[1]) + '$'
                das3 = '$' + str(s_list[2]) + '$'

                # Nội dung câu hỏi
                # Bất phương trình: [x^2 + (m + a)x + b] / [x^2 + cx + d] >= 0
                tu_thuc = 'x^2 + (m + %s)x + %s' % (latex(a), latex(b))
                mau_thuc = 'x^2 + %sx + %s' % (latex(c), latex(d))

                noidungcauhoi = ('''Có tất cả bao nhiêu giá trị nguyên của tham số $m$ để bất phương trình $\\frac{%s}{%s} \\geq 0$ nghiệm đúng với mọi $x \\in \\mathbb{R}$?'''
                                 %(tu_thuc, mau_thuc))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                delta_mau = c**2 - 4*d
                loigiai = ('''Ta có: $%s = (x + %s)^2 + %s > 0, \\forall x \\in \\mathbb{R}$ (vì $\\Delta = %s < 0$ và hệ số $a=1>0$).\\\\
                           Do đó: $\\frac{%s}{%s} \\geq 0, \\forall x \\in \\mathbb{R} \\Leftrightarrow %s \\geq 0, \\forall x \\in \\mathbb{R}$\\\\
                           $\\Leftrightarrow \\begin{cases} 1 > 0 \\text{ (luôn đúng)} \\\\ \\Delta = (m + %s)^2 - 4 \\cdot 1 \\cdot %s \\leq 0 \\end{cases} \\Leftrightarrow (m + %s)^2 \\leq %s$\\\\
                           $\\Leftrightarrow %s \\leq m + %s \\leq %s \\Leftrightarrow %s \\leq m \\leq %s$.\\\\
                           Vậy các giá trị nguyên của $m$ thỏa mãn là $m \\in \\{%s\\}$. Có $%s$ giá trị.'''
                           %(mau_thuc, latex(Rational(c,2)), latex(d - (c//2)**2), latex(delta_mau),
                             tu_thuc, mau_thuc, tu_thuc,
                             latex(a), latex(b), latex(a), latex(4*b),
                             latex(round(-2*math.sqrt(b), 2)), latex(a), latex(round(2*math.sqrt(b), 2)), 
                             latex(round(float(m_min), 2)), latex(round(float(m_max), 2)),
                             '; '.join(map(str, val_m)), latex(kq_num)
                            ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

