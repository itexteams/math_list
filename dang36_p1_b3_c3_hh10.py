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


def bt_dang36_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # --- BƯỚC 1: RANDOM DỮ LIỆU ---
            # Đường tròn (C): (x-xI)^2 + (y-yI)^2 = R^2
            xI = random.randint(-3, 3)
            yI = random.randint(-3, 3)
            R2 = random.choice([5, 10, 13, 17, 25]) # R^2
            R = sqrt(R2)

            # Tâm K của đường tròn (C')
            # Để bài toán có nghiệm đẹp, ta chọn K sao cho khoảng cách IK không quá phức tạp
            xK = xI + random.choice([-4, 4])
            yK = yI + random.choice([-4, 4])
            d2_IK = (xK - xI)**2 + (yK - yI)**2

            # Độ dài dây cung AB = L. Gọi h = d(I, AB). Ta có h^2 = R^2 - (L/2)^2
            # Chọn L sao cho h^2 dương và gọn
            L_sq = random.choice([2, 4, 8]) # AB^2
            L = sqrt(L_sq)
            h2 = R2 - Rational(L_sq, 4)
            h = sqrt(h2)

            # --- BƯỚC 2: GIẢI TOÁN ---
            # (C): (x - xI)^2 + (y - yI)^2 = R2  => x^2 + y^2 - 2xI*x - 2yI*y + xI^2 + yI^2 - R2 = 0
            c1 = xI**2 + yI**2 - R2
            eqC_str = f"(x - {xI})^2 + (y - {yI})^2 = {R2}"

            # Giả sử (C') có bán kính a. (C'): (x - xK)^2 + (y - yK)^2 = a^2
            # Đường thẳng AB (trục đẳng phương): (C) - (C') = 0
            # [(x-xI)^2 + (y-yI)^2 - R2] - [(x-xK)^2 + (y-yK)^2 - a^2] = 0
            # Rút gọn: 2(xK-xI)x + 2(yK-yI)y + (xI^2+yI^2-R2) - (xK^2+yK^2-a^2) = 0
            coeff_x = 2 * (xK - xI)
            coeff_y = 2 * (yK - yI)
            const_part = (xI**2 + yI**2 - R2) - (xK**2 + yK**2)
            # PT đường thẳng AB: coeff_x*x + coeff_y*y + const_part + a^2 = 0

            # Tính khoảng cách từ I(xI, yI) đến AB bằng h
            # |coeff_x*xI + coeff_y*yI + const_part + a^2| / sqrt(coeff_x^2 + coeff_y^2) = h
            tu_so_tu_do = coeff_x * xI + coeff_y * yI + const_part
            mau_so = sqrt(coeff_x**2 + coeff_y**2)

            # Giải phương trình trị tuyệt đối: |tu_so_tu_do + a^2| = h * mau_so
            val_rhs = simplify(h * mau_so)
            a2_1 = val_rhs - tu_so_tu_do
            a2_2 = -val_rhs - tu_so_tu_do

            # Lọc các giá trị a^2 > 0
            results_a2 = []
            if a2_1 > 0: results_a2.append(a2_1)
            if a2_2 > 0: results_a2.append(a2_2)

            # Tạo các phương trình đường tròn kết quả
            list_kq = [f"(x - {xK})^2 + (y - {yK})^2 = {latex(val)}" for val in results_a2]
            da = "; ".join([f"${s}$" for s in list_kq])

            # --- BƯỚC 3: TẠO ĐÁP ÁN TRẮC NGHIỆM ---
            def generate_fake(original_a2):
                fakes = [original_a2 + random.randint(5, 15), abs(original_a2 - random.randint(5, 10)), original_a2 + 20]
                return fakes

            fake_vals = []
            for val in results_a2:
                fake_vals.extend(generate_fake(val))

            random.shuffle(fake_vals)
            da_s1 = f"$(x - {xK})^2 + (y - {yK})^2 = {latex(fake_vals[0])}$"
            da_s2 = f"$(x - {xK})^2 + (y - {yK})^2 = {latex(fake_vals[1])}$"
            da_s3 = f"$(x - {xK})^2 + (y - {yK})^2 = {latex(fake_vals[2])}$"

            # --- NỘI DUNG ---
            noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường tròn $(C): {eqC_str}$. "
                             f"Phương trình đường tròn $(C')$ có tâm $K({xK}; {yK})$ và cắt đường tròn $(C)$ "
                             f"theo một dây cung $AB$ có độ dài bằng ${latex(L)}$ là")

            loigiai = (f"Đường tròn $(C)$ có tâm $I({xI}; {yI})$ và bán kính $R = {latex(R)}$.\\\\"
                       f"Gọi $a$ ($a>0$) là bán kính đường tròn $(C')$, phương trình $(C')$ là: $(x - {xK})^2 + (y - {yK})^2 = a^2$.\\\\"
                       f"Tọa độ giao điểm $A, B$ là nghiệm hệ phương trình của $(C)$ và $(C')$. "
                       f"Trừ vế theo vế hai phương trình, ta được phương trình đường thẳng $AB$: "
                       f"${latex(coeff_x)}x + {latex(coeff_y)}y + {latex(const_part)} + a^2 = 0$.\\\\"
                       f"Kẻ $IH \\perp AB$ tại trung điểm $H$ của $AB$. Ta có $AH = \\frac{{AB}}{2} = {latex(simplify(L/2))}$.\\\\"
                       f"Suy ra $IH = \\sqrt{{IA^2 - AH^2}} = \\sqrt{{{R2} - {latex(Rational(L_sq, 4))}}} = {latex(h)}$.\\\\"
                       f"Mặt khác $d(I, AB) = IH \\Leftrightarrow \\frac{{|{coeff_x}({xI}) + {coeff_y}({yI}) + {const_part} + a^2|}}{{\\sqrt{{{coeff_x}^2 + ({coeff_y})^2}}}} = {latex(h)}$.\\\\"
                       f"$\\Leftrightarrow |a^2 + {tu_so_tu_do}| = {latex(val_rhs)}$. "
                       f"Giải ra ta được $a^2 = {latex(a2_1)}$ hoặc $a^2 = {latex(a2_2)}$.\\\\ "
                       f"Vậy có các đường tròn thỏa mãn là: {da}.")

            # Xuất câu trắc nghiệm
            da_d = '\\True ' + da
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+').replace('+ -','-')
            return content

