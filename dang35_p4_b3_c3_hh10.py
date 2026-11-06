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


def bt_dang35_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, m = symbols('x y m')

            # Hàm định dạng tập nghiệm m thuộc...
            def format_set_vietnamese(sol):
                if sol == S.Reals:
                    return r"m \in \mathbb{R}"
                if sol == S.EmptySet:
                    return r"m \in \varnothing"

                # Chuyển đổi ký hiệu: SymPy dùng dấu phẩy (,), Việt Nam thường dùng chấm phẩy (;)
                # Ví dụ: (1, 2) -> (1; 2)
                sol_latex = latex(sol).replace(',', ';')
                return f"m \\in {sol_latex}"

            # B1 & B3: Thiết lập random để có nhiều trường hợp nghiệm
            dang_kq = random.choice(['all', 'interval', 'outside'])

            x0 = random.randint(1, 3)
            y0 = random.randint(-2, 2) # Để y0 nhỏ giúp m^2 dễ có nghiệm hữu hạn

            if dang_kq == 'all':
                R = random.randint(5, 7)
                k = random.randint(2, 3)
            else:
                R = random.randint(1, 2)
                k = random.randint(2, 5)

            # Đường tròn (C)
            circle_expr = expand((x - x0)**2 + (y - y0)**2 - R**2)
            # Đường thẳng delta: sqrt(k)x + my + (1 - x0*sqrt(k)) = 0
            c_line_val = 1 - x0 * sqrt(k)

            # Bất phương trình: (y0*m + 1)^2 < R^2 * (m^2 + k)
            # Chuyển về dạng: f(m) < 0
            f_m_expr = expand((y0*m + 1)**2 - R**2 * (m**2 + k))

            # Giải bất phương trình
            sol = solve_univariate_inequality(f_m_expr < 0, m, relational=False)
            ket_qua_cuoi = format_set_vietnamese(sol)

            # --- Tạo nội dung câu hỏi ---
            noidungcauhoi = (r'''Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $(C): %s = 0$ và đường thẳng $\Delta: %s x + my + %s = 0$. Tính giá trị $m$ để $(C)$ cắt $\Delta$ tại $2$ điểm phân biệt.'''
                            %(latex(circle_expr), latex(sqrt(k)), latex(simplify(c_line_val))))

            # --- Tạo đáp án ---
            da_d = r'\True $%s$' % ket_qua_cuoi
            s_fake = [
                r'$m \in \mathbb{R}$', 
                r'$m \in \varnothing$', 
                r'$m \in (-1; 1)$', 
                r'$m \in (-\infty; -2) \cup (2; +\infty)$',
                r'$m > 0$',
                r'$m < 5$'
            ]
            s_filtered = [i for i in s_fake if i not in da_d]
            random.shuffle(s_filtered)
            list_1 = [da_d, s_filtered[0], s_filtered[1], s_filtered[2]]
            random.shuffle(list_1)

            # --- B2: Lời giải ---
            loigiai = (r'''Đường tròn $(C)$ có tâm $I(%s; %s)$ và bán kính $R = %s$. \\
                      Để $(C)$ cắt $\Delta$ tại $2$ điểm phân biệt $\Leftrightarrow d(I; \Delta) < R$ \\
                      $\Leftrightarrow \frac{|%s \cdot %s + m \cdot (%s) + %s|}{\sqrt{(%s)^2 + m^2}} < %s$ \\
                      $\Leftrightarrow \frac{|%s m + 1|}{\sqrt{%s + m^2}} < %s$ \\
                      $\Leftrightarrow (%s m + 1)^2 < %s^2(%s + m^2)$ \\
                      $\Leftrightarrow %s < 0$ \\
                      $\Leftrightarrow %s$. \\
                      Vậy tập giá trị $m$ cần tìm là $%s$.'''
                      %(x0, y0, R, 
                        latex(sqrt(k)), x0, y0, latex(simplify(c_line_val)), latex(sqrt(k)), R,
                        y0, k, R,
                        y0, R, k,
                        latex(f_m_expr), ket_qua_cuoi, ket_qua_cuoi))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

