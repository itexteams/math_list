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


def bt_dang36_p1_b2_c3_ds12(self):
            # Khai báo biến
            # --- Bước 1 & 2: Nghiên cứu đề bài và lời giải ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- Bước 3: Random bài toán ---
                # r là bán kính nửa đường tròn. Ví dụ r=2 thì x chạy từ 0 đến 4.
                r = random.randint(2, 4)
                # a là độ dài đoạn từ điểm kết thúc đường tròn đến đỉnh gấp khúc (đoạn lên dốc)
                a = random.randint(2, 3)
                # b là độ dài đoạn nằm ngang cuối cùng
                b = random.randint(1, 2)
                h = r # Giữ chiều cao bằng bán kính để đồ thị liên tục như hình mẫu

                x1 = 2 * r      # Điểm kết thúc nửa đường tròn
                x2 = x1 + a     # Điểm đạt đỉnh cao nhất của đường gấp khúc
                x3 = x2 + b     # Điểm kết thúc đồ thị

                # Tính diện tích (Tích phân)
                coeff_pi = Rational(r**2, 2)
                s_tamgiac = Rational(a * h, 2)
                s_hcn = b * h
                coeff_num = s_tamgiac + s_hcn

                # Định dạng đáp án đúng
                def format_ans(cp, cn):
                    part1 = f"{latex(cp)}\\pi" if cp != 1 else "\\pi"
                    part2 = f" + {latex(cn)}"
                    return (part1 + part2)

                da_value = format_ans(coeff_pi, coeff_num)
                da = f"${da_value}$"

                # --- Bước 4: Tạo phương án sai ---
                s = set()
                while len(s) < 3:
                    offset_pi = random.choice([Rational(1,2), 1, 2]) * random.choice([-1, 1])
                    offset_num = random.randint(1, 3) * random.choice([-1, 1])
                    c_pi_sai = abs(coeff_pi + offset_pi)
                    c_num_sai = abs(coeff_num + offset_num)
                    fake_ans = format_ans(c_pi_sai, c_num_sai)
                    if fake_ans != da_value:
                        s.add(f"${fake_ans}$")
                list_sai = list(s)

                # Vẽ hình bằng TikZ - Đã fix lỗi đối số
                # Tổng cộng có 32 vị trí %s cần điền vào tuple
                tikz_code = r"""\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-1,0) -- (%s,0) node[below] {$x$};
                \draw[->] (0,-1) -- (0,%s) node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw[thick] (0,0) arc (180:0:%s);
                \draw[thick] (%s,0) -- (%s,%s) -- (%s,%s);
                \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s) node[left] {$%s$};
                \draw[dashed] (%s,0) -- (%s,%s);
                \draw[dashed] (%s,0) -- (%s,%s);
                \node[below] at (%s,0) {$%s$};
                \node[below] at (%s,0) {$%s$};
                \node[below] at (%s,0) {$%s$};
                \node[below] at (%s,0) {$%s$};
            \end{tikzpicture}""" % (
                    x3+1, r+1.5,                      # Trục x, Trục y
                    r,                                 # Bán kính cung tròn
                    x1, x2, r, x3, r,                  # Đường gấp khúc
                    r, r, r, r, r,                     # Đường dashed tại đỉnh cung tròn (tọa độ r,r)
                    x2, x2, r,                         # Đường dashed tại x2
                    x3, x3, r,                         # Đường dashed tại x3
                    r, r,                              # Label r trên trục x
                    x1, x1,                            # Label 2r trên trục x
                    x2, x2,                            # Label x2 trên trục x
                    x3, x3,                            # Label x3 trên trục x
                )

                noidungcauhoi = (r"Cho hàm số $y=f(x)$ có đồ thị trên đoạn $[0;%s]$ như hình vẽ (một phần là nửa đường tròn, một phần là đường gấp khúc). Tích phân $\int_0^{%s} f(x)dx$ bằng"
                                 % (latex(x3), latex(x3)))

                loigiai = (r"Diện tích hình phẳng giới hạn bởi đồ thị và trục hoành là tích phân cần tính: \\ "
                           r"- Phần 1 (Nửa hình tròn): $S_1 = \frac{1}{2}\pi \cdot %s^2 = %s\pi$. \\ "
                           r"- Phần 2 (Hình tam giác): $S_2 = \frac{1}{2} \cdot (%s-%s) \cdot %s = %s$. \\ "
                           r"- Phần 3 (Hình chữ nhật): $S_3 = (%s-%s) \cdot %s = %s$. \\ "
                           r"Vậy $\int_0^{%s} f(x) \text{d}x = S_1 + S_2 + S_3 = %s$."
                           % (latex(r), latex(coeff_pi), 
                              latex(x2), latex(x1), latex(r), latex(s_tamgiac),
                              latex(x3), latex(x2), latex(r), latex(s_hcn),
                              latex(x3), da_value))

                da_d = ('\\True ' + str(da))
                list_1 = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_1)

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                       '\\begin{center}\n' + tikz_code + '\\end{center}\n' +
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

