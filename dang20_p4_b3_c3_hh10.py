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


def bt_dang20_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, y, t = symbols('x y t')

            def solve_for_rational():
                while True:
                    # --- B3: Ngẫu nhiên hóa ---
                    k = random.choice([1, 2, 3, 5]) 
                    m = random.randint(-5, 5)
                    xa, ya = random.randint(-8, -4), random.randint(-3, 2)
                    x0, y0 = random.randint(-3, 3), random.randint(-3, 5)
                    R2 = random.choice([5, 10, 13, 17, 20, 25, 26, 34, 40, 50])

                    # Thiết lập phương trình tham số
                    xN_expr = k*t + m
                    yN_expr = t
                    xM_expr = 2*xa - xN_expr
                    yM_expr = 2*ya - yN_expr

                    # Phương trình: (xM - x0)**2 + (yM - y0)**2 - R2 = 0
                    pt = (xM_expr - x0)**2 + (yM_expr - y0)**2 - R2
                    pt_expand = expand(pt)

                    # Lấy hệ số và ép kiểu về int để tính delta chuẩn Python
                    a = int(pt_expand.coeff(t, 2))
                    b = int(pt_expand.coeff(t, 1))
                    c = int(pt_expand.coeff(t, 0))

                    delta = b**2 - 4*a*c

                    # Điều kiện nghiệm hữu tỷ: Delta > 0 và Delta là số chính phương
                    if delta > 0:
                        can_delta = int(math.sqrt(delta))
                        if can_delta * can_delta == delta:
                            return k, m, xa, ya, x0, y0, R2, xN_expr, yN_expr, xM_expr, yM_expr, pt_expand

            # Khởi tạo bộ số đẹp
            k, m, xa, ya, x0, y0, R2, xN_expr, yN_expr, xM_expr, yM_expr, pt_rut_gon = solve_for_rational()

            # Giải tìm t
            sols_t = solve(pt_rut_gon, t)

            # Hàm làm sạch dấu theo yêu cầu
            def clean_tex(expr):
                s = latex(expr)
                s = s.replace('+ -', '-').replace('- -', '+')
                return s

            # --- B1 & B2: Nội dung đề bài và lời giải ---

            noidungcauhoi = (r'''Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường tròn $(C): %s = %s$ và đường thẳng $d: %s = 0$. Tìm trên $(C)$ điểm $M$ và trên $d$ điểm $N$ sao cho hai điểm $M, N$ đối xứng nhau qua điểm $A(%s; %s)$.'''
                            % (clean_tex((x - x0)**2 + (y - y0)**2), latex(R2), 
                               clean_tex(x - k*y - m), latex(xa), latex(ya)))

            loigiai = (r'''Do $N \in d$ nên $N(%s; t)$. Điểm $M$ đối xứng với $N$ qua $A$, suy ra $M(%s; %s)$. \\ 
            Mặt khác $M \in (C)$, nên: \\
            $(%s)^2 + (%s)^2 = %s$ \\
            $\Leftrightarrow %s = 0$ \\''' 
                      % (clean_tex(xN_expr), clean_tex(xM_expr), clean_tex(yM_expr),
                         clean_tex(xM_expr - x0), clean_tex(yM_expr - y0), latex(R2),
                         clean_tex(pt_rut_gon)))

            # Hiển thị t
            t_tex = " \\text{ hoặc } ".join([ "t = " + latex(val) for val in sols_t])
            loigiai += r"$\Leftrightarrow %s$. \\ " % t_tex

            pairs = []
            for val_t in sols_t:
                ptN = (xN_expr.subs(t, val_t), yN_expr.subs(t, val_t))
                ptM = (xM_expr.subs(t, val_t), yM_expr.subs(t, val_t))
                pairs.append("M(%s; %s), N(%s; %s)" % (latex(ptM[0]), latex(ptM[1]), latex(ptN[0]), latex(ptN[1])))

            da_dung = " \\text{ hoặc } ".join(pairs)
            loigiai += "Vậy có hai cặp điểm cần tìm là $%s$." % da_dung

            # Tạo danh sách đáp án
            da_d = '\\True $' + da_dung + '$'
            da_s1 = '$M(0; 0), N(1; 1)$'
            da_s2 = '$M(2; 3), N(-4; -5)$'
            da_s3 = 'Không có cặp điểm nào thỏa mãn'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

