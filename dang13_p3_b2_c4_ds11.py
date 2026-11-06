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


def bt_dang13_p3_b2_c4_ds11(self):
            # Khai báo biến
            # --- B3: Tư duy Random bài toán ---
            u=symbols('u')
            k=symbols('k')
            n = random.randint(2008, 2030)
            m = n + 1
            list_a = [4, 9, 16, 25, 36]
            a = random.choice(list_a)
            sqrt_a = int(a**0.5)
            b = random.randint(2, 5)

            huong_tien = random.choice(['+\\infty', '-\\infty'])

            # --- B2: Tính toán kết quả ---
            if huong_tien == '+\\infty':
                dau_kq = ''
                kq_final = rf'\frac{{1}}{{{b}^{{{m-1}}}}}'
            else:
                dau_kq = '-'
                kq_final = rf'-\frac{{1}}{{{b}^{{{m-1}}}}}'

            # Các đáp án trắc nghiệm
            da_dung = f'${kq_final}$'
            s = ['$0$', '$1$', f'$-{kq_final}$' if dau_kq=='' else f'${kq_final[1:]}$', rf'$\frac{{1}}{{{b}^{{{m}}}}}$']
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Câu hỏi
            noidungcauhoi = rf'Giới hạn $\lim_{{x \to {huong_tien}}} \frac{{x^{{{n}}}\sqrt{{{a}x^2 + 1}}}}{{({b}x + 1)^{{{m}}}}}$ bằng $\frac{{1}}{{u^k}}$. Giá trị của $k$ bằng bao nhiêu?'

            # --- LỜI GIẢI DÙNG F-STRING (CHÍNH XÁC & SẠCH SẼ) ---
            buoc_rut_x = 'x' if huong_tien == '+\\infty' else '-x'
            dk_x = 'x > 0' if huong_tien == '+\\infty' else 'x < 0'
            dau_tu = '' if huong_tien == '+\\infty' else '-'

            loigiai = rf'''Ta có: $x \to {huong_tien}$ nên ${dk_x}$. \\
                Khi đó $\sqrt{{x^2}} = |x| = {buoc_rut_x}$. \\
                $$\lim_{{x \to {huong_tien}}} \frac{{x^{{{n}}}\sqrt{{{a}x^2 + 1}}}}{{({b}x + 1)^{{{m}}}}} 
                = \lim_{{x \to {huong_tien}}} \frac{{x^{{{n}}} \cdot \sqrt{{x^2\left({a} + \frac{{1}}{{x^2}}\right)}}}}{{\left[x\left({b} + \frac{{1}}{{x}}\right)\right]^{{{m}}}}}$$
                $$= \lim_{{x \to {huong_tien}}} \frac{{x^{{{n}}} \cdot ({buoc_rut_x}) \cdot \sqrt{{{a} + \frac{{1}}{{x^2}}}}}}{{x^{{{m}}}\left({b} + \frac{{1}}{{x}}\right)^{{{m}}}}}
                = \lim_{{x \to {huong_tien}}} \frac{{{dau_tu}\sqrt{{{a} + \frac{{1}}{{x^2}}}}}}{{\left({b} + \frac{{1}}{{x}}\right)^{{{m}}}}}$$
                $$= \frac{{{dau_tu}\sqrt{{{a} + 0}}}}{{({b} + 0)^{{{m}}}}} = \frac{{{dau_tu}{sqrt_a}}}{{{b}^{{{m}}}}} = {kq_final}.$$'''

            # Xuất câu trắc nghiệm
            list_1 = ['\\True ' + da_dung, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(m-1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

