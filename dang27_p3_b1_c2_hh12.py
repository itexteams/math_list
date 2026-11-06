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


def bt_dang27_p3_b1_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':


        while True:
            # Chọn tọa độ A, B
            xA, yA, zA = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            xB, yB, zB = randint(-3, 3), randint(-3, 3), randint(-3, 3)

            # Vectơ AB
            u1, u2, u3 = xB - xA, yB - yA, zB - zA
            if u1 == 0 and u2 == 0 and u3 == 0:
                continue

            # Hệ số của mặt phẳng (P)
            Ap = randint(-4, 4)
            Bp = randint(-4, 4)
            Cp = randint(-4, 4)
            Dp = randint(-6, 6)
            if Ap == 0 and Bp == 0 and Cp == 0:
                continue


            nx = u2 * Cp - u3 * Bp
            ny = u3 * Ap - u1 * Cp
            nz = u1 * Bp - u2 * Ap


            if nx == 0:
                continue


            # k * D_Q = c  (với D_Q = -(nx*xA + ny*yA + nz*zA)) => c = -(2*xA - a*yA - b*zA)
            k_val = Rational(2, nx)
            a_val = -k_val * ny
            b_val = -k_val * nz

            # Đảm bảo a, b, c là các số nguyên
            if a_val.q == 1 and b_val.q == 1:
                a = int(a_val)
                b = int(b_val)
                c = -(2 * xA - a * yA - b * zA)

                # Kiểm tra giá trị biểu thức
                ans = a + 2 * b + 3 * c
                if -999 < ans < 9999:
                    break

        # Chuỗi hiển thị phương trình (P): Ap*x + Bp*y + Cp*z + Dp = 0
        p_terms = []
        if Ap == 1:
            p_terms.append('x')
        elif Ap == -1:
            p_terms.append('-x')
        elif Ap != 0:
            p_terms.append('%sx' % Ap)

        if Bp == 1:
            p_terms.append('+ y' if p_terms else 'y')
        elif Bp == -1:
            p_terms.append('- y' if p_terms else '-y')
        elif Bp > 0:
            p_terms.append('+ %sy' % Bp if p_terms else '%sy' % Bp)
        elif Bp < 0:
            p_terms.append('- %sy' % abs(Bp) if p_terms else '-%sy' % abs(Bp))

        if Cp == 1:
            p_terms.append('+ z' if p_terms else 'z')
        elif Cp == -1:
            p_terms.append('- z' if p_terms else '-z')
        elif Cp > 0:
            p_terms.append('+ %sz' % Cp if p_terms else '%sz' % Cp)
        elif Cp < 0:
            p_terms.append('- %sz' % abs(Cp) if p_terms else '-%sz' % abs(Cp))

        if Dp > 0:
            p_terms.append('+ %s' % Dp)
        elif Dp < 0:
            p_terms.append('- %s' % abs(Dp))
        pt_P_str = ' '.join(p_terms) + ' = 0'

        # Chuỗi phương trình mặt phẳng cần tìm 2x - ay - bz + c = 0
        q_terms = ['2x']
        if a > 0:
            q_terms.append('- %sy' % a if a != 1 else '- y')
        elif a < 0:
            q_terms.append('+ %sy' % abs(a) if a != -1 else '+ y')

        if b > 0:
            q_terms.append('- %sz' % b if b != 1 else '- z')
        elif b < 0:
            q_terms.append('+ %sz' % abs(b) if b != -1 else '+ z')

        if c > 0:
            q_terms.append('+ %s' % c)
        elif c < 0:
            q_terms.append('- %s' % abs(c))
        pt_Q_str = ' '.join(q_terms) + ' = 0'

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$ cho hai điểm $A(%s; %s; %s)$, $B(%s; %s; %s)$ và mặt phẳng $(P): %s$. Phương trình của mặt phẳng đi qua hai điểm $A, B$, đồng thời vuông góc $(P)$ là $2x - ay - bz + c = 0$. Giá trị của biểu thức $a + 2b + 3c$ bằng bao nhiêu?'''
                         % (xA, yA, zA, xB, yB, zB, pt_P_str))

        # Nội dung lời giải
        loigiai = ('''Ta có $\\vec{AB} = (%s; %s; %s)$.\\\\
    Mặt phẳng $(P)$ có một vectơ pháp tuyến là $\\vec{n}_P = (%s; %s; %s)$.\\\\
    Gọi $(Q)$ là mặt phẳng đi qua hai điểm $A, B$ và vuông góc với $(P)$.\\\\
    Khi đó mặt phẳng $(Q)$ có một vectơ pháp tuyến cùng phương với tích có hướng $[\\vec{AB}, \\vec{n}_P]$:\\\\
    $[\\vec{AB}, \\vec{n}_P] = \\left( (%s)\\cdot(%s) - (%s)\\cdot(%s);\\; (%s)\\cdot(%s) - (%s)\\cdot(%s);\\; (%s)\\cdot(%s) - (%s)\\cdot(%s) \\right) = (%s; %s; %s)$.\\\\
    Do phương trình mặt phẳng có dạng $2x - ay - bz + c = 0$ (hệ số của $x$ bằng $2$), ta chọn vectơ pháp tuyến của $(Q)$ là:\\\\
    $\\vec{n}_Q = \\frac{2}{%s} [\\vec{AB}, \\vec{n}_P] = (2; %s; %s)$.\\\\
    Mặt phẳng $(Q)$ đi qua điểm $A(%s; %s; %s)$ và nhận $\\vec{n}_Q = (2; %s; %s)$ làm vectơ pháp tuyến nên có phương trình:\\\\
    $2(x - (%s)) + (%s)(y - (%s)) + (%s)(z - (%s)) = 0$\\\\
    $\\Leftrightarrow %s$.\\\\
    Đồng nhất phương trình trên với dạng $2x - ay - bz + c = 0$, ta được:\\\\
    $-a = %s \\Rightarrow a = %s$,\\\\
    $-b = %s \\Rightarrow b = %s$,\\\\
    $c = %s$.\\\\
    Khi đó giá trị của biểu thức $a + 2b + 3c$ là:\\\\
    $a + 2b + 3c = %s + 2\\cdot(%s) + 3\\cdot(%s) = %s$.'''
                   % (u1, u2, u3,
                      Ap, Bp, Cp,
                      u2, Cp, u3, Bp,
                      u3, Ap, u1, Cp,
                      u1, Bp, u2, Ap,
                      nx, ny, nz,
                      nx, -a, -b,
                      xA, yA, zA,
                      -a, -b,
                      xA, -a, yA, -b, zA,
                      pt_Q_str,
                      -a, a,
                      -b, b,
                      c,
                      a, b, c, ans))

        # Đáp án
        dapan = '\\shortans{$%s$}\n' % (ans)

    # Xuất câu hỏi với đáp án và lời giải đã được định dạng
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

