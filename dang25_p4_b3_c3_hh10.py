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


def bt_dang25_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo tọa độ tâm I(a, b) và bán kính R của đường tròn (C)
                a = random.randint(-5, 5)
                b = random.randint(-5, 5)
                R = random.randint(2, 5)

                # 2. Tạo hệ số A, B cho đường thẳng d: Ax + By + m = 0 sao cho A^2 + B^2 là số chính phương
                # Các bộ số Pythagore phổ biến: (3,4), (5,12), (8,15)
                triples = [(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6)]
                A, B = random.choice(triples)
                # Ngẫu nhiên đổi dấu A hoặc B
                if random.choice([True, False]): A = -A
                if random.choice([True, False]): B = -B

                # 3. Tính toán theo logic bài toán
                # Tam giác PAB đều -> góc API = 30 độ -> IP = R / sin(30) = 2R
                R_prime = 2 * R
                deno = int(math.sqrt(A**2 + B**2)) # Mẫu số của công thức khoảng cách

                # Khoảng cách d(I, d) = R_prime <=> |A*a + B*b + m| / sqrt(A^2 + B^2) = R_prime
                # <=> |A*a + B*b + m| = R_prime * deno
                K = R_prime * deno
                temp_sum = A*a + B*b

                m1 = K - temp_sum
                m2 = -K - temp_sum

                # Đảm bảo m1, m2 hiển thị đẹp
                kq_list = sorted([int(m1), int(m2)])
                da_dung = f"m = {kq_list[0]} \\text{{ hoặc }} m = {kq_list[1]}"

                # 4. Tạo các phương án nhiễu
                # Nhiễu 1: Quên nhân đôi R (tức là dùng R thay vì 2R)
                K_err = R * deno
                m_err1 = sorted([int(K_err - temp_sum), int(-K_err - temp_sum)])

                # Nhiễu 2: Sai dấu trong biểu thức m
                m_err2 = sorted([int(m1 + 2*temp_sum), int(m2 + 2*temp_sum)])

                # Nhiễu 3: Một giá trị ngẫu nhiên khác
                m_err3 = sorted([int(m1 + random.randint(1, 5)), int(m2 - random.randint(1, 5))])

                # --- BƯỚC 3: ĐỊNH DẠNG HIỂN THỊ ---
                # Xử lý dấu cho phương trình đường thẳng
                sign_B = "+" if B > 0 else "-"
                abs_B = abs(B)
                line_eq = f"{A}x {sign_B} {abs_B}y + m = 0"
                line_eq = line_eq.replace(" 1x", " x").replace("-1x", "-x").replace(" 1y", " y").replace("+-", "- ")

                # Xử lý dấu cho tâm I trong phương trình đường tròn
                sign_a_c = "+" if a <= 0 else "-"
                abs_a_c = abs(a)
                sign_b_c = "+" if b <= 0 else "-"
                abs_b_c = abs(b)
                circle_eq = f"(x {sign_a_c} {abs_a_c})^2 + (y {sign_b_c} {abs_b_c})^2 = {R**2}"
                circle_eq = circle_eq.replace(" 0", "").replace("(x )^2", "x^2").replace("(y )^2", "y^2").replace("- -", "+ ").replace("+ -", "- ")

                # Nội dung câu hỏi
                noidungcauhoi = (f"Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường tròn $(C): {circle_eq}$ và đường thẳng $d: {line_eq}$. "
                                 f"Tìm $m$ để trên đường thẳng $d$ có duy nhất một điểm $P$ mà từ đó có thể kẻ được hai tiếp tuyến $PA, PB$ "
                                 f"tới $(C)$ ($A, B$ là các tiếp điểm) sao cho tam giác $PAB$ đều.")

                # Các đáp án
                da_d = f"\\True ${da_dung}$"
                da_s1 = f"$m = {m_err1[0]} \\text{{ hoặc }} m = {m_err1[1]}$"
                da_s2 = f"$m = {m_err2[0]} \\text{{ hoặc }} m = {m_err2[1]}$"
                da_s3 = f"$m = {m_err3[0]} \\text{{ hoặc }} m = {m_err3[1]}$"

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                # Xử lý hiển thị d(I, d) cho đẹp
                val_sub = f"{A}({a}) {'+' if B*b >=0 else '-'} {abs(B*b)}"

            # Nội dung lời giải (Đã sửa lỗi ngoặc nhọn trong f-string)
                loigiai = ('''\\begin{center}
                               \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.6cm,y=0.6cm]
                	\\clip(-3,-1) rectangle (9,6);
                	\\draw (3.,2.)-- (3.,5.);
                	\\draw (6.,2.)-- (3.,2.);
                	\\draw(3.,2.) circle (1.8cm);
                	\\draw (0.,5.)-- (6.,5.);
                	\\draw (6.,5.)-- (6.,0.);
                	\\draw (3.,2.)-- (6.,5.);
                	\\draw (4.,6.)-- (9.35,3.289);
                	\\draw (8.3,4.9) node[anchor=north west] {$d$};
                	\\draw (2.6,2) node[anchor=north west] {$I$};
                	\\draw (6.,6.) node[anchor=north west] {$P$};
                	\\draw (2.66,6) node[anchor=north west] {$A$};
                	\\draw (6,2.7) node[anchor=north west] {$B$};
                	\\draw (3.,5.)-- (6.,2.);
                \\end{tikzpicture}
                \\end{center}'''

                    f"Đường tròn $(C)$ có tâm $I({a}; {b})$, bán kính $R = {R}$.\\\\ "
                    f"Tam giác $PAB$ đều nên $\\widehat{{APB}} = 60^\\circ \\Rightarrow \\widehat{{API}} = 30^\\circ$.\\\\ "
                    f"Xét tam giác $API$ vuông tại $A$, ta có: $IP = \\frac{{IA}}{{\\sin \\widehat{{API}}}} = \\frac{{{R}}}{{\\sin 30^\\circ}} = {R_prime}$.\\\\ "
                    f"Do đó $P$ thuộc đường tròn $(C')$ có tâm $I$, bán kính $R' = IP = {R_prime}$.\\\\ "
                    f"Mặt khác, để trên $d$ có duy nhất một điểm $P$ thỏa yêu cầu bài toán thì $d$ tiếp xúc với $(C')$ nên: "
                    f"$d(I, d) = R' \\Leftrightarrow \\frac{{ |{A}({a}) {'+' if B >= 0 else ''} {B}({b}) + m| }}{{\\sqrt{{ ({A})^2 + ({B})^2 }}}} = {R_prime} $ "
                    f"$\\Leftrightarrow \\frac{{ |{temp_sum} + m| }}{{ {deno} }} = {R_prime} \\Leftrightarrow |{temp_sum} + m| = {K}$.\\\\ "
                    f"Suy ra ${temp_sum} + m = {K}$ hoặc ${temp_sum} + m = -{K}$.\\\\ "
                    f"Vậy $m = {kq_list[1]}$ hoặc $m = {kq_list[0]}$ là các giá trị cần tìm."
                )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

