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


def bt_dang13_p3_b3_c4_ds11(self):
            # Khai báo biến
            def generate_question():
                x, m = symbols('x m')

                # 1. Random x0 và nghiệm thứ hai để tạo tử số
                x0 = random.randint(-3, 3)
                x1 = random.randint(-5, 5) 
                # Đảm bảo tử số chia hết cho (x - x0)
                tu_so = expand((x - x0) * (x - x1))
                mau_so = x - x0

                # Tính giới hạn L
                L = x0 - x1

                # 2. Tạo biểu thức m^2 + Am + B
                # Để kiểm soát số nghiệm nguyên, ta chọn trước nghiệm m1, m2
                dang_nghiem = random.choice(['2_nghiem', '1_nghiem', '0_nghiem'])

                if dang_nghiem == '2_nghiem':
                    m1, m2 = random.sample(range(-4, 5), 2)
                    # (m-m1)(m-m2) = m^2 - (m1+m2)m + m1*m2
                    A = -(m1 + m2)
                    # Ta muốn m^2 + Am + B = L có nghiệm m1, m2 => B - L = m1*m2
                    B = m1 * m2 + L
                elif dang_nghiem == '1_nghiem':
                    m1 = random.randint(-4, 4)
                    A = -2 * m1
                    B = m1**2 + L
                else: # Vô nghiệm nguyên (thường là vô nghiệm thực hoặc nghiệm vô tỷ)
                    A = random.randint(-2, 2)
                    B = L + random.randint(5, 10) # Đẩy Delta âm

                f_tai_x0 = m**2 + A*m + B

                # --- Giải chi tiết ---
                pt_m = f_tai_x0 - L
                ds_m = solve(pt_m, m)
                ds_m_nguyen = [val for val in ds_m if val.is_integer]
                kq_dung = len(ds_m_nguyen)

                # --- Tạo nội dung ---
                noidung = (r"Có bao nhiêu số nguyên $m$ để hàm số $f(x) = \begin{cases} \frac{%s}{%s} & \text{khi } x \neq %s \\ %s & \text{khi } x = %s \end{cases}$ liên tục tại điểm $x = %s$?" 
                           % (latex(tu_so), latex(mau_so), latex(x0), latex(f_tai_x0), latex(x0), latex(x0)))

                # Tạo đáp án trắc nghiệm
                dap_an_dung = f"${kq_dung}$"
                cac_lua_chon = ["$0$", "$1$", "$2$", "$3$"]
                if dap_an_dung not in cac_lua_chon: # Trường hợp đặc biệt
                    cac_lua_chon[0] = dap_an_dung

                random.shuffle(cac_lua_chon)
                # Đánh dấu đáp án đúng cho format mẫu
                choices = []
                for c in cac_lua_chon:
                    if c == dap_an_dung:
                        choices.append("\\True " + c)
                    else:
                        choices.append(c)

                # Lời giải chi tiết
                loigiai = r"""Ta có $\lim_{x \to %s} \frac{%s}{%s} = \lim_{x \to %s} (%s) = %s$. \\
            Để hàm số liên tục tại $x = %s$, ta cần $\lim_{x \to %s} f(x) = f(%s)$. \\
            $\Leftrightarrow %s = %s \Leftrightarrow %s = 0$. \\
            """ % (latex(x0), latex(tu_so), latex(mau_so), latex(x0), latex(x - x1), latex(L), 
                   latex(x0), latex(x0), latex(x0), latex(f_tai_x0), latex(L), latex(expand(pt_m)))

                if len(ds_m_nguyen) > 0:
                    loigiai += "Phương trình có các nghiệm nguyên là: $m = " + ", m = ".join([latex(v) for v in ds_m_nguyen]) + "$. \\\\"
                else:
                    loigiai += "Phương trình không có nghiệm nguyên. \\\\"

                loigiai += f"Vậy có {kq_dung} giá trị nguyên của $m$ thỏa mãn."
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_dung))

                # Xuất theo template
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + noidung +str(dapan)+ '\n'
                    '\\loigiai{' + loigiai + '}\n'
                    '\\end{ex}\n \\end{minipage} \n')
                return content
            content = generate_question()
            return content   

