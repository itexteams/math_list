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


def bt_dang39_p1_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                valid = False
                while not valid:
                    k = random.randint(1, 3) # cot C = k
                    m = random.choice([1, 2]) # m trong BC = m * sqrt(1 + k^2)
                    b = random.randint(2, 6) # AC = b

                    val_under_sqrt = 1 + k**2
                    BC = m * sp.sqrt(val_under_sqrt)
                    AC = b
                    cot_C = k

                    # BC^2 = m^2 * (1 + k^2)
                    # 2 * BC * AC * cos C = 2 * (m * sqrt(1+k^2)) * b * (k / sqrt(1+k^2)) = 2 * m * b * k
                    BC_sq = m**2 * val_under_sqrt
                    AC_sq = b**2
                    term2 = 2 * m * b * k

                    AB_sq = BC_sq + AC_sq - term2

                    if AB_sq > 0:
                        AB = simplify(sqrt(AB_sq))
                        AB_float = float(AB)
                        BC_float = float(BC)
                        # Kiểm tra bất đẳng thức tam giác
                        if (BC_float + AC > AB_float) and (BC_float + AB_float > AC) and (AC + AB_float > BC_float):
                            valid = True

                kq = latex(AB)

                # Tạo các phương án sai (distractors)
                # Sai lầm 1: Nhầm dấu trong định lí cosin
                fake1_sq = BC_sq + AC_sq + term2
                fake1 = simplify(sqrt(fake1_sq))

                # Sai lầm 2: Áp dụng Pytago (BC^2 + AC^2)
                fake2_sq = BC_sq + AC_sq
                fake2 = simplify(sqrt(fake2_sq))

                # Sai lầm 3: Dùng sin C thay vì cos C
                term2_sin = 2 * m * b * 1
                fake3_sq = BC_sq + AC_sq - term2_sin
                fake3 = simplify(sqrt(fake3_sq)) if fake3_sq > 0 else simplify(sqrt(AB_sq + 5))

                # Sai lầm 4: Quên lấy căn bậc hai (AB_sq)
                fake4 = AB_sq

                s_cands = [fake1, fake2, fake3, fake4]
                unique_s_cands = []
                for cand in s_cands:
                    if cand != AB and cand not in unique_s_cands:
                        unique_s_cands.append(cand)

                # Đảm bảo có đủ 3 phương án sai
                while len(unique_s_cands) < 3:
                    bogus = simplify(sqrt(AB_sq + random.choice([-3, -1, 1, 3, 5])))
                    if bogus > 0 and bogus != AB and bogus not in unique_s_cands:
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
                noidungcauhoi = ('Tam giác $ABC$ có $BC = %s, AC = %s$ và $\\cot C = %s$. Cạnh $AB$ bằng'
                                 % (latex(BC), AC, cot_C))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('Vì $\\cot C = %s > 0$ nên góc $C$ là góc nhọn.\\\\ \n'
                           'Ta có: $1 + \\cot^2 C = \\frac{1}{\\sin^2 C} \\Rightarrow 1 + %s^2 = \\frac{1}{\\sin^2 C} \\Rightarrow \\sin^2 C = \\frac{1}{%s} \\Rightarrow \\sin C = \\frac{1}{\\sqrt{%s}}$.\\\\ \n'
                           'Suy ra $\\cos C = \\cot C \\cdot \\sin C = %s \\cdot \\frac{1}{\\sqrt{%s}} = \\frac{%s}{\\sqrt{%s}}$.\\\\ \n'
                           'Áp dụng định lí côsin trong tam giác $ABC$, ta có:\\\\ \n'
                           '$AB^2 = BC^2 + AC^2 - 2 \\cdot BC \\cdot AC \\cdot \\cos C$\\\\ \n'
                           '$\\Rightarrow AB^2 = \\left(%s\\right)^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\frac{%s}{\\sqrt{%s}}$\\\\ \n'
                           '$\\Rightarrow AB^2 = %s + %s - %s = %s$.\\\\ \n'
                           'Vậy $AB = %s$.'
                           % (cot_C, cot_C, val_under_sqrt, val_under_sqrt,
                              cot_C, val_under_sqrt, cot_C, val_under_sqrt,
                              latex(BC), AC, latex(BC), AC, cot_C, val_under_sqrt,
                              BC_sq, AC_sq, term2, AB_sq,
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

