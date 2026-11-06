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


def bt_dang29_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random công bội q và số hạng đầu u1
                q_val = random.randint(2, 4)
                u1_val = random.randint(1, 5)

                # Tính u5 + u2 và u6 - u4
                A = u1_val * (q_val**4 + q_val)
                B = u1_val * (q_val**5 - q_val**3)

                # Rút gọn phân số A/B thành k1/k2
                frac_AB = Rational(A, B)
                k1 = frac_AB.p
                k2 = frac_AB.q

                q_var = symbols('q')

                # Đa thức bậc 4 sau khi nhóm q
                poly_q4 = -k1 * q_var**4 + k2 * q_var**3 + k1 * q_var**2 + k2
                # Tam thức bậc 2 sau khi chia cho (q + 1)(q - q_val) và đổi dấu
                quad_neg = -sp.simplify(poly_q4 / ((q_var + 1) * (q_var - q_val)))

                # Giá trị u1 + 2024q cần tìm
                ans_val = u1_val + 2024 * q_val

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(ans_val))]
                da = random.choice(du)

                # Sinh các đáp án sai không trùng đáp án đúng và không trùng nhau
                s_set = set()
                while len(s_set) < 6:
                    diff = random.choice(
                        [-2000, -1000, -500, -100, -2, -1, 1, 2, 100, 500, 1000, 2000]
                    )
                    val_wrong = ans_val + diff
                    if val_wrong > 0 and val_wrong != ans_val:
                        s_set.add('$%s$' % (latex(val_wrong)))

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    '''Cho một cấp số nhân $(u_n)$ có công bội $q$ thỏa mãn $\\begin{cases} u_5 + u_2 = %s \\\\ u_6 - u_4 = %s \\end{cases}$. Giá trị $u_1 + 2024q$ bằng bao nhiêu?'''
                    % (latex(A), latex(B))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    '''Ta có: $\\begin{cases} u_5 + u_2 = %s \\\\ u_6 - u_4 = %s \\end{cases} \\Leftrightarrow \\begin{cases} u_1 \\cdot q^4 + u_1 \\cdot q = %s \\\\ u_1 \\cdot q^5 - u_1 \\cdot q^3 = %s \\end{cases} \\Leftrightarrow \\begin{cases} u_1(q^4 + q) = %s \\\\ u_1(q^5 - q^3) = %s \\end{cases} \\Leftrightarrow \\begin{cases} u_1 = \\frac{%s}{q^4 + q} \\\\ \\frac{q^4 + q}{q^5 - q^3} = \\frac{%s}{%s} \\end{cases}$\\\\
            $\\Rightarrow %s \\cdot (q^4 + q) = %s \\cdot (q^5 - q^3)$\\\\
            $\\Leftrightarrow %sq^4 + %sq = %sq^5 - %sq^3 \\Leftrightarrow %sq^4 + %sq - %sq^5 + %sq^3 = 0$\\\\
            $\\Leftrightarrow q(%s) = 0 \\Leftrightarrow \\begin{bmatrix} q = 0 \\\\ q = -1 \\\\ q = %s \\\\ %s = 0 \\end{bmatrix}$\\\\
            $\\Leftrightarrow q = %s \\text{ (do } q \\neq 0; q \\neq -1\\text{)}$\\\\
            Với $q = %s$ thì $u_1 = \\frac{%s}{%s^4 + %s} = %s$\\\\
            Vậy $q = %s; u_1 = %s$ nên $u_1 + 2024q = %s$.'''
                    % (
                        latex(A),
                        latex(B),
                        latex(A),
                        latex(B),
                        latex(A),
                        latex(B),
                        latex(A),
                        latex(A),
                        latex(B),
                        latex(k2),
                        latex(k1),
                        latex(k2),
                        latex(k2),
                        latex(k1),
                        latex(k1),
                        latex(k2),
                        latex(k2),
                        latex(k1),
                        latex(k1),
                        latex(poly_q4),
                        latex(q_val),
                        latex(quad_neg),
                        latex(q_val),
                        latex(q_val),
                        latex(A),
                        latex(q_val),
                        latex(q_val),
                        latex(u1_val),
                        latex(q_val),
                        latex(u1_val),
                        latex(ans_val),
                    )
                )
            dapan='\\shortans[0]{$%s$}\n'%(latex(ans_val))
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

