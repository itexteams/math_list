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


def bt_dang31_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # Bước 3: Thiết lập các tham số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # f'(x) + 2kx * f(x) = m * e^(-kx^2)
                # Trong đề bài gốc: k = 1, m = 1
                k = random.randint(1, 4)
                m = random.randint(1, 5)

                # Biểu thức trong đề bài
                he_so_f = 2 * k
                mu_e = -k

                # Đáp án đúng: f(1) = m / e^k
                # f(x) * e^{kx^2} = mx + C. Vì f(0)=0 => C=0 => f(x) = mx / e^{kx^2}
                # f(1) = m / e^k

                if k == 1:
                    mau_so_chuan = "e"
                else:
                    mau_so_chuan = "e^{%s}" % k

                if m == 1:
                    tu_so_chuan = "1"
                else:
                    tu_so_chuan = str(m)

                da_dung = r'$\frac{%s}{%s}$' % (tu_so_chuan, mau_so_chuan)

                # Bước 4: Tạo các phương án sai (không trùng với đáp án đúng)
                s = [
                    r'$\frac{%s}{%s}$' % (m + 1, mau_so_chuan),
                    r'$%s %s$' % (m, mau_so_chuan),
                    r'$\frac{1}{%s}$' % (mau_so_chuan),
                    r'$\frac{%s}{e^{%s}}$' % (m, k + 1),
                    r'$%s$' % m,
                    r'$0$'
                ]

                # Lọc bỏ đáp án đúng nếu lỡ trùng trong danh sách sai
                s = [item for item in s if item != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # f'(x) + (2k)x.f(x) = m.e^(-kx^2)
                ve_phai_latex = ""
                if m == 1:
                    ve_phai_latex = "e^{-%s x^2}" % (k if k != 1 else "")
                else:
                    ve_phai_latex = "%s e^{-%s x^2}" % (m, k if k != 1 else "")

                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$ thỏa mãn $f\'(x) + %s x \\cdot f(x) = %s, \\forall x \\in \\mathbb{R}$ và $f(0)=0$. Tính $f(1)$.'
                                 % (latex(he_so_f), ve_phai_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có:
                             $f'(x) + %s x \cdot f(x) = %s \Leftrightarrow e^{%s x^2} \cdot f'(x) + %s x \cdot e^{%s x^2} \cdot f(x) = %s$ \\
                             $\Leftrightarrow \left( e^{%s x^2} \cdot f(x) \right)' = %s$. \\
                             Suy ra $\int \left( e^{%s x^2} \cdot f(x) \right)' \text{d}x = \int %s \text{d}x \Leftrightarrow e^{%s x^2} \cdot f(x) = %s x + C$. \\
                             Vì $f(0)=0 \Rightarrow e^{%s \cdot 0^2} \cdot 0 = %s \cdot 0 + C \Rightarrow C = 0$. \\
                             Do đó $f(x) = \frac{%s x}{e^{%s x^2}}$. Vậy $f(1) = \frac{%s \cdot 1}{e^{%s \cdot 1^2}} = %s$.'''
                           % (latex(he_so_f), ve_phai_latex, k if k != 1 else "", latex(he_so_f), k if k != 1 else "", m,
                              k if k != 1 else "", m,
                              k if k != 1 else "", m, k if k != 1 else "", m,
                              k if k != 1 else "", m,
                              m, k if k != 1 else "", m, k if k != 1 else "", da_dung.replace('$', '')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

