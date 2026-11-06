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


def bt_dang9_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random các thông số:
        # h: chiều cao OA
        # d: độ dài OB
        # angle_deg: góc tạo bởi OB và trục Oy
        h = random.choice([5, 8, 10, 12, 14, 15, 20])
        d = random.choice([10, 12, 14, 16, 18, 20])
        angle_deg = random.choice([30, 60])

        # Tính toán bằng sympy để ra LaTeX chuẩn (phân số, căn thức)
        alpha = angle_deg * sp.pi / 180
        x_B = d * sp.sin(alpha)
        y_B = d * sp.cos(alpha)

        # Biến a, b, c theo vec{AB}
        a = x_B
        b = y_B
        c = -h

        # Chọn biểu thức tính toán T để đảm bảo kết quả đẹp (hết căn)
        if angle_deg == 30:
            var_name = "a"
            val1 = a
            # Sẽ tính T = m*a + p*c
        else:
            var_name = "b"
            val1 = b
            # Sẽ tính T = m*b + p*c

        m = random.choice([2, 4]) # Hệ số chẵn để triệt tiêu mẫu 2
        p = random.choice([-3, -2, -1, 1, 2, 3])

        ans = int(m * val1 + p * c) # Chắc chắn là số nguyên

        # Xử lý chuỗi biểu thức hiển thị T = ma + pc
        str_m = str(m) if m not in [1, -1] else ("" if m == 1 else "-")
        str_p = str(abs(p)) if abs(p) != 1 else ""
        sign_p = "+" if p > 0 else "-"
        expr_str = f"{str_m}{var_name} {sign_p} {str_p}c"

        # Xử lý chuỗi phép thế, LUÔN thay thế + - thành -
        str_val1_latex = sp.latex(val1)
        str_c_latex = f"({c})" if c < 0 else str(c)

        if m == 1:
             term1_sub = f"{str_val1_latex}"
        elif m == -1:
             term1_sub = f"-\\left({str_val1_latex}\\right)"
        else:
             term1_sub = f"{m}\\cdot \\left({str_val1_latex}\\right)"

        if p == 1 or p == -1:
             term2_sub = f"{str_c_latex}"
        else:
             term2_sub = f"{abs(p)}\\cdot {str_c_latex}"

        sub_str = f"{term1_sub} {sign_p} {term2_sub}"

        # Ép buộc xử lý dấu để triệt để fix lỗi "+ -" hoặc "- -"
        sub_str = sub_str.replace("+ -", "- ").replace("- -", "+ ")

        # Đề bài
        noidungcauhoi = (f"Một chiếc xe đang kéo căng sợi dây cáp $AB$ trong công trường xây dựng, trên đó đã thiết lập "
                         f"hệ tọa độ $Oxyz$ với độ dài đơn vị trên các trục tọa độ bằng $1\\text{{ m}}$. "
                         f"Biết điểm $A$ nằm trên phần dương của trục $Oz$ với $OA = {h}\\text{{ m}}$. "
                         f"Điểm $B$ thuộc mặt phẳng $(Oxy)$ có hoành độ và tung độ đều dương sao cho $OB = {d}\\text{{ m}}$ "
                         f"và góc giữa $OB$ và chiều dương trục $Oy$ bằng ${angle_deg}^\\circ$. "
                         f"Biết tọa độ của vectơ $\\overrightarrow{{AB}} = (a;b;c)$. Giá trị biểu thức $T = {expr_str}$ bằng bao nhiêu?")
        # Lời giải
        loigiai = (f"Ta có: Điểm $A$ nằm trên trục $Oz$ và $OA = {h} \\Rightarrow A(0;0;{h})$. \\\\\n"
                   f"Gọi $H, K$ lần lượt là hình chiếu vuông góc của $B$ lên các trục $Oy, Ox$.\\\\\n"
                   f"Trong mặt phẳng $(Oxy)$, góc giữa $OB$ và trục $Oy$ bằng ${angle_deg}^\\circ$, ta có:\\\\\n"
                   f"Tung độ của $B$ là $y_B = OH = OB \\cdot \\cos {angle_deg}^\\circ = {d} \\cdot \\cos {angle_deg}^\\circ = {sp.latex(y_B)}$. \\\\\n"
                   f"Hoành độ của $B$ là $x_B = OK = HB = OB \\cdot \\sin {angle_deg}^\\circ = {d} \\cdot \\sin {angle_deg}^\\circ = {sp.latex(x_B)}$. \\\\\n"
                   f"Do $B$ thuộc mặt phẳng $(Oxy)$ nên $z_B = 0$. Suy ra $B\\left({sp.latex(x_B)}; {sp.latex(y_B)}; 0\\right)$. \\\\\n"
                   f"$\\Rightarrow \\overrightarrow{{AB}} = \\left({sp.latex(x_B)}; {sp.latex(y_B)}; -{h}\\right)$. \\\\\n"
                   f"Theo bài ra $\\overrightarrow{{AB}} = (a;b;c)$ nên đối chiếu tọa độ ta có: $\\begin{{cases}} a = {sp.latex(x_B)} \\\\ b = {sp.latex(y_B)} \\\\ c = -{h} \\end{{cases}}$. \\\\\n"
                   f"Vậy $T = {expr_str} = {sub_str} = {ans}$.")

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(ans))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

