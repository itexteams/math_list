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


def bt_dang69_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Khởi tạo các giá trị random
        k = random.choice([2, 3, 4, 5, 6, 7]) # Tỉ lệ k:1
        a_val = random.choice([50, 60, 80, 100, 120, 150, 200]) # Đáp án a
        c1 = random.choice([100, 200, 300, 400, 500]) # Hằng số trong R(x)
        c2 = random.choice([3000, 4000, 4200, 5000, 6000]) # Hằng số trong Q(x)

        # Tính toán x0 (p) ngược lại để đảm bảo kết quả a là số nguyên
        p = int(2 * a_val * (k + 1) + (c1 + c2) / 2)

        kq = a_val

        # Các đáp án trắc nghiệm
        du = ['$%s$'%(latex(kq)),
              ]
        da = random.choice(du)

        # Sinh các phương án sai (đảm bảo không âm và không trùng đáp án đúng)
        s_opts = [kq + 10, kq + 20, kq - 10, kq - 20, kq + 50, kq + 30, kq + 40]
        s_opts = list(set([val for val in s_opts if val > 0 and val != kq]))
        random.shuffle(s_opts)

        s = ['$%s$'%(latex(val)) for val in s_opts]

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('''Một doanh nghiệp kinh doanh một loại sản phẩm $T$ được sản xuất trong nước. Qua nghiên cứu và phân tích, công ty thấy rằng nếu chi phí sản xuất mỗi sản phẩm $T$ là $x$ (USD) thì số sản phẩm $T$ các nhà máy sản xuất sẽ là $R(x)=x-%s$ và số sản phẩm $T$ mà doanh nghiệp bán được trên thị trường trong nước sẽ là $Q(x)=%s-x$. Số sản phẩm còn dư doanh nghiệp xuất khẩu ra thị trường quốc tế với giá bán mỗi sản phẩm ổn định trên thị trường quốc tế là $x_0=%s$ (USD). Nhà nước đánh thuế trên mỗi sản phẩm xuất khẩu là $a$ (USD) và luôn đảm bảo tỉ lệ giữa lãi xuất xuất khẩu của doanh nghiệp và thuế thu được của nhà nước tương ứng là $%s:1$. Giá trị của $a$ biết lãi mà doanh nghiệp thu được do xuất khẩu là nhiều nhất bằng bao nhiêu?'''
                         %(latex(c1), latex(c2), latex(p), latex(k)))

        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Số sản phẩm doanh nghiệp xuất khẩu là $E(x) = R(x) - Q(x) = (x - %s) - (%s - x) = 2x - %s$.\\\\
                     Lãi xuất khẩu trên mỗi sản phẩm là $x_0 - x - a = %s - x - a$.\\\\
                     Thuế nhà nước thu được trên mỗi sản phẩm xuất khẩu là $a$.\\\\
                     Theo bài ra, tỉ lệ giữa lãi xuất khẩu và thuế là $%s:1$ nên ta có:\\\\
                     $\\frac{%s - x - a}{a} = %s \\Leftrightarrow %s - x - a = %s a \\Leftrightarrow x = %s - %s a$.\\\\
                     Thay $x$ vào biểu thức $E(x)$ ta được số lượng sản phẩm xuất khẩu theo $a$:\\\\
                     $E(a) = 2(%s - %s a) - %s = %s - %s a$.\\\\
                     Tổng lãi xuất khẩu của doanh nghiệp là:\\\\
                     $P(a) = %s a \\cdot E(a) = %s a (%s - %s a)$.\\\\
                     Đây là một hàm số bậc hai biến $a$ có hệ số của $a^2$ âm, do đó $P(a)$ đạt giá trị lớn nhất tại đỉnh parabol:\\\\
                     $a = \\frac{%s}{2 \\cdot %s} = %s$.\\\\
                     Vậy $a = %s$ thì doanh nghiệp thu được lãi xuất khẩu lớn nhất.'''
                     % (latex(c1), latex(c2), latex(c1+c2),
                        latex(p),
                        latex(k),
                        latex(p), latex(k), latex(p), latex(k), latex(p), latex(k+1),
                        latex(p), latex(k+1), latex(c1+c2), latex(2*p - (c1+c2)), latex(2*(k+1)),
                        latex(k), latex(k), latex(2*p - (c1+c2)), latex(2*(k+1)),
                        latex(2*p - (c1+c2)), latex(2 * 2*(k+1)), latex(kq),
                        latex(kq)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

