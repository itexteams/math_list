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


def bt_dang21_p1_b4_c2_hh12(self):
            # 1. Tâm I(a; b; c)
            a, b, c = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # 2. Vector chỉ phương u(u1, u2, u3)
            u1 = randint(-3, 3)
            u2 = randint(-3, 3)
            u3 = randint(1, 3) # u3 phải khác 0

            # 3. Random tham số t trước để tọa độ giao điểm A là số nguyên
            t_gd = randint(-3, 3)
            z0 = -u3 * t_gd  # Tính z0 để khi z = z0 + u3*t = 0 thì t = t_gd
            x0 = randint(-5, 5)
            y0 = randint(-5, 5)

            # 4. Tọa độ giao điểm A(xa, ya, za)
            xa = x0 + u1 * t_gd
            ya = y0 + u2 * t_gd
            za = 0

            # 5. Tính bán kính R^2
            R2 = (xa - a)**2 + (ya - b)**2 + (za - c)**2

            # Hàm hỗ trợ viết pt mặt cầu với dấu ngoặc nhọn f-string được fix
            def format_sph(h, k, l, r2):
                def term(var, val):
                    if val == 0: return f"{var}^2"
                    # Dùng {{ }} để LaTeX hiển thị đúng { }
                    return f"({var} - {val})^2" if val > 0 else f"({var} + {-val})^2"
                return f"{term('x', h)} + {term('y', k)} + {term('z', l)} = {r2}"

            kq = format_sph(a, b, c, R2)

            # 6. Tạo đáp án đúng và nhiễu
            da_d = f"\\True ${kq}$"
            s = [
                f"${format_sph(a, b, c, R2 + randint(1, 5))}$",
                f"${format_sph(a, b, c, abs(R2 - randint(1, 5)))}$",
                f"${format_sph(-a, b, c, R2)}$",
                f"${format_sph(a, -b, c, R2)}$"
            ]

            s = list(set(s))
            if da_d in s: s.remove(da_d)
            random.shuffle(s)
            list_ans = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_ans)

            # 7. Xử lý chuỗi hiển thị hệ phương trình
            u1_s = f"+ {u1}t" if u1 > 0 else (f"- {-u1}t" if u1 < 0 else "")
            u2_s = f"+ {u2}t" if u2 > 0 else (f"- {-u2}t" if u2 < 0 else "")
            u3_s = f"+ {u3}t" if u3 > 0 else (f"- {-u3}t" if u3 < 0 else "")

            # CHÚ Ý: {{cases}} và {{matrix}} phải dùng ngoặc nhọn kép
            noidungcauhoi = (f"Trong không gian $Oxyz$, cho đường thẳng $d: \\begin{{cases}} x = {x0} {u1_s} \\\\ y = {y0} {u2_s} \\\\ z = {z0} {u3_s} \\end{{cases}}$ "
                             f"và điểm $I({a}; {b}; {c})$. Phương trình mặt cầu có tâm $I$ và đi qua giao điểm của $d$ với mặt phẳng $(Oxy)$ là")

            # CHÚ Ý: \\sqrt{{...}} dùng ngoặc nhọn kép để tránh lỗi "int + set"
            loigiai = (f"Phương trình mặt phẳng $(Oxy)$ là $z = 0$. \\\\\n"
                       f"Gọi $A$ là giao điểm của $d$ và $(Oxy)$. Thay $z=0$ vào phương trình $d$, ta được: \\\\\n"
                       f"${z0} {u3_s} = 0 \\Rightarrow t = {t_gd}$. \\\\\n"
                       f"Thay $t={t_gd}$ vào phương trình $d$, ta được $A({xa}; {ya}; {za})$. \\\\\n"
                       f"Bán kính mặt cầu là $R = IA = \\sqrt{{ ({xa} - {a})^2 + ({ya} - {b})^2 + ({za} - {c})^2 }} = \\sqrt{{{R2}}}$. \\\\\n"
                       f"Phương trình mặt cầu cần tìm là: ${kq}$.")

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n'
                       '\\choice \n'
                       '{' + list_ans[0] + '}\n'
                       '{' + list_ans[1] + '}\n'
                       '{' + list_ans[2] + '}\n'
                       '{' + list_ans[3] + '}\n'
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content

