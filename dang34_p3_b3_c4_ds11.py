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


def bt_dang34_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC RANDOM THÔNG SỐ ---
                t0 = random.randint(3, 10)  # Thời điểm thay đổi (giây)
                k1 = random.randint(1, 5)   # Hệ số t^2 giai đoạn 1
                k2 = random.randint(5, 20)  # Hệ số t giai đoạn 1
                k3 = random.randint(2, 10)  # Hệ số t giai đoạn 2

                # --- TÍNH TOÁN GIÁ TRỊ a ---
                # S_left = k1*t0^2 + k2*t0
                # S_right = a*t0^2 + k3*t0
                # a = (k1*t0^2 + k2*t0 - k3*t0) / t0^2
                s_t0 = k1 * (t0**2) + k2 * t0
                tu_so = s_t0 - k3 * t0
                mau_so = t0**2

                a_rational = Rational(tu_so, mau_so)
                a_float = float(a_rational)

                # Định dạng hiển thị kết quả (lấy 1 hoặc 2 chữ số thập phân)
                if a_float.is_integer():
                    kq_str = str(int(a_float))
                else:
                    kq_str = str(round(a_float, 2)).replace('.', ',')

                # --- TẠO ĐÁP ÁN ---
                kq_chinh_xac = round(a_float, 2)
                da_dung = f"${kq_str}$"

                # Tạo các đáp án nhiễu
                s = []
                while len(s) < 3:
                    nhieu = round(kq_chinh_xac + random.choice([-2, -1.5, -1, 0.5, 1, 1.5, 2, 3]), 2)
                    nhieu_str = f"${str(nhieu).replace('.', ',')}$"
                    if nhieu_str != da_dung and nhieu_str not in s:
                        s.append(nhieu_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # --- NỘI DUNG CÂU HỎI (LATEX) ---
                noidungcauhoi = (
                    f"Một chuyển động thẳng biến đổi đều trong ${t0}$ giây đầu có phương trình đường đi là "
                    f"$s(t) = {k1}t^2 + {k2}t$, sau đó tiếp tục chuyển động theo phương trình $S(t) = at^2 + {k3}t$ "
                    f"trong đó $s$ tính bằng mét, $t$ tính bằng giây. Giá trị của $a$ bằng bao nhiêu?"
                )

                # --- NỘI DUNG LỜI GIẢI (LATEX) ---
                loigiai = (
                    f"Ta có phương trình của chuyển động là $S(t) = \\begin{{cases}} {k1}t^2 + {k2}t & \\text{{khi }} 0 \\le t \\le {t0} \\\\ at^2 + {k3}t & \\text{{khi }} t > {t0} \\end{{cases}}$. \\\\\n"
                    f"Vì đây là phương trình của 1 chuyển động nên $S(t)$ là hàm số liên tục. \\\\\n"
                    f"Hàm số $S(t)$ liên tục trên các khoảng $(0;{t0})$ và $({t0};+\\infty)$, để hàm số $S(t)$ liên tục thì nó phải liên tục tại $t = {t0}$. \\\\\n"
                    f"$\\lim_{{t \\to {t0}^-}} S(t) = \\lim_{{t \\to {t0}^-}} ({k1}t^2 + {k2}t) = {s_t0}$, "
                    f"$\\lim_{{t \\to {t0}^+}} S(t) = \\lim_{{t \\to {t0}^+}} (at^2 + {k3}t) = {t0**2}a + {k3*t0}$, $S({t0}) = {s_t0}$. \\\\\n"
                    f"Hàm số liên tục tại $t = {t0}$ khi $\\lim_{{t \\to {t0}^-}} S(t) = \\lim_{{t \\to {t0}^+}} S(t) = {s_t0} "
                    f"\\Leftrightarrow {t0**2}a + {k3*t0} = {s_t0} \\Leftrightarrow a = {kq_str}$. \\\\\n"
                    f"Vậy $a = {kq_str}$."
                )

                # --- XUẤT KẾT QUẢ ---
                list_da = ['\\True ' + da_dung, das1, das2, das3]
                random.shuffle(list_da)
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq_str))

                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + noidungcauhoi +dapan+ '\n'
                    '\\loigiai{' + loigiai + '}\n'
                    '\\end{ex}\n \\end{minipage} \n' )
            return content 

