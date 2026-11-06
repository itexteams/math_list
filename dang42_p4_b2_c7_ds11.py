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


def bt_dang42_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x, m = symbols('x m')

            def generate_question():
                # Cố định hệ số a = 1 để y' >= 0 có nghiệm
                A = 1 
                # Random B sao cho Delta có dạng đẹp (thường chọn số chẵn)
                B = random.choice([-4, -2, 2, 4])
                C = random.randint(1, 5)
                const_d = random.randint(1, 10)

                # Đạo hàm: y' = Ax^2 + Bmx + Cm
                # Biệt thức Delta = (Bm)^2 - 4*A*(Cm)
                delta_expr = (B*m)**2 - 4*A*(C*m)

                # Giải Delta <= 0
                try:
                    tap_nghiem = solve_univariate_inequality(delta_expr <= 0, m, relational=False)
                except:
                    tap_nghiem = S.EmptySet

                # Chuyển tập nghiệm sang Latex
                if tap_nghiem == S.EmptySet:
                    kq_dung_latex = r"m \in \emptyset"
                elif tap_nghiem == S.Reals:
                    kq_dung_latex = r"m \in \mathbb{R}"
                else:
                    # Xử lý định dạng khoảng nghiệm cho đẹp
                    kq_dung_latex = latex(tap_nghiem).replace("Interval", "").replace("(", "").replace(")", "")
                    if isinstance(tap_nghiem, Interval):
                        start = latex(tap_nghiem.start)
                        end = latex(tap_nghiem.end)
                        kq_dung_latex = f"{start} \\le m \\le {end}"

                # Nội dung câu hỏi
                sign_B = "+" if B > 0 else "-"
                abs_B = abs(B)
                noidungcauhoi = (r"Cho hàm số $y = \dfrac{1}{3}x^3 %s \dfrac{%sm}{2}x^2 + %smx + %s$. "
                                 r"Tìm các giá trị của tham số $m$ để $y' \ge 0, \forall x \in \mathbb{R}$." 
                                 % (sign_B, latex(abs_B) if abs_B != 1 else "", latex(C) if C != 1 else "", latex(const_d)))

                # Lời giải
                loigiai = (r"Ta có $y' = x^2 %s %smx + %sm$. \\ "
                           r"Để $y' \ge 0, \forall x \in \mathbb{R} \Leftrightarrow x^2 %s %smx + %sm \ge 0, \forall x \in \mathbb{R}$. \\ "
                           r"Vì hệ số $a = 1 > 0$ nên điều kiện tương đương với: \\ "
                           r"$\Delta = (%sm)^2 - 4(%sm) \le 0 \Leftrightarrow %s \le 0 \Leftrightarrow %s$."
                           %(sign_B, latex(abs_B), latex(C), sign_B, latex(abs_B), latex(C), latex(B), latex(C), latex(delta_expr.expand()), kq_dung_latex))

                # Đáp án nhiễu
                da_sai = [f"$m < 0$", f"$m > {random.randint(5,10)}$", r"$m \in \mathbb{R}$"]
                if kq_dung_latex == r"m \in \mathbb{R}": da_sai[2] = r"$m \in \emptyset$"

                return noidungcauhoi, kq_dung_latex, da_sai, loigiai

            # Thực thi và in kết quả
            noidungcauhoi, kq_dung_latex, da_sai, loigiai = generate_question()
            da_d = '\\True $' + kq_dung_latex + '$'
            list_1 = [da_d] + da_sai
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

