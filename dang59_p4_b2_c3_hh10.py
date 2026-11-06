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


def bt_dang59_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            m = symbols('m')

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo các giá trị ngẫu nhiên
                # Đường thẳng d: x - ky*y - kc = 0 => x = ky*m + kc
                ky = random.randint(1, 3) 
                kc = random.randint(-3, 3)

                # Tọa độ điểm A và B
                xa, ya = random.randint(-5, 5), random.randint(-5, 5)
                xb, yb = random.randint(-5, 5), random.randint(-5, 5)

                # Hệ số k trong MA^2 - k*MB^2 (Chọn k > 1 để biểu thức có cực đại)
                he_so_k = random.randint(2, 3)

                # 2. Thiết lập biểu thức tọa độ tham số
                # M(ky*m + kc; m)
                xm = ky * m + kc
                ym = m

                # MA^2 = (xa - xm)^2 + (ya - ym)^2
                ma2 = expand((xa - xm)**2 + (ya - ym)**2)
                # MB^2 = (xb - xm)**2 + (yb - ym)**2
                mb2 = expand((xb - xm)**2 + (yb - ym)**2)

                # Biểu thức P = MA^2 - k*MB^2
                P = expand(ma2 - he_so_k * mb2)

                # Tìm đỉnh của parabol (giá trị m để P lớn nhất)
                # P có dạng Am^2 + Bm + C
                coeff_A = P.coeff(m, 2)
                coeff_B = P.coeff(m, 1)
                coeff_C = P.coeff(m, 0)

                m_max = Rational(-coeff_B, 2 * coeff_A)
                P_max = P.subs(m, m_max)

                # Tọa độ điểm M tương ứng
                xm_val = ky * m_max + kc
                ym_val = m_max

                # 3. Tạo các đáp án trắc nghiệm
                da_dung = 'M\\left(%s; %s\\right)' % (latex(xm_val), latex(ym_val))

                # Tạo các đáp án nhiễu
                s = []
                # Nhiễu 1: Đổi dấu tọa độ
                s.append('M\\left(%s; %s\\right)' % (latex(-xm_val), latex(-ym_val)))
                # Nhiễu 2: Thay đổi giá trị m khác
                m_sai1 = m_max + random.randint(1, 2)
                s.append('M\\left(%s; %s\\right)' % (latex(ky * m_sai1 + kc), latex(m_sai1)))
                # Nhiễu 3: Một điểm ngẫu nhiên khác trên d
                m_sai2 = m_max - random.randint(1, 2)
                s.append('M\\left(%s; %s\\right)' % (latex(ky * m_sai2 + kc), latex(m_sai2)))

                # Đảm bảo các đáp án không trùng nhau
                s = list(set(s))
                while len(s) < 3:
                    m_random = random.randint(-5, 5)
                    s.append('M\\left(%s; %s\\right)' % (latex(ky * m_random + kc), latex(m_random)))
                    s = list(set(s))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # 4. Nội dung câu hỏi
                # Đường thẳng d: x - ky*y - kc = 0
                str_d = 'x'
                if ky == 1: str_d += ' - y'
                else: str_d += ' - %sy' % ky
                if kc > 0: str_d += ' - %s = 0' % kc
                elif kc < 0: str_d += ' + %s = 0' % abs(kc)
                else: str_d += ' = 0'

                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d: %s$ và hai điểm $A(%s; %s)$, $B(%s; %s)$. Tìm điểm $M$ thuộc $d$ sao cho $MA^2 - %sMB^2$ lớn nhất.'''
                                 % (str_d, xa, ya, xb, yb, he_so_k))

                # 5. Nội dung lời giải
                # Vector MA, MB
                # MA = (xa - (ky*m+kc); ya - m)
                v_ma_x = simplify(xa - (ky*m + kc))
                v_ma_y = simplify(ya - m)
                v_mb_x = simplify(xb - (ky*m + kc))
                v_mb_y = simplify(yb - m)

                loigiai = ('''Điểm $M \\in d$ nên có tọa độ dạng $M(%s m %s; m)$. \\\\
                             Ta có $\\overrightarrow{MA} = (%s; %s)$, suy ra $MA^2 = (%s)^2 + (%s)^2$; \\\\
                             $\\overrightarrow{MB} = (%s; %s)$, suy ra $%sMB^2 = %s \\left[ (%s)^2 + (%s)^2 \\right]$. \\\\
                             Do đó: $MA^2 - %sMB^2 = %s = %s \\left( m - %s \\right)^2 + %s \\leq %s$. \\\\
                             Dấu "$=$" xảy ra khi và chỉ khi $m = %s$. \\\\
                             Vậy $MA^2 - %sMB^2$ đạt giá trị lớn nhất bằng $%s$ khi $M\\left( %s; %s \\right)$.'''
                           % (latex(ky) if ky != 1 else "", 
                              "+ " + str(kc) if kc > 0 else (str(kc) if kc < 0 else ""),
                              latex(v_ma_x), latex(v_ma_y), latex(v_ma_x), latex(v_ma_y),
                              latex(v_mb_x), latex(v_mb_y), he_so_k, he_so_k, latex(v_mb_x), latex(v_mb_y),
                              he_so_k, latex(P), latex(coeff_A), latex(m_max), latex(P_max), latex(P_max),
                              latex(m_max), he_so_k, latex(P_max), latex(xm_val), latex(ym_val)
                            ))

                # 6. Xuất nội dung
                da_d = ('\\True $' + str(da_dung) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content 

