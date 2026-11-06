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


def bt_dang8_p2_b2_c6_ds10(self):
            # Khai báo biến
            x = symbols('x')

            # B3: Random hệ số a (khác 0) và b
            # Tránh a = 0 để hàm số không suy biến thành đường thẳng
            a = random.choice([-3, -2, -1, 2, 3])
            b = random.randint(-5, 5)

            bt = a * x + b

            # Xử lý chuỗi hiển thị biểu thức để không bị lỗi dấu hoặc số 1
            if a == 1:
                term_ax = "- x"      
                term_a = ""          
                deriv_const = "- 1"
            elif a == -1:
                term_ax = "+ x"      
                term_a = "-"         
                deriv_const = "+ 1"
            elif a > 0:
                term_ax = f"- {a}x"
                term_a = f"{a}"
                deriv_const = f"- {a}"
            else:
                term_ax = f"+ {abs(a)}x"
                term_a = f"{a}"
                deriv_const = f"+ {abs(a)}"

            # =====================================================================
            # NỘI DUNG CÂU HỎI & CÁC Ý a, b, c, d
            # =====================================================================
            noidungcauhoi = f"Cho hàm số $f(x)=e^{{{latex(bt)}}} {term_ax}$."

            # ---------------------------------------------------------
            # (a) Nhận biết
            nb_da_1_d = '\\True Tập xác định của hàm số là $\\mathscr{D}=\\mathbb{R}$'
            nb_da_1_s = 'Tập xác định của hàm số là $\\mathscr{D}=(0;+\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = "Hàm số có tập xác định là $\\mathscr{D}=\\mathbb{R}$."

            # ---------------------------------------------------------
            # (b) Thông hiểu
            th_da_1_d = f"\\True Đạo hàm của hàm số là $f'(x)={term_a}e^{{{latex(bt)}}} {deriv_const}$"
            th_da_1_s = f"Đạo hàm của hàm số là $f'(x)={term_a}e^{{{latex(bt)}}} {term_ax}$" 
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = f"Ta có $f'(x)={term_a}e^{{{latex(bt)}}} {deriv_const}$."

            # ---------------------------------------------------------
            # (c) Vận dụng
            nghiem = Rational(-b, a)
            vd_da_1_d = f"\\True Tập nghiệm của bất phương trình $f'(x)>0$ là $\\left( {latex(nghiem)}; +\\infty \\right)$"
            vd_da_1_s = f"Tập nghiệm của bất phương trình $f'(x)>0$ là $\\left( -\\infty; {latex(nghiem)} \\right)$"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Logic lời giải: Dù a > 0 hay a < 0, kết quả bất phương trình x luôn lớn hơn -b/a
            if a > 0:
                loigiai_vd_1 = (f"Ta có \\\\\n"
                                f"$f'(x)>0 \\Leftrightarrow {term_a}e^{{{latex(bt)}}} {deriv_const} > 0 \\Leftrightarrow e^{{{latex(bt)}}} > 1$ \\\\\n"
                                f"$\\Leftrightarrow {latex(bt)} > 0 \\Leftrightarrow x > {latex(nghiem)}$. \\\\\n"
                                f"Vậy tập nghiệm của bất phương trình là $\\left( {latex(nghiem)}; +\\infty \\right)$.")
            else:
                loigiai_vd_1 = (f"Ta có \\\\\n"
                                f"$f'(x)>0 \\Leftrightarrow {term_a}e^{{{latex(bt)}}} {deriv_const} > 0 \\Leftrightarrow e^{{{latex(bt)}}} < 1$ \\\\\n"
                                f"$\\Leftrightarrow {latex(bt)} < 0 \\Leftrightarrow x > {latex(nghiem)}$. \\\\\n"
                                f"Vậy tập nghiệm của bất phương trình là $\\left( {latex(nghiem)}; +\\infty \\right)$.")

            # ---------------------------------------------------------
            # (d) Vận dụng cao
            gtct = 1 + b
            vdc_da_1_d = f"\\True Hàm số có giá trị cực tiểu là ${latex(gtct)}$"
            vdc_da_1_s = f"Hàm số có giá trị cực tiểu là ${latex(b)}$"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (f"Ta có bảng biến thiên \\\\\n"
                             f"\\begin{{tikzpicture}}\n"
                             f"\\tkzTabInit[espcl=2.5,lgt=1.5]\n"
                             f"{{$x$/1,$f'(x)$/0.7,$f(x)$/2.1}}\n"
                             f"{{$-\\infty$,${latex(nghiem)}$,$+\\infty$}}\n"
                             f"\\tkzTabLine{{,-,0,+}}\n"
                             f"\\tkzTabVar{{+/$+\\infty$,-/${latex(gtct)}$,+/$+\\infty$}}\n"
                             f"\\end{{tikzpicture}} \\\\\n"
                             f"Hàm số có giá trị cực tiểu là $f\\left({latex(nghiem)}\\right)={latex(gtct)}$.")

            # =====================================================================
            # XỬ LÝ ĐÁP ÁN RANDOM VÀ XUẤT TEX
            # =====================================================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi số câu Đúng nằm trong khoảng 1 đến 3
            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung chuẩn LaTeX
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choiceTFn \n'
                '{' + nb_da + '}\n'
                '{' + th_da + '}\n'
                '{' + vd_da + '}\n'
                '{' + vdc_da + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

