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


def bt_dang18_p4_b2_c2_ds10(self):
    # Khai báo biến
    def round_SA(a): 
        # Kiểm tra nếu a là số nguyên
        if a == int(a):
            return "", int(a)

        # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
        str_a = f"{float(a):.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
        integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

        # Xác định cách làm tròn
        if len(integer_part) > 2:
            number = Decimal(str(float(a))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng đơn vị)."
        elif len(integer_part) == 2 and len(decimal_part) > 1:
            number = Decimal(str(float(a))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng phần chục)."
        elif len(decimal_part) <= 2:
            number = str_a  # Không cần làm tròn thêm
            cirle = ""
        else:
            number = Decimal(str(float(a))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng phần trăm)."

        # Chuyển dấu chấm thành dấu phẩy (nếu có)
        return cirle, str(number).replace('.', ',')

    # ------------------------------------------------------------------------------BÀI TOÁN
    x, y = sp.symbols('x y')

    # Khởi tạo các giá trị ngẫu nhiên
    bien_x, bien_y = random.sample(list(range(25, 40)), 2)
    nuoc = random.choice(["cam", "chanh"])
    an = random.choice(["bắp rang", "khoai chiên"])
    gia_nuoc = random.randint(10, 15)
    gia_an = gia_nuoc + random.randint(2, 5)

    # Đảm bảo 2 combo có tỉ lệ thành phần khác nhau để hệ phương trình luôn có nghiệm duy nhất
    danh_sach_combo = [
        (gia_nuoc + gia_an, f"một cốc nước {nuoc} và một túi {an}", 1, 1),
        (round(gia_nuoc + gia_an * 2 * 0.9), f"một cốc nước {nuoc} và hai túi {an}", 1, 2),
        (round(gia_nuoc * 2 * 0.9 + gia_an), f"hai cốc nước {nuoc} và một túi {an}", 2, 1),
        (round(gia_nuoc * 3 * 0.85 + gia_an), f"ba cốc nước {nuoc} và một túi {an}", 3, 1),
        (round(gia_nuoc + gia_an * 3 * 0.85), f"một cốc nước {nuoc} và ba túi {an}", 1, 3),
        (round(gia_nuoc * 3 * 0.8 + gia_an * 2 * 0.85), f"ba cốc nước {nuoc} và hai túi {an}", 3, 2),
        (round(gia_nuoc * 2 * 0.85 + gia_an * 3 * 0.8), f"hai cốc nước {nuoc} và ba túi {an}", 2, 3),
        (round(gia_nuoc * 3 * 0.8 + gia_an * 4 * 0.75), f"ba cốc nước {nuoc} và bốn túi {an}", 3, 4),
        (round(gia_nuoc * 4 * 0.75 + gia_an * 3 * 0.8), f"bốn cốc nước {nuoc} và ba túi {an}", 4, 3)
    ]

    while True:
        compo1, compo2 = random.sample(danh_sach_combo, 2)
        gia1, thuc_don1, so_nuoc1, so_an1 = compo1
        gia2, thuc_don2, so_nuoc2, so_an2 = compo2
        # Định thức khác 0 để hệ phương trình luôn xác định nghiệm duy nhất B
        if so_nuoc1 * so_an2 - so_nuoc2 * so_an1 != 0:
            break

    max_nuoc = so_nuoc1 * bien_x + so_nuoc2 * bien_y
    max_an = so_an1 * bien_x + so_an2 * bien_y

    Eq1 = so_nuoc1 * x + so_nuoc2 * y
    Eq2 = so_an1 * x + so_an2 * y

    # SỬA LỖI: dùng sp.solve thay vì solve tự do để tránh conflict namespace
    nghiem = sp.solve([sp.Eq(Eq1, max_nuoc), sp.Eq(Eq2, max_an)], (x, y))
    ham_F = gia1 * x + gia2 * y

    xA, yA = min([sp.Rational(max_nuoc, so_nuoc1), sp.Rational(max_an, so_an1)]), 0
    yC, xC = min([sp.Rational(max_nuoc, so_nuoc2), sp.Rational(max_an, so_an2)]), 0
    xB, yB = nghiem[x], nghiem[y]

    toa_do_cac_dinh = [(0, 0), (xA, yA), (xB, yB), (xC, yC)]
    cac_gia_tri = [ham_F.subs({x: dinh[0], y: dinh[1]}) for dinh in toa_do_cac_dinh]
    so_dinh = len(toa_do_cac_dinh)
    ket_qua = max(cac_gia_tri)
    max_index = cac_gia_tri.index(ket_qua)
    max_dinh = toa_do_cac_dinh[max_index]

    xmin = -1 if min(xA, xB) < 11 else -3 if min(xA, xB) < 21 else -4 
    xmax = (1 if max(xA, xB) < 11 else 3 if max(xA, xB) < 21 else 4) + round(float(max(xA, xB)), 1)
    ymin = -1 if min(yC, yB) < 11 else -3 if min(yC, yB) < 21 else -4  
    ymax = (1 if max(yC, yB) < 11 else 3 if max(yC, yB) < 21 else 4) + round(float(max(yC, yB)), 1)

    scale_val = 0.7 if abs(ymax-ymin) < 6 else 0.5 if abs(ymax-ymin) < 11 else 0.25 if abs(ymax-ymin) < 21 else 0.1 if abs(ymax-ymin) < 31 else 0.08

    # Vẽ hình bằng TikZ theo phong cách gạch sọc
    tikz_latex = f'''\\begin{{tikzpicture}}[>=stealth, scale={scale_val}, line width=1pt, font=\\footnotesize]
