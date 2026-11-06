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


def bt_dang44_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khởi tạo biến
            x, y = symbols('x y')

            # --- BƯỚC 1: RANDOM THÔNG SỐ (Dựa trên khung bài mẫu) ---
            # Chọn tâm I(a, b) và bán kính R
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            R = random.randint(5, 8)

            # Chọn nửa độ dài dây cung h = HA sao cho HA < R
            # Để giống bài gốc có căn, ta có thể chọn HA sao cho IH^2 = R^2 - HA^2 không phải số chính phương
            h = random.randint(3, R - 1)
            L = 2 * h # Độ dài dây cung AB

            # Tính IH^2 và IH
            ih_sq = R**2 - h**2
            ih_val = sqrt(ih_sq)

            # Chọn hệ số đường thẳng d (Ưu tiên bộ 3, 4 để mẫu số là 5 cho đẹp)
            A, B = 4, 3
            C_orig = random.randint(-15, -5)

            # --- BƯỚC 2: TÍNH TOÁN LỜI GIẢI ĐÚNG ---
            # PT đường tròn (C): x^2 + y^2 - 2ax - 2by + (a^2 + b^2 - R^2) = 0
            c_const = a**2 + b**2 - R**2
            pt_tron = x**2 - 2*a*x + y**2 - 2*b*y + c_const

            # Khoảng cách từ I đến d': |Aa + Bb + m| / 5 = ih_val
            # => |m + (Aa + Bb)| = 5 * ih_val
            tu_so_tu_m = A*a + B*b
            delta = 5 * ih_val
            m1 = -tu_so_tu_m + delta
            m2 = -tu_so_tu_m - delta

            # --- BƯỚC 3: ĐỊNH DẠNG NỘI DUNG ---

            noidungcauhoi = (r"Trong mặt phẳng với hệ toạ độ $Oxy$, cho đường tròn $(C) : %s = 0$. "
                             r"Lập phương trình đường thẳng song song với đường thẳng $d : %sx + %sy %s = 0$ và cắt đường tròn theo một dây cung có độ dài bằng $%s$."
                             %(latex(pt_tron), A, B, ("+ " + str(C_orig) if C_orig >= 0 else "- " + str(abs(C_orig))), L))

            # Đáp án (Lấy m1, m2 đã tính)
            def fmt_m(val):
                v = simplify(val)
                return ("+ " + latex(v) if v >= 0 else "- " + latex(abs(v)))

            da_d = r"\True $4x + 3y %s = 0; 4x + 3y %s = 0$" % (fmt_m(m1), fmt_m(m2))
            da_s1 = r"$4x + 3y + 5 = 0; 4x + 3y - 49 = 0$"
            da_s2 = r"$4x + 3y + 1 = 0; 4x + 3y - 45 = 0$"
            da_s3 = r"$4x + 3y - 2 = 0; 4x + 3y - 42 = 0$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = (r"Đường tròn $(C)$ có tâm $I(%s; %s)$ và bán kính $R = %s$.\\"
                       r"Đường thẳng $d'$ song song với $d$ nên có phương trình $d' : 4x + 3y + m = 0$ ($m \neq %s$).\\"
                       r"Gọi $H$ là hình chiếu của $I$ lên $d'$, dây cung có độ dài bằng %s nên $HA = %s$.\\"
                       r"Xét tam giác vuông $IHA$, ta có: $IH^2 = IA^2 - HA^2 = %s^2 - %s^2 = %s$.\\"
                       r"Do đó $IH = %s$. Khoảng cách từ $I$ đến $d'$ là: $IH = \frac{|4 \cdot (%s) + 3 \cdot (%s) + m|}{\sqrt{4^2 + 3^2}} = %s$.\\"
                       r"$\Leftrightarrow \frac{|m + %s|}{5} = %s \Leftrightarrow |m + %s| = %s \Leftrightarrow \left[\begin{matrix} m = %s \\ m = %s \end{matrix}\right. $.\\"
                       r"Vậy có hai đường thẳng: $4x + 3y %s = 0$ và $4x + 3y %s = 0$."
                       %(a, b, R, C_orig, L, h, R, h, ih_sq, latex(ih_val), a, b, latex(ih_val), 
                         tu_so_tu_m, latex(ih_val), tu_so_tu_m, latex(delta), latex(simplify(m1)), latex(simplify(m2)),
                         fmt_m(m1), fmt_m(m2)))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

