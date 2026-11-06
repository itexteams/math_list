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


def bt_dang30_p1_b2_c4_ds11(self):
            # Khai báo biến
            # 1. Chọn danh sách các số chính phương cho hệ số trong căn để khai căn ra số nguyên
            chinh_phuong = [1, 4, 9, 16, 25]

            # 2. Random các tham số
            a = random.randint(2, 10)                     # Hệ số của x trên tử (chọn từ 2-10)
            b = random.randint(-10, 10)                    # Hệ số tự do trên tử
            c = random.choice(chinh_phuong)                # Hệ số x^2 (phải là số chính phương)
            d = random.randint(1, 20)                      # Số dương trong căn
            e = random.randint(-10, 10)                    # Số tự do dưới mẫu

            # Loại bỏ trường hợp b=0 hoặc e=0 để đề bài nhìn đầy đủ (tùy chọn)
            if b == 0: b = 1
            if e == 0: e = -1

            # 3. Tính toán kết quả
            # Khi x -> -vô cùng, sqrt(c*x^2) = -x*sqrt(c)
            can_c = int(sqrt(c))
            kq_val = Rational(a, -can_c)
            kq = latex(kq_val)

            # 4. Xử lý hiển thị dấu (+ -) trong LaTeX
            def format_sign(val):
                return f"+ {val}" if val > 0 else f"- {abs(val)}"

            str_b = format_sign(b)
            str_d = format_sign(d)
            str_e = format_sign(e)
            str_c = f"{c}" if c != 1 else ""

            # 5. Các đáp án gây nhiễu
            du = ['\\True $%s$' % kq]
            s = [
                '$%s$' % latex(Rational(a, can_c)),    # Sai dấu (quên x -> -inf)
                '$0$',                                 # Đáp án phổ biến
                '$%s$' % latex(Rational(b, can_c) if b != 0 else 1), # Nhầm hệ số tự do
                '$- \\infty$',
                '$1$'
            ]
            random.shuffle(s)
            list_choices = [du[0], s[0], s[1], s[2]]
            random.shuffle(list_choices)

            # 6. Nội dung câu hỏi
            noidungcauhoi = r"Giá trị của $\displaystyle \lim_{x \to -\infty} \frac{%sx %s}{\sqrt{%sx^2 %s} %s}$ bằng" % (a, str_b, str_c, str_d, str_e)

            # 7. Lời giải chi tiết (tự động điều chỉnh theo x -> -inf)
            loigiai = r'''Ta có: $\displaystyle \lim_{x \to -\infty} \frac{%sx %s}{\sqrt{%sx^2 %s} %s}$ 
            $= \lim_{x \to -\infty} \frac{x\left(%s %s/x\right)}{-x\sqrt{%s %s/x^2} %s}$ 
            $= \lim_{x \to -\infty} \frac{%s %s/x}{-\sqrt{%s %s/x^2} %s/x} = \frac{%s}{-\sqrt{%s}} = %s$.''' % (
                a, str_b, str_c, str_d, str_e,
                a, b, c, d, str_e,
                a, b, c, d, e,
                a, c, kq
            )

            # 8. Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_choices[0])+'}\n'
                '{'+str(list_choices[1])+'}\n'
                '{'+str(list_choices[2])+'}\n'
                '{'+str(list_choices[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

