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


def bt_dang26_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- PHẦN RANDOM DỮ LIỆU ---
                # Thiết lập để tìm bộ số đẹp (nguyên)
                found = False
                while not found:
                    # Chọn e và m sao cho b = 2m/e là số nguyên
                    e_val = random.randint(1, 4)
                    m_val = random.choice([-4, -3, -2, 2, 3, 4])

                    if (2 * m_val) % e_val == 0:
                        b_val = (2 * m_val) // e_val
                        d_val = m_val + e_val**2
                        if d_val <= 0: continue

                        a_val = 4 * m_val + b_val**2
                        p_val = random.randint(1, 2) # Hệ số x+p ở mẫu

                        # Tính giới hạn L = m / [ (1/2 + p) * (b + 2e) ]
                        val_L = Rational(m_val, (Rational(1, 2) + p_val) * (b_val + 2 * e_val))
                        c_val = 2 * val_L

                        if c_val.denominator == 1: # Chỉ lấy c nguyên cho đẹp
                            found = True

                # Gán các giá trị đã tìm được
                a, b, c, d, e, p, m = a_val, b_val, c_val, d_val, e_val, p_val, m_val
                S_val = a * b * c

                # Mẫu số dạng đa thức khai triển
                mau_so_da_thuc = expand((2*x-1)**2 * (x+p))
                bx_e_display = latex(b*x + e)

                # --- PHẦN ĐÁP ÁN ---
                kq = S_val
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án sai (nhiễu)
                s = [
                    '$%s$' % (latex(kq + 12)),
                    '$%s$' % (latex(kq - 12)),
                    '$%s$' % (latex(kq + 24)),
                    '$%s$' % (latex(-kq)),
                    '$%s$' % (latex(Rational(kq, 2))),
                    '$%s$' % (latex(0)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{\sqrt{%sx^2+%s}-(%s)}{%s} & \text{khi } x \neq \dfrac{1}{2} \\ \dfrac{c}{2} & \text{khi } x = \dfrac{1}{2} \end{cases}$ (với $a, b, c \in \mathbb{R}$). Biết hàm số liên tục tại $x = \dfrac{1}{2}$. Giá trị $S = abc$ bằng'''
                                 % (latex(a), latex(d), bx_e_display, latex(mau_so_da_thuc)))

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (r'''Ta có mẫu số $%s = (2x-1)^2(x+%s)$. \\
                           Biến đổi tử số bằng cách nhân liên hợp: \\
                           $\dfrac{\sqrt{%sx^2+%s}-(%s)}{(2x-1)^2(x+%s)} = \dfrac{%sx^2+%s - (%s)^2}{(2x-1)^2(x+%s)(\sqrt{%sx^2+%s}+%s)}$ \\
                           $= \dfrac{%s(2x-1)^2}{(2x-1)^2(x+%s)(\sqrt{%sx^2+%s}+%s)}$ \\
                           Khi đó: $\lim_{x \to \frac{1}{2}} f(x) = \lim_{x \to \frac{1}{2}} \dfrac{%s}{(x+%s)(\sqrt{%sx^2+%s}+%s)} = %s$. \\
                           Để hàm số liên tục tại $x=\frac{1}{2}$ thì $f\left(\frac{1}{2}\right) = \lim_{x \to \frac{1}{2}} f(x) \Leftrightarrow \dfrac{c}{2} = %s \Rightarrow c = %s$. \\
                           Vậy $S = abc = (%s) \cdot (%s) \cdot (%s) = %s$.'''
                           % (latex(mau_so_da_thuc), latex(p), 
                              latex(a), latex(d), bx_e_display, latex(p),
                              latex(a), latex(d), bx_e_display, latex(p), latex(a), latex(d), bx_e_display,
                              latex(m), latex(p), latex(a), latex(d), bx_e_display,
                              latex(m), latex(p), latex(a), latex(d), bx_e_display, latex(val_L),
                              latex(val_L), latex(c),
                              latex(a), latex(b), latex(c), latex(S_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

