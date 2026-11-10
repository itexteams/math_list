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


def bt_dang2_p1_b2_c1_ds11(self):
        # Khai báo biến
        lisdang = ['1', '2', '3', '4', '5', '6']
        dang = random.choice(lisdang)

        # -------------------------------------------------------------------------
        # DẠNG 1: cos(a + b) = cos(a)cos(b) - sin(a)sin(b)
        # -------------------------------------------------------------------------
        if dang == '1':
            lisgoc = [30, 45, 60, 90]
            a_do = random.choice(lisgoc)
            lisgoc.remove(a_do)
            b_do = random.choice(lisgoc)

            a, b = a_do * pi / 180, b_do * pi / 180

            # Giá trị đúng
            val_d = cos(a + b)
            da = f'${latex(val_d)}$'

            # Các giá trị sai điển hình do nhầm công thức:
            # 1. Nhầm dấu công thức cos: cos(a)cos(b) + sin(a)sin(b) = cos(a-b)
            # 2. Nhầm sang công thức sin tổng: sin(a+b)
            # 3. Nhầm sang công thức sin hiệu: sin(a-b)
            # 4. Đổi dấu kết quả đúng
            # 5. Các giá trị đối xứng/lệch dấu khác
            sai_candidates = [
                cos(a - b),
                sin(a + b),
                sin(a - b),
                -val_d,
                -cos(a - b),
                cos(a) * cos(b)
            ]

            # Lọc phân biệt và khác đáp án đúng
            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            # Dự phòng nếu thiếu
            delta = Rational(1, 2)
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + Rational(1, 2)

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\cos \\left( {latex(a+b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\cos \\left( {latex(a+b)} \\right) = \\cos \\left( {latex(a)}+{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\cos {latex(a)} \\cos {latex(b)} - \\sin {latex(a)} \\sin {latex(b)}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(cos(a))} \\cdot {latex(cos(b))} - {latex(sin(a))} \\cdot {latex(sin(b))}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # DẠNG 2: cos(a - b) = cos(a)cos(b) + sin(a)sin(b)
        # -------------------------------------------------------------------------
        elif dang == '2':
            lisgoc = [30, 45, 60, 90]
            a_do = random.choice(lisgoc)
            lisgoc.remove(a_do)
            b_do = random.choice(lisgoc)

            a, b = a_do * pi / 180, b_do * pi / 180

            val_d = cos(a - b)
            da = f'${latex(val_d)}$'

            sai_candidates = [
                cos(a + b),
                sin(a - b),
                sin(a + b),
                -val_d,
                -cos(a + b),
                sin(a) * sin(b)
            ]

            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            delta = Rational(1, 2)
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + Rational(1, 2)

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\cos \\left( {latex(a-b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\cos \\left( {latex(a-b)} \\right) = \\cos \\left( {latex(a)}-{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\cos {latex(a)} \\cos {latex(b)} + \\sin {latex(a)} \\sin {latex(b)}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(cos(a))} \\cdot {latex(cos(b))} + {latex(sin(a))} \\cdot {latex(sin(b))}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # DẠNG 3: sin(a + b) = sin(a)cos(b) + cos(a)sin(b)
        # -------------------------------------------------------------------------
        elif dang == '3':
            lisgoc = [30, 45, 60, 90]
            a_do = random.choice(lisgoc)
            lisgoc.remove(a_do)
            b_do = random.choice(lisgoc)

            a, b = a_do * pi / 180, b_do * pi / 180

            val_d = sin(a + b)
            da = f'${latex(val_d)}$'

            sai_candidates = [
                sin(a - b),
                cos(a + b),
                cos(a - b),
                -val_d,
                -sin(a - b),
                sin(a) * cos(b)
            ]

            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            delta = Rational(1, 2)
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + Rational(1, 2)

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\sin \\left( {latex(a+b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\sin \\left( {latex(a+b)} \\right) = \\sin \\left( {latex(a)}+{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\sin {latex(a)} \\cos {latex(b)} + \\cos {latex(a)} \\sin {latex(b)}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(sin(a))} \\cdot {latex(cos(b))} + {latex(cos(a))} \\cdot {latex(sin(b))}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # DẠNG 4: sin(a - b) = sin(a)cos(b) - cos(a)sin(b)
        # -------------------------------------------------------------------------
        elif dang == '4':
            lisgoc = [30, 45, 60, 90]
            a_do = random.choice(lisgoc)
            lisgoc.remove(a_do)
            b_do = random.choice(lisgoc)

            a, b = a_do * pi / 180, b_do * pi / 180

            val_d = sin(a - b)
            da = f'${latex(val_d)}$'

            sai_candidates = [
                sin(a + b),
                cos(a - b),
                cos(a + b),
                -val_d,
                -sin(a + b),
                cos(a) * sin(b)
            ]

            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            delta = Rational(1, 2)
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + Rational(1, 2)

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\sin \\left( {latex(a-b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\sin \\left( {latex(a-b)} \\right) = \\sin \\left( {latex(a)}-{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\sin {latex(a)} \\cos {latex(b)} - \\cos {latex(a)} \\sin {latex(b)}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(sin(a))} \\cdot {latex(cos(b))} - {latex(cos(a))} \\cdot {latex(sin(b))}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # DẠNG 5: tan(a + b) = (tan a + tan b) / (1 - tan a * tan b)
        # -------------------------------------------------------------------------
        elif dang == '5':
            while True:
                lisgoc = [30, 45, 60]
                a_do = random.choice(lisgoc)
                lisgoc.remove(a_do)
                b_do = random.choice(lisgoc)
                if a_do + b_do != 90:  # Tránh tan(90) không xác định
                    break

            a, b = a_do * pi / 180, b_do * pi / 180

            val_d = (tan(a) + tan(b)) / (1 - tan(a) * tan(b))
            da = f'${latex(val_d)}$'

            # Sai do nhầm dấu tử/mẫu hoặc đảo tỉ số
            s1 = (tan(a) - tan(b)) / (1 + tan(a) * tan(b))  # tan(a - b)
            s2 = (tan(a) + tan(b)) / (1 + tan(a) * tan(b))  # nhầm dấu mẫu
            s3 = (tan(a) - tan(b)) / (1 - tan(a) * tan(b))  # nhầm dấu tử
            s4 = -val_d
            s5 = 1 / val_d

            sai_candidates = [s1, s2, s3, s4, s5]

            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            delta = 1
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + 1

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\tan \\left( {latex(a+b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\tan \\left( {latex(a+b)} \\right) = \\tan \\left( {latex(a)}+{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\dfrac{{\\tan {latex(a)}+\\tan {latex(b)}}}{{1-\\tan {latex(a)} \\tan {latex(b)}}}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\dfrac{{{latex(tan(a))}+{latex(tan(b))}}}{{1-{latex(tan(a))} \\cdot {latex(tan(b))}}}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # DẠNG 6: tan(a - b) = (tan a - tan b) / (1 + tan a * tan b)
        # -------------------------------------------------------------------------
        else:
            lisgoc = [30, 45, 60]
            a_do = random.choice(lisgoc)
            lisgoc.remove(a_do)
            b_do = random.choice(lisgoc)

            a, b = a_do * pi / 180, b_do * pi / 180

            val_d = (tan(a) - tan(b)) / (1 + tan(a) * tan(b))
            da = f'${latex(val_d)}$'

            # Sai do nhầm dấu:
            s1 = (tan(a) + tan(b)) / (1 - tan(a) * tan(b)) if (a_do + b_do != 90) else -val_d  # tan(a + b)
            s2 = (tan(a) - tan(b)) / (1 - tan(a) * tan(b))  # nhầm dấu mẫu
            s3 = (tan(a) + tan(b)) / (1 + tan(a) * tan(b))  # nhầm dấu tử
            s4 = -val_d
            s5 = 1 / val_d

            sai_candidates = [s1, s2, s3, s4, s5]

            unique_sai = []
            for s_val in sai_candidates:
                if simplify(s_val - val_d) != 0 and not any(simplify(s_val - u) == 0 for u in unique_sai):
                    unique_sai.append(s_val)

            delta = 1
            while len(unique_sai) < 3:
                cand = val_d + delta
                if simplify(cand - val_d) != 0 and not any(simplify(cand - u) == 0 for u in unique_sai):
                    unique_sai.append(cand)
                delta = -delta if delta > 0 else -delta + 1

            selected_sai = unique_sai[:3]
            das1, das2, das3 = [f'${latex(v)}$' for v in selected_sai]

            noidungcauhoi = f'Giá trị $\\tan \\left( {latex(a-b)} \\right)$ bằng'

            loigiai = (
                'Ta có \\\\ \n'
                f'\\hspace*{{1cm}} $\\tan \\left( {latex(a-b)} \\right) = \\tan \\left( {latex(a)}-{latex(b)} \\right)$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\dfrac{{\\tan {latex(a)}-\\tan {latex(b)}}}{{1+\\tan {latex(a)} \\tan {latex(b)}}}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= \\dfrac{{{latex(tan(a))}-{latex(tan(b))}}}{{1+{latex(tan(a))} \\cdot {latex(tan(b))}}}$\\\\ \n'
                f'\\hspace*{{2.35cm}} $= {latex(val_d)}$.'
            )

        # -------------------------------------------------------------------------
        # Đóng gói và xáo trộn đáp án
        # -------------------------------------------------------------------------
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Xuất câu trắc nghiệm
        content = (
            '\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
            '\\choice \n'
            '{' + str(list_1[0]) + '}\n'
            '{' + str(list_1[1]) + '}\n'
            '{' + str(list_1[2]) + '}\n'
            '{' + str(list_1[3]) + '}\n'
            '\\loigiai{' + str(loigiai) + '}\n'
            '\\end{ex}\n'
            '\\end{minipage}\n\n').replace('\\frac', '\\dfrac')

        return content

