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


def bt_dang8_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các số liệu trong bài
                t_0 = random.choice([3, 4, 5, 6]) # Thời gian mở cửa xả lũ (giờ)
                y_0 = randint(1, 2)               # Lưu lượng lúc đầu và lúc cuối (nghìn m^3/s)
                y_max = y_0 + randint(2, 4)       # Lưu lượng cực đại (nghìn m^3/s)

                # Tính toán chính xác các hệ số a, b, c
                a_val = Rational(-27 * (y_max - y_0), 4 * t_0**3)
                b_val = -t_0 * a_val
                c_val = Rational(y_0, 1)

                # Tùy chỉnh các hệ số M, N sao cho T = Ma + Nb + c luôn là số nguyên đẹp (sử dụng thủ thuật M = t_0 * N)
                k = random.choice([50, 100, 200])
                N = k
                M = k * t_0

                # Giá trị của biểu thức T
                T_val = M * a_val + N * b_val + c_val

                # Tạo chuỗi cho đồ thị TikZ
                t_max_f = 2.0 * t_0 / 3.0
                t_max_str = latex(Rational(2*t_0, 3))
                a_f = float(a_val)
                b_f = float(b_val)
                c_f = float(c_val)

                tikz_str = ('''\\begin{center}
            \\begin{tikzpicture}[>=stealth, x=1.5cm, y=1.0cm, scale=0.8]
            \\draw[->] (-0.5,0) -- (%s,0) node[below] {$t$};
            \\draw[->] (0,-0.5) -- (0,%s) node[right] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\draw[domain=0:%s, smooth, variable=\\x, thick] plot ({\\x}, {%s*\\x*\\x*\\x + %s*\\x*\\x + %s});
            \\draw[dashed] (0,%s) node[left]{$%s$} -- (%s,%s) -- (%s,0) node[below]{$%s$};
            \\draw[dashed] (0,%s) node[left]{$%s$} -- (%s,%s) -- (%s,0) node[below]{$%s$};
            \\fill (0,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (
                    t_0 + 1.2, y_max + 1,
                    t_0, a_f, b_f, c_f,
                    y_max, y_max, t_max_f, y_max, t_max_f, t_max_str,
                    y_0, y_0, t_0, y_0, t_0, t_0,
                    y_0, t_max_f, y_max, t_0, y_0
                ))

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (T_val)]
                da = random.choice(du)

                s = [
                    '$%s$' % (T_val + 1),
                    '$%s$' % (T_val - 1) if T_val > 1 else '$%s$' % (T_val + 3),
                    '$%s$' % (T_val + 2),
                    '$%s$' % (T_val + 4),
                    '$%s$' % (y_max),
                    '$%s$' % (T_val * 2)
                ]
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Nhằm điều tiết mực nước của hồ chứa trong những ngày mưa lớn, một hồ thủy điện thông báo mở cửa xả lũ trong $%s$ giờ, bắt đầu từ thời điểm $0$ giờ. Lưu lượng nước xả lũ là lượng nước hồ thủy điện xả về hạ lưu trên mỗi đơn vị thời gian, được ước tính bởi hàm số $f(t) = at^3 + bt^2 + c$ (đơn vị nghìn $m^3/s$), trong đó $t$ được tính bằng đơn vị giờ, là thời gian từ $0$ giờ đến $%s$ giờ. Tại thời điểm $0$ giờ, lưu lượng nước xả về hạ lưu là $%s$ nghìn $m^3/s$ và bắt đầu tăng cho đến khi đạt cực đại bằng $%s$ nghìn $m^3/s$ thì lưu lượng nước giảm dần, đến thời điểm $%s$ giờ thì trở về lại $%s$ nghìn $m^3/s$. Hàm số $y = f(t)$ có đồ thị như hình vẽ dưới đây.
            %s
            Giá trị của biểu thức $T = %sa + %sb + c$ bằng bao nhiêu?''' % (
                    t_0, t_0, y_0, y_max, t_0, y_0, tikz_str, M, N
                ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $f(0) = c = %s$.\\\\
            Đạo hàm $f'(t) = 3at^2 + 2bt = t(3at + 2b)$.\\\\
            Theo giả thiết, tại thời điểm $t = %s$ thì lưu lượng trở về $%s$ nên:
            $$f(%s) = a \\cdot %s^3 + b \\cdot %s^2 + %s = %s \\Rightarrow %s a + %s b = 0 \\Rightarrow b = -%s a.$$
            Hàm số đạt cực đại khi $f'(t) = 0 \\Rightarrow t = -\\frac{2b}{3a} = -\\frac{2(-%s a)}{3a} = %s$.\\\\
            Lưu lượng cực đại bằng $%s$ nên $f\\left(%s\\right) = %s$:
            $$a \\left(%s\\right)^3 + b \\left(%s\\right)^2 + %s = %s \\Rightarrow a = %s \\Rightarrow b = %s.$$
            Vậy $T = %sa + %sb + c = %s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) + %s = %s$.''' % (
                    y_0,
                    t_0, y_0,
                    t_0, t_0, t_0, y_0, y_0, t_0**3, t_0**2, t_0,
                    t_0, t_max_str,
                    y_max, t_max_str, y_max,
                    t_max_str, t_max_str, y_0, y_max, latex(a_val), latex(b_val),
                    M, N, M, latex(a_val), N, latex(b_val), y_0, T_val
                ))
            dapan='\\shortans[0]{$%s$}\n'%(T_val)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

