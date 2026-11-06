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


def bt_dang20_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1, B3: Nghiên cứu và Random thông số bài toán
                # Tổng số thẻ từ 40 đến 60
                n_tong = randint(40, 60)
                # Số thẻ xanh (chiếm khoảng 60%)
                n_xanh = randint(25, n_tong - 15)
                # Số thẻ trắng
                n_trang = n_tong - n_xanh

                # Tính toán xác suất theo Sympy Rational để giữ độ chính xác
                p_a = Rational(n_xanh, n_tong)
                p_b_a = Rational(n_trang, n_tong - 1)
                p_ab = p_a * p_b_a

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_float = float(p_ab)
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da_dung = '$%s$' % (kq_str)

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    # Tạo sai số ngẫu nhiên từ -0,10 đến 0,10
                    sai_so = random.uniform(-0.1, 0.1)
                    if sai_so == 0: continue

                    val_sai = Decimal(str(kq_float + sai_so)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    val_sai_str = '$%s$' % (str(val_sai).replace('.', ','))

                    if val_sai_str != da_dung and val_sai_str not in s_list:
                        s_list.append(val_sai_str)

                das1, das2, das3 = s_list

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = ('''Một thùng thăm đựng $%s$ thẻ giảm giá cho nhân viên có kích thước, chất liệu như nhau, trong đó có $%s$ thẻ xanh và $%s$ thẻ trắng. Lấy ngẫu nhiên ra một thẻ, rồi lại lấy ngẫu nhiên ra một thẻ nữa. Xác suất để lấy được một thẻ xanh ở lần thứ nhất và một thẻ trắng ở lần thứ hai bằng bao nhiêu? (kết quả được làm tròn đến hàng phần trăm).'''
                                 % (latex(n_tong), latex(n_xanh), latex(n_trang)))

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Lời giải chi tiết không viết tắt
                loigiai = ('''Gọi $A$ là biến cố "lấy được một thẻ xanh ở lần thứ nhất". \\\\
                             Gọi $B$ là biến cố "lấy được một thẻ trắng ở lần thứ hai". \\\\
                             Vậy $AB$ là biến cố "lấy được một thẻ xanh ở lần thứ nhất và một thẻ trắng ở lần thứ hai". \\\\
                             Ta có xác suất của biến cố $A$ là: $P(A) = \\frac{%s}{%s} = %s$. \\\\
                             Sau khi lấy một thẻ xanh ở lần thứ nhất, số thẻ còn lại trong thùng là $%s$ thẻ. \\\\
                             Khi đó, xác suất để lấy được thẻ trắng ở lần thứ hai với điều kiện lần thứ nhất đã lấy được thẻ xanh là: $P(B|A) = \\frac{%s}{%s}$. \\\\
                             Ta có công thức nhân xác suất: \\\\
                             $P(AB) = P(A) \\cdot P(B|A) = %s \\cdot \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$.'''
                           % (latex(n_xanh), latex(n_tong), latex(p_a),
                              latex(n_tong - 1),
                              latex(n_trang), latex(n_tong - 1),
                              latex(p_a), latex(n_trang), latex(n_tong - 1),
                              latex(p_ab.p), latex(p_ab.q), kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

