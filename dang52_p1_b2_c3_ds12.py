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


def bt_dang52_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random tọa độ đỉnh I(xI; yI) và điểm đi qua A(0; yA)
                # Để đồ thị giống hình (parabol quay xuống), chọn yI > yA
                xI = random.randint(2, 3) 
                yI = random.randint(8, 12)
                yA = random.randint(4, 7)
                T = random.randint(3, 4) # Thời gian xét (trong hình là 3)

                t_sym = symbols('t')

                # Tìm hàm v(t) = a(t - xI)^2 + yI
                # Tại t = 0, v(0) = yA => yA = a(0 - xI)^2 + yI => a = (yA - yI) / xI^2
                a = Rational(yA - yI, xI**2)
                v_func = simplify(a * (t_sym - xI)**2 + yI)

                # Khai triển v(t) = at^2 + bt + c để giống mẫu lời giải
                c_val = yA
                b_val = -2 * a * xI
                a_val = a

                # --- B2: Viết lại bài toán và tính toán ---
                # Tính quãng đường S = tích phân từ 0 đến T của v(t)
                S_expr = integrate(v_func, (t_sym, 0, T))
                kq_num = float(S_expr)

                # Định dạng kết quả (lấy 2 chữ số thập phân nếu lẻ, dùng dấu phẩy cho thập phân)
                kq_str = str(round(kq_num, 2)).replace('.', ',')

                # Tạo các phương án sai (không trùng đáp án đúng)
                da_dung = f"${kq_str}$"

                s_list = []
                while len(s_list) < 3:
                    sai = round(kq_num + random.choice([-2.5, -1.25, 1.5, 2.75, 3.2, -3.1]), 2)
                    sai_str = f"${str(sai).replace('.', ',')}$"
                    if sai_str != da_dung and sai_str not in s_list:
                        s_list.append(sai_str)

                # TikZ code cho hình vẽ
                # Tính tọa độ y tại t=T để vẽ đường dóng
                yT = float(v_func.subs(t_sym, T))

                tikz_code = r"""\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-0.5,0) -- (%s,0) node[below] {$t$};
                \draw[->] (0,-0.5) -- (0, %s) node[left] {$v$};
                \draw (0,0) node[below left] {$O$};
                \draw[thick, samples=100, domain=0:%s] plot (\x, {%s*(\x-%s)^2 + %s});
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) -- (0,%s) node[left] {$%s$};
                \draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s);
                \draw (0,%s) node[left] {$%s$};
                \fill (%s,%s) circle (1.5pt) node[above] {$I$};
            \end{tikzpicture}""" % (T+1, yI+2, T, float(a), xI, yI, xI, xI, xI, yI, yI, yI, T, T, T, yT, yA, yA, xI, yI)

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r"Một vật chuyển động trong $%s$ giờ với vận tốc $v$ (km/h) phụ thuộc thời gian $t$ (h) có đồ thị là một phần của đường parabol có đỉnh $I(%s;%s)$ và trục đối xứng song song với trục tung như hình bên. Quãng đường $s$ mà vật di chuyển được trong $%s$ giờ đó là"
                                 % (latex(T), latex(xI), latex(yI), latex(T)))

                # --- Nội dung lời giải ---
                loigiai = (r"""Gọi $v(t) = at^2 + bt + c$. \\
                Đồ thị $v(t)$ là một phần parabol có đỉnh $I(%s;%s)$ và đi qua điểm $A(0;%s)$ nên ta có hệ:\\
                $\begin{cases} \frac{-b}{2a} = %s \\ a(%s)^2 + b(%s) + c = %s \\ a(0)^2 + b(0) + c = %s \end{cases} \Rightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$. 
                Tìm được $v(t) = %s$.\\
                Vậy $S = \int_{0}^{%s} \left( %s \right) \text{d}t = %s$ (km)."""
                           % (latex(xI), latex(yI), latex(yA), 
                              latex(xI), latex(xI), latex(xI), latex(yI), latex(yA),
                              latex(a_val), latex(b_val), latex(c_val), latex(v_func),
                              latex(T), latex(v_func), kq_str))

                # --- Xuất câu trắc nghiệm ---
                da_d = '\\True ' + da_dung
                list_ans = [da_d, s_list[0], s_list[1], s_list[2]]
                random.shuffle(list_ans)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n \\immini{' + str(noidungcauhoi) + '}{' + tikz_code + '}'
                           '\n\\choice \n'
                           '{' + str(list_ans[0]) + '}\n'
                           '{' + str(list_ans[1]) + '}\n'
                           '{' + str(list_ans[2]) + '}\n'
                           '{' + str(list_ans[3]) + '}\n'
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content

