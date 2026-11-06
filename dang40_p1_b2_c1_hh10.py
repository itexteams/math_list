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


def bt_dang40_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                valid = False
                while not valid:
                    # Chọn mẫu số k của cos A = -1/k
                    k = random.choice([2, 3, 4, 5])
                    c = random.randint(2, 7) # Cạnh AB
                    b = random.randint(2, 7) # Cạnh AC
                    # Đảm bảo phép tính có giá trị nguyên và các cạnh không bằng nhau để đa dạng
                    if c != b and (2 * c * b) % k == 0:
                        valid = True

                # Tính giá trị tan A dựa vào k
                tan_val = -sp.simplify(sp.sqrt(k**2 - 1))
                tan_str = latex(tan_val)
                cos_val = Rational(-1, k)

                # Tính BC^2 theo định lí côsin
                term3 = (2 * c * b) // k
                BC_sq = c**2 + b**2 + term3
                BC = sp.simplify(sp.sqrt(BC_sq))
                kq = latex(BC)

                # Tạo các phương án sai (distractors)
                # Sai lầm 1: Nhầm dấu cos A (nghĩ rằng cos A = 1/k)
                fake1_sq = c**2 + b**2 - term3
                fake1 = sp.simplify(sp.sqrt(fake1_sq)) if fake1_sq > 0 else sp.simplify(sp.sqrt(BC_sq + 5))

                # Sai lầm 2: Áp dụng định lí Pytago
                fake2_sq = c**2 + b**2
                fake2 = sp.simplify(sp.sqrt(fake2_sq))

                # Sai lầm 3: Quên nhân hệ số 2 trong định lí côsin
                if (c * b) % k == 0:
                    fake3_sq = c**2 + b**2 + (c * b) // k
                else:
                    fake3_sq = BC_sq + 3
                fake3 = sp.simplify(sp.sqrt(fake3_sq))

                # Đưa vào danh sách và lọc trùng
                s_cands = [fake1, fake2, fake3]
                unique_s_cands = []
                for cand in s_cands:
                    if cand != BC and cand not in unique_s_cands:
                        unique_s_cands.append(cand)

                # Đảm bảo đủ 3 phương án sai
                while len(unique_s_cands) < 3:
                    bogus = sp.simplify(sp.sqrt(BC_sq + random.choice([2, 4, -2, 6, 8])))
                    if bogus > 0 and bogus != BC and bogus not in unique_s_cands:
                        unique_s_cands.append(bogus)

                random.shuffle(unique_s_cands)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(unique_s_cands[0])),
                    '$%s$' % (latex(unique_s_cands[1])),
                    '$%s$' % (latex(unique_s_cands[2]))
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Tam giác $ABC$ có $AB = %s, AC = %s$ và $\\tan A = %s$. Cạnh $BC$ bằng'
                                 % (c, b, tan_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Vì $\\tan A = %s < 0$ nên góc $A$ là góc tù, do đó $\\cos A < 0$.\\\\ \n'
                           'Ta có: $1 + \\tan^2 A = \\frac{1}{\\cos^2 A} \\Rightarrow 1 + \\left(%s\\right)^2 = \\frac{1}{\\cos^2 A} \\Rightarrow \\frac{1}{\\cos^2 A} = %s \\Rightarrow \\cos^2 A = \\frac{1}{%s}$.\\\\ \n'
                           'Vì $\\cos A < 0$ nên $\\cos A = -\\frac{1}{%s}$.\\\\ \n'
                           'Áp dụng định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'
                           '$BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A$\\\\ \n'
                           '$\\Rightarrow BC^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(-\\frac{1}{%s}\\right)$\\\\ \n'
                           '$\\Rightarrow BC^2 = %s + %s + %s = %s$.\\\\ \n'
                           'Vậy $BC = %s$.'
                           % (tan_str, tan_str, k**2, k**2, k,
                              c, b, c, b, k,
                              c**2, b**2, term3, BC_sq,
                              kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

