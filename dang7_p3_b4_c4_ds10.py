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


def bt_dang7_p3_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các bộ số (v1, v2, d1, d2, L) sao cho phương trình có nghiệm x hữu tỉ đẹp
                # Bộ 1: Gốc trong ảnh (x = 1.2h = 1h12p)
                # Bộ 2: v1=30, v2=40, d1=18, d2=24, L=100 (x = 1.4h = 1h24p)
                # Bộ 3: v1=60, v2=80, d1=20, d2=40, L=200 (x = 1.2h = 1h12p)
                sets = [
                    {'v1': 55, 'v2': 45, 'd1': 14, 'd2': 6, 'L': 100, 'start_h': 8},
                    {'v1': 30, 'v2': 40, 'd1': 18, 'd2': 24, 'L': 100, 'start_h': 7},
                    {'v1': 110, 'v2': 90, 'd1': 28, 'd2': 12, 'L': 200, 'start_h': 9}
                ]

                chosen = random.choice(sets)
                v1 = chosen['v1']
                v2 = chosen['v2']
                d1 = chosen['d1']
                d2 = chosen['d2']
                L = chosen['L']
                start_h = chosen['start_h']

                # Giải phương trình tìm x (thời gian di chuyển)
                x_sym = symbols('x')
                eq = (v1*x_sym + d1)**2 + (v2*x_sym + d2)**2 - L**2
                sol = solve(eq, x_sym)

                # Lấy nghiệm dương
                x_val = [s for s in sol if s > 0][0]

                # Tính toán thời gian
                total_minutes = int(x_val * 60)
                h_move = total_minutes // 60
                m_move = total_minutes % 60

                final_h = start_h + h_move
                a_val = m_move # Giá trị a cần tìm theo đề bài

                # Đáp án đúng
                da = '$%s$' % (latex(a_val))

                # Tạo các đáp án sai không trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    fake = a_val + random.choice([-5, -2, 2, 5, 8, 10, 15])
                    if fake > 0 and fake < 60 and fake != a_val:
                        s.add('$%s$' % (latex(fake)))

                list_s = list(s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Lúc $%s$ giờ sáng, hai ô tô cùng xuất phát tại vị trí $A$ và vị trí $B$ cách nhau $%s$ km chạy về thành phố $T$. Vận tốc của hai ô tô chạy từ vị trí $A$ và vị trí $B$ lần lượt là $%s$ km/h và $%s$ km/h. Biết rằng tại thời điểm ô tô đi từ vị trí $A$ đến địa điểm $D$ cách thành phố $T$ là $%s$ km thì ô tô đi từ vị trí $B$ đến địa điểm $C$ cách thành phố $T$ là $%s$ km. Thời điểm đó là $a$ giờ $b$ phút. Giá trị của $b$ bằng bao nhiêu?'''
                                 % (latex(start_h), latex(L), latex(v1), latex(v2), latex(d1), latex(d2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $x$ (giờ) là thời gian ô tô đi từ vị trí $A$ đến địa điểm $D (x > 0)$. Vì hai ô tô xuất phát cùng một lúc nên thời gian ô tô đi từ vị trí $B$ đến địa điểm $C$ cũng là $x$ giờ. \\\\
                            Do đó, quãng đường $AD$ và $BC$ lần lượt là $%sx$ (km) và $%sx$ (km). \\\\
                            Suy ra khoảng cách từ vị trí $A$ và vị trí $B$ đến thành phố $T$ lần lượt là $%sx + %s$ (km) và $%sx + %s$ (km). \\\\
                            Vì khoảng cách giữa hai vị trí $A$ và $B$ là $%s$ km nên ta có phương trình: \\\\
                            $\\sqrt{(%sx + %s)^2 + (%sx + %s)^2} = %s \\Rightarrow %sx^2 + %sx + %s = %s$. \\\\
                            Giải phương trình này và kết hợp với điều kiện $x > 0$, ta nhận $x = %s$. \\\\
                            Đổi: $%s$ giờ = $%s$ giờ $%s$ phút. \\\\
                            Vậy thời điểm ô tô đi từ vị trí $A$ đến địa điểm $D$ là: \\\\
                            $%s$ giờ + $%s$ giờ $%s$ phút = $%s$ giờ $%s$ phút. \\\\
                            Vậy $b = %s$.'''
                           % (latex(v1), latex(v2), 
                              latex(v1), latex(d1), latex(v2), latex(d2), 
                              latex(L),
                              latex(v1), latex(d1), latex(v2), latex(d2), latex(L),
                              latex(v1**2 + v2**2), latex(2*(v1*d1 + v2*d2)), latex(d1**2 + d2**2), latex(L**2),
                              latex(x_val), 
                              latex(x_val), latex(h_move), latex(m_move),
                              latex(start_h), latex(h_move), latex(m_move), latex(final_h), latex(m_move),
                              latex(a_val)
                           ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(a_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

