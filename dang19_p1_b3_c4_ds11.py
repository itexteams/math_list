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


def bt_dang19_p1_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho sympy
            x = symbols('x')

            # Danh sách dạng (ở đây chỉ có 1 dạng theo yêu cầu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random các thông số cho bài toán
                x0 = randint(-3, 3) # Điểm xét tính liên tục

                # Hàm f1(x) = Ax^2 + Bx + C (khi x <= x0)
                A = randint(1, 3)
                B = randint(-5, 5)
                C = randint(-5, 10)
                f1 = A*x**2 + B*x + C

                # Hàm f2(x) = Dx + a (khi x > x0)
                D = randint(-5, 5)
                if D == 0: D = 1 # Tránh hệ số 0 cho đẹp
                f2_part = D*x # Phần không chứa 'a' của f2

                # B1 & B2: Tính toán lời giải
                val_f1 = f1.subs(x, x0)      # Tính f1(x0)
                val_f2_part = D * x0         # Tính D*x0

                kq_a = val_f1 - val_f2_part  # a = f1(x0) - D*x0

                # Các đáp án trắc nghiệm
                da = kq_a
                s = [da + 1, da - 1, da + 2, da - 2, da + 3, -da]
                # Loại bỏ các đáp án trùng với đáp án đúng
                s = list(set([i for i in s if i != da]))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Sử dụng latex() để hiển thị công thức đẹp
                bieuthuc_f1 = latex(f1)
                bieuthuc_f2 = latex(D*x) + " + a"

                noidungcauhoi = (r'''Để hàm số $y = \begin{cases} %s & \text{khi } x \le %s \\ %s & \text{khi } x > %s \end{cases}$ liên tục tại điểm $x = %s$ thì giá trị của $a$ là'''
                                 % (bieuthuc_f1, latex(x0), bieuthuc_f2, latex(x0), latex(x0)))

                # Các đáp án
                da_d = ('\\True $%s$' % (latex(da)))
                da_s1 = '$%s$' % (latex(das1))
                da_s2 = '$%s$' % (latex(das2))
                da_s3 = '$%s$' % (latex(das3))

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Hàm số liên tục tại $x = %s$ khi và chỉ khi $\lim_{x \to %s^+} y = \lim_{x \to %s^-} y = y(%s)$ \\
                             $\Leftrightarrow \lim_{x \to %s^+} (%s) = \lim_{x \to %s^-} (%s) = y(%s)$ \\
                             $\Leftrightarrow %s + a = %s$ \\
                             $\Leftrightarrow a = %s$.'''
                           % (latex(x0), latex(x0), latex(x0), latex(x0),
                              latex(x0), bieuthuc_f2, latex(x0), bieuthuc_f1, latex(x0),
                              latex(val_f2_part), latex(val_f1), latex(kq_a)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

