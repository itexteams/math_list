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


def bt_dang17_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Ngẫu nhiên hóa bài toán ---
                xm = random.randint(-2, 2)
                ym = random.randint(1, 3)
                k = 2 

                a, b = symbols('a b')
                x, y = symbols('x y')

                # d1: x + 2y + 1 = 0 => x = -1 - 2a, y = a
                xA, yA = -1 - 2*a, a
                # d2: 2x + y + 2 = 0 => y = -2 - 2x => B(b, -2 - 2b)
                xB, yB = b, -2 - 2*b

                # Vector MA và MB
                vMAx, vMAy = xA - xm, yA - ym
                vMBx, vMBy = xB - xm, yB - ym

                def solve_case(is_positive):
                    ratio = k if is_positive else -k
                    # Giải hệ phương trình hoành độ và tung độ
                    eq_x = vMAx - ratio * vMBx
                    eq_y = vMAy - ratio * vMBy
                    sol = solve([eq_x, eq_y], [a, b])

                    if not sol: return None, None, None, None

                    aval, bval = sol[a], sol[b]
                    # Tọa độ điểm A và B cụ thể
                    pA = (xA.subs(a, aval), yA.subs(a, aval))
                    pB = (xB.subs(b, bval), yB.subs(b, bval))

                    # Viết phương trình đường thẳng Delta qua M và A
                    ux, uy = pA[0] - xm, pA[1] - ym
                    nx, ny = uy, -ux
                    const = -(nx*xm + ny*ym)

                    gcd_val = sp.gcd(sp.gcd(nx, ny), const)
                    final_pt = (nx*x + ny*y + const) / gcd_val

                    # Chuẩn hóa hệ số x dương
                    poly_pt = Poly(final_pt, x, y)
                    if poly_pt.coeff_monomial(x) < 0 or (poly_pt.coeff_monomial(x) == 0 and poly_pt.coeff_monomial(y) < 0):
                        final_pt = -final_pt

                    return aval, bval, pA, pB, final_pt

                # Giải 2 trường hợp
                a1, b1, A1, B1, pt1 = solve_case(True)
                a2, b2, A2, B2, pt2 = solve_case(False)

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho điểm $M({xm};{ym})$ và hai đường thẳng "
                                 f"$d_1: x+2y+1=0$, $d_2: 2x+y+2=0$. Phương trình đường thẳng $\\Delta$ đi qua $M$ "
                                 f"và cắt $d_1$ tại $A$, cắt $d_2$ tại $B$ sao cho $MA=2MB$ là")

                # --- Đáp án ---
                da_dung = f"$\\Delta: {latex(pt1)} = 0$ hoặc $\\Delta: {latex(pt2)} = 0$"
                s = [f"$\\Delta: {latex(pt1 + 1)} = 0$", f"$\\Delta: {latex(pt2 - x)} = 0$", f"$\\Delta: x+y+{random.randint(1,9)} = 0$"]
                random.shuffle(s)

                da_d = '\\True ' + da_dung
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # --- Lời giải chi tiết (Phần yêu cầu chính của bạn) ---
                loigiai = (
                    f"Ta có $\\Delta \\cap d_1 = A \\Rightarrow A \\in d_1$ nên $A(-1-2a; a)$, "
                    f"$\\Delta \\cap d_2 = B \\Rightarrow B \\in d_2$ nên $B(b; -2-2b)$.\\\\ "
                    f"Suy ra $\\vec{{MA}} = ({latex(vMAx)}; {latex(vMAy)})$ và $\\vec{{MB}} = ({latex(vMBx)}; {latex(vMBy)})$.\\\\ "
                    f"Do $A, B, M$ thẳng hàng và $MA=2MB$, ta có hai trường hợp:\\\\ "
                    f"Trường hợp 1 \\ $\\vec{{MA}} = 2\\vec{{MB}}$"
                    f"$\\Leftrightarrow \\begin{{cases}} {latex(vMAx)} = 2({latex(vMBx)}) \\\\ {latex(vMAy)} = 2({latex(vMBy)}) \\end{{cases}} "
                    f"\\Leftrightarrow \\begin{{cases}} a = {latex(a1)} \\\\ b = {latex(b1)} \\end{{cases}} \\Rightarrow A({latex(A1[0])}; {latex(A1[1])}), B({latex(B1[0])}; {latex(B1[1])})$.\\\\ "
                    f"Khi đó $\\Delta$ đi qua $M({xm};{ym})$ có VTCP $\\vec{{MA}}=({latex(A1[0]-xm)}; {latex(A1[1]-ym)}) \\sim ({latex(Poly(pt1,x,y).coeff_monomial(y))}; {latex(-Poly(pt1,x,y).coeff_monomial(x))})$.\\\\ "
                    f"Phương trình đường thẳng $\\Delta: {latex(pt1)} = 0$.\\\\ "
                    f"Trường hợp 2:\\ $\\vec{{MA}} = -2\\vec{{MB}}$"
                    f"$\\Leftrightarrow \\begin{{cases}} {latex(vMAx)} = -2({latex(vMBx)}) \\\\ {latex(vMAy)} = -2({latex(vMBy)}) \\end{{cases}} "
                    f"\\Leftrightarrow \\begin{{cases}} a = {latex(a2)} \\\\ b = {latex(b2)} \\end{{cases}} \\Rightarrow A({latex(A2[0])}; {latex(A2[1])}), B({latex(B2[0])}; {latex(B2[1])})$.\\\\ "
                    f"Khi đó $\\Delta$ đi qua $M({xm};{ym})$ có phương trình $\\Delta: {latex(pt2)} = 0$.\\\\ "
                    f"Vậy có hai đường thẳng thỏa mãn là ${latex(pt1)}=0$ hoặc ${latex(pt2)}=0$."
                )

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

