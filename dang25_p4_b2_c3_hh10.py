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


def bt_dang25_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            x, y = symbols('x y')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để khớp với hình ảnh mẫu (đường thẳng có thể khuyết y hoặc x)
            x0, y0 = random.randint(-5, 5), random.randint(-5, 5)
            # Random hệ số a, b, c cho đường thẳng d: ax + by + c = 0
            a = random.choice([-3, -2, -1, 1, 2, 3])
            b = random.choice([0, -2, -1, 1, 2]) # Cho phép b=0 như trong ảnh mẫu
            c = random.randint(-5, 10)

            # Phương trình d: a*x + b*y + c = 0
            pt_d = a*x + b*y + c

            # B1 & B2: Viết lại bài toán và lời giải
            # Vectơ pháp tuyến n_d = (a, b). Vectơ pháp tuyến d' vuông góc d là n_d' = (b, -a)
            # d' qua A(x0, y0) có dạng: b(x - x0) - a(y - y0) = 0
            # Sử dụng simplify để xử lý dấu -- thành + tự động
            v_phai_d_prime = b*(x - x0) - a*(y - y0)
            pt_d_prime = v_phai_d_prime.simplify()

            # Giải hệ phương trình tìm tọa độ H
            he_pt = [Eq(pt_d, 0), Eq(pt_d_prime, 0)]
            sol = solve(he_pt, (x, y))
            hx, hy = sol[x], sol[y]

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho đường thẳng $d : {latex(pt_d)} = 0$ và điểm $A({x0};{y0})$. "
                             f"Tìm tọa độ hình chiếu vuông góc của $A$ lên $d$.")

            # Nội dung lời giải (Xử lý hiển thị dấu chặt chẽ)
            # Thay thế cụm b(x - x0) - a(y - y0) thủ công để giống mẫu ảnh nhưng đẹp hơn
            buoc_the_so = f"{b}(x - {x0}) - {a}(y - {y0}) = 0"
            # Làm sạch dấu -- trong bước thế số
            buoc_the_so = buoc_the_so.replace("- -", "+ ")

            loigiai = (f"Phương trình $d'$ đi qua $A({x0};{y0})$, vuông góc với $d$ có dạng:\\\\ "
                       f"${buoc_the_so} \\Leftrightarrow {latex(pt_d_prime)} = 0$.\\\\ "
                       f"Hình chiếu $H$ là giao điểm của $d$ và $d'$ nên có tọa độ thỏa mãn hệ: \\\\"
                       f"$\\begin{{cases}} {latex(pt_d)} = 0 \\\\ {latex(pt_d_prime)} = 0 \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} x = {latex(hx)} \\\\ y = {latex(hy)} \\end{{cases}}$.\\\\ "
                       f"Vậy $H({latex(hx)}; {latex(hy)})$.")

            # Các đáp án
            da_dung = f'({latex(hx)}; {latex(hy)})'
            da_sai1 = f'({latex(hx + 1)}; {latex(hy)})'
            da_sai2 = f'({latex(hx)}; {latex(hy - 1)})'
            da_sai3 = f'({latex(hy)}; {latex(hx)})'

            da_d = '\\True $' + da_dung + '$'
            list_1 = [da_d, f'${da_sai1}$', f'${da_sai2}$', f'${da_sai3}$']
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

