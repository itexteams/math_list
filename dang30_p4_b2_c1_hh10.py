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


def bt_dang30_p4_b2_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random góc và 2 cạnh
                angles = [30, 45, 60, 120, 135, 150]
                A_deg = random.choice(angles)
                b = random.randint(4, 9)
                c = random.randint(4, 10)

                # Đảm bảo b khác c để tam giác đa dạng
                while b == c:
                    c = random.randint(4, 10)

                A_rad = A_deg * sp.pi / 180

                # Tính cạnh a
                cos_A = sp.cos(A_rad)
                a_sq = b**2 + c**2 - 2*b*c*cos_A
                a_val = sp.simplify(sp.sqrt(a_sq))

                kq = latex(a_val)

                # Tạo các đáp án sai
                s_cands = []

                # Sai lầm 1: cộng nhầm dấu (a^2 = b^2 + c^2 + 2bc cosA)
                fake1 = sp.simplify(sp.sqrt(b**2 + c**2 + 2*b*c*cos_A))
                if fake1 != a_val: 
                    s_cands.append(fake1)

                # Sai lầm 2: quên trừ phần 2bc cosA (Pytago)
                fake2 = sp.simplify(sp.sqrt(b**2 + c**2))
                if fake2 not in s_cands and fake2 != a_val: 
                    s_cands.append(fake2)

                # Sai lầm 3: quên nhân 2 (a^2 = b^2 + c^2 - bc cosA)
                fake3_sq = b**2 + c**2 - b*c*cos_A
                if fake3_sq > 0:
                    fake3 = sp.simplify(sp.sqrt(fake3_sq))
                    if fake3 not in s_cands and fake3 != a_val: 
                        s_cands.append(fake3)

                # Bổ sung nếu chưa đủ 3 đáp án sai
                while len(s_cands) < 3:
                    f_sq = a_sq + random.choice([-5, -4, 4, 5, 8, 12])
                    if f_sq > 0:
                        f = sp.simplify(sp.sqrt(f_sq))
                        if f not in s_cands and f != a_val:
                            s_cands.append(f)

                random.shuffle(s_cands)
                das1 = '$%s$' % latex(s_cands[0])
                das2 = '$%s$' % latex(s_cands[1])
                das3 = '$%s$' % latex(s_cands[2])

                # Câu hỏi
                noidungcauhoi = ('Cho $\\Delta ABC$ có $b = %s, c = %s, A = %s^\\circ$. Tính độ dài cạnh $a$.'
                                 % (b, c, A_deg))

                # Các đáp án
                da_d = ('\\True $%s$' % kq)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Tính toán chi tiết cho lời giải
                cos_val_str = latex(cos_A)
                a_sq_val = latex(a_sq)
                bc2 = latex(2*b*c)

                # Nội dung lời giải
                loigiai = ('Áp dụng định lí côsin trong tam giác $ABC$, ta có: \\\\ '
                           '$a^2 = b^2 + c^2 - 2bc \\cos A$ \\\\ '
                           '$\\Rightarrow a^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos %s^\\circ$ \\\\ '
                           '$\\Rightarrow a^2 = %s + %s - %s \\cdot \\left(%s\\right) = %s$ \\\\ '
                           '$\\Rightarrow a = %s$.' 
                           % (b, c, b, c, A_deg, b**2, c**2, bc2, cos_val_str, a_sq_val, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

