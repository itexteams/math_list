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


def bt_dang26_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số liệu bài toán
                x0 = random.choice([2, 3, 4, 5])
                y0 = random.choice([-4, -3, -2])

                # Phương trình đường thẳng đi qua (x0, 0) và (0, y0): y0*x + x0*y - x0*y0 = 0
                # Vì y0 < 0 nên nhân cả 2 vế với -1: (-y0)*x + (-x0)*y + x0*y0 = 0
                a_raw = -y0
                b_raw = -x0
                c_raw = x0 * y0

                # Rút gọn các hệ số theo ước chung lớn nhất
                g = math.gcd(a_raw, math.gcd(abs(b_raw), abs(c_raw)))
                a = a_raw // g
                b = b_raw // g
                c = c_raw // g

                # Random dấu bất phương trình
                op = random.choice(['<=', '>='])

                # Biểu diễn các hệ số dưới dạng chuỗi
                if a == 1:
                    str_a = "x"
                else:
                    str_a = f"{a}x"

                if b == -1:
                    str_b = "- y"
                elif b == 1:
                    str_b = "+ y"
                elif b < 0:
                    str_b = f"- {abs(b)}y"
                else:
                    str_b = f"+ {b}y"

                if c < 0:
                    str_c = f"- {abs(c)}"
                else:
                    str_c = f"+ {c}"

                bpt_str = f"{str_a} {str_b} {str_c}"

                if op == '<=':
                    bpt_tex = f"{bpt_str} \\le 0"
                    op_tex = "\\le"
                    is_correct = "mệnh đề đúng"
                    contains_str = "chứa gốc tọa độ $O(0;0)$"
                    correct_fig = "H1"
                    unshaded_desc = "chứa gốc tọa độ $O(0;0)$"
                else:
                    bpt_tex = f"{bpt_str} \\ge 0"
                    op_tex = "\\ge"
                    is_correct = "mệnh đề sai"
                    contains_str = "không chứa gốc tọa độ $O(0;0)$"
                    correct_fig = "H3"
                    unshaded_desc = "không chứa gốc tọa độ $O(0;0)$"

                # Hàm vẽ hình bằng TikZ (đã tăng kích thước khung và trục thêm 1 đơn vị)
                def draw_tikz(x_val, y_val, shade_above, label_str):
                    m = -y_val / x_val
                    y_m6 = -6 * m + y_val
                    y_p6 = 6 * m + y_val

                    if shade_above:
                        fill_path = f"(-6,{y_m6:.2f}) -- (6,{y_p6:.2f}) -- (6,10) -- (-6,10) -- cycle"
                    else:
                        fill_path = f"(-6,{y_m6:.2f}) -- (6,{y_p6:.2f}) -- (6,-10) -- (-6,-10) -- cycle"

                    x_node_pos = "below" if y_val > 0 else "above"
                    y_node_pos = "left"

                    tikz = (
                        "\\begin{tikzpicture}[scale=0.38, >=stealth, line width=1pt]\n"
                        "\\begin{scope}\n"
                        "\\clip (-3.2,-4.2) rectangle (5.2,4.2);\n"
                        "\\fill[pattern=north west lines, pattern color=gray!60] " + fill_path + ";\n"
                        f"\\draw[line width=1pt] (-6,{y_m6:.2f}) -- (6,{y_p6:.2f});\n"
                        "\\end{scope}\n"
                        "\\draw[->, line width=1pt] (-3.2,0) -- (5.2,0) node[above]{$x$};\n"
                        "\\draw[->, line width=1pt] (0,-4.2) -- (0,4.2) node[right]{$y$};\n"
                        "\\node at (-0.5,-0.5) {$O$};\n"
                        f"\\draw[line width=1pt] ({x_val},0.1) -- ({x_val},-0.1) node[{x_node_pos}]{{${x_val}$}};\n"
                        f"\\draw[line width=1pt] (0.1,{y_val}) -- (-0.1,{y_val}) node[{y_node_pos}]{{${y_val}$}};\n"
                        f"\\node[below=0.2cm] at (1,-4.2) {{\\textbf{{{label_str}}}}};\n"
                        "\\end{tikzpicture}"
                    )
                    return tikz

                # Tạo 4 hình vẽ H1, H2, H3, H4
                h1_tikz = draw_tikz(x0, y0, False, "H1")
                h2_tikz = draw_tikz(x0, -y0, True, "H2")
                h3_tikz = draw_tikz(x0, y0, True, "H3")
                h4_tikz = draw_tikz(x0, -y0, False, "H4")

                # Nội dung câu hỏi
                noidungcauhoi = (
                    "Hình vẽ nào sau đây biểu diễn miền nghiệm của bất phương trình $%s$ (miền không tô đậm kể cả bờ)?\n"
                    "\\begin{center}\n"
                    "\\begin{tabular}{cccc}\n"
                    "%s &\n %s &\n %s &\n %s\n"
                    "\\end{tabular}\n"
                    "\\end{center}"
                    % (bpt_tex, h1_tikz, h2_tikz, h3_tikz, h4_tikz)
                )

                # Các đáp án trắc nghiệm
                du = ['$%s$' % correct_fig]
                da = random.choice(du)

                s = ['$H1$', '$H2$', '$H3$', '$H4$']
                s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    "Đường thẳng bờ $d: %s = 0$ đi qua hai điểm $(%s; 0)$ và $(0; %s)$.\\\\ \n"
                    "Do đó loại các hình biểu diễn đường thẳng không đi qua hai điểm này (hình H2 và H4).\\\\ \n"
                    "Thay tọa độ gốc tọa độ $O(0;0)$ vào bất phương trình $%s$, ta được:\\\\ \n"
                    "$%s \\cdot 0 %s %s \\cdot 0 %s %s = %s %s 0$ (%s).\\\\ \n"
                    "Do đó miền nghiệm của bất phương trình %s.\\\\ \n"
                    "Quan sát các hình H1 và H3, ta thấy miền không tô đậm của hình %s %s.\\\\ \n"
                    "Vậy hình %s biểu diễn miền nghiệm của bất phương trình đã cho."
                    % (
                        bpt_str, x0, y0,
                        bpt_tex,
                        a, "-" if b < 0 else "+", abs(b), "-" if c < 0 else "+", abs(c), c, op_tex, is_correct,
                        contains_str,
                        correct_fig, unshaded_desc,
                        correct_fig
                    )
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

