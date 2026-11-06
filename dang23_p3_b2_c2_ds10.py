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


def bt_dang23_p3_b2_c2_ds10(self):
            # Khai báo biến
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

                # Vẽ đồ thị bằng TikZ lồng trong LaTeX
                tikz_code = f"""\\begin{{center}}
                \\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
                \\clip (-2,-2) rectangle (7,7);
                \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (7,7);
                \\fill[white] (0,-2) rectangle (7,7);
                \\fill[pattern=north east lines, pattern color=black] (-2, {{(-{a}*(-2)+{k})/{b}}}) -- (7, {{(-{a}*(7)+{k})/{b}}}) -- (7,-2) -- (-2,-2) -- cycle;
                \\fill[pattern=north east lines, pattern color=black] (-2, {{(-{c}*(-2))/{d}}}) -- (7, {{(-{c}*(7))/{d}}}) -- (7,-2) -- (-2,-2) -- cycle;
                \\draw[->] (-2,0) -- (7,0) node[below] {{$x$}};
                \\draw[->] (0,-2) -- (0,7) node[left] {{$y$}};
                \\node at (0,0) [below left] {{$O$}};
                \\draw[black] (-2,0) -- (7,0);
                \\draw[black] (0,-2) -- (0,7);
                \\draw[black] (-1, {{(-{a}*(-1)+{k})/{b}}}) -- (7, {{(-{a}*(7)+{k})/{b}}});
                \\draw[black] (-1, {{(-{c}*(-1))/{d}}}) -- (7, {{(-{c}*(7))/{d}}});
                \\coordinate (P) at ({x1},{y1});
                \\fill (0,0) circle (1pt);
                \\fill (P) circle (1pt);
                \\draw[dashed, thin] ({x1},0) node[below] {{${x1}$}} -- (P) -- (0,{y1}) node[left] {{${y1}$}};
                \\end{{tikzpicture}}
                \\end{{center}}"""

                # Câu hỏi
                noidungcauhoi = f"Phần không bị tô màu biểu diễn miền nghiệm của hệ bất phương trình: $\\begin{{cases}} x > 0 \\\\ ax + by > {k} \\\\ cx + dy < 0 \\end{{cases}}$. Giá trị của biểu thức $T = a + b + c + d$ bằng bao nhiêu? \n {tikz_code}"


                # Nội dung lời giải
                loigiai = (f"Trên mặt phẳng $Oxy$, $d_1: x = 0$ ($Oy$) \\\\ \n"
                           f"$d_2$ đi qua điểm $({x0}; 0), (0; {y0})$ nên ta có hệ $\\begin{{cases}} a \\cdot {x0} + b \\cdot 0 = {k} \\\\ a \\cdot 0 + b \\cdot {y0} = {k} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} a = {a} \\\\ b = {b} \\end{{cases}}$ nên $d_2: {format_term(a, 'x')} + {format_term(b, 'y')} = {k}$ \\\\ \n"
                           f"$d_3$ đi qua điểm $(0; 0), ({x1}; {y1})$ nên $d_3: {c_str}x - {d_str}y = 0$ \\\\ \n"
                           f"Biểu diễn từng miền nghiệm của mỗi bất phương trình trên mặt phẳng $Oxy$. \\\\ \n"
                           f"Miền không bị tô màu trong hình trên là phần giao của ba miền nghiệm của ba bất phương trình và cũng là phần biểu diễn miền nghiệm của hệ bất phương trình đã cho. \\\\ \n"
                           f"Vậy $a + b + c + d = {a} + {b} + {c} + ({d}) = {T}$.")

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(T))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

