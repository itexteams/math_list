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


def bt_dang3_p2_b2_c1_ds10(self):
            # Khai báo biến
            # 1. Tạo tập hợp M = {x thuộc N | start <= x <= end}
            start_val = random.randint(-2, 0)
            end_val = random.randint(2, 4)
            # Tập M thực tế (chỉ lấy số tự nhiên)
            M_set = {i for i in range(start_val, end_val + 1) if i >= 0}
            M_list_sorted = sorted(list(M_set))
            M_latex = "\\{" + "; ".join(map(str, M_list_sorted)) + "\\}"

            # 2. Tạo tập hợp N (Ngẫu nhiên có phần tử âm và phần tử chung với M)
            N_set = {start_val, 0, end_val} # Đảm bảo có phần tử âm và phần tử biên
            N_latex = "\\{" + "; ".join(map(str, sorted(list(N_set)))) + "\\}"

            # 3. Tính toán các phép toán tập hợp chuẩn
            inter_true = M_set.intersection(N_set)
            union_true = M_set.union(N_set)
            diff_true = M_set.difference(N_set)

            def to_latex_set(s):
                if not s: return "\\emptyset"
                return "\\{" + "; ".join(map(str, sorted(list(s)))) + "\\}"

            # ================= BƯỚC 2: NỘI DUNG CÂU HỎI =================
            noidungcauhoi = (f"Cho hai tập hợp $M = \\{{x \\in \\mathbb{{N}} | {start_val} \\le x \\le {end_val} \\}}$, "
                             f"$N = {N_latex}$.")

            # --- Ý a) Liệt kê phần tử ---
            a_is_true = random.choice([True, False])
            if a_is_true:
                nb_da_1 = f"\\True Viết lại tập $M$ bằng cách liệt kê các phần tử, ta có $M = {M_latex}$."
            else:
                # Sai lầm phổ biến: lấy cả số âm
                M_wrong = "\\{" + "; ".join(map(str, range(start_val, end_val + 1))) + "\\}"
                nb_da_1 = f"Viết lại tập $M$ bằng cách liệt kê các phần tử, ta có $M = {M_wrong}$"
            loigiai_nb_1 = f"Vì $x \\in \\mathbb{{N}}$ nên ta chỉ lấy các số nguyên không âm. Vậy $M = {M_latex}$"

            # --- Ý b) Phép Giao ---
            b_is_true = random.choice([True, False])
            inter_res = to_latex_set(inter_true)
            if b_is_true:
                th_da_1 = f"\\True $M \\cap N = {inter_res}$"
            else:
                th_da_1 = f"$M \\cap N = {to_latex_set(union_true)}$" # Sai: nhầm thành hợp
            loigiai_th_1 = f"Giao của hai tập hợp là các phần tử chung: $M \\cap N = {inter_res}$."

            # --- Ý c) Phép Hợp ---
            c_is_true = random.choice([True, False])
            union_res = to_latex_set(union_true)
            if c_is_true:
                vd_da_1 = f"\\True $M \\cup N = {union_res}$"
            else:
                vd_da_1 = f"$M \\cup N = {inter_res}$" # Sai: nhầm thành giao
            loigiai_vd_1 = f"Hợp của hai tập hợp là tất cả phần tử của cả hai: $M \\cup N = {union_res}$."

            # --- Ý d) Phép Hiệu ---
            d_is_true = random.choice([True, False])
            diff_res = to_latex_set(diff_true)
            if d_is_true:
                vdc_da_1 = f"\\True $M \\setminus N = {diff_res}$"
            else:
                vdc_da_1 = f"$M \\setminus N = {to_latex_set({start_val})}$" # Sai: lấy nhầm phần tử thuộc N
            loigiai_vdc_1 = f"Hiệu $M \\setminus N$ là các phần tử thuộc $M$ nhưng không thuộc $N$: $M \\setminus N = {diff_res}$."

            # ================= BƯỚC 3: XỬ LÝ TRÌNH BÀY (THEO MẪU) =================

            # Gom nhóm theo cấu trúc mẫu của bạn
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất content
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

