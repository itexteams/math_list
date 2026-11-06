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


def bt_dang45_p4_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random sin(alpha) = a/b với a < b
                pairs = [(1, 3), (1, 4), (2, 5), (1, 5), (2, 3)]
                a, b = random.choice(pairs)

                # Hệ số trong biểu thức M = (tan(alpha) - k1*cot(alpha) + k2) / (tan(alpha) + cot(alpha))
                k1 = random.choice([2, 3, 4])
                k2 = random.choice([1, 2, 3])

                sin_a = Rational(a, b)
                cos_a = simplify(sqrt(1 - sin_a**2))
                tan_a = simplify(sin_a / cos_a)
                cot_a = simplify(1 / tan_a)

                num_expr = simplify(tan_a - k1 * cot_a + k2)
                den_expr = simplify(tan_a + cot_a)
                M_val = simplify(num_expr / den_expr)

                # Đáp án đúng
                du = ['$%s$' % latex(M_val)]
                da = du[0]

                # Các phương án sai (nhiễu)
                w1 = simplify((tan_a + k1 * cot_a + k2) / den_expr)
                w2 = simplify((tan_a - k1 * cot_a - k2) / den_expr)
                w3 = simplify((tan_a - k1 * cot_a + k2 + 1) / den_expr)
                w4 = simplify((-tan_a - k1 * cot_a + k2) / den_expr)

                candidates = [w1, w2, w3, w4]
                s_set = set()
                for cand in candidates:
                    cand_str = '$%s$' % latex(cand)
                    if cand != M_val and cand_str != da:
                        s_set.add(cand_str)

                # Bổ sung nếu trùng lặp
                count = 1
                while len(s_set) < 3:
                    fake = M_val + Rational(count, 3)
                    fake_str = '$%s$' % latex(fake)
                    if fake != M_val and fake_str != da:
                        s_set.add(fake_str)
                    count += 1

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\alpha$ là góc nhọn và thỏa mãn $\\sin \\alpha = %s$. Tính giá trị của biểu thức $M = \\frac{\\tan \\alpha - %s\\cot \\alpha + %s}{\\tan \\alpha + \\cot \\alpha}$.'''
                                 % (latex(sin_a), latex(k1), latex(k2)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Vì $\\alpha$ là góc nhọn ($0^\\circ < \\alpha < 90^\\circ$) nên $\\cos \\alpha > 0$. \\\\
                              Ta có: $\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - \\left(%s\\right)^2} = %s$. \\\\
                              Suy ra $\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} = \\frac{%s}{%s} = %s$ \\\\
                              và $\\cot \\alpha = \\frac{1}{\\tan \\alpha} = %s$. \\\\
                              Thay $\\tan \\alpha$ và $\\cot \\alpha$ vào biểu thức $M$, ta được: \\\\
                              Tử số: $\\tan \\alpha - %s\\cot \\alpha + %s = %s - %s \\cdot \\left(%s\\right) + %s = %s$. \\\\
                              Mẫu số: $\\tan \\alpha + \\cot \\alpha = %s + %s = %s$. \\\\
                              Do đó $M = \\frac{%s}{%s} = %s$.'''
                           % (latex(sin_a), latex(cos_a),
                              latex(sin_a), latex(cos_a), latex(tan_a),
                              latex(cot_a),
                              latex(k1), latex(k2), latex(tan_a), latex(k1), latex(cot_a), latex(k2), latex(num_expr),
                              latex(tan_a), latex(cot_a), latex(den_expr),
                              latex(num_expr), latex(den_expr), latex(M_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

