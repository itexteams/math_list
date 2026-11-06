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


def bt_dang10_p1_b3_c7_ds11(self):
            # Khai báo biến
            # Ở đây a = 2, b = -1
            lis_a = [2, 3, 4, 5]
            lis_b = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

            a = random.choice(lis_a)
            b = random.choice(lis_b)

            # Định nghĩa hàm số
            y = 1 / (a*x + b)

            # Tính đạo hàm cấp 1 và cấp 2
            y1 = diff(y, x)
            y2 = diff(y1, x)

            # --- BƯỚC 2: VIẾT LẠI THEO MẪU CODE PYTHON ---

            # Câu hỏi
            noidungcauhoi = (r'Đạo hàm cấp hai của hàm số $y = %s$ bằng' % (latex(y)))

            # Đáp án đúng
            da = '$y\'\' = %s$' % (latex(y2))
            da_d = '\\True ' + da

            # Tạo các đáp án nhiễu (sai)
            # Sai dấu, sai hệ số hoặc sai bậc của mẫu số
            s1 = '$y\'\' = -%s$' % (latex(y2)) # Sai dấu
            s2 = '$y\'\' = %s$' % (latex(simplify(a * y1 / (a*x + b)))) # Sai đạo hàm (bậc thấp hơn)
            s3 = '$y\'\' = %s$' % (latex(a * y2)) # Sai hệ số

            # Trộn đáp án
            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            # Xử lý hiển thị dấu cho b trong chuỗi latex
            mau_thuc = f"{a}x + {b}" if b > 0 else f"{a}x - {abs(b)}"
            if b == 0: mau_thuc = f"{a}x"

            # Lời giải chi tiết theo đúng logic hình ảnh
            loigiai = (r'''Ta có $y = \frac{1}{%s} \Rightarrow y' = -\frac{(%s)'}{(%s)^2} = -\frac{%s}{(%s)^2}$. \\
                       Đạo hàm cấp hai: \\
                       $y'' = (y')' = \left( -%s \cdot (%s)^{-2} \right)' = -%s \cdot (-2) \cdot (%s)^{-3} \cdot (%s)'$ \\
                       $\Rightarrow y'' = \frac{%s \cdot 2 \cdot %s}{(%s)^3} = %s$.'''
                       % (latex(a*x + b), latex(a*x + b), latex(a*x + b), latex(a), latex(a*x + b),
                          latex(a), latex(a*x + b), latex(a), latex(a*x + b), latex(a*x + b),
                          latex(a), latex(a), latex(a*x + b), latex(y2)
                         ))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
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

