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


def bt_dang16_p4_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho bài toán tròn số và thực tế
                V0 = random.choice([500, 800, 1000, 1200, 1500, 2000])
                c = random.choice([10, 12, 15, 20, 25, 30, 35])
                r = random.choice([10, 15, 20, 25, 30, 40])

                # Đáp án đúng là nồng độ muối của nước bơm vào (tiệm cận ngang khi t tiến tới vô cùng)
                kq = c

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Tạo danh sách các đáp án nhiễu logic
                s = [
                    '$%s$' % (latex(c + 5)),
                    '$%s$' % (latex(c - 5 if c > 5 else c + 8)),
                    '$%s$' % (latex(r)),
                    '$%s$' % (latex(c * 2)),
                    '$%s$' % (latex(c + 10)),
                    '$%s$' % (latex(V0 // r if V0 % r == 0 else c + 3))
                ]

                # Xóa trùng và xóa đáp án đúng ra khỏi danh sách nhiễu
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Một bể chứa $%s$ lít nước tinh khiết. Người ta bơm vào bể đó nước muối có nồng độ $%s$ gam muối cho mỗi lít nước với tốc độ $%s$ lít/phút. Biết rằng nồng độ muối trong bể sau $t$ phút (tính bằng tỉ số của khối lượng muối trong bể và thể tích nước trong bể, đơn vị: gam/lít) là một hàm số $f(t)$, thời gian $t$ tính bằng phút. Phương trình tiệm cận ngang của đồ thị hàm số $f(t)$ là $y = a, (a \\in \\mathbb{R})$. Tính giá trị của $a$.'''
                                 % (latex(V0), latex(c), latex(r)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                cr = c * r
                loigiai = ('''Sau $t$ phút ($t \\ge 0$): \\\\
            - Thể tích nước trong bể là: $V(t) = %s + %st$ (lít). \\\\
            - Khối lượng muối trong bể là: $m(t) = %s \\cdot %st = %st$ (gam). \\\\
            - Nồng độ muối trong bể tại thời điểm $t$ là: $f(t) = \\frac{m(t)}{V(t)} = \\frac{%st}{%s + %st}$ (gam/lít). \\\\
            Ta có $\\lim_{t \\to +\\infty} f(t) = \\lim_{t \\to +\\infty} \\frac{%st}{%st + %s} = %s$. \\\\
            Do đó, đồ thị hàm số $f(t)$ có phương trình tiệm cận ngang là $y = %s$, suy ra $a = %s$.'''
                           % (latex(V0), latex(r), latex(c), latex(r), latex(cr), latex(cr), latex(V0), latex(r),
                              latex(cr), latex(r), latex(V0), latex(c), latex(c), latex(c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content     

