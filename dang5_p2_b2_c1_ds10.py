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


def bt_dang5_p2_b2_c1_ds10(self):
            # Khai báo biến
            # Tập A = [a; b)
            a = random.randint(-2, 1)
            b = a + random.randint(4, 5)  # A thường có 4 đến 5 số nguyên

            # Tập B = (m + c; m + d)
            c = random.randint(-7, -5)
            d = random.randint(6, 8)

            # Danh sách các số nguyên trong A
            A_int = [i for i in range(a, b)]
            count_A = len(A_int)

            noidungcauhoi = (r"Cho $A=[%s; %s)$; $B=(m%s; m+%s)$ với $m$ là tham số. Khi đó:" 
                             % (a, b, c, d))

            # =============================================================================
            # 2. LOGIC CÁC CÂU HỎI (NB - TH - VD - VDC)
            # =============================================================================

            # --- a) Nhận biết: Số lượng phần tử nguyên ---
            nb_da_d = r'\True Tập $A$ chứa %s phần tử là những số nguyên' % count_A
            nb_da_s = r'Tập $A$ chứa %s phần tử là những số nguyên' % (count_A + 1)
            loigiai_a = r"Sai. " if "True" not in nb_da_d else "" # Logic phụ trợ
            loigiai_a = r"Các số nguyên thuộc tập $A=[%s; %s)$ là $%s$ (gồm %s phần tử)." % (a, b, "; ".join(map(str, A_int)), count_A)

            # --- b) Thông hiểu: Giao tập hợp tại m cụ thể ---
            m_fix = random.randint(4, 6)
            bl, br = m_fix + c, m_fix + d
            il, ir = max(a, bl), min(b, br)
            th_da_d = r'\True $A \cap B = (%s; %s)$ khi $m=%s$' % (il, ir, m_fix)
            th_da_s = r'$A \cap B = [%s; %s)$ khi $m=%s$' % (il, ir, m_fix)
            loigiai_b = r"Khi $m=%s$, ta có $B=(%s; %s)$. Suy ra $A \cap B = (%s; %s)$." % (m_fix, bl, br, il, ir)

            # --- c) Vận dụng: Tập con ---
            # A subset B <=> m+c < a AND m+d >= b => m < a-c AND m >= b-d
            m_max = a - c
            m_min = b - d
            vd_da_d = r'\True $A \subset B$ khi $%s \leq m < %s$' % (m_min, m_max)
            vd_da_s = r'$A \subset B$ khi $%s < m \leq %s$' % (m_min, m_max)
            loigiai_c = (r"Để $A \subset B$ thì $\begin{cases} m%s < %s \\ m+%s \geq %s \end{cases} \Leftrightarrow \begin{cases} m < %s \\ m \geq %s \end{cases} \Leftrightarrow %s \leq m < %s$." 
                        % (c, a, d, b, m_max, m_min, m_min, m_max))

            # --- d) Vận dụng cao: Tìm m nguyên để giao có đúng k phần tử ---
            k = 2
            S = []
            # Quét m để tìm tập S
            for mt in range(min(A_int)-d-1, max(A_int)-c+2):
                cnt = sum(1 for x in A_int if mt + c < x < mt + d)
                if cnt == k: S.append(mt)

            tong_S = sum(S)
            is_d_correct = random.choice([True, False])
            val_d = tong_S if is_d_correct else tong_S + random.randint(1, 10)

            vdc_da = (r"\True " if is_d_correct else "") + r"Gọi $S$ là tập hợp tất cả các giá trị nguyên của $m$ để $A \cap B$ chứa đúng %s phần tử là số nguyên. Tổng các phần tử của $S$ là %s" % (k, val_d)

            # Lời giải chi tiết cho câu d
            loigiai_d = (r"Các số nguyên thuộc $A$ là $I = \{%s\}$. Một số $x \in I$ thuộc $B$ khi $m%s < x < m+%s \Leftrightarrow x-(%s) < m < x-(%s)$. "
                         r"Để $A \cap B$ có đúng %s phần tử nguyên, ta xét các trường hợp trượt của tập $B$ trên tập số nguyên: "
                         r"Tìm được $m \in \{%s\}$. Vậy tổng các phần tử của $S$ là %s." 
                         % (", ".join(map(str, A_int)), c, d, d, c, k, "; ".join(map(str, S)), tong_S))

            # =============================================================================
            # 3. TRỘN VÀ XUẤT BÀI TẬP
            # =============================================================================
            answers = [nb_da_d, th_da_d, vd_da_d, vdc_da]
            solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]

            # Vòng lặp đảm bảo số câu đúng từ 1 đến 3
            while True:
                choices = [random.choice([nb_da_d, nb_da_s]), random.choice([th_da_d, th_da_s]), 
                           random.choice([vd_da_d, vd_da_s]), vdc_da]
                true_cnt = sum(1 for c in choices if "\\True" in c)
                if 1 <= true_cnt <= 3:
                    break

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choiceTFn \n'
                '{' + choices[0] + '}\n'
                '{' + choices[1] + '}\n'
                '{' + choices[2] + '}\n'
                '{' + choices[3] + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + solutions[0] + '\n'
                '\\item ' + solutions[1] + '\n'
                '\\item ' + solutions[2] + '\n'
                '\\item ' + solutions[3] + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

