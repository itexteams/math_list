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


def bt_dang26_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ tạo hiển thị đa thức dạng (an+b) hoặc (a-n) cho đẹp
            def format_term(a, b, n_symbol='n', power=1):
                # Xử lý dấu của a
                if a == 0:
                    base = f"{b}"
                elif a == 1:
                    base = f"{n_symbol}" if b == 0 else f"{n_symbol}+{b}" if b > 0 else f"{n_symbol}{b}"
                elif a == -1:
                    base = f"-{n_symbol}" if b == 0 else f"{b}-{n_symbol}" if b > 0 else f"-{n_symbol}{b}"
                else:
                    base = f"{a}{n_symbol}" if b == 0 else f"{a}{n_symbol}+{b}" if b > 0 else f"{a}{n_symbol}{b}"

                # Xử lý trường hợp đặc biệt giống đề bài (3-n) thay vì (-n+3)
                if a < 0 and b > 0:
                    base = f"{b}{a}{n_symbol}" # a đã có dấu âm

                if power == 1:
                    return f"({base})"
                else:
                    return f"({base})^{power}"

            # Hàm hỗ trợ tạo hiển thị bước rút n (dạng 3 - 1/n)
            def format_factor_limit(a, b, power=1):
                # a là hệ số của n, b là hằng số
                # Kết quả mong muốn: (a + b/n) hoặc (a - |b|/n)
                if b == 0:
                    inside = f"{a}"
                elif b > 0:
                    inside = f"{a}+\\frac{{{b}}}{{n}}"
                else:
                    inside = f"{a}-\\frac{{{abs(b)}}}{{n}}"

                if power == 1:
                    return f"\\left({inside}\\right)"
                else:
                    return f"\\left({inside}\\right)^{power}"

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN ---
                # Cấu trúc đề bài: u_n = [ (c1*n + d1) * (c2*n + d2)^2 ] / (c3*n + d3)^3
                # Để giới hạn là hằng số khác 0, bậc tử = bậc mẫu = 3.

                # Random các hệ số
                # Tử số: Term 1 bậc 1
                c1 = randint(2, 5)        # Hệ số n (ví dụ: 3)
                d1 = randint(-5, -1)      # Hằng số (ví dụ: -1)

                # Tử số: Term 2 bậc 2 (bình phương)
                # Để giống mẫu (3-n)^2 -> hệ số n là -1, hằng số là 3
                c2 = random.choice([-1, 1, -2, 2]) 
                d2 = randint(1, 5)

                # Mẫu số: Term 3 bậc 3 (lập phương)
                c3 = randint(2, 5)        # Hệ số n (ví dụ: 4)
                d3 = randint(-9, -1)      # Hằng số (ví dụ: -5)

                # Tính toán kết quả
                # Lim = (c1 * c2^2) / c3^3
                tu_so_lim = c1 * (c2**2)
                mau_so_lim = c3**3

                # Sử dụng Rational để tối giản phân số a/b
                phan_so = Rational(tu_so_lim, mau_so_lim)
                a = phan_so.p
                b = phan_so.q

                # Kết quả bài toán: Tích a.b
                ket_qua_ab = a * b

                # Tạo các chuỗi hiển thị Latex
                # Đề bài
                term1_str = format_term(c1, d1, 'n', 1) # (3n-1)
                term2_str = format_term(c2, d2, 'n', 2) # (3-n)^2
                term3_str = format_term(c3, d3, 'n', 3) # (4n-5)^3

                un_expression = f"\\frac{{{term1_str}{term2_str}}}{{{term3_str}}}"

                # Lời giải
                # Bước rút n ra ngoài:
                factor1_str = format_factor_limit(c1, d1, 1) # (3 - 1/n)
                factor2_str = format_factor_limit(c2, d2, 2) # (3/n - 1)^2 hoặc tương tự
                factor3_str = format_factor_limit(c3, d3, 3) # (4 - 5/n)^3

                limit_calc_str = f"\\frac{{{tu_so_lim}}}{{{mau_so_lim}}}" # 3/64 chưa rút gọn (nếu cần) hoặc số nguyên
                fraction_final_str = latex(phan_so) # Phân số đã tối giản a/b

                # Tạo các đáp án nhiễu (Distractors)
                ans_true = ket_qua_ab

                # Nhiễu 1: Sai lệch nhỏ
                ans_false1 = ket_qua_ab + randint(1, 10)
                # Nhiễu 2: Sai lệch nhỏ hướng âm
                ans_false2 = ket_qua_ab - randint(1, 10)
                # Nhiễu 3: Tính sai a hoặc b (ví dụ quên bình phương c2)
                tu_so_sai = c1 * c2 # Quên bình phương
                phan_so_sai = Rational(tu_so_sai, mau_so_lim)
                ans_false3 = phan_so_sai.p * phan_so_sai.q

                # Đảm bảo các đáp án khác nhau
                list_ans = {ans_true, ans_false1, ans_false2, ans_false3}
                while len(list_ans) < 4:
                    list_ans.add(ans_true + randint(11, 50))

                # Chuyển về list để trộn
                final_options = list(list_ans)
                if ans_true in final_options:
                    final_options.remove(ans_true)
                # Lấy 3 đáp án sai
                ds1, ds2, ds3 = final_options[:3]

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + f'${ans_true}$')
                da_s1 = f'${ds1}$'
                da_s2 = f'${ds2}$'
                da_s3 = f'${ds3}$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---

                noidungcauhoi = ('''Dãy số $(u_n)$ với $u_n = %s$ có giới hạn bằng phân số tối giản $\\frac{a}{b}$. Tích $a.b$ bằng''' % (un_expression))

                loigiai = ('''Ta có: $\\lim_{n \\to +\\infty} %s = \\lim_{n \\to +\\infty} \\frac{%s %s}{%s} = \\frac{%s \\cdot (%s)^2}{(%s)^3} = %s = \\frac{%s}{%s}$.\\\\
            Do đó: $a=%s, b=%s$.\\\\
            Vậy $a.b = %s \\cdot %s = %s$.''' 
                % (un_expression, factor1_str, factor2_str, factor3_str, c1, c2, c3, limit_calc_str, a, b, a, b, a, b, ans_true))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

