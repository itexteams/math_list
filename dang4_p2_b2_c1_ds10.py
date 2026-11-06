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


def bt_dang4_p2_b2_c1_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- Bước 1: Tạo dữ liệu ngẫu nhiên (Random hóa bài toán) ---
            # Tập A = {x | m*x - n >= 0}
            m = random.choice([2, 3, 4, 5])
            n = random.choice([1, 3, 5, 7])
            val_A = Rational(n, m)

            # Tập B = {x | p*x - q < 0}
            p = 2
            q = random.choice([2020, 2022, 2024, 2026])
            val_B = q // p 

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hai tập hợp $A = \{x \in \mathbb{R} | %s x - %s \geq 0\}$; $B = \{x \in \mathbb{R} | %s x - %s < 0\}$.''' % (m, n, p, q)

            ######################################################################## Nhận biết ############################################
            # Câu a: Kiểm tra tập B
            nb_da_d = r'\True $B = (-\infty; %s)$' % val_B
            nb_da_s = r'$B = (%s; +\infty)$' % val_B
            list_nb = [(nb_da_d, r'''Ta có $%s x - %s < 0 \Leftrightarrow x < %s$. Vậy $B = (-\infty; %s)$.''' % (p, q, val_B, val_B)),
                       (nb_da_s, r'''Ta có $%s x - %s < 0 \Leftrightarrow x < %s$. Vậy $B = (-\infty; %s)$.''' % (p, q, val_B, val_B))]

            ######################################################################## Thông hiểu ############################################
            # Câu b: Kiểm tra tập A
            th_da_d = r'\True $A = \left[ %s; +\infty \right)$' % latex(val_A)
            th_da_s = r'$A = \left( %s; +\infty \right)$' % latex(val_A)
            list_th = [(th_da_d, r'''Ta có $%s x - %s \geq 0 \Leftrightarrow x \geq %s$. Vậy $A = \left[ %s; +\infty \right)$.''' % (m, n, latex(val_A), latex(val_A))),
                       (th_da_s, r'''Ta có $%s x - %s \geq 0 \Leftrightarrow x \geq %s$. Vậy $A = \left[ %s; +\infty \right)$.''' % (m, n, latex(val_A), latex(val_A)))]

            ######################################################################## Vận dụng ############################################
            # Câu c: Phần bù của A
            vd_da_d = r'\True $C_{\mathbb{R}}A = \left( -\infty; %s \right)$' % latex(val_A)
            vd_da_s = r'$C_{\mathbb{R}}A = \left( -\infty; %s \right]$' % latex(val_A)
            list_vd = [(vd_da_d, r'''Vì $A = \left[ %s; +\infty \right)$ nên $C_{\mathbb{R}}A = \mathbb{R} \setminus A = \left( -\infty; %s \right)$.''' % (latex(val_A), latex(val_A))),
                       (vd_da_s, r'''Vì $A = \left[ %s; +\infty \right)$ nên $C_{\mathbb{R}}A = \mathbb{R} \setminus A = \left( -\infty; %s \right)$.''' % (latex(val_A), latex(val_A)))]

            ######################################################################## Vận dụng cao ############################################
            # Câu d: Hiệu A \ B
            vdc_da_d = r'\True $A \setminus B = [%s; +\infty)$' % val_B
            vdc_da_s = r'$A \setminus B = (%s; +\infty)$' % val_B
            list_vdc = [(vdc_da_d, r'''Ta có $A \setminus B = \{x \in A \mid x \notin B\}$. Vì $B = (-\infty; %s)$ nên $x \notin B \Leftrightarrow x \geq %s$. Kết hợp $x \geq %s$, ta được $A \setminus B = [%s; +\infty)$.''' % (val_B, val_B, latex(val_A), val_B)),
                        (vdc_da_s, r'''Ta có $A \setminus B = \{x \in A \mid x \notin B\}$. Vì $B = (-\infty; %s)$ nên $x \notin B \Leftrightarrow x \geq %s$. Kết hợp $x \geq %s$, ta được $A \setminus B = [%s; +\infty)$.''' % (val_B, val_B, latex(val_A), val_B))]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp xáo trộn đến khi đạt yêu cầu số câu đúng (từ 1 đến 3)
            while True:
                choice_nb = random.choice(list_nb)
                choice_th = random.choice(list_th)
                choice_vd = random.choice(list_vd)
                choice_vdc = random.choice(list_vdc)

                shuffled_answers = [choice_nb[0], choice_th[0], choice_vd[0], choice_vdc[0]]
                shuffled_solutions = [choice_nb[1], choice_th[1], choice_vd[1], choice_vdc[1]]

                if 1 <= count_true_answers(shuffled_answers) <= 3:
                    break

            # --- Xuất content (Giữ đúng cấu trúc theo ảnh image_99b436.png) ---
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
                '\\end{ex}\n' '\\end{minipage} \n\n')
            return content

