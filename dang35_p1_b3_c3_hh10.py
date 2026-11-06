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


def bt_dang35_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM DỮ LIỆU ---
                # Giả sử A(0; m). Để giống bài mẫu, ta chọn m dương.
                m = random.randint(1, 4) 
                # Chọn bán kính R của (C) sao cho R > m để a^2 = R^2 - m^2 > 0
                # Để đẹp, ta thường chọn R = 2m (như bài mẫu m=2, R=4)
                R = 2 * m
                R_prime = random.randint(1, 3) # Bán kính R' của (C')

                # Tính toán các hệ số của đường tròn (C): x^2 + y^2 + 2ax + c = 0
                # Với tâm I(-a, 0) và đi qua A(0, m)
                # Ta có R^2 = a^2 + 0 - c. Vì A thuộc (C) nên 0^2 + m^2 + 0 + c = 0 => c = -m^2
                # => a^2 = R^2 + c = R^2 - m^2
                c_val = -m**2
                a_sq = R**2 - m**2
                a_val = sqrt(a_sq) # Tâm I(-a, 0)

                # --- BƯỚC 2: TÍNH TOÁN LỜI GIẢI ---
                # Tâm I(-a, 0)
                I_coords = (-a_val, 0)
                # Điểm A(0, m)
                A_coords = (0, m)


                x_I_prime = (Rational(R_prime, R) * a_val)
                y_I_prime = m + (Rational(R_prime, R) * m)

                # Phương trình (C'): (x - x_I')^2 + (y - y_I')^2 = R'^2
                R_prime_sq = R_prime**2

                # --- BƯỚC 3: TẠO ĐÁP ÁN ---
                def get_eq(xi, yi, r2):
                    # Hàm hỗ trợ viết phương trình đường tròn từ tâm và R^2
                    part1 = "x" if xi == 0 else f"(x - {latex(xi)})" if xi > 0 else f"(x + {latex(-xi)})"
                    part2 = "y" if yi == 0 else f"(y - {latex(yi)})" if yi > 0 else f"(y + {latex(-yi)})"
                    return f"{part1}^2 + {part2}^2 = {r2}"

                da_dung = f"${get_eq(x_I_prime, y_I_prime, R_prime_sq)}$"

                # Tạo các đáp án nhiễu (thay đổi tâm hoặc bán kính)
                s = [
                    f"${get_eq(-x_I_prime, y_I_prime, R_prime_sq)}$",
                    f"${get_eq(x_I_prime, -y_I_prime, R_prime_sq)}$",
                    f"${get_eq(x_I_prime, y_I_prime, R_prime_sq + 2)}$",
                    f"${get_eq(x_I_prime + 1, y_I_prime, R_prime_sq)}$",
                    f"${get_eq(x_I_prime, y_I_prime - 1, R_prime_sq)}$"
                ]
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                # Phương trình (C) dạng x^2 + y^2 + 2ax + c = 0
                # Lưu ý: 2*a có thể chứa căn
                coeff_x = 2 * a_val
                eq_C = f"x^2 + y^2 + {latex(coeff_x)}x {c_val} = 0"
                eq_C = eq_C.replace("+ -", "- ").replace("- -", "+ ")

                noidungcauhoi = (f"Trong mặt phẳng $Oxy$, cho đường tròn $(C): {eq_C}$. Tia $Oy$ cắt $(C)$ tại $A$. "
                                 f"Phương trình đường tròn $(C')$ có bán kính $R'={R_prime}$ và tiếp xúc ngoài với $(C)$ tại $A$ là")

                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                loigiai = (f"Đường tròn $(C)$ có tâm $I({latex(-a_val)}; 0)$, bán kính $R={R}$.\\\\ "
                           f"Tọa độ $A$ là nghiệm hệ $\\begin{{cases}} {eq_C} \\\\ x = 0, y > 0 \\end{{cases}} \\Rightarrow A(0; {m})$.\\\\ "
                           f"Đường thẳng $IA$ đi qua $I$ và $A$. Vì $(C')$ tiếp xúc ngoài với $(C)$ tại $A$ nên tâm $I'$ của $(C')$ thuộc đường thẳng $IA$ "
                           f"và $A$ nằm giữa $I, I'$.\\\\ "
                           f"Ta có: "
                           f"$\\vec{{AI'}} = -\\frac{{R'}}{{R}}\\vec{{AI}} = -\\frac{{{R_prime}}}{{{R}}}({latex(-a_val)}; {latex(-m)}) = ({latex(x_I_prime)}; {latex(y_I_prime - m)})$.\\\\ "
                           f"Suy ra tâm $I'({latex(x_I_prime)}; {latex(y_I_prime)})$.\\\\ "
                           f"Vậy phương trình $(C')$ là: ${get_eq(x_I_prime, y_I_prime, R_prime_sq)}$.")

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

