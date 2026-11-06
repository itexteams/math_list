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


def bt_dang7_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp để đảm bảo u1 != 0 và M2 KHÔNG thuộc Delta_1
                while True:
                    # 1. Ngẫu nhiên hóa VTCP u1(a1, b1, c1)
                    # Đảm bảo a1, b1, c1 khác 0 để có phương trình chính tắc
                    a1 = choice([-3, -2, -1, 1, 2, 3])
                    b1 = choice([-3, -2, -1, 1, 2, 3])
                    c1 = choice([-3, -2, -1, 1, 2, 3])

                    # 2. Ngẫu nhiên hóa Điểm M1 và M2
                    x1, y1, z1 = randint(-4, -1), randint(1, 4), randint(1, 4)
                    x2, y2, z2 = randint(1, 4), randint(-4, -1), randint(-4, -1)

                    # 3. Kiểm tra M2 KHÔNG thuộc Delta_1 (M2 không nằm trên Delta_1)
                    # Tính các tử số của tham số t
                    tx_num = x2 - x1
                    ty_num = y2 - y1
                    tz_num = z2 - z1

                    # Tính các tỉ số t_x, t_y, t_z (sử dụng float để so sánh)
                    tx = Rational(tx_num , a1)
                    ty = Rational(ty_num , b1)
                    tz = Rational(tz_num , c1)

                    # Điều kiện M2 KHÔNG thuộc Delta_1: Các tỉ số không bằng nhau
                    # Chỉ cần tx khác ty (hoặc tx khác tz, ty khác tz)
                    # Dùng abs(t1 - t2) > 1e-6 để so sánh số thực
                    if abs(tx - ty) > 1e-6 or abs(ty - tz) > 1e-6:
                         break # Thoát vòng lặp khi điều kiện song song được đảm bảo

                # 4. Ngẫu nhiên hóa VTCP u2 và tính m
                k = choice([-2, -1, 1, 2]) # Hệ số tỉ lệ u2 = k * u1

                # Giả sử m nằm ở tọa độ z của u2
                a2_val = k * a1
                b2_val = k * b1
                kq = k * c1 # Giá trị của m (đáp án đúng)

                # VTCP u2: (a2, b2, m)
                a2, b2, m_val = a2_val, b2_val, kq

                # Các đáp án trắc nghiệm
                du = [str(kq)]
                da= random.choice(du)

                s_list = list(range(kq - 3, kq)) + list(range(kq + 1, kq + 4))
                s = [str(x) for x in set(s_list) if x != kq]
                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                # Dấu cho pt Delta_1
                y1_sign = '+' if y1 < 0 else '-'
                z1_sign = '+' if z1 < 0 else '-'

                pt_D1 = '\\frac{x %s %s}{%s} = \\frac{y %s %s}{%s} = \\frac{z %s %s}{%s}'%(
                    '-' if x1 > 0 else '+', latex(abs(x1)), latex(a1), 
                    y1_sign, latex(abs(y1)), latex(b1), 
                    z1_sign, latex(abs(z1)), latex(c1)
                )

                # Dấu cho pt Delta_2
                a2_sign = '+' if a2_val > 0 else '-'
                b2_sign = '+' if b2_val > 0 else '-'

                # SỬA LỖI TẠI ĐÂY: Đảm bảo đủ 6 placeholder
                pt_D2 = '\\begin{cases} x = %s %s %s t \\\\ y = %s %s %s t \\\\ z = %s + mt \\end{cases}'%(
                    latex(x2), a2_sign, latex(abs(a2_val)), # 3 placeholders cho dòng x
                    latex(y2), b2_sign, latex(abs(b2_val)), # 3 placeholders cho dòng y
                    latex(z2) # Dòng z: z = z2 + mt -> cần 1 placeholder cho z2
                )

                noidungcauhoi = ('''Trong không gian $Oxyz$, cho hai đường thẳng \\begin{center} $\\Delta_1: %s$ và
                                 $\\Delta_2: %s$ \\end{center}
                                 Giá trị của $m$ để hai đường thẳng $\\Delta_1$ và $\\Delta_2$ song song bằng bao nhiêu?'''
                                  %(pt_D1, pt_D2
                                  ))


                # Nội dung lời giải
                loigiai=('''Đường thẳng $\\Delta_1$ đi qua điểm $M_1(%s;%s;%s)$ có vectơ chỉ phương là $\\vec{u}_1(%s;%s;%s)$.\\\\
                            Đường thẳng $\\Delta_2$ đi qua điểm $M_2(%s;%s;%s)$ có vectơ chỉ phương là $\\vec{u}_2(%s;%s;m)$.\\\\
                            Điều kiện để $\\Delta_1 // \\Delta_2$ là $\\vec{u}_1$ cùng phương với $\\vec{u}_2$ (tức $\\vec{u}_2 = k\\vec{u}_1$) và $M_2 \\notin \\Delta_1$.
                            Điều kiện cùng phương:
                            $$\\frac{a_2}{a_1} = \\frac{b_2}{b_1} = \\frac{m}{c_1} \\Leftrightarrow  \\frac{%s}{%s} = \\frac{%s}{%s} = \\frac{m}{%s}$$
                            Từ hai tỉ lệ đầu tiên ta có hệ số tỉ lệ $k = \\frac{%s}{%s} = %s$.
                            Áp dụng cho tỉ lệ cuối ta có:
                            $$m = k \\cdot (%s) = %s \\cdot (%s) = %s.$$
                            Kiểm tra $M_2 \\notin \\Delta_1$:
                            Thế tọa độ $M_2(%s;%s;%s)$ vào phương trình $\\Delta_1$, ta được các tham số $t$ khác nhau:
                            $$t_x = \\frac{%s - %s}{%s} = %s \\quad ; \\quad t_y = \\frac{%s - %s}{%s} = %s \\quad ; \\quad t_z = \\frac{%s - %s}{%s} = %s$$
                            (Vì $t_x \\neq t_y$ hoặc các tỉ số khác nhau) nên $M_2 \\notin \\Delta_1$.
                            Vậy giá trị $m$ cần tìm là $m=%s$.'''
                        %(latex(x1),latex(y1),latex(z1), latex(a1),latex(b1),latex(c1),
                          latex(x2),latex(y2),latex(z2), latex(a2),latex(b2),
                          latex(a2),latex(a1),latex(b2),latex(b1),latex(c1),
                          latex(a2),latex(a1),latex(k),
                          latex(c1),latex(k),latex(c1),latex(kq),
                          latex(x2),latex(y2),latex(z2),
                          latex(x2),latex(x1),latex(a1), latex(tx),
                          latex(y2),latex(y1),latex(b1), latex(ty),
                          latex(z2),latex(z1),latex(c1), latex(tz),
                          latex(kq)
                        ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content    

