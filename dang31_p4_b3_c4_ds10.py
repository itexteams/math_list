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


def bt_dang31_p4_b3_c4_ds10(self):
            # Khai báo biến
            # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN ---

            a = random.randint(5, 8)
            b = random.randint(1, 3)
            k = random.randint(3, 5)

            m = symbols('m')

            # 1. Giải điều kiện có 2 nghiệm phân biệt (*)
            # m - a != 0 và Delta' > 0
            # Delta' = (m-b)^2 - m(m-a) = m^2 - 2bm + b^2 - m^2 + am = (a-2b)m + b^2
            coef_m_delta = a - 2*b
            const_delta = b**2
            # Điều kiện: (a-2b)m + b^2 > 0
            cond_delta = solve_univariate_inequality(coef_m_delta*m + const_delta > 0, m, relational=False)
            m_threshold_delta = -sp.Rational(const_delta, coef_m_delta)

            # 2. Giải điều kiện x1 < k < x2
            # (x1-k)(x2-k) < 0 <=> x1x2 - k(x1+x2) + k^2 < 0
            # Biến đổi tử số: m + 2k(m-b) + k^2(m-a) = (k+1)^2*m - (2kb + ak^2)
            num_coef = (k + 1)**2
            num_const = 2*k*b + a*k**2
            expr_viet_numerator = num_coef * m - num_const
            expr_full = expr_viet_numerator / (m - a)

            # Tìm tập nghiệm cho m
            sol_interval = solve_univariate_inequality(expr_full < 0, m, relational=False)
            m_min = sol_interval.start
            m_max = sol_interval.end

            # --- BƯỚC 2: VIẾT LẠI Y HỆT BÀI TOÁN (DÙNG BIẾN RANDOM) ---

            # Nội dung câu hỏi
            noidungcauhoi = (r"Cho phương trình $(m-%s)x^2+2(m-%s)x+m=0$ (1). Tìm giá trị của $m$ để (1) có 2 nghiệm $x_1, x_2$ thỏa $x_1 < %s < x_2$." 
                             % (latex(a), latex(b), latex(k)))

            # Nội dung lời giải chi tiết
            loigiai = (r"""Phương trình (1) có hai nghiệm phân biệt $\Leftrightarrow \begin{cases} m-%s \neq 0 \\ (m-%s)^2 - m(m-%s) > 0 \end{cases}$ \\
                       $\Leftrightarrow \begin{cases} m \neq %s \\ %sm + %s > 0 \end{cases} \Leftrightarrow \begin{cases} m \neq %s \\ m > %s \end{cases} (*)$. \\
                       Khi đó theo định lý Vi-ét, ta có: $\begin{cases} x_1+x_2 = -\frac{2(m-%s)}{m-%s} \\ x_1x_2 = \frac{m}{m-%s} \end{cases}$. \\
                       Với $x_1 < %s < x_2 \Rightarrow (x_1-%s)(x_2-%s) < 0 \Leftrightarrow x_1x_2 - %s(x_1+x_2) + %s < 0$ \\
                       $\Leftrightarrow \frac{m}{m-%s} + \frac{%s(m-%s)}{m-%s} + %s < 0 \Leftrightarrow \frac{%sm - %s}{m-%s} < 0$ \\
                       $\Leftrightarrow %s < m < %s$. Kiểm tra điều kiện (*) ta được $%s < m < %s$."""
                       % (a, b, a, a, coef_m_delta, const_delta, a, latex(m_threshold_delta),
                          b, a, a, k, k, k, k, k**2, a, 2*k, b, a, k**2, num_coef, num_const, a,
                          latex(m_min), latex(m_max), latex(m_min), latex(m_max)))

            # Các đáp án trắc nghiệm
            da_dung = r"\True $%s < m < %s$" % (latex(m_min), latex(m_max))
            da_s1 = r"$m \geq %s$" % latex(a)
            da_s2 = r"$m < %s$" % latex(m_min)
            da_s3 = r"$%s \leq m \leq %s$" % (latex(m_min), latex(m_max))

            list_ans = [da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # --- XUẤT CÂU TRẮC NGHIỆM (Đúng theo mẫu image_724056.png) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

