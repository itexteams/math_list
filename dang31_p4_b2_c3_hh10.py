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


def bt_dang31_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Random tọa độ các điểm trong khoảng từ -10 đến 10
            xA, yA = random.randint(-5, 5), random.randint(-5, 5)
            xB, yB = random.randint(-5, 5), random.randint(-5, 5)
            xP, yP = random.randint(-5, 5), random.randint(-5, 5)

            # Đảm bảo A khác B và P không làm cho bài toán suy biến (tùy chọn)
            while (xA == xB and yA == yB) or (xA == xP and yA == yP):
                xB, yB = random.randint(-5, 5), random.randint(-5, 5)

            # --- B2: Viết lại bài toán theo mẫu ---
            a, b = symbols('a b')

            # Biểu thức trong trị tuyệt đối của d(A, delta) và d(B, delta)
            # Delta: a(x - xP) + b(y - yP) = 0  => ax + by - (a*xP + b*yP) = 0
            exprA = a*(xA - xP) + b*(yA - yP)
            exprB = a*(xB - xP) + b*(yB - yP)

            # Giải phương trình |exprA| = |exprB| <=> exprA = exprB hoặc exprA = -exprB
            # TH1: exprA = exprB
            sol1 = simplify(exprA - exprB) # Dạng: ma + nb = 0
            # TH2: exprA = -exprB
            sol2 = simplify(exprA + exprB) # Dạng: ka + la = 0

            def get_line(expr_ab):
                # Trích xuất hệ số của a và b từ biểu thức dạng ma + nb
                m = expr_ab.coeff(a)
                n = expr_ab.coeff(b)
                # Chọn a = n, b = -m (để ma + nb = 0)
                val_a, val_b = int(n), int(-m)
                # Rút gọn hệ số bằng GCD
                from math import gcd
                common = gcd(val_a, val_b)
                if common != 0:
                    val_a //= common
                    val_b //= common
                # Đảm bảo hệ số đầu tiên dương cho đẹp
                if val_a < 0 or (val_a == 0 and val_b < 0):
                    val_a, val_b = -val_a, -val_b

                # Phương trình: val_a(x - xP) + val_b(y - yP) = 0
                c = -(val_a * xP + val_b * yP)
                return val_a, val_b, c

            a1, b1, c1 = get_line(sol1)
            a2, b2, c2 = get_line(sol2)

            # Chuẩn hóa xâu phương trình
            def fmt_line(a, b, c):
                res = ""
                if a != 0: res += f"{a}x"
                if b > 0: res += f"+{b}y" if a != 0 else f"{b}y"
                elif b < 0: res += f"{b}y"
                if c > 0: res += f"+{c}"
                elif c < 0: res += f"{c}"
                return res + "=0"

            line1 = fmt_line(a1, b1, c1)
            line2 = fmt_line(a2, b2, c2)

            # --- Xuất nội dung ---
            noidungcauhoi = f"Cho ba điểm $A({xA};{yA}), B({xB};{yB})$ và $P({xP};{yP})$. Lập phương trình đường thẳng đi qua $P$ đồng thời cách đều $A$ và $B$."

            da_d = f"\\True ${line1}$ và ${line2}$"
            # Tạo đáp án nhiễu (đổi dấu hoặc đổi số ngẫu nhiên)
            da_s1 = f"${fmt_line(a1, -b1, c1)}$ và ${line2}$"
            da_s2 = f"${line1}$ và ${fmt_line(a2, b2, -c1)}$"
            da_s3 = f"${fmt_line(b1, a1, c1)}$ và ${line2}$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = f"""Đường thẳng $\\Delta$ đi qua $P$ có dạng $a(x - ({xP})) + b(y - ({yP})) = 0$ ($a^2 + b^2 \\neq 0$).
            $\\Delta$ cách đều $A$ và $B$ khi và chỉ khi:
            $d(A; \\Delta) = d(B; \\Delta) \\Leftrightarrow \\frac{{|{latex(exprA)}|}}{{\\sqrt{{a^2+b^2}}}} = \\frac{{|{latex(exprB)}|}}{{\\sqrt{{a^2+b^2}}}}$
            $\\Leftrightarrow \\left[ \\begin{{array}}{{l}} {latex(exprA)} = {latex(exprB)} \\\\ {latex(exprA)} = -({latex(exprB)}) \\end{{array}} \\right. 
            \\Leftrightarrow \\left[ \\begin{{array}}{{l}} {latex(sol1)} = 0 \\\\ {latex(sol2)} = 0 \\end{{array}} \\right.$\\\\
            Trường hợp 1: ${latex(sol1)} = 0$, chọn $a={a1}, b={b1} \\Rightarrow \\Delta_1: {line1}$.\\\\
            Trường hợp 2: ${latex(sol2)} = 0$, chọn $a={a2}, b={b2} \\Rightarrow \\Delta_2: {line2}$.\\\\
            Vậy có hai đường thẳng thỏa mãn là $\\Delta_1: {line1}$ và $\\Delta_2: {line2}$."""

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

