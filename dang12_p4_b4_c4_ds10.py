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


def bt_dang12_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khởi tạo biến x
            x = symbols('x')

            # --- B3: DANH SÁCH CÁC BỘ SỐ RANDOM ĐẸP ---
            # (a, b, K) tương ứng với: (x - a)sqrt(K - x^2) = (x - a)(x - b)
            cac_bo_so = [
                (1, 2, 10), # Nghiệm: 1 và 3
                (3, 4, 20), # Nghiệm: 3 và 2 + sqrt(6)
                (2, 3, 13), # Nghiệm: 2 và 2 + sqrt(2)
                (1, 2, 6),  # Nghiệm: 1 và 1 + sqrt(3)
                (2, 4, 18), # Nghiệm: 2 và 4
            ]

            # Chọn ngẫu nhiên một bộ số
            a, b, K = random.choice(cac_bo_so)

            # --- TÍNH TOÁN LOGIC ---
            # Vế phải dạng tam thức bậc hai: expand((x - a) * (x - b))
            vp_tam_thuc = expand((x - a) * (x - b))

            # Các thông số cho phương trình bậc 2 trong lời giải: 2x^2 - 2bx + b^2 - K = 0
            he_so_bac_2 = 2
            he_so_bac_1 = -2 * b
            so_hang_tu_do = b**2 - K

            # Giải phương trình (*) : sqrt(K - x^2) = x - b
            roots_star = solve(sqrt(K - x**2) - (x - b), x)
            valid_roots_star = [r for r in roots_star if r >= b]

            # Nghiệm và tổng nghiệm
            all_roots = [a] + valid_roots_star
            tong_nghiem = sum(all_roots)

            # --- XỬ LÝ HIỂN THỊ CHUẨN LATEX ---
            def to_latex(expr):
                return latex(expr)

            txt_tong_nghiem = to_latex(tong_nghiem)
            txt_root_star = to_latex(valid_roots_star[0]) if valid_roots_star else "Vô nghiệm"

            # Xử lý dấu cho phương trình bậc 2 trong lời giải để tránh lỗi "+ -4"
            dau_b1 = "" if he_so_bac_1 < 0 else "+"
            dau_c = "" if so_hang_tu_do < 0 else "+"

            # --- TRẮC NGHIỆM ---
            da_dung = '$%s$' % txt_tong_nghiem
            nhieu = [
                simplify(tong_nghiem + 1),
                simplify(tong_nghiem + random.randint(2, 3)),
                simplify(tong_nghiem - 1)
            ]
            s = ['$%s$' % to_latex(val) for val in nhieu]
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # --- NỘI DUNG CÂU HỎI ---
            # Hiển thị vế phải là tam thức bậc hai đã expand
            noidungcauhoi = r'''Tìm tổng các nghiệm của phương trình $(x - %s)\sqrt{%s - x^2} = %s$.''' % (a, K, to_latex(vp_tam_thuc))

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = r'''
            Điều kiện xác định: $-\sqrt{%s} \le x \le \sqrt{%s}$. \\
            Phương trình tương đương:
            $(x - %s)\sqrt{%s - x^2} = %s$ \\
            $\Leftrightarrow (x - %s)\sqrt{%s - x^2} = (x - %s)(x - %s)$ \\
            $\Leftrightarrow \left[\begin{aligned} &x = %s \\ &\sqrt{%s - x^2} = x - %s \quad (*) \end{aligned}\right.$ \\
            Giải (*): $\sqrt{%s - x^2} = x - %s \Leftrightarrow \begin{cases} x \ge %s \\ %s - x^2 = (x - %s)^2 \end{cases}$ \\
            $\Leftrightarrow \begin{cases} x \ge %s \\ %s x^2 %s %s x %s %s = 0 \end{cases} \Leftrightarrow x = %s$. \\
            Vậy các nghiệm của phương trình là $x = %s, x = %s$. \\
            Tổng các nghiệm là: $%s + %s = %s$.
            ''' % (
                K, K, 
                a, K, to_latex(vp_tam_thuc),
                a, K, a, b,
                a, K, b,
                K, b, b, K, b,
                b, he_so_bac_2, dau_b1, he_so_bac_1, dau_c, so_hang_tu_do,
                txt_root_star,
                a, txt_root_star,
                a, txt_root_star, txt_tong_nghiem
            )

            # --- XUẤT KẾT QUẢ ---
            list_1 = ['\\True ' + da_dung, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

