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


def bt_dang37_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # Chọn hoành độ 2 giao điểm Ox là x1 và x2 (nguyên)
                x1 = random.randint(-5, 5)
                x2 = x1 + random.randint(1, 4) # Đảm bảo x2 khác x1

                # Chọn tọa độ điểm M(xm; ym) sao cho không nằm trên Ox và tạo ra số đẹp
                xm = x2 + random.randint(1, 2)
                # Giả định a là số nguyên đẹp (ví dụ từ -3 đến 3, khác 0)
                a_fix = random.choice([-3, -2, -1, 1, 2, 3])
                # Tính ym dựa trên công thức phân tích: y = a(x-x1)(x-x2)
                ym = a_fix * (xm - x1) * (xm - x2)

                # Thiết lập hệ phương trình để giải (giống logic trong ảnh)
                a, b, c = symbols('a b c')
                eq1 = xm**2 * a + xm * b + c - ym
                eq2 = x1**2 * a + x1 * b + c
                eq3 = x2**2 * a + x2 * b + c

                sol = solve((eq1, eq2, eq3), (a, b, c))
                res_a = sol[a]
                res_b = sol[b]
                res_c = sol[c]

                # Phương trình Parabol đúng
                def format_poly(a, b, c):
                    res = f"{latex(a)}x^2"
                    if b > 0: res += f"+{latex(b)}x"
                    elif b < 0: res += f"{latex(b)}x"

                    if c > 0: res += f"+{latex(c)}"
                    elif c < 0: res += f"{latex(c)}"
                    return res

                da_dung = f"$y = {format_poly(res_a, res_b, res_c)}$"

                # Bước 4: Điều chỉnh các phương án sai
                s = []
                while len(s) < 3:
                    # Tạo phương án sai bằng cách thay đổi hệ số a, b hoặc c
                    wa = res_a + random.choice([-1, 1, 2])
                    wb = res_b + random.randint(-2, 2)
                    wc = res_c + random.randint(-2, 2)
                    if wa == 0: wa = 1
                    fake_da = f"$y = {format_poly(wa, wb, wc)}$"
                    if fake_da != da_dung and fake_da not in s:
                        s.append(fake_da)

                das1, das2, das3 = s

                # Câu hỏi
                noidungcauhoi = (f"Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó đi qua điểm $M({xm}; {ym})$, "
                                 f"cắt trục $Ox$ tại hai điểm có hoành độ lần lượt là ${x1}$ và ${x2}$.")

                # Các đáp án
                da_d = '\\True ' + str(da_dung)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt mẫu trong ảnh)
                loigiai = (f"Gọi $E$ và $F$ là hai giao điểm của $(P)$ với trục $Ox$ có hoành độ lần lượt là ${x1}$ và ${x2}$. "
                           f"Suy ra $E({x1}; 0), F({x2}; 0)$.\\\\ "
                           f"Theo giả thiết $(P)$ đi qua ba điểm $M, E, F$ nên ta có: "
                           f"$\\begin{{cases}} {xm**2}a + {xm}b + c = {ym} \\\\ {x1**2}a + {x1}b + c = 0 \\\\ {x2**2}a + {x2}b + c = 0 \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} a = {latex(res_a)} \\\\ b = {latex(res_b)} \\\\ c = {latex(res_c)} \\end{{cases}}$ "
                           f"\\\\ Vậy $(P): y = {format_poly(res_a, res_b, res_c)}$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

