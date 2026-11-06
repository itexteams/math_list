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


def bt_dang16_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')

            # Danh sách các dạng (ở đây chỉ có 1 dạng liên tục)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: RANDOM CÁC THÔNG SỐ ---
                # Chọn x0 ngẫu nhiên (thường là số nhỏ: 1, 2, 3)
                x0 = random.randint(1, 3)

                # Chọn k để căn thức là số chính phương: sqrt(a*x0 + b) = k
                # Chọn k từ 1 đến 4, a từ 1 đến 4
                k = random.randint(1, 4)
                a = random.randint(1, 5)

                # Tính b dựa trên k = sqrt(a*x0 + b) => b = k^2 - a*x0
                b = k**2 - a*x0

                # m chính là giá trị k để tử số bằng 0 tại x0
                m_val = k

                # Tính n bằng cách tính giới hạn (khử dạng 0/0)
                # f_lim = (sqrt(a*x + b) - m) / (x - x0)
                tuso = sqrt(a*x + b) - m_val
                mauso = x - x0
                n_val = limit(tuso/mauso, x, x0)

                # Kết quả cần tìm S = m + n
                kq_sym = m_val + n_val
                da_dung = '$%s$' % latex(kq_sym)

                # --- TẠO ĐÁP ÁN NHIỄU ---
                s = []
                # Các giá trị nhiễu xung quanh kết quả đúng
                offsets = [Rational(1, 2), 1, Rational(3, 2), Rational(-1, 2), -1]
                for off in offsets:
                    sai = kq_sym + off
                    s.append('$%s$' % latex(sai))

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # --- BƯỚC 2: VIẾT LẠI NỘI DUNG THEO MẪU ---

                # Biểu thức f(x) để hiển thị trong đề
                bieuthuc_f = r'\frac{\sqrt{%s x + %s} - m}{x - %s}' % (
                    latex(a) if a != 1 else "", 
                    latex(b) if b >= 0 else "- " + latex(abs(b)),
                    latex(x0)
                )

                noidungcauhoi = (r'Cho hàm số $f(x) = \begin{cases} %s & \text{khi } x \neq %s \\ n & \text{khi } x = %s \end{cases}$. '
                                 r'Để hàm số liên tục tại $x_0 = %s$ thì giá trị của biểu thức $m + n$ tương ứng bằng bao nhiêu?'
                                 % (bieuthuc_f, latex(x0), latex(x0), latex(x0)))

                # Nội dung lời giải chi tiết
                loigiai = (r'Ta có: $f(%s) = n$. \\ '
                           r'Để hàm số liên tục tại $x = %s \Leftrightarrow \lim_{x \to %s} f(x) = f(%s) \Leftrightarrow \lim_{x \to %s} \frac{\sqrt{%sx + %s} - m}{x - %s} = n \quad (1)$. \\ '
                           r'Giới hạn tồn tại khi $%s$ là nghiệm của tử số: $\sqrt{%s \cdot %s + %s} - m = 0 \Rightarrow m = %s$. \\ '
                           r'Khi $m = %s$, ta có: \\ '
                           r'$(1) \Rightarrow n = \lim_{x \to %s} \frac{\sqrt{%sx + %s} - %s}{x - %s} = \lim_{x \to %s} \frac{%sx + %s - %s}{(x - %s)(\sqrt{%sx + %s} + %s)} $ \\ '
                           r'$\Rightarrow n = \lim_{x \to %s} \frac{%s(x - %s)}{(x - %s)(\sqrt{%sx + %s} + %s)} = \lim_{x \to %s} \frac{%s}{\sqrt{%sx + %s} + %s} = %s$. \\ '
                           r'Vậy $m + n = %s + %s = %s$.'
                           % (latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(a), latex(b), latex(x0),
                              latex(x0), latex(a), latex(x0), latex(b), latex(m_val),
                              latex(m_val), latex(x0), latex(a), latex(b), latex(m_val), latex(x0),
                              latex(x0), latex(a), latex(b), latex(m_val**2), latex(x0), latex(a), latex(b), latex(m_val),
                              latex(x0), latex(a), latex(x0), latex(x0), latex(a), latex(b), latex(m_val),
                              latex(x0), latex(a), latex(a), latex(b), latex(m_val), latex(n_val),
                              latex(m_val), latex(n_val), latex(kq_sym)))

                # Đóng gói đáp án
                da_d = r'\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_sym))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   

