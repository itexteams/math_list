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


def bt_dang43_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo các ký hiệu
            x, y = symbols('x y')

            # Bước 1: Tạo các điểm cơ sở để đảm bảo kết quả là số nguyên đẹp
            # Ta chọn ngẫu nhiên tọa độ A, M (trung điểm BC) và C
            # Từ đó tính được B = 2M - C
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)

            xM = random.randint(-5, 5)
            yM = random.randint(-5, 5)
            # Đảm bảo A không trùng M
            while xA == xM and yA == yM:
                xM = random.randint(-5, 5)
                yM = random.randint(-5, 5)

            xC = random.randint(-5, 5)
            yC = random.randint(-5, 5)
            # Đảm bảo C không trùng M và A, C, M không thẳng hàng để tạo thành tam giác
            while (xC == xM and yC == yM) or (xA == xC and yA == yC) or (xA*(yM-yC) + xM*(yC-yA) + xC*(yA-yM) == 0):
                xC = random.randint(-5, 5)
                yC = random.randint(-5, 5)

            # Tọa độ điểm B
            xB = 2 * xM - xC
            yB = 2 * yM - yC

            # Bước 2: Viết phương trình d1 (đường cao kẻ từ A - vuông góc với BC)
            # Vectơ BC = (xC - xB, yC - yB). Vì d1 vuông góc với BC nên n_d1 = BC
            n1_a = xC - xB
            n1_b = yC - yB
            const1 = -(n1_a * xA + n1_b * yA)

            # Tối giản phương trình d1
            common1 = gcd(gcd(n1_a, n1_b), const1)
            n1_a //= common1
            n1_b //= common1
            const1 //= common1
            if n1_a < 0 or (n1_a == 0 and n1_b < 0):
                n1_a, n1_b, const1 = -n1_a, -n1_b, -const1

            # Chuỗi hiển thị d1: ax + by + c = 0
            d1_expr = ""
            if n1_a != 0:
                d1_expr += f"{n1_a}x"
            if n1_b > 0:
                d1_expr += f"+{n1_b}y" if d1_expr else f"{n1_b}y"
            elif n1_b < 0:
                d1_expr += f"{n1_b}y"
            if const1 > 0:
                d1_expr += f"+{const1}"
            elif const1 < 0:
                d1_expr += f"{const1}"
            d1_expr += "=0"

            # Bước 3: Viết phương trình d2 (trung tuyến kẻ từ A - đi qua A và M)
            # Vectơ AM = (xM - xA, yM - yA) => Vectơ pháp tuyến n_d2 = (-(yM-yA), xM-xA)
            n2_a = -(yM - yA)
            n2_b = xM - xA
            const2 = -(n2_a * xA + n2_b * yA)

            # Tối giản phương trình d2
            common2 = gcd(gcd(n2_a, n2_b), const2)
            n2_a //= common2
            n2_b //= common2
            const2 //= common2
            if n2_a < 0 or (n2_a == 0 and n2_b < 0):
                n2_a, n2_b, const2 = -n2_a, -n2_b, -const2

            d2_expr = ""
            if n2_a != 0:
                d2_expr += f"{n2_a}x"
            if n2_b > 0:
                d2_expr += f"+{n2_b}y" if d2_expr else f"{n2_b}y"
            elif n2_b < 0:
                d2_expr += f"{n2_b}y"
            if const2 > 0:
                d2_expr += f"+{const2}"
            elif const2 < 0:
                d2_expr += f"{const2}"
            d2_expr += "=0"

            # Bước 4: Tạo các phương án trắc nghiệm
            da = f"({xB};{yB})"
            # Tạo các đáp án sai bằng cách cộng/trừ ngẫu nhiên
            s = set()
            while len(s) < 3:
                dx = random.randint(-3, 3)
                dy = random.randint(-3, 3)
                if dx == 0 and dy == 0: continue
                fake_ans = f"({xB + dx};{yB + dy})"
                if fake_ans != da:
                    s.add(fake_ans)

            list_s = list(s)
            da_d = "\\True $" + da + "$"
            da_s1 = "$" + list_s[0] + "$"
            da_s2 = "$" + list_s[1] + "$"
            da_s3 = "$" + list_s[2] + "$"

            list_all = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_all)

            # Bước 5: Nội dung câu hỏi và lời giải
            noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có $C({xC};{yC})$, đường cao và trung tuyến kẻ từ đỉnh $A$ có phương trình lần lượt là $d_1: {d1_expr}$, $d_2: {d2_expr}$. Tìm tọa độ điểm $B$.")

            # Xây dựng lời giải chi tiết
            bc_a = n1_b
            bc_b = -n1_a
            bc_const = -(bc_a * xC + bc_b * yC)
            bc_expr = f"{bc_a}x + {bc_b}y + {bc_const} = 0".replace("+ -", "- ").replace("1x", "x").replace("1y", "y")

            loigiai = (f"Ta có $A = d_1 \\cap d_2$, nên tọa độ điểm $A(x; y)$ thỏa mãn hệ: "
                       f"$\\begin{{cases}} {d1_expr} \\\\ {d2_expr} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {xA} \\\\ y = {yA} \\end{{cases}}$. "
                       f"Ta được $A({xA}; {yA})$.\\\\ "
                       f"Đường thẳng $BC$ đi qua $C({xC}; {yC})$ và vuông góc với $d_1$ nên có phương trình: ${bc_expr}$.\\\\ "
                       f"Gọi $M$ là trung điểm $BC$, suy ra $M = BC \\cap d_2$. Tọa độ điểm $M$ thỏa mãn hệ: "
                       f"$\\begin{{cases}} {bc_expr} \\\\ {d2_expr} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {xM} \\\\ y = {yM} \\end{{cases}}$. "
                       f"Do đó $M({xM}; {yM})$.\\\\ "
                       f"Vì $M$ là trung điểm của $BC$ nên $\\begin{{cases}} x_B = 2x_M - x_C = 2({xM}) - ({xC}) = {xB} \\\\ y_B = 2y_M - y_C = 2({yM}) - ({yC}) = {yB} \\end{{cases}}$. "
                       f"Vậy $B({xB}; {yB})$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

