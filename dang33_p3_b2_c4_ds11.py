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


def bt_dang33_p3_b2_c4_ds11(self):
                x = symbols('x')

                # --- Định nghĩa hàm sinh câu hỏi ---
                def generate_question():
                    while True:
                        x0 = random.randint(1, 5)
                        a_val = random.randint(2, 6)
                        k_tu = random.randint(2, 6) 
                        b_val = k_tu**2 - a_val * x0
                        m_val = k_tu - x0

                        c_val = random.randint(1, 3)
                        d_val = x0**2 - c_val * x0
                        if d_val < 0: 
                            d_val = 0
                            c_val = x0

                        tu_bieuthuc = x + m_val - sqrt(a_val*x + b_val)
                        mau_bieuthuc = x - sqrt(c_val*x + d_val)

                        L = limit(tu_bieuthuc / mau_bieuthuc, x, x0)
                        res = simplify(L)
                        num, den = fraction(res)

                        try:
                            a, b = int(num), int(den)
                            if a != 0: break
                        except:
                            continue

                    kq_final = a - b
                    tu_cum_1 = x + m_val
                    tu_sau_lh = simplify(tu_cum_1**2 - (a_val*x + b_val))
                    mau_sau_lh = simplify(x**2 - (c_val*x + d_val))

                    # Nội dung câu hỏi
                    noidung_cau = (r"Giới hạn $L = \lim_{x \to %s} \frac{%s}{%s}$ bằng $\frac{a}{b}$ (với $\frac{a}{b}$ là phân số tối giản). Giá trị của $a-b$ bằng" 
                                    % (latex(x0), latex(tu_bieuthuc), latex(mau_bieuthuc)))

                    # Đáp án trắc nghiệm
                    da_d = r'\True $%s$' % (latex(kq_final))
                    s_set = set()
                    while len(s_set) < 3:
                        fake = kq_final + random.choice([-2, -1, 1, 2, 3, 5])
                        if fake != kq_final:
                            s_set.add(fake)
                    s_list = list(s_set)
                    list_ans = [da_d, r'$%s$' % s_list[0], r'$%s$' % s_list[1], r'$%s$' % s_list[2]]
                    random.shuffle(list_ans)

                    # Lời giải
                    loigiai_chi_tiet = (r"Ta có dạng vô định $\frac{0}{0}$. Thực hiện nhân liên hợp: \\"
                                    r"$L = \lim_{x \to %s} \frac{(%s)^2 - (%s)}{x^2 - (%s)} \cdot \frac{x + \sqrt{%s}}{%s + \sqrt{%s}} "
                                    r"= \frac{%s}{%s}.\\ \text{ Suy ra } a=%s, b=%s \Rightarrow a-b=%s.$" 
                                    % (x0, latex(tu_cum_1), latex(a_val*x + b_val), latex(c_val*x + d_val), 
                                        latex(c_val*x + d_val), latex(tu_cum_1), latex(a_val*x + b_val),
                                        a, b, a, b, kq_final))

                    dapan_short = ' \\shortans[0]{$%s$} ' % (latex(kq_final))
                    return noidung_cau, list_ans, loigiai_chi_tiet, dapan_short

                # --- BƯỚC QUAN TRỌNG: Gọi hàm để lấy dữ liệu ---
                noidung, choices, giai, ans = generate_question()

                # --- Xuất nội dung theo cấu trúc iTex ---
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidung) + str(ans) + '\n'
                    '\\loigiai{' + str(giai) + '}\n'
                    '\\end{ex}\n'
                    '\\end{minipage} \n\n'
                )
                return content

