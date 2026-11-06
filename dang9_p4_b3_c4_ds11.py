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


def bt_dang9_p4_b3_c4_ds11(self):
            # Khai báo biến ký hiệu cho SymPy
            x = symbols('x')

            # --- BƯỚC 1: NGẪU NHIÊN THÔNG SỐ ---
            a = random.choice([-2, -1, 1, 2, 3]) # Điểm xét tính liên tục
            n = random.randint(2, 4)             # Số mũ (x^2, x^3, x^4)
            # Biểu thức tử số: a^n - x^n
            tu_so = a**n - x**n
            mau_so = a - x
            f_left = tu_so / mau_so

            # Tính giới hạn trái tại a
            lim_left = limit(f_left, x, a, dir='-')

            # Ngẫu nhiên giá trị f(a). Có 50% cơ hội f(a) bằng giới hạn trái để hàm liên tục
            if random.random() > 0.5:
                f_right_val = lim_left
            else:
                f_right_val = lim_left + random.choice([-2, -1, 1, 2])

            # --- BƯỚC 2: XỬ LÝ LỜI GIẢI VÀ ĐÁP ÁN ---
            y_a = f_right_val
            lim_right = f_right_val

            # Xác định khẳng định đúng
            if lim_left == y_a:
                da_dung = f"Hàm số liên tục tại $x = {a}$"
                da_sai_1 = f"Hàm số gián đoạn tại $x = {a}$"
                da_sai_2 = f"Hàm số chỉ liên tục trái tại $x = {a}$"
                da_sai_3 = f"Hàm số không xác định tại $x = {a}$"
            else:
                da_dung = f"Hàm số liên tục phải tại $x = {a}$"
                da_sai_1 = f"Hàm số liên tục tại $x = {a}$"
                da_sai_2 = f"Hàm số liên tục trái tại $x = {a}$"
                da_sai_3 = f"Hàm số gián đoạn tại mọi điểm"

            # --- BƯỚC 3: BIÊN SOẠN NỘI DUNG ---
            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y = \begin{cases} \frac{%s}{%s}, & \text{khi } x < %s \\ %s, & \text{khi } x \ge %s \end{cases}$. Xét tính liên tục của hàm số tại tại $x = %s$.'''
                             % (latex(tu_so), latex(mau_so), latex(a), latex(f_right_val), latex(a),latex(a)))

            # Nội dung lời giải
            # Rút gọn phân thức để hiển thị trong lời giải
            f_rut_gon = simplify(tu_so / mau_so)

            loigiai = (r'''Ta có: $y(%s) = %s$. \\
                          Giới hạn bên phải: $\lim_{x \to %s^+} y = \lim_{x \to %s^+} %s = %s$. \\
                          Giới hạn bên trái: $\lim_{x \to %s^-} y = \lim_{x \to %s^-} \frac{%s}{%s} = \lim_{x \to %s^-} (%s) = %s$. \\
                          ''' % (latex(a), latex(y_a), 
                                 latex(a), latex(a), latex(f_right_val), latex(lim_right),
                                 latex(a), latex(a), latex(tu_so), latex(mau_so), latex(a), latex(f_rut_gon), latex(lim_left)))

            if lim_left == y_a:
                loigiai += f"Vì $\\lim_{{x \\to {a}^+}} y = \\lim_{{x \\to {a}^-}} y = y({a}) = {y_a}$ nên hàm số liên tục tại $x = {a}$."
            else:
                loigiai += f"Vì $\\lim_{{x \\to {a}^+}} y = y({a}) = {y_a} \\neq \\lim_{{x \\to {a}^-}} y$ nên hàm số liên tục phải tại $x = {a}$."

            # Trộn đáp án
            list_da = ['\\True ' + da_dung, da_sai_1, da_sai_2, da_sai_3]
            random.shuffle(list_da)

            # Xuất kết quả theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

