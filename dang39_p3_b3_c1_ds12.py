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


def bt_dang39_p3_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Sinh ngẫu nhiên nghiệm của tử x0 và bán hệ số k của x ở mẫu (bậc hai: x^2 - 2kx + m)
                x0 = randint(1, 3)
                k = randint(x0 + 1, 6)

                coeff_x = 2 * k
                k_sq = k**2
                m0 = 2 * k * x0 - x0**2

                # Số nguyên dương tối đa < k^2 là k^2 - 1
                limit_m = k_sq - 1

                # Số giá trị m thỏa mãn = (k^2 - 1) - 1 (do m != m0)
                kq = limit_m - 1

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$%s$' % (latex(limit_m)),
                    '$%s$' % (latex(k_sq)),
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq - 2))
                ]

                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu giá trị nguyên dương của tham số $m$ để đồ thị hàm số $y = \\frac{x - %s}{x^2 - %sx + m}$ có $3$ đường tiệm cận?'''
                                 % (latex(x0), latex(coeff_x)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có $\\lim_{x \\to \\pm\\infty} y = \\lim_{x \\to \\pm\\infty} \\frac{x - %s}{x^2 - %sx + m} = 0$ nên đồ thị hàm số luôn có $1$ đường tiệm cận ngang là $y = 0$.\\\\
            Để đồ thị hàm số có $3$ đường tiệm cận thì đồ thị phải có đúng $2$ đường tiệm cận đứng.\\\\
            Đồ thị hàm số có $2$ đường tiệm cận đứng khi và chỉ khi phương trình $x^2 - %sx + m = 0$ có $2$ nghiệm phân biệt khác $%s$.\\\\
            Xét phương trình $g(x) = x^2 - %sx + m = 0$, điều kiện là:\\\\
            $$\\begin{cases} \\Delta' > 0 \\\\ g(%s) \\ne 0 \\end{cases} \\iff \\begin{cases} %s - m > 0 \\\\ %s^2 - %s \\cdot %s + m \\ne 0 \\end{cases} \\iff \\begin{cases} m < %s \\\\ m \\ne %s \\end{cases}$$\\\\
            Vì $m$ là số nguyên dương nên $m \\in \\{1; 2; \\dots; %s\\}$ và $m \\ne %s$.\\\\
            Do đó, $m \\in \\{1; 2; \\dots; %s\\} \\setminus \\{%s\\}$.\\\\
            Vậy có $%s - 1 = %s$ giá trị nguyên dương của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                           % (latex(x0), latex(coeff_x),
                              latex(coeff_x), latex(x0),
                              latex(coeff_x), latex(x0), latex(k_sq), latex(x0), latex(coeff_x), latex(x0), latex(k_sq), latex(m0),
                              latex(limit_m), latex(m0),
                              latex(limit_m), latex(m0),
                              latex(limit_m), latex(kq)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

