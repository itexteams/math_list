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


def bt_dang30_p4_b1_c3_ds12(self):
            # Khai báo biến
            k = random.randint(1, 4) 


            C = random.randint(-4, 4)

            # Tính các thành phần của f(1) = const_f1 + ln_coeff_f1 * ln(2)
            const_f1 = 2*k + 2*C
            ln_coeff_f1 = -2*k

            # Chuỗi hiển thị cho f(1)
            if const_f1 == 0:
                f1_display = f"{ln_coeff_f1}\\ln 2"
            else:
                sign = "+" if ln_coeff_f1 > 0 else ""
                f1_display = f"{const_f1} {sign} {ln_coeff_f1}\\ln 2"

            # Tính a và b trong f(2) = a + b*ln(3)
            # a = 3/2 * (2k + C), b = -3k/2
            a_val = Rational(3 * (2*k + C), 2)
            b_val = Rational(-3 * k, 2)

            # Tính giá trị cần tìm: S = a^2 + b^2
            kq_final = a_val**2 + b_val**2
            kq_latex = latex(kq_final)

            # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
            def generate_distractors(correct_val):
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi tử số hoặc cộng trừ số nguyên
                    offset = random.choice([Rational(1, 2), 1, 2, Rational(3, 2), Rational(5, 2)])
                    direction = random.choice([1, -1])
                    wrong = correct_val + direction * offset
                    if wrong > 0 and wrong != correct_val:
                        s.add(f"${latex(wrong)}$")
                return list(s)

            distractors = generate_distractors(kq_final)

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
            noidungcauhoi = (
                f"Cho hàm số $y = f(x)$ liên tục trên $\\mathbb{{R}} \\setminus \\{{0; -1\\}}$ thỏa mãn điều kiện "
                f"$f(1) = {f1_display}$ và $x(x+1) \\cdot f'(x) + f(x) = {latex(k)}(x^2 + x)$. "
                f"Giá trị $f(2) = a + b \\ln 3$, với $a, b \\in \\mathbb{{Q}}$. Tính $a^2 + b^2$."
            )

            # Xử lý hiển thị k trong lời giải (nếu k=1 thì không hiện số 1 trước ngoặc)
            k_str = "" if k == 1 else latex(k)

            loigiai = (
                f"Từ giả thiết, chia cả hai vế cho $(x+1)^2$ ta có:\\\\"
                f"$\\frac{{x}}{{x+1}} \\cdot f'(x) + \\frac{{1}}{{(x+1)^2}} f(x) = \\frac{{{k_str}x}}{{x+1}} "
                f"\\Leftrightarrow \\left[ \\frac{{x}}{{x+1}} f(x) \\right]' = {k_str} \\left( 1 - \\frac{{1}}{{x+1}} \\right)$.\\\\"
                f"Suy ra $\\frac{{x}}{{x+1}} f(x) = \\int {k_str} \\left( 1 - \\frac{{1}}{{x+1}} \\right) \\text{{d}}x = {k_str} (x - \\ln|x+1|) + C$.\\\\"
                f"Mặt khác, $f(1) = {f1_display}$ nên ta thay $x=1$ vào:\\\\"
                f"$\\frac{{1}}{{2}} f(1) = {k_str} (1 - \\ln 2) + C \\Rightarrow C = {latex(C)}$.\\\\"
                f"Do đó $\\frac{{x}}{{x+1}} f(x) = {k_str} (x - \\ln|x+1|) + {latex(C)}$.\\\\"
                f"Với $x=2$ thì $\\frac{{2}}{{3}} f(2) = {k_str} (2 - \\ln 3) + {latex(C)} \\Leftrightarrow f(2) = {latex(a_val)} {latex(b_val)} \\ln 3$.\\\\"
                f"Suy ra $a = {latex(a_val)}$ và $b = {latex(b_val)}$. Vậy $a^2 + b^2 = {kq_latex}$."
            )

            # Xuất kết quả theo mẫu
            da_d = '\\True $' + kq_latex + '$'
            list_ans = [da_d] + distractors
            random.shuffle(list_ans)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

