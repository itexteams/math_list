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


def bt_dang15_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            danh_sach_bo_so = [
                (sqrt(3), 1, 1, -1, 75), # Góc lẻ, ta sẽ ưu tiên các góc chuẩn SGK
                (1, 0, 1, 1, 45),       # n1(1,0), u2(1,1) -> n2(1,-1). Cos = 1/sqrt(2)
                (sqrt(3), 1, 0, 1, 60),  # n1(sqrt(3),1), u2(0,1) -> n2(1,0). Cos = sqrt(3)/2 -> 30 độ (góc giữa 2 VTPT), góc đt là 30
                (1, sqrt(3), 1, 0, 60),  # n1(1, sqrt(3)), u2(1,0) -> n2(0,1). Cos = sqrt(3)/2 -> 30 độ
                (1, 1, 1, 0, 45),        # n1(1,1), u2(1,0) -> n2(0,1). Cos = 1/sqrt(2)
                (0, 1, 1, 1, 45),        # n1(0,1), u2(1,1) -> n2(1,-1). Cos = 1/sqrt(2)
                (1, -2, 2, 1, 0),        # n1(1,-2), u2(2,1) -> n2(1,-2). Song song/Trùng -> 0 độ
                (3, -2, 1, -5, 45),      # n1(3,-2), u2(1,-5) -> n2(5,1). Cos = 13/(sqrt(13)*sqrt(26)) = 1/sqrt(2)
            ]

            # Chọn ngẫu nhiên bộ số
            n1x, n1y, u2x, u2y = random.choice([
                (sqrt(3), 1, 1, 1),   # Bộ 1
                (1, sqrt(3), 1, 0),   # Bộ 2
                (3, -2, 1, -5),       # Bộ 3 (Giống câu 1 bạn gửi)
                (1, 1, 1, 0)          # Bộ 4
            ])

            # Random hệ số tự do
            c1 = random.randint(-10, 10)
            x0 = random.randint(-5, 5)
            y0 = random.randint(-5, 5)

            # --- Tính toán VTPT Delta 2 chính xác ---
            # VTCP u2 = (u2x, u2y) => VTPT n2 = (u2y, -u2x)
            n2x, n2y = u2y, -u2x

            # Tính Cosin
            tu_so = abs(n1x * n2x + n1y * n2y)
            mau_so = sqrt(n1x**2 + n1y**2) * sqrt(n2x**2 + n2y**2)
            cos_val = simplify(tu_so / mau_so)

            # Tính góc
            val_float = float(cos_val)
            goc_deg = int(round(float(acos(val_float) * 180 / 3.1415926535)))

            # Định dạng hiển thị LaTeX cho phương trình
            def fmt(val, var="", is_first=False):
                if val == 0: return ""
                v_latex = latex(val)
                if v_latex == "1" and var != "": v_latex = ""
                if v_latex == "-1" and var != "": v_latex = "-"

                sign = "+" if not str(v_latex).startswith("-") and not is_first else ""
                return f"{sign}{v_latex}{var}"

            d1_str = f"{fmt(n1x, 'x', True)} {fmt(n1y, 'y')} {fmt(c1)} = 0".replace("+ -", "- ").replace("- -", "+ ")
            d2_y_str = f"{y0} {fmt(u2y, 't')}".replace("+ -", "- ").replace("- -", "+ ")

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (f"Góc giữa hai đường thẳng: $\\Delta_1: {d1_str}$ và "
                             f"$\\Delta_2: \\begin{{cases}} x = {x0} {fmt(u2x, 't')} \\\\ y = {d2_y_str} \\end{{cases}} (t \\in \\mathbb{{R}})$ bằng")

            # --- Lời giải (Sửa lỗi VTPT) ---
            loigiai = (f"Đường thẳng $\\Delta_2$ có vectơ chỉ phương $\\vec{{u}}_2 = ({latex(u2x)}; {latex(u2y)})$ "
                       f"nên có vectơ pháp tuyến $\\vec{{n}}_2 = ({latex(n2x)}; {latex(n2y)})$. \\\\"
                       f"Ta có $\\vec{{n}}_1({latex(n1x)}; {latex(n1y)})$ là vectơ pháp tuyến của $\\Delta_1$. Suy ra: \\\\"
                       f"$\\cos(\\Delta_1; \\Delta_2) = \\frac{{|{latex(n1x)} \\cdot {latex(n2x)} + {latex(n1y)} \\cdot ({latex(n2y)})|}}{{\\sqrt{{({latex(n1x)})^2 + ({latex(n1y)})^2}} \\cdot \\sqrt{{({latex(n2x)})^2 + ({latex(n2y)})^2}}}} = {latex(cos_val)}$. \\\\"
                       f"Do đó $(\\Delta_1; \\Delta_2) = {goc_deg}^0$.")

            # --- Đáp án ---
            da_d = f"\\True ${goc_deg}^0$"
            s_options = [f"${a}^0$" for a in [30, 45, 60, 90] if a != goc_deg]
            random.shuffle(s_options)
            list_1 = [da_d, s_options[0], s_options[1], s_options[2]]
            random.shuffle(list_1)

            # --- Xuất câu trắc nghiệm ---
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

