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


def bt_dang8_p4_b4_c4_ds10(self):
            # Khai báo biến
            # --- CẤU HÌNH BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ cách random bài toán
                # Để bài toán đẹp, ta chọn m, a, c là các số nguyên.
                # Phương trình: (x - a) * sqrt(m^2 - x^2) = (x - a)(x - c)

                m = randint(2, 6)        # Bán kính căn thức (ví dụ m=2 => sqrt(4-x^2))
                a = m + randint(1, 5)    # Chọn a > m để nghiệm x=a luôn bị loại (giống bài mẫu)
                c = randint(-m + 1, m - 1) # Chọn c sao cho x-c >= 0 có khả năng giao với [-m, m]
                while c==0:
                    m = randint(2, 6)        # Bán kính căn thức (ví dụ m=2 => sqrt(4-x^2))
                    a = m + randint(1, 5)    # Chọn a > m để nghiệm x=a luôn bị loại (giống bài mẫu)
                    c = randint(-m + 1, m - 1) # Chọn c sao cho x-c >= 0 có khả năng giao với [-m, m]

                m_sq = m**2
                # Vế phải: x^2 - (a+c)x + ac
                tong_ac = a + c
                tich_ac = a * c

                x = symbols('x')

                # 1. Điều kiện xác định
                dk_v = f"-{m} \\le x \\le {m}"

                # 2. Phân tích vế phải thành (x-a)(x-c)
                # Hiển thị vế phải dạng khai triển
                vp_hien_thi = f"x^2 - {tong_ac}x + {tich_ac}" if tich_ac > 0 else f"x^2 - {tong_ac}x {tich_ac}"
                vp_hien_thi = vp_hien_thi.replace("- -", "+ ").replace("+ -", "- ")

                # 3. Giải phương trình hệ quả: sqrt(m^2 - x^2) = x - c
                # Điều kiện: x >= c
                # Bình phương: m^2 - x^2 = x^2 - 2cx + c^2  => 2x^2 - 2cx + c^2 - m^2 = 0
                A = 2
                B = -2 * c
                C = c**2 - m**2

                delta_phay = c**2 - 2*(c**2 - m_sq) # Biệt thức rút gọn

                # Tìm nghiệm bằng sympy
                pt_bac_2 = A*x**2 + B*x + C
                nghiem_list = solve(pt_bac_2, x)

                nghiem_thoa_man = []
                loigiai_nghiem = ""

                for ng in nghiem_list:
                    val = float(ng.evalf())
                    # Kiểm tra đồng thời 2 điều kiện: x >= c và -m <= x <= m
                    if val >= c and -m <= val <= m:
                        nghiem_thoa_man.append(ng)
                        loigiai_nghiem += f"x = {latex(ng)} \\quad \\text{{(TM)}} \\\\"
                    else:
                        loigiai_nghiem += f"x = {latex(ng)} \\quad \\text{{(L)}} \\\\"

                so_nghiem = len(nghiem_thoa_man)

                # --- TẠO NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (f"Tìm số nghiệm của phương trình $(x - {a})\\sqrt{{{m_sq} - x^2}} = {vp_hien_thi}$.")

                # --- ĐÁP ÁN ---
                da_dung = f"\\True {so_nghiem}"

                # Tạo danh sách đáp án nhiễu
                s_nhieu = {0, 1, 2, 3}
                if so_nghiem in s_nhieu:
                    s_nhieu.remove(so_nghiem)

                list_nhieu = [f"{n}" for n in s_nhieu]
                list_ans = [da_dung] + list_nhieu[:3]
                random.shuffle(list_ans)

                # --- LỜI GIẢI CHI TIẾT (B2) ---
                loigiai = (f"Điều kiện xác định ${dk_v}$ \\\\"
                           f"$(x - {a})\\sqrt{{{m_sq} - x^2}} = {vp_hien_thi}$ \\\\"
                           f"$\\Leftrightarrow (x - {a})\\sqrt{{{m_sq} - x^2}} = (x - {a})(x - {c})$ \\\\"
                           f"$\\Leftrightarrow \\left[\\begin{{array}}{{l}} x = {a} \\quad \\text{{(L)}} \\\\ \\sqrt{{{m_sq} - x^2}} = x - {c} \\quad (*) \\end{{array}}\\right.$ \\\\"
                           f"Giải (*): \\\\"
                           f"$\\sqrt{{{m_sq} - x^2}} = x - {c} \\Leftrightarrow \\begin{{cases}} x \\ge {c} \\\\ {m_sq} - x^2 = (x - {c})^2 \\end{{cases}}$ \\\\"
                           f"$\\Leftrightarrow \\begin{{cases}} x \\ge {c} \\\\ {A}x^2 {B:+}x {C:+} = 0 \\end{{cases}} \\Leftrightarrow \\left[\\begin{{array}}{{l}} {loigiai_nghiem} \\end{{array}}\\right.$ \\\\"
                           f"Vậy phương trình có {so_nghiem} nghiệm.")

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content

