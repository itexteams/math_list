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


def bt_dang54_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- Bước 3: Thiết lập Logic Random ---
            # Cấu trúc: lim_{x->x0} [f(x)-A]/[x-x0] = L
            # Tính: lim_{x->x0} [căn bậc 3(m*f(x) + n) - p] / [x^2 + bx + c]

            # 1. Chọn x0 và p (để căn bậc 3 của m*A + n = p)
            x0 = random.randint(1, 5)
            p = random.choice([2, 3, 4, 5])

            # 2. Chọn m và A (A là giá trị f(x0))
            m = random.randint(2, 8)
            A = random.randint(5, 20)

            # 3. Tính n để đảm bảo tử số bằng 0 khi x = x0
            # m*A + n = p^3  => n = p^3 - m*A
            n = p**3 - m * A

            # 4. Giá trị giới hạn cho trước L
            L = random.randint(2, 15)

            # 5. Mẫu số dạng (x - x0)(x - x1)
            # Chọn x1 khác x0 để không bị nghiệm kép phức tạp
            x1 = random.choice([v for v in range(-6, 6) if v != x0])
            mau_so_da_thuc = expand((x - x0) * (x - x1))

            # --- Tính toán kết quả (kq) ---
            # Theo công thức đạo hàm/liên hợp: 
            # Kết quả = L * [ m / ( (x0 - x1) * 3 * p^2 ) ]
            tu_so_kq = L * m
            mau_so_kq = (x0 - x1) * 3 * (p**2)
            kq_final = Rational(tu_so_kq, mau_so_kq)

            # --- Tạo danh sách đáp án ---
            da_dung = '$%s$' % latex(kq_final)

            # Tạo các đáp án sai bằng cách cộng trừ phân số
            s = [
                '$%s$' % latex(kq_final + Rational(1, 2)),
                '$%s$' % latex(kq_final - Rational(1, 3)),
                '$%s$' % latex(kq_final * Rational(2, 3)),
                '$%s$' % latex(Rational(random.randint(1, 5), random.randint(6, 20)))
            ]

            das1 = random.choice(s); s.remove(das1)
            das2 = random.choice(s); s.remove(das2)
            das3 = random.choice(s)

            # --- Nội dung câu hỏi ---
            # Xử lý hiển thị dấu n (nếu n âm thì hiện "5f(x) - 16")
            bieu_thuc_trong_can = f"{m}f(x) + {n}" if n >= 0 else f"{m}f(x) - {abs(n)}"

            noidungcauhoi = (r"Cho hàm số $f(x)$ xác định trên $\mathbb{R}$ thỏa mãn $\lim_{x \to %s} \frac{f(x) - %s}{x - %s} = %s$. Giới hạn "
                             r"$\lim_{x \to %s} \frac{\sqrt[3]{%s} - %s}{%s}$ bằng"
                             %(latex(x0), latex(A), latex(x0), latex(L),
                               latex(x0), bieu_thuc_trong_can, latex(p), latex(mau_so_da_thuc)))

            # --- Nội dung lời giải ---
            # Biểu thức liên hợp: (A^2 + AB + B^2)
            lien_hop = r"\left(\sqrt[3]{(%s)^2} + %s\sqrt[3]{%s} + %s\right)" % (bieu_thuc_trong_can, p, bieu_thuc_trong_can, p**2)

            loigiai = (r"Do $\lim_{x \to %s} \frac{f(x) - %s}{x - %s} = %s$ nên ta có $f(%s) - %s = 0$ hay $f(%s) = %s$. \\\\"
                       r"$\lim_{x \to %s} \frac{\sqrt[3]{%s} - %s}{%s} = \lim_{x \to %s} \frac{%s(f(x) - %s)}{(x - %s)(x - %s)%s}$ \\\\"
                       r"$= \lim_{x \to %s} \frac{f(x) - %s}{x - %s} \cdot \frac{%s}{(x - %s)%s}$ \\\\"
                       r"$= %s \cdot \frac{%s}{(%s - %s) \cdot %s} = %s$."
                       %(latex(x0), latex(A), latex(x0), latex(L), latex(x0), latex(A), latex(x0), latex(A),
                         latex(x0), bieu_thuc_trong_can, latex(p), latex(mau_so_da_thuc), latex(x0), m, latex(A), latex(x0), latex(x1), lien_hop,
                         latex(x0), latex(A), latex(x0), m, latex(x1), lien_hop,
                         L, m, x0, x1, 3*(p**2), latex(kq_final)))

            # --- Xuất câu trắc nghiệm theo mẫu ---
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất kết quả theo format mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

