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


def bt_dang21_p4_b2_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ giao điểm cho d2
                x0 = random.randint(2, 5)
                y0 = random.randint(2, 5)
                k = x0 * y0
                a = y0
                b = x0

                # Random tọa độ điểm đi qua cho d3
                x1 = random.randint(1, 4)
                y1 = random.randint(1, 4)
                c = y1
                d = -x1

                # Tính kết quả
                T = a + b + c + d

                # Hàm xử lý chuỗi hiển thị tránh 1x, -1y
                def format_term(coef, var):
                    if coef == 1: return f"{var}"
                    if coef == -1: return f"- {var}"
                    if coef < 0: return f"- {-coef}{var}"
                    return f"{coef}{var}"

                c_str = "" if c == 1 else str(c)
                d_abs = abs(d)
                d_str = "" if d_abs == 1 else str(d_abs)

                # Tính toán tọa độ để vẽ đa giác màu trắng (miền nghiệm)
                # Giao điểm của d2 và d3
                x_int = (x0 * y0 * x1) / (y0 * x1 + x0 * y1)
                y_int = (x0 * y0 * y1) / (y0 * x1 + x0 * y1)

                # Tọa độ kéo dài 2 đầu của d2 và d3 để vẽ đường thẳng
                y_d2_start = (x0 * y0 + 2 * y0) / x0
                y_d2_end = (x0 * y0 - 7 * y0) / x0
                y_d3_start = -2 * y1 / x1
                y_d3_end = 7 * y1 / x1

                # Tọa độ đỉnh xa để đa giác trắng bao phủ toàn bộ vùng trên
                y_top = 100 * y1 / x1

                # Vẽ đồ thị bằng TikZ lồng trong LaTeX
                tikz_code = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
                \\clip (-2,-2) rectangle (7,7);
                \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (7,7);
                %% Miền nghiệm: x > 0, nằm trên d2 và d3
                \\fill[white] (0, {y0}) -- ({x_int}, {y_int}) -- (100, {y_top}) -- (0, {y_top}) -- cycle;
                \\draw[black] (-2, {y_d2_start}) -- (7, {y_d2_end});
                \\draw[black] (-2, {y_d3_start}) -- (7, {y_d3_end});
                \\draw[->] (-2,0) -- (7,0) node[below] {{$x$}};
                \\draw[->] (0,-2) -- (0,7) node[left] {{$y$}};
                \\node at (0,0) [below left] {{$O$}};
                \\foreach \\x in {{-1,1,2,3,4,5,6}} \\draw[shift={{(\\x,0)}}] (0pt,2pt) -- (0pt,-2pt) node[below] {{\\footnotesize $\\x$}};
                \\foreach \\y in {{-1,1,2,3,4,5,6}} \\draw[shift={{(0,\\y)}}] (2pt,0pt) -- (-2pt,0pt) node[left] {{\\footnotesize $\\y$}};
                \\node at ({x0 + 1}, {-y0/x0}) [above right] {{$d_2$}};
                \\node at ({x1 + 1}, {y1 + y1/x1}) [above left] {{$d_3$}};
                \\draw[dashed] ({x1},0) -- ({x1},{y1}) -- (0,{y1});
                \\fill ({x1},{y1}) circle (0.5pt);
                \\fill ({x0}, 0) circle (0.5pt);
                \\fill (0, {y0}) circle (0.5pt);
            \\end{{tikzpicture}}
            \\end{{center}}"""

                # Câu hỏi
                noidungcauhoi = f"Phần không bị gạch chéo biểu diễn miền nghiệm của hệ bất phương trình: $\\begin{{cases}} x > 0 \\\\ ax + by > {k} \\\\ cx + dy < 0 \\end{{cases}}$. Tính giá trị của biểu thức $T = a + b + c + d$. \n {tikz_code}"

                # Nội dung lời giải
                loigiai = (f"Trên mặt phẳng $Oxy$, $d_1: x = 0$ ($Oy$) \\\\ \n"
                           f"$d_2$ đi qua điểm $({x0}; 0), (0; {y0})$ nên ta có hệ $\\begin{{cases}} a \\cdot {x0} + b \\cdot 0 = {k} \\\\ a \\cdot 0 + b \\cdot {y0} = {k} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} a = {a} \\\\ b = {b} \\end{{cases}}$ nên $d_2: {format_term(a, 'x')} + {format_term(b, 'y')} = {k}$ \\\\ \n"
                           f"$d_3$ đi qua điểm $(0; 0), ({x1}; {y1})$ nên $d_3: {c_str}x - {d_str}y = 0$ \\\\ \n"
                           f"Biểu diễn từng miền nghiệm của mỗi bất phương trình trên mặt phẳng $Oxy$. \\\\ \n"
                           f"Miền không bị gạch chéo trong hình trên là phần giao của ba miền nghiệm của ba bất phương trình và cũng là phần biểu diễn miền nghiệm của hệ bất phương trình đã cho. \\\\ \n"
                           f"Vậy $a + b + c + d = {a} + {b} + {c} + ({d}) = {T}$.")

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\n\\loigiai{ \n'
                +str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

