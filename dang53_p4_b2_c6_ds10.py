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


def bt_dang53_p4_b2_c6_ds10(self):
            #Khai báo biến
            # r1: bi xanh, r2: bi đỏ, r3: bi vàng
            r1 = random.randint(3, 6)
            r2 = random.randint(4, 7)
            r3 = random.randint(5, 8)
            tong_bi = r1 + r2 + r3

            # B2: Tính toán các giá trị theo lời giải trong ảnh
            # n(Omega) = C(tong_bi, 2)
            n_omega = math.comb(tong_bi, 2)

            # n(A) = C(r1,1)*C(r2,1) + C(r1,1)*C(r3,1) + C(r2,1)*C(r3,1)
            n_a = r1*r2 + r1*r3 + r2*r3

            # Tính xác suất P(A) = n(A)/n(Omega) và chuyển sang %
            p_a = float(n_a) / n_omega
            p_percent = p_a * 100

            # Làm tròn 1 chữ số thập phân theo kiểu Việt Nam (dùng dấu phẩy)
            kq_decimal = Decimal(str(p_percent)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq = str(kq_decimal).replace('.', ',') + '\\%'

            # B4: Điều chỉnh phương án sai (không trùng đáp án đúng)
            s = []
            while len(s) < 3:
                sai_val = float(kq_decimal) + random.choice([-15.3, -10.5, 5.2, 12.4, -8.7, 9.6, 15.5])
                if sai_val < 0 or sai_val > 100: 
                    continue
                sai_str = str(round(sai_val, 1)).replace('.', ',') + '\\%'
                if sai_str != kq and sai_str not in s:
                    s.append('$%s$' % sai_str)

            da_d = '\\True $%s$' % kq
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = ('Lấy ngẫu nhiên hai viên bi từ một thùng gồm $%s$ bi xanh, $%s$ bi đỏ và $%s$ bi vàng. Tính xác suất để lấy được hai viên bi khác màu.'
                             % (latex(r1), latex(r2), latex(r3)))

            # Nội dung lời giải chi tiết (không viết tắt, đúng định dạng yêu cầu)
            loigiai = ('Số kết quả có thể xảy ra là $n\\left(\\Omega\\right) = C_{%s}^{2} = %s$. \\\\ '
                       'Gọi biến cố $A$: "Lấy được hai viên bi khác màu". \\\\ '
                       'Số kết quả thuận lợi cho biến cố $A$ là: \\\\ '
                       '$n\\left(A\\right) = C_{%s}^{1} \\cdot C_{%s}^{1} + C_{%s}^{1} \\cdot C_{%s}^{1} + C_{%s}^{1} \\cdot C_{%s}^{1} = %s$. \\\\ '
                       'Xác suất của biến cố $A$ là: \\\\ '
                       '$P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{%s} \\approx %s = %s$.'
                       % (latex(tong_bi), latex(n_omega), 
                          latex(r1), latex(r2), latex(r1), latex(r3), latex(r2), latex(r3), latex(n_a),
                          latex(n_a), latex(n_omega), str(round(p_a, 3)).replace('.', ','), kq))

            # Xuất câu trắc nghiệm theo đúng cấu trúc content (không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

