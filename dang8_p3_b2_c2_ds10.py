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


def bt_dang8_p3_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo loại bài toán
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B1: Random thông số bài toán ---
                # Thiết lập hệ số cố định để đảm bảo hình dáng miền nghiệm ổn định
                # d1: a1*x + a2*y <= max_n
                # d2: b1*x + b2*y <= max_b
                a1, a2 = 3, 4
                b1, b2 = 1, 2

                # Random điểm giao B(x0, y0) nguyên để bài toán "đẹp"
                x0 = random.randint(15, 25) # Gốc 20
                y0 = random.randint(30, 40) # Gốc 35

                # Tính toán giới hạn tài nguyên dựa trên điểm giao
                max_n = a1 * x0 + a2 * y0
                max_b = b1 * x0 + b2 * y0

                # Giá tiền
                p1 = random.randint(40, 50) 
                p2 = random.randint(65, 75)

                # --- B2: Xác định các đỉnh của miền nghiệm ---
                # Đỉnh O(0,0)
                # Đỉnh A trên trục Oy: min(max_n/a2, max_b/b2)
                val_A = min(max_n / a2, max_b / b2)
                # Đỉnh C trên trục Ox: min(max_n/a1, max_b/b1)
                val_C = min(max_n / a1, max_b / b1)

                # Giá trị hàm mục tiêu F = p1*x + p2*y
                f_O = 0
                f_A = int(p2 * val_A)
                f_B = p1 * x0 + p2 * y0
                f_C = int(p1 * val_C)

                kq_num = max(f_O, f_A, f_B, f_C)
                kq = str(kq_num).replace('.', ',')

                # --- B3: Tạo TikZ String ---
                # Tính toán giới hạn vẽ để hình không bị cắt
                xlim = float(val_C) + 15
                ylim = float(val_A) + 15

                tikz_code = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.08, line width=1pt]
            \\draw[->] (-10, 0) -- ({xlim}, 0) node[below] {{$x$}};
            \\draw[->] (0, -10) -- (0, {ylim}) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};
            \\clip (-10,-10) rectangle ({xlim - 5},{ylim - 5});
            \\fill[pattern=north east lines, pattern color=black] (-10,-10) rectangle ({xlim - 5},{ylim - 5});
            \\fill[white] (0,0) -- (0,{val_A}) -- ({x0},{y0}) -- ({val_C},0) -- cycle;
            \\draw[black] (-10,0) -- ({xlim},0); 
            \\draw[black] (0,-10) -- (0,{ylim});
            \\draw[black, smooth, domain=-5:{xlim}] plot(\\x, {{-({a1}/{a2})*\\x + {max_n}/{a2}}});
            \\draw[black, smooth, domain=-5:{xlim}] plot(\\x, {{-({b1}/{b2})*\\x + {max_b}/{b2}}});
            \\coordinate (A) at (0,{val_A});
            \\coordinate (B) at ({x0},{y0});
            \\coordinate (C) at ({val_C},0);
            \\fill (0,0) circle (0.5pt);
            \\fill (A) circle (0.5pt) node[above right] {{$A$}};
            \\fill (B) circle (0.5pt) node[above right] {{$B$}};
            \\fill (C) circle (0.5pt) node[above right] {{$C$}};
            \\draw[dashed, thin] ({x0},0) node[below] {{${x0}$}} -- (B) -- (0,{y0}) node[left] {{${y0}$}};
            \\node[left] at (A) {{${latex(val_A)}$}};
            \\node[below] at (C) {{${latex(val_C)}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''

                # --- B4: Nội dung câu hỏi và lời giải ---
                noidungcauhoi = ('''Để gây quỹ từ thiện, câu lạc bộ thiện nguyện của một trường THPT tổ chức hoạt động bán hàng với hai mặt hàng là nước và bánh. Câu lạc bộ thiết kế hai thực đơn. Thực đơn 1 có giá $%s$ nghìn đồng, bao gồm $%s$ chai nước và $%s$ hộp bánh. Thực đơn 2 có giá $%s$ nghìn đồng, bao gồm $%s$ chai nước và $%s$ hộp bánh. Biết rằng câu lạc bộ chỉ có không quá $%s$ chai nước và $%s$ hộp bánh. Số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng bằng bao nhiêu nghìn đồng?'''
                                 %(latex(p1), latex(a1), latex(b1), 
                                   latex(p2), latex(a2), latex(b2),
                                   latex(max_n), latex(max_b)))

                loigiai = ('''Gọi $x, y$ lần lượt là số lượng thực đơn 1 và thực đơn 2 được bán ra $\\left( x, y \\in \\mathbb{N} \\right)$.\\\\
                             Theo bài ra, ta có hệ bất phương trình giới hạn tài nguyên là:
                             $\\begin{cases} %sx + %sy \\le %s \\\\ x + %sy \\le %s \\\\ x \\ge 0, y \\ge 0 \\end{cases}$.\\\\
                             Số tiền thu được là $F(x;y) = %sx + %sy$ (nghìn đồng).\\\\
                             Miền nghiệm của hệ bất phương trình là miền tứ giác $OABC$ (kể cả biên) như hình vẽ sau:
                             %s
                             Tọa độ các đỉnh là: $O(0;0)$, $A(0;%s)$, $B(%s;%s)$, $C\\left(\\frac{%s}{%s};0\\right)$.\\\\
                             Tính giá trị của $F(x;y)$ tại các đỉnh:\\\\
                             $F(0;0) = 0$.\\\\
                             $F(0;%s) = %s \\cdot %s = %s$.\\\\
                             $F(%s;%s) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
                             Tại điểm $C\\left(\\frac{%s}{%s};0\\right)$, do $x$ nguyên nên ta xét điểm nguyên gần nhất là \\\\$x = %s$: $F(%s;0) = %s \\cdot %s = %s$.\\\\
                             So sánh các giá trị trên, ta thấy số tiền lớn nhất thu được là $%s$ nghìn đồng.'''
                           %(latex(a1), latex(a2), latex(max_n), 
                             latex(b2), latex(max_b),
                             latex(p1), latex(p2),
                             tikz_code,
                             latex(val_A), latex(x0), latex(y0), latex(max_n), latex(a1),
                             latex(val_A), latex(p2), latex(val_A), latex(f_A),
                             latex(x0), latex(y0), latex(p1), latex(x0), latex(p2), latex(y0), latex(f_B),
                             latex(max_n), latex(a1), latex(int(val_C)), latex(int(val_C)), latex(p1), latex(int(val_C)), latex(f_C),
                             latex(kq)))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

                # --- B5: Đáp án ---
                s_set = set()
                while len(s_set) < 3:
                    sai = kq_num + random.choice([-200, -100, 100, 200, 300])
                    if sai != kq_num and sai > 0:
                        s_set.add(sai)

                list_sai = [str(s).replace('.', ',') for s in s_set]
                da_d = '\\True $' + kq + '$'
                list_1 = [da_d]
                for s in list_sai:
                    list_1.append('$' + s + '$')
                random.shuffle(list_1)

            # --- B6: Xuất bản ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

