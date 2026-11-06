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


def bt_dang22_p1_b2_c2_hh12(self):
            # --- PHẦN 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Tọa độ điểm A, B, C
            Ax, Ay, Az = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Bx, By, Bz = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Cx, Cy, Cz = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # Đảm bảo B và C không trùng nhau để vectơ BC khác vectơ không
            while (Bx, By, Bz) == (Cx, Cy, Cz):
                Cx, Cy, Cz = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # Vectơ chỉ phương u = BC
            ux, uy, uz = Cx - Bx, Cy - By, Cz - Bz

            # --- PHẦN 2: HÀM HỖ TRỢ ĐỊNH DẠNG ---
            def format_param(p, u):
                """Định dạng x = x0 + ut chuẩn toán học"""
                if u == 0: return f"{p}"
                u_str = ""
                if u == 1: u_str = "+ t"
                elif u == -1: u_str = "- t"
                else: u_str = f"{u:+}t"

                if p == 0: return u_str.lstrip("+ ")
                return f"{p} {u_str}"

            def get_full_eq(x0, y0, z0, vx, vy, vz):
                """Tạo khối cases LaTeX"""
                eq_x = f"x = {format_param(x0, vx)}"
                eq_y = f"y = {format_param(y0, vy)}"
                eq_z = f"z = {format_param(z0, vz)}"
                return f"\\begin{{cases}}{eq_x}\\\\{eq_y}\\\\{eq_z}\\end{{cases}}".replace("+ -", "-")

            # --- PHẦN 3: TẠO CÁC PHƯƠNG ÁN (KHÔNG TRÙNG LẶP) ---
            da_dung = get_full_eq(Ax, Ay, Az, ux, uy, uz)

            # Dùng set để lưu trữ, đảm bảo không trùng
            options = {f"\\True ${da_dung}$"}

            # Các kịch bản tạo đáp án nhiễu
            candidates = [
                get_full_eq(Bx, By, Bz, ux, uy, uz),           # Nhầm đi qua điểm B
                get_full_eq(Cx, Cy, Cz, ux, uy, uz),           # Nhầm đi qua điểm C
                get_full_eq(Ax, Ay, Az, Bx-Ax, By-Ay, Bz-Az), # Nhầm VCP là AB
                get_full_eq(Ax, Ay, Az, ux, uy, uz+1),        # Đảo dấu VCP
                get_full_eq(Ax, Ay, Az, ux, uy+1, uz), # Sai 1 tọa độ VCP
                get_full_eq(Ax, Ay, Az, ux+1, uy, uz),       # Sai điểm đi qua
            ]

            # Lọc và thêm vào set phương án
            for cand in candidates:
                cand_str = f"${cand}$"
                # Kiểm tra xem phương án nhiễu có trùng với phương án đúng (đã bỏ \True) không
                if cand_str not in [opt.replace("\\True ", "") for opt in options]:
                    options.add(cand_str)
                if len(options) == 4: break

            # Nếu vẫn chưa đủ 4 phương án (trường hợp hiếm), tạo ngẫu nhiên
            while len(options) < 4:
                dummy = get_full_eq(Ax, Ay, Az, ux + randint(1, 3), uy, uz)
                options.add(f"${dummy}$")

            list_1 = list(options)
            random.shuffle(list_1)

            # --- PHẦN 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
            noidungcauhoi = (
                f"Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A({Ax};{Ay};{Az})$, "
                f"$B({Bx};{By};{Bz})$ và $C({Cx};{Cy};{Cz})$. Phương trình tham số của đường thẳng "
                f"$d$ đi qua điểm $A$ và song song với đường thẳng $BC$ là"
            )

            loigiai = (
                f"Đường thẳng $d$ song song với $BC$ nên nhận $\\vec{{u}} = \\vec{{BC}} = "
                f"({Cx}-({Bx}); {Cy}-({By}); {Cz}-({Bz})) = ({ux}; {uy}; {uz})$ làm vectơ chỉ phương.\\\\"
                f"Vì $d$ đi qua $A({Ax}; {Ay}; {Az})$ nên có phương trình tham số là:\\\\"
                f"${da_dung}$."
            ).replace("- -", "+ ").replace("+ -", "- ")

            # --- PHẦN 5: XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n' )

            return content

