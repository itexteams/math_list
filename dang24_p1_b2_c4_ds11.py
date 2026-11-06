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


def bt_dang24_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1: Random giá trị a theo yêu cầu của bạn
            a_val = randint(2, 9)

            # B2: Tính toán b để x = -2 là nghiệm của tử số (điều kiện cần để có giới hạn hữu hạn)
            # (-2)^2 + a*(-2) + b = 0  => 4 - 2a + b = 0 => b = 2a - 4
            b_val = 2 * a_val - 4

            # B3: Tính giá trị giới hạn bên trái (L) tại x = -2 sau khi khử dạng 0/0
            # lim [ (x+2)(x+a-2) / (x-2)(x+2) ] = (-2 + a - 2) / (-2 - 2) = (a - 4) / -4
            limit_val = Rational(a_val - 4, -4)

            # B4: Để hàm số có giới hạn thì nhánh x >= -2 (x + k) phải có giá trị tại x = -2 bằng limit_val
            # -2 + k = limit_val => k = limit_val + 2
            k_val = limit_val + 2
            nhanh_phai_str = f"x + {latex(k_val)}" if k_val >= 0 else f"x {latex(k_val)}"

            # B5: Tính giá trị biểu thức yêu cầu: 3a - b
            res_val = 3 * a_val - b_val

            # --- Tạo đáp án trắc nghiệm ---
            da_dung = f'${res_val}$'
            # Tạo các đáp án nhiễu quanh kết quả đúng
            s = [f'${res_val + 2}$', f'${res_val - 2}$', f'${res_val + 4}$', f'${res_val + 1}$', f'${res_val - 3}$']
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = r'''Gọi $a, b$ là các giá trị để hàm số $f(x) = \begin{cases} \dfrac{x^2 + ax + b}{x^2 - 4}, & x < -2 \\ %s, & x \ge -2 \end{cases}$ có giới hạn hữu hạn khi $x$ dần tới $-2$. Giá trị $3a - b$ bằng''' % (nhanh_phai_str)

            # --- Đáp án ---
            da_d = r'\True ' + da_dung
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # --- Lời giải chi tiết ---
            loigiai = r'''Do hàm số $f(x)$ có giới hạn hữu hạn khi $x \to -2$ nên $x = -2$ là nghiệm của phương trình $x^2 + ax + b = 0$, do đó ta có $4 - 2a + b = 0 \Rightarrow b = 2a - 4$. \\
            Ta viết lại tử số: $x^2 + ax + 2a - 4 = (x + 2)(x + a - 2)$. \\
            Khi đó $\lim_{x \to -2^-} f(x) = \lim_{x \to -2^-} \dfrac{(x + 2)(x + a - 2)}{(x - 2)(x + 2)} = \dfrac{-2 + a - 2}{-2 - 2} = \dfrac{a - 4}{-4}$. \\
            Mặt khác $\lim_{x \to -2^+} f(x) = f(-2) = -2 + %s = %s$. \\
            Để tồn tại giới hạn hữu hạn thì: $\dfrac{a - 4}{-4} = %s \Leftrightarrow a = %s$. \\
            Với $a = %s \Rightarrow b = 2(%s) - 4 = %s$. \\
            Vậy giá trị của $3a - b = 3(%s) - %s = %s$.''' % (latex(k_val), latex(limit_val), latex(limit_val), a_val, a_val, a_val, b_val, a_val, b_val, res_val)

            # --- Xuất nội dung ---
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

