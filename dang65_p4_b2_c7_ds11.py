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


def bt_dang65_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Tạo các hệ số ngẫu nhiên cho hàm số: y = tan(ax) - (1/b)*cot(cx) + sqrt(sin(dx))
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            c = random.randint(2, 6)
            d = 1 # Giữ d=1 như trong đề bài gốc để đảm bảo tính thẩm mỹ, hoặc có thể random

            # Thiết lập hàm số
            f1 = tan(a*x)
            f2 = Rational(1, b) * cot(c*x)
            f3 = sqrt(sin(x))
            y = f1 - f2 + f3

            # Tính đạo hàm từng thành phần để trình bày lời giải
            df1 = diff(f1, x)
            df2 = diff(f2, x)
            df3 = diff(f3, x)
            y_prime = df1 - df2 + df3

            # Chuyển sang định dạng LaTeX
            # Xử lý hiển thị dấu -- thành + cho phần đạo hàm cot
            # Đạo hàm của -cot(ux) là +u/sin^2(ux)
            dau_f2 = "+" if b > 0 else "-"

            # Câu hỏi
            noidungcauhoi = r"Tính đạo hàm của hàm số $y = \tan %sx - \frac{1}{%s} \cot %sx + \sqrt{\sin x}$." % (latex(a), latex(b), latex(c))

            # Đáp án đúng
            da = r"$y' = %s$" % latex(y_prime).replace('**', '^')
            da_d = r'\True ' + da

            # Tạo các đáp án nhiễu (sai hệ số hoặc sai dấu)
            s = [
                r"$y' = \frac{%s}{\cos^2 %sx} - \frac{%s}{%s \sin^2 %sx} + \frac{\cos x}{2\sqrt{\sin x}}$" % (a, a, c, b, c),
                r"$y' = \frac{1}{\cos^2 %sx} + \frac{1}{%s \sin^2 %sx} + \frac{\cos x}{\sqrt{\sin x}}$" % (a, b, c),
                r"$y' = \frac{%s}{\cos^2 %sx} + \frac{%s}{%s \sin^2 %sx} - \frac{\sin x}{2\sqrt{\cos x}}$" % (a, a, c, b, c),
                r"$y' = \frac{%s}{\sin^2 %sx} + \frac{%s}{%s \cos^2 %sx} + \frac{\cos x}{2\sqrt{\sin x}}$" % (a, a, c, b, c)
            ]

            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Nội dung lời giải chi tiết
            loigiai = r'''Ta có: $y' = (\tan %sx)' - \frac{1}{%s}(\cot %sx)' + (\sqrt{\sin x})'$ \\
            $y' = \frac{(%sx)'}{\cos^2 %sx} - \frac{1}{%s} \cdot \left( -\frac{(%sx)'}{\sin^2 %sx} \right) + \frac{(\sin x)'}{2\sqrt{\sin x}}$ \\
            $y' = \frac{%s}{\cos^2 %sx} + \frac{%s}{%s \sin^2 %sx} + \frac{\cos x}{2\sqrt{\sin x}}$.''' % (
                latex(a), latex(b), latex(c), 
                latex(a), latex(a), latex(b), latex(c), latex(c),
                latex(a), latex(a), latex(c), latex(b), latex(c)
            )

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

