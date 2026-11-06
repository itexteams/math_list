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


def bt_dang31_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                m = random.choice([2, 4, 5, 8, 10])
                k_sqrt = random.choice([20, 30, 40, 50])
                x_max = 2 * k_sqrt

                k = (k_sqrt**2) // m
                n = random.choice([2, 3, 4, 5])

                # Giá bán: (p - qx). Thông tin này không ảnh hưởng đến "chi phí trung bình"
                p = random.choice([800, 900, 1000])
                q = random.choice([4, 5, 6, 8])

                kq = k_sqrt

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng với đáp án đúng)
                s = ['$%s$'%(latex(kq + 10)),
                     '$%s$'%(latex(kq - 10)),
                     '$%s$'%(latex(kq + 20)),
                     '$%s$'%(latex(kq - 20)),
                     '$%s$'%(latex(kq + 5)),
                     '$%s$'%(latex(kq - 5)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Giả sử tổng chi phí sản xuất $x$ $(0 < x \\le %s)$ đơn vị sản phẩm $A$ mỗi ngày tại một nhà máy được cho bởi công thức $C(x) = \\frac{x^2}{%s} + %sx + %s$ (nghìn đồng) và toàn bộ chúng được bán hết với giá $(%s - %sx)$ nghìn đồng một sản phẩm. Mức sản lượng (đó là số lượng sản phẩm được sản xuất) để chi phí trung bình tính trên mỗi đơn vị sản phẩm là đạt cực tiểu bằng bao nhiêu?'''
                                 %(x_max, m, n, k, p, q))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm chi phí trung bình là $\\overline{C}(x) = \\frac{C(x)}{x} = \\frac{x}{%s} + %s + \\frac{%s}{x}$ với $0 < x \\le %s$.\\\\
                             Đạo hàm: $\\overline{C}'(x) = \\frac{1}{%s} - \\frac{%s}{x^2}$.\\\\
                             $\\overline{C}'(x) = 0 \\Leftrightarrow \\frac{1}{%s} - \\frac{%s}{x^2} = 0 \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ (do $x > 0$).\\\\
                             Ta có bảng biến thiên của $\\overline{C}(x)$ trên $(0; %s]$:\\\\
                             Tại $x = %s$, $\\overline{C}'(x) = 0$, qua $x = %s$ thì $\\overline{C}'(x)$ đổi dấu từ âm sang dương nên hàm số đạt cực tiểu tại $x = %s$.\\\\
                             Vậy mức sản lượng cần tìm là $%s$ đơn vị sản phẩm.'''
                             %(m, n, k, x_max,
                               m, k,
                               m, k, m*k, kq,
                               x_max,
                               kq, kq, kq,
                               kq))
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content  

