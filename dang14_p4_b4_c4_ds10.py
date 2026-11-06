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


def bt_dang14_p4_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x_sym = symbols('x')

            def generate_question():
                # --- BƯỚC 1: RANDOM HỆ SỐ ĐỂ ĐẢM BẢO NGHIỆM ĐẸP ---
                # Phương trình dạng: x - d = sqrt(ax^2 + bx + c)
                # Chọn d và nghiệm x0 sao cho x0 >= d để nghiệm đó có thể nhận được
                d = random.randint(-3, 3)
                x0 = d + random.randint(0, 5) # Đảm bảo thỏa mãn điều kiện x >= d

                # Chọn hệ số a (thường là 2 hoặc 3 để khác với hệ số x^2 sau khi bình phương)
                a = random.choice([2, 3, 5])

                # Chọn hệ số b ngẫu nhiên
                b = random.randint(-10, 10)

                # Tính c sao cho x0 là nghiệm của: a*x0^2 + b*x0 + c = (x0 - d)^2
                # c = (x0 - d)^2 - a*x0^2 - b*x0
                c = (x0 - d)**2 - a*x0**2 - b*x0

                expr_inside = a*x_sym**2 + b*x_sym + c

                # --- BƯỚC 2: GIẢI TOÁN BẰNG SYMPY ---
                # Phương trình gốc: x - sqrt(expr_inside) = d
                eq = x_sym - sqrt(expr_inside) - d
                solutions = solve(eq, x_sym)
                # Lọc lấy nghiệm thực
                real_solutions = [sol for sol in solutions if sol.is_real]
                num_sol = len(real_solutions)

                # --- BƯỚC 3: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = f"Tìm số nghiệm của phương trình sau $x - \\sqrt{{{latex(expr_inside)}}} = {d}$."

                # Đáp án đúng
                da_d = f"\\True {num_sol}"

                # Tạo các đáp án sai ngẫu nhiên (0, 1, 2, 3)
                wrong_options = {0, 1, 2, 3}
                if num_sol in wrong_options:
                    wrong_options.remove(num_sol)

                list_wrong = random.sample(list(wrong_options), 3)
                list_1 = [da_d, str(list_wrong[0]), str(list_wrong[1]), str(list_wrong[2])]
                random.shuffle(list_1)

                # --- BƯỚC 4: LỜI GIẢI CHI TIẾT (FIXED LATEX) ---
                vphai = x_sym - d
                vphai_sq = expand(vphai**2)
                pt_he_qua = simplify(expr_inside - vphai_sq)

                loigiai = f"""
                $x - \\sqrt{{{latex(expr_inside)}}} = {d} \\Leftrightarrow \\sqrt{{{latex(expr_inside)}}} = {latex(vphai)}$ \\\\
                $\\Leftrightarrow \\begin{{cases}} {latex(vphai)} \\ge 0 \\\\ {latex(expr_inside)} = ({latex(vphai)})^2 \\end{{cases}}$
                $\\Leftrightarrow \\begin{{cases}} x \\ge {d} \\\\ {latex(expr_inside)} = {latex(vphai_sq)} \\end{{cases}}$ \\\\
                $\\Leftrightarrow \\begin{{cases}} x \\ge {d} \\\\ {latex(pt_he_qua)} = 0 \\end{{cases}}$ \\\\
                """

                if num_sol == 0:
                    loigiai += "Giải phương trình bậc hai và đối chiếu điều kiện, ta thấy không có nghiệm thỏa mãn. \\\\"
                else:
                    # Liệt kê các nghiệm thực tìm được
                    str_solutions = ", ".join([latex(s) for s in real_solutions])
                    loigiai += f"Giải phương trình và đối chiếu điều kiện $x \\ge {d}$, ta được $x \\in \\lbrace{{ {str_solutions} \\rbrace}}.$ \\\\"

                loigiai += f"Vậy số nghiệm của phương trình là {num_sol}."

                return noidungcauhoi, list_1, loigiai

            # --- XUẤT KẾT QUẢ THEO MẪU ---
            noidung, list_ans, giai = generate_question()

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidung) + '\n'
                '\\loigiai{' + str(giai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

