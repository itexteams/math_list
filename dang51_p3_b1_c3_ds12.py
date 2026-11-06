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


def bt_dang51_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ cấu hình: (S, P0, t1, P1, P2)
                # Tương ứng: Tổng SV, Số SV ban đầu, Thời gian t1, Số cài đặt ở t1, Số cài đặt cần đạt ở t2
                # Các thông số được chọn cẩn thận để ra nghiệm nguyên và logarit chẵn đẹp
                configs = [
                    (1000, 100, 5, 500, 900),
                    (2000, 200, 4, 1000, 1800),
                    (1000, 50, 4, 500, 950),
                    (5000, 1000, 3, 2500, 4000),
                    (2000, 500, 6, 1000, 1500),
                    (3000, 300, 5, 1500, 2700)
                ]

                S, P0, t1, P1, P2 = random.choice(configs)

                # Tính toán hằng số C
                C_num = P0
                C_den = S - P0
                gcd = math.gcd(C_num, C_den)
                C_num //= gcd
                C_den //= gcd

                if C_den == 1:
                    C_str = str(C_num)
                else:
                    C_str = "\\frac{%s}{%s}" % (C_num, C_den)

                # Tính toán các giá trị bên trong ln(...)
                # E1 = e^{rt_1}
                # Do các config đều thiết kế P1 = S/2 nên P1/(S-P1) = 1.
                E1 = C_den # E1 = 1 / C

                # E2 = e^{rt_2}
                L2_num = P2
                L2_den = S - P2
                L2_val = L2_num // L2_den 
                E2 = L2_val * C_den

                # Tỉ lệ K = ln(E2) / ln(E1). Các bộ số đều thỏa mãn E2 = (E1)^2 nên tỉ lệ luôn là 2
                K = 2 
                t2 = t1 * K

                # Các đáp án trắc nghiệm
                du = ['$%s$' % t2]
                da = du[0]

                # Random phương án sai
                s_options = set([
                    '$%s$' % (t2 + 1),
                    '$%s$' % (t2 + 2),
                    '$%s$' % (t2 + 3),
                    '$%s$' % (t2 - 1),
                    '$%s$' % (t2 - 2),
                    '$%s$' % (t2 + 4),
                    '$%s$' % (t2 + 5)
                ])
                if da in s_options:
                    s_options.remove(da)
                s_list = list(s_options)

                das1 = random.choice(s_list)
                s_list.remove(das1)
                das2 = random.choice(s_list)
                s_list.remove(das2)
                das3 = random.choice(s_list)

                # Câu hỏi
                noidungcauhoi = '''Trong một ký túc xá sinh viên công nghệ có tổng cộng $%s$ sinh viên. Một nhóm sinh viên khởi nghiệp tung ra một ứng dụng mới dành riêng cho khu ký túc xá này. Giả sử tốc độ lan truyền của ứng dụng (tốc độ tăng số người cài đặt) tại mọi thời điểm luôn tỷ lệ thuận với tích của số người đã cài đặt và số người chưa cài đặt. Ban đầu, nhóm phát triển cài đặt trước ứng dụng cho $%s$ sinh viên nòng cốt để dùng thử. Sau $%s$ ngày, nhờ hiệu ứng truyền miệng nên số người cài đặt đã tăng lên đến $%s$ sinh viên. Hỏi sau bao nhiêu ngày (tính từ thời điểm ban đầu) thì số lượng người cài đặt ứng dụng sẽ đạt con số $%s$ sinh viên?''' % (S, P0, t1, P1, P2)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = '''Gọi $P(t)$ là số người cài đặt sau $t$ ngày và theo đề bài, tổng số sinh viên $S = %s$ sinh viên.\\\\
            Từ yêu cầu bài toán ta có : $\\frac{\\text{d}P}{\\text{d}t} = kP(S - P)(*)$\\\\
            Từ $(*) \\Leftrightarrow \\frac{\\text{d}P}{P(S - P)} = k\\text{d}t$ , ta lấy nguyên hàm cả hai vế :\\\\
            $\\Leftrightarrow \\int \\frac{\\text{d}P}{P(S - P)} = \\int k\\text{d}t \\Leftrightarrow \\frac{1}{S} \\int \\left( \\frac{1}{P} + \\frac{1}{S - P} \\right) \\text{d}P = kt + C \\Leftrightarrow \\ln\\left| \\frac{P}{S - P} \\right| = Skt + C_1$\\\\
            Đặt $C = e^{C_1}$ và $r = Sk$ , ta có công thức nghiệm tổng quát : $\\frac{P(t)}{S - P(t)} = e^{rt} \\cdot C$\\\\
            Tại $t = 0$ thì ta có $P(0) = %s \\Leftrightarrow \\frac{%s}{%s - %s} = C \\cdot e^0 \\Rightarrow C = %s \\Rightarrow \\frac{P(t)}{%s - P(t)} = %s e^{rt}$\\\\
            Tại $t = %s$ thì ta có $P(%s) \\Leftrightarrow \\frac{%s}{%s - %s} = %s \\cdot e^{%sr} \\Rightarrow %sr = \\ln(%s) \\quad (1)$\\\\
            Tìm thời gian để $P(t) = %s \\Leftrightarrow \\frac{%s}{%s - %s} = %s \\cdot e^{rt} \\Rightarrow rt = \\ln(%s) \\quad (2)$\\\\
            Lấy $\\frac{(2)}{(1)} \\Leftrightarrow \\frac{rt}{%sr} = \\frac{\\ln(%s)}{\\ln(%s)} \\Rightarrow \\frac{t}{%s} = %s \\Rightarrow t = %s$ ngày.''' % (
                    S,
                    P0, P0, S, P0, C_str, S, C_str,
                    t1, t1, P1, S, P1, C_str, t1, t1, E1,
                    P2, P2, S, P2, C_str, E2,
                    t1, E2, E1, t1, K, t2
                )
                dapan='\\shortans[0]{$%s$}\n'%(t2)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content  

