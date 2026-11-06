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


def bt_dang27_p4_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Để kết quả cuối cùng M luôn là một số nguyên, ta thiết kế sẵn các bộ giá trị thỏa mãn lượng giác:
                # Mỗi bộ gồm: (tan_x, sin_x, cos_x, hệ số nhân của cos x ở tử số để biểu thức nguyên)
                # Biểu thức tổng quát: M = (sin^2 x - k * cos x) / (sin x - cos^2 x)
                # Ta chọn các cặp sao cho kết quả phép tính M thu được một số nguyên đẹp
                bo_so_thoa_man = [
                    # Bộ 1: tan x = -4/3, k = -11/25 -> M = 1
                    (Rational(-4, 3), Rational(4, 5), Rational(-3, 5), Rational(-11, 25), 1),
                    # Bộ 2: tan x = -3/4, k = -19/16 -> M = 2
                    (Rational(-3, 4), Rational(3, 5), Rational(-4, 5), Rational(-19, 16), 2),
                    # Bộ 3: tan x = -12/5, k = -323/25 -> M = 3
                    (Rational(-12, 5), Rational(12, 13), Rational(-5, 13), Rational(-323, 25), 3),
                    # Bộ 4: tan x = -5/12, k = -73/144 -> M = 1
                    (Rational(-5, 12), Rational(5, 13), Rational(-12, 13), Rational(-73, 144), 1)
                ]

                # Chọn ngẫu nhiên một bộ số từ danh sách
                tan_val, sin_x, cos_x, he_so_k, kq_nguyen = random.choice(bo_so_thoa_man)

                # Tính toán tử số và mẫu số theo hệ số k mới để đảm bảo kết quả nguyên nguyên bản
                tu_so = sin_x**2 - he_so_k * cos_x
                mau_so = sin_x - cos_x**2

                da = '$%s$' % (latex(kq_nguyen))

                # Tạo các đáp án trắc nghiệm nhiễu là số nguyên
                s = [
                    '$%s$' % (latex(-kq_nguyen)),
                    '$%s$' % (latex(kq_nguyen + 1)),
                    '$%s$' % (latex(kq_nguyen + 2)),
                    '$%s$' % (latex(0)),
                    '$%s$' % (latex(kq_nguyen - 2 if kq_nguyen - 2 != 0 else kq_nguyen + 3)),
                    '$%s$' % (latex(2 * kq_nguyen))
                ]

                # Lọc bỏ phần tử trùng với đáp án đúng và lọc trùng
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Thiết lập hiển thị chuỗi hệ số k trong latex câu hỏi và lời giải
                if he_so_k == 1:
                    chuoi_tu = '\\sin^2 x - \\cos x'
                    chuoi_the = '- \\left(%s\\right)' % (latex(cos_x))
                elif he_so_k == -1:
                    chuoi_tu = '\\sin^2 x + \\cos x'
                    chuoi_the = '+ \\left(%s\\right)' % (latex(cos_x))
                elif he_so_k < 0:
                    chuoi_tu = '\\sin^2 x + %s \\cos x' % (latex(abs(he_so_k)))
                    chuoi_the = '+ %s \\cdot \\left(%s\\right)' % (latex(abs(he_so_k)), latex(cos_x))
                else:
                    chuoi_tu = '\\sin^2 x - %s \\cos x' % (latex(he_so_k))
                    chuoi_the = '- %s \\cdot \\left(%s\\right)' % (latex(he_so_k), latex(cos_x))

                # Câu hỏi
                noidungcauhoi = ('''Cho $\\tan x = %s$ và $\\frac{\\pi}{2} < x < \\pi$. Tính giá trị của biểu thức $M = \\frac{%s}{\\sin x - \\cos^2 x}$.'''
                                 % (latex(tan_val), chuoi_tu))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Vì $\\frac{\\pi}{2} < x < \\pi$ nên $\\sin x > 0$ và $\\cos x < 0$. \\\\
                           Ta có công thức lượng giác cơ bản: $1 + \\tan^2 x = \\frac{1}{\\cos^2 x}$ \\\\
                           $\\Rightarrow \\cos^2 x = \\frac{1}{1 + \\tan^2 x} = \\frac{1}{1 + \\left(%s\\right)^2} = %s$. \\\\
                           Vì $\\cos x < 0$ nên $\\cos x = -\\sqrt{%s} = %s$. \\\\
                           Từ đó ta suy ra: $\\sin x = \\tan x \\cdot \\cos x = \\left(%s\\right) \\cdot \\left(%s\\right) = %s$. \\\\
                           Thay giá trị của $\\sin x$ và $\\cos x$ vừa tìm được vào biểu thức $M$, ta thu được: \\\\
                           $M = \\frac{\\left(%s\\right)^2 %s}{\\frac{%s}{%s} - \\left(%s\\right)^2} = \\frac{%s}{%s} = %s$.'''
                           % (latex(tan_val), latex(cos_x**2), latex(cos_x**2), latex(cos_x),
                              latex(tan_val), latex(cos_x), latex(sin_x),
                              latex(sin_x), chuoi_the, latex(sin_x.p), latex(sin_x.q), latex(cos_x),
                              latex(tu_so), latex(mau_so), latex(kq_nguyen)))



            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

