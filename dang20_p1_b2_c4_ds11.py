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


def bt_dang20_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Cách random bài toán
            # Ta tạo bài toán dạng: lim_{x -> a} (x^2 - a^2) / (x - k) 
            # Trong đó k = a hoặc k = -a để triệt tiêu nhân tử.
            a = random.choice([i for i in range(-10, 11) if i != 0])
            loai = random.choice(['tong_hieu', 'dat_nhan_tu'])

            if loai == 'tong_hieu':
                # Dạng: (x^2 - a^2) / (x - a) hoặc (x^2 - a^2) / (x + a)
                tu_thuc = x**2 - a**2
                # Chọn ngẫu nhiên mẫu là (x-a) hoặc (x+a)
                bien_so = random.choice([a, -a])
                mau_thuc = x - bien_so
                x_tien_den = bien_so

                # Nhân tử để triệt tiêu
                nhan_tu_triet_tieu = x - bien_so
                nhan_tu_con_lai = x + bien_so
            else:
                # Dạng: (x^2 + bx) / x (giống câu đầu trong hình)
                b = random.randint(1, 10)
                tu_thuc = x**2 + b*x
                mau_thuc = x
                x_tien_den = 0
                nhan_tu_triet_tieu = x
                nhan_tu_con_lai = x + b

            # Tính kết quả
            kq_limit = nhan_tu_con_lai.subs(x, x_tien_den)

            # --- B2: Viết lại theo mẫu code ---

            # Câu hỏi
            noidungcauhoi = r"$\lim_{x \to %s} \frac{%s}{%s}$ bằng" % (latex(x_tien_den), latex(tu_thuc), latex(mau_thuc))

            # Đáp án
            da_dung = '$%s$' % latex(kq_limit)
            s = set()
            while len(s) < 3:
                sai = kq_limit + random.choice([-5, -2, -1, 1, 2, 5, 10])
                if sai != kq_limit: s.add('$%s$' % latex(sai))
            list_sai = list(s)

            da_d = '\\True ' + da_dung
            list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            # Lời giải (Sửa lỗi hiển thị dấu từ hình ảnh)
            loigiai = r"Ta có $\lim_{x \to %s} \frac{%s}{%s} = \lim_{x \to %s} \frac{(%s)(%s)}{%s} = \lim_{x \to %s} (%s) = %s$." % (
                latex(x_tien_den), latex(tu_thuc), latex(mau_thuc),
                latex(x_tien_den), latex(nhan_tu_triet_tieu), latex(nhan_tu_con_lai), latex(mau_thuc),
                latex(x_tien_den), latex(nhan_tu_con_lai), latex(kq_limit)
            )

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_ans[0])+'}\n'
                '{'+str(list_ans[1])+'}\n'
                '{'+str(list_ans[2])+'}\n'
                '{'+str(list_ans[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

