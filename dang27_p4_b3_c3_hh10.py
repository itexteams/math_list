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


def bt_dang27_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến SymPy
            x, y = symbols('x y')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Để bài toán có nghiệm đẹp, ta chọn hệ số a, b nhỏ
            a = random.randint(1, 4)
            b = random.randint(1, 4)
            # Chọn c sao cho không quá phức tạp, tránh c=0 để đường thẳng không đi qua gốc tọa độ
            c = random.randint(-15, 15)
            if c == 0: c = 5

            # Hàm xử lý hiển thị dấu phương trình đường thẳng ax + by + c = 0
            def format_line(a, b, c):
                term1 = f"{a}x" if a != 1 else "x"
                term2 = f" + {b}y" if b > 0 else f" - {abs(b)}y"
                if b == 1: term2 = " + y"
                elif b == -1: term2 = " - y"

                term3 = f" + {c}" if c > 0 else f" - {abs(c)}"
                if c == 0: term3 = ""
                return f"{term1}{term2}{term3} = 0"

            line_eq_display = format_line(a, b, c)

            # --- B1 & B2: Nghiên cứu và Viết lại bài toán ---
            # Tâm I(x0, y0) thuộc d => a*x0 + b*y0 + c = 0
            # Tiếp xúc Ox, Oy => |x0| = |y0| = R
            x0 = symbols('x0')
            # Trường hợp 1: y0 = x0
            sol1 = solve(a*x0 + b*x0 + c, x0)
            # Trường hợp 2: y0 = -x0
            sol2 = solve(a*x0 - b*x0 + c, x0)

            all_sols = []
            for s in sol1:
                all_sols.append((s, s)) # (x0, y0)
            for s in sol2:
                all_sols.append((s, -s))

            results = []
            for res_x, res_y in all_sols:
                r = Abs(res_x)
                if r != 0:
                    # Phương trình: (x-x0)^2 + (y-y0)^2 = r^2
                    eq = f"(x - {latex(res_x)})^2 + (y - {latex(res_y)})^2 = {latex(r**2)}"
                    # Làm đẹp dấu trừ: - - thành +
                    eq = eq.replace("- -", "+ ")
                    results.append(f"${eq}$")

            # Tạo nội dung câu hỏi
            noidungcauhoi = f"Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $d: {line_eq_display}$. Lập phương trình đường tròn tiếp xúc với hai trục tọa độ $Ox, Oy$ và có tâm nằm trên đường thẳng $d$."

            # Đáp án đúng (lấy tất cả các phương trình tìm được)
            da_dung = " và ".join(results)
            da_d = "\\True " + da_dung

            # Tạo đáp án nhiễu (giả lập bằng cách đổi dấu hoặc giá trị)
            da_s1 = da_dung.replace("x -", "x +").replace("y -", "y +")
            da_s2 = f"$(x - {a})^2 + (y - {b})^2 = {c**2}$"
            da_s3 = "Không có đường tròn nào thỏa mãn."

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = f"Gọi tâm đường tròn là $I(x_0; y_0)$. Vì đường tròn tiếp xúc với hai trục tọa độ nên $|x_0| = |y_0| = R > 0$. \\\\\n"
            loigiai += f"Suy ra $y_0 = x_0$ hoặc $y_0 = -x_0$. \\\\\n"
            loigiai += f"Mặt khác $I \\in d$ nên $a x_0 + b y_0 + c = 0$. \\\\\n"
            loigiai += f"Với $y_0 = x_0$, ta có: ${a}x_0 + {b}x_0 + ({c}) = 0 \\Rightarrow x_0 = {latex(sol1[0] if sol1 else 'none')}$. \\\\\n"
            loigiai += f"Với $y_0 = -x_0$, ta có: ${a}x_0 - {b}x_0 + ({c}) = 0 \\Rightarrow x_0 = {latex(sol2[0] if sol2 else 'none')}$. \\\\\n"
            loigiai += f"Vậy các phương trình đường tròn thỏa mãn là: {da_dung}."

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

