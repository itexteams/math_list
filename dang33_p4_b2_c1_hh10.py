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


def bt_dang33_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ ba Pytago (x, y, z) tương ứng cosA = x/z, sinA = y/z (với góc A nhọn)
                triples = [
                    (4, 3, 5),   # cosA = 4/5, sinA = 3/5
                    (3, 4, 5),   # cosA = 3/5, sinA = 4/5
                    (12, 5, 13), # cosA = 12/13, sinA = 5/13
                    (5, 12, 13)  # cosA = 5/13, sinA = 12/13
                ]

                x_val, y_val, z_val = random.choice(triples)
                sin_A = Rational(y_val, z_val)
                cos_A = Rational(x_val, z_val)

                # Sinh độ dài cạnh AB (c_val) và AC (b_val) sao cho diện tích S là số nguyên
                m1 = random.randint(1, 2)
                m2 = random.randint(2, 4)

                c_val = m1 * z_val  # AB
                b_val = m2 * 2      # AC

                if c_val == b_val:
                    b_val += 2

                # Diện tích S = 1/2 * AB * AC * sinA
                S_val = Rational(1, 2) * c_val * b_val * sin_A
                S_int = int(S_val)

                # Tính BC theo định lí cosin: BC^2 = AB^2 + AC^2 - 2*AB*AC*cosA
                BC_sq = c_val**2 + b_val**2 - 2 * c_val * b_val * cos_A
                BC = simplify(sqrt(BC_sq))

                # Các phương án sai (distractors)
                fake1 = simplify(sqrt(c_val**2 + b_val**2 + 2 * c_val * b_val * cos_A)) # Nhầm góc tù (sai dấu)
                fake2 = simplify(sqrt(c_val**2 + b_val**2)) # Nhầm Pytago
                fake3_sq = c_val**2 + b_val**2 - 2 * c_val * b_val * sin_A # Nhầm dùng sinA cho định lí cos
                fake3 = simplify(sqrt(fake3_sq)) if fake3_sq > 0 else simplify(sqrt(c_val**2 + b_val**2 + 5))
                fake4 = simplify(sqrt(c_val**2 + b_val**2 - c_val * b_val * cos_A)) # Quên nhân 2

                cands = [fake1, fake2, fake3, fake4]
                unique_cands = []
                for cand in cands:
                    if cand != BC and cand not in unique_cands:
                        unique_cands.append(cand)

                while len(unique_cands) < 3:
                    extra = simplify(sqrt(BC_sq + random.choice([4, 9, 16, -4, -9])))
                    if extra > 0 and extra != BC and extra not in unique_cands:
                        unique_cands.append(extra)

                random.shuffle(unique_cands)

                # Đáp án đúng và sai
                du = ['$%s$' % (latex(BC))]
                da = random.choice(du)

                das1 = '$%s$' % (latex(unique_cands[0]))
                das2 = '$%s$' % (latex(unique_cands[1]))
                das3 = '$%s$' % (latex(unique_cands[2]))

                # Câu hỏi
                noidungcauhoi = ('''Tam giác $ABC$ có góc $A$ nhọn, $AB = %s, AC = %s$, diện tích bằng $%s$. Tính độ dài cạnh $BC$.'''
                                 % (latex(c_val), latex(b_val), latex(S_int)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $S_{\\Delta ABC} = \\frac{1}{2} \\cdot AB \\cdot AC \\cdot \\sin A \\Rightarrow \\sin A = \\frac{2S}{AB \\cdot AC} = \\frac{2 \\cdot %s}{%s \\cdot %s} = %s$. \\\\
                             Vì góc $A$ nhọn nên $\\cos A > 0 \\Rightarrow \\cos A = \\sqrt{1 - \\sin^2 A} = \\sqrt{1 - \\left(%s\\right)^2} = %s$. \\\\
                             Áp dụng định lí côsin trong tam giác $ABC$, ta có: \\\\
                             $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A$ \\\\
                             $\\Rightarrow BC^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot %s = %s + %s - %s = %s$. \\\\
                             Vậy $BC = %s$.'''
                           % (latex(S_int), latex(c_val), latex(b_val), latex(sin_A),
                              latex(sin_A), latex(cos_A),
                              latex(c_val), latex(b_val), latex(c_val), latex(b_val), latex(cos_A),
                              latex(c_val**2), latex(b_val**2), latex(simplify(2*c_val*b_val*cos_A)), latex(BC_sq),
                              latex(BC)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

