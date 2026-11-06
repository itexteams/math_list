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


def bt_dang39_p1_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM THÔNG SỐ ĐỂ ĐẢM BẢO NGHIỆM ĐẸP ---
                # Ta có phương trình: (a + m*b)/n = sqrt(a*b)
                # Để giải ra a = r*b với r là số nguyên dương > 1
                # n = (r + m) / sqrt(r). Để n hữu tỉ, r nên là số chính phương.

                r_sqrt = random.choice([2, 3, 5]) # sqrt(r)
                r = r_sqrt**2                    # r = 4, 9, 25
                m = random.randint(1, 3)         # Hệ số m trong (a + m*b)

                n_rat = Rational(r + m, r_sqrt)  # n = (r + m) / sqrt(r)

                # Random các hệ số A, B, C cho biểu thức P = (A*a^2 + B*ab + C*b^2) / (a + m*b)^2
                A = random.randint(1, 3)
                B = random.randint(1, 5)
                C = random.randint(1, 3)

                # --- BƯỚC 2: TÍNH TOÁN ĐÁP ÁN ĐÚNG ---
                # Thay a = r*b vào P: P = (A*r^2 + B*r + C) / (r + m)^2
                tu_so_P = A * (r**2) + B * r + C
                mau_so_P = (r + m)**2
                kq_P = Rational(tu_so_P, mau_so_P)

                da = '$%s$' % latex(kq_P)

                # --- BƯỚC 3: TẠO CÁC PHƯƠNG ÁN SAI ---
                s = set()
                while len(s) < 3:
                    # Tạo các phân số lân cận hoặc đảo ngược
                    sai = Rational(random.randint(1, 20), random.randint(2, 20))
                    if sai != kq_P:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (
                    r'Cho $a, b, x > 0$; $a > b$ và $b, x \neq 1$ thỏa mãn '
                    r'$\log_x \frac{a + %s b}{%s} = \log_x \sqrt{a} + \frac{1}{\log_b x^2}$. '
                    r'Khi đó biểu thức $P = \frac{%s a^2 + %s ab + %s b^2}{(a + %s b)^2}$ có giá trị bằng:'
                    % (latex(m), latex(n_rat), latex(A), latex(B), latex(C), latex(m))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- BƯỚC 5: NỘI DUNG LỜI GIẢI ---
                # Biến đổi: 1/log_b(x^2) = 1/(2*log_b(x)) = 1/2 * log_x(b) = log_x(sqrt(b))
                he_so_ab = (n_rat**2)
                # PT: a^2 + (2m - n^2)ab + m^2*b^2 = 0
                he_so_giua = 2*m - he_so_ab

                loigiai = (
                    r'Ta có: $\log_x \frac{a + %s b}{%s} = \log_x \sqrt{a} + \log_x \sqrt{b} = \log_x \sqrt{ab}$. \\ '
                    r'$\Leftrightarrow \frac{a + %s b}{%s} = \sqrt{ab} \Leftrightarrow a + %s b = %s \sqrt{ab}$. \\ '
                    r'Bình phương hai vế ta được: $(a + %s b)^2 = %s ab$ \\ '
                    r'$\Leftrightarrow a^2 + %s ab + %s b^2 = %s ab \Leftrightarrow a^2 %s ab + %s b^2 = 0$. \\ '
                    r'$\Leftrightarrow (a - b)(a - %s b) = 0$. \\ '
                    r'Vì $a > b$ nên $a = %s b$. \\ '
                    r'Thay $a = %s b$ vào biểu thức $P$, ta được: \\ '
                    r'$P = \frac{%s(%s b)^2 + %s(%s b)b + %s b^2}{(%s b + %s b)^2} = \frac{%s b^2}{%s b^2} = %s$.'
                    % (latex(m), latex(n_rat), 
                       latex(m), latex(n_rat), latex(m), latex(n_rat),
                       latex(m), latex(he_so_ab),
                       latex(2*m), latex(m**2), latex(he_so_ab), latex(he_so_giua), latex(m**2),
                       latex(r), latex(r), latex(r),
                       latex(A), latex(r), latex(B), latex(r), latex(C), latex(r), latex(m),
                       latex(tu_so_P), latex(mau_so_P), latex(kq_P))
                )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

