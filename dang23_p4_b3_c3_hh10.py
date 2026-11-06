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


def bt_dang23_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Ta sẽ cố định bán kính và điều chỉnh khoảng cách từ tâm đến đường thẳng.

            def generate_problem():
                x, y = symbols('x y')

                # 1. Tạo tâm I(a, b) ngẫu nhiên
                a = random.randint(-4, 4)
                b = random.randint(-4, 4)

                # 2. Tạo đường thẳng d: Ax + By + C = 0
                # Để vuông góc dễ dàng, ta chọn A, B là các số nguyên nhỏ
                A = random.choice([-2, -1, 1, 2])
                B = random.choice([-2, -1, 1, 2])
                if A == 0 and B == 0: A = 1 # Tránh trường hợp cả 2 bằng 0

                # 3. Chọn R^2 = 10 (giống đề bài mẫu để có căn đẹp khi giải hệ)
                R_sq = 10

                # 4. Tìm C_const sao cho d(I, d) < R
                # Khoảng cách h = |A*a + B*b + C| / sqrt(A^2 + B^2)
                # Ta chọn h sao cho h^2 < 10. Ví dụ h = 4/sqrt(5) => h^2 = 16/5 = 3.2 < 10
                sum_sq = A**2 + B**2
                # Tính C_const để tử số bằng một giá trị cố định (ví dụ 4)
                target_num = 4 
                C_const = target_num - (A*a + B*b)

                # Đường thẳng d
                d_expr = A*x + B*y + C_const

                # Đường tròn (C)
                # Lưu ý: Viết (y - b) để đúng dạng (y - (-2)) = y + 2
                circle_expr = (x - a)**2 + (y - b)**2 - R_sq

                # 5. Tìm đường trung trực Delta qua I(a,b) và vuông góc d
                # d có cp (B, -A) -> Delta có cp (A, B) -> pttq: B(x-a) - A(y-b) = 0
                delta_expr = B*(x - a) - A*(y - b)
                delta_simplified = simplify(delta_expr)

                # 6. Giải hệ tìm tọa độ C
                sol = solve([delta_simplified, circle_expr], [x, y])

                # Chuyển tọa độ sang dạng latex
                pts = []
                for s in sol:
                    pts.append(f"C({latex(s[0])}; {latex(s[1])})")

                da_dung = f"${pts[0]}$ hoặc ${pts[1]}$"

                # Tạo đáp án nhiễu
                da_s1 = f"${pts[0]}$"
                da_s2 = f"${pts[1]}$"
                da_s3 = f"$C(0;0)$ hoặc ${pts[0]}$"

                # Nội dung câu hỏi
                # Xử lý hiển thị đường thẳng d và đường tròn (C)
                # Thay thế các cụm '+ -' thành '-' để công thức chuẩn
                d_str = latex(d_expr).replace('+ -', '- ')

                # Chuẩn hóa hiển thị (y - b) trong phương trình đường tròn
                y_part = f"(y - {b})" if b < 0 else f"(y - {b})"
                # Sympy latex đôi khi gộp (y - -2) thành (y + 2), ta để nguyên logic đề bài
                c_str = f"(x - {a})^2 + (y - {b})^2 = {R_sq}"
                c_str = c_str.replace('- -', '+ ')

                noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường thẳng $d: {d_str} = 0$ "
                                 f"và đường tròn $(C): {c_str}$. Chứng minh $(d)$ cắt $(C)$ tại hai điểm phân biệt $A, B$. "
                                 f"Tìm tọa độ điểm $C$ thuộc $(C)$ sao cho tam giác $ABC$ cân tại $C$.")

                # Nội dung lời giải
                dist_num = abs(A*a + B*b + C_const)
                loigiai = (f"Đường tròn $(C)$ có tâm $I({a}; {b})$, bán kính $R = \\sqrt{{{R_sq}}}$. Ta có: \\\\"
                           f"$d(I,d) = \\frac{{|{A} \\cdot ({a}) + {B} \\cdot ({b}) + {C_const}|}}{{\\sqrt{{{A}^2 + {B}^2}}}} = "
                           f"\\frac{{{dist_num}}}{{\\sqrt{{{sum_sq}}}}} < R$. \\\\"
                           f"Điều đó chứng tỏ $d$ cắt $(C)$ tại hai điểm phân biệt $A, B$. \\\\"
                           f"Vì $AB$ là dây cung của $(C)$ nên đường trung trực $\\Delta$ của đoạn thẳng $AB$ qua tâm $I$ và vuông góc với $d$. \\\\"
                           f"Phương trình $\\Delta: {latex(delta_simplified)} = 0$. \\\\"
                           f"Tam giác $ABC$ cân tại $C$ nên $C \\in \\Delta$. Hơn nữa $C \\in (C)$ nên tọa độ $C$ thỏa mãn hệ: \\\\"
                           f"$\\begin{{cases}} {latex(delta_simplified)} = 0 \\\\ {c_str} = {R_sq} \\end{{cases}} "
                           f"\\Leftrightarrow \\left[ \\begin{{array}}{{l}} x = {latex(sol[0][0])}, y = {latex(sol[0][1])} \\\\ x = {latex(sol[1][0])}, y = {latex(sol[1][1])} \\end{{array}} \\right.$ \\\\"
                           f"Vậy ${pts[0]}$ hoặc ${pts[1]}$ thỏa mãn yêu cầu bài toán.")

                return noidungcauhoi, da_dung, da_s1, da_s2, da_s3, loigiai

            # B2: Xuất kết quả theo mẫu
            noidungcauhoi, da_d_raw, das1, das2, das3, loigiai = generate_problem()

            da_d = ('\\True ' + str(da_d_raw))
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

