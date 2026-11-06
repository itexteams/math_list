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


def bt_dang47_p4_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- 1. Random hóa các tham số ---

                # Khối lượng ban đầu (kg)
                m0_kg = random.choice([1, 2, 4]) # 1 kg, 2 kg, 4 kg

                # Chu kì bán rã (năm, là bội của 1000)
                T = randint(20, 50) * 1000 

                # Ngưỡng không độc hại (g) - 10^-k g
                k = randint(5, 8) # k = 5, 6, 7, 8
                m_min_g = 10**(-k) 


                m_min_ratio = m_min_g / (m0_kg * 1000)


                try:
                    n_float = 1 + math.log10(m_min_ratio) / math.log10(0.5)
                    n_min = math.ceil(n_float)
                except ValueError:
                    # Xử lý trường hợp không tính được log (nếu có)
                    n_min = 31 # Giá trị mặc định an toàn

                # Số năm cần thiết (đáp án chính xác)
                so_nam_kq = n_min * T

                # --- 3. Tạo câu hỏi và đáp án trắc nghiệm ---

                # Các đáp án trắc nghiệm
                da = '${}$'.format(latex(so_nam_kq)) # Đáp án đúng

                # Tạo đáp án sai: (n_min +/- k) * T
                s = []
                for offset in [-3, -2, -1, 1, 2, 3]:
                    n_wrong = n_min + offset
                    if n_wrong > 0:
                        s.append('${}$'.format(latex(n_wrong * T)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Số năm cần thiết cho lời giải
                n_min_loigiai = n_min 

                # Câu hỏi
                noidungcauhoi = ('''Có $%s$ kg chất phóng xạ độc hại. Biết rằng, sau một khoảng thời gian $T = %s$ năm thì một nửa số chất phóng xạ này bị phân rã. Gọi $u_n$ là khối lượng chất phóng xạ còn lại sau chu kì thứ $n$. Hỏi sau ít nhất bao nhiêu năm thì khối lượng chất phóng xạ còn lại không còn độc hại đối với con người, biết rằng chất phóng xạ này sẽ không độc hại nữa nếu khối lượng chất phóng xạ còn lại bé hơn $%s$ g.'''
                                  %(latex(m0_kg),latex(T),latex(m_min_g)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Biểu diễn giới hạn logarit cho lời giải
                log_lhs = Rational(m_min_g, m0_kg * 1000)

                # Nội dung lời giải
                loigiai=('''Khối lượng chất phóng xạ còn lại sau $n$ chu kì là $u_n = %s \\cdot \\left(\\frac{1}{2}\\right)^{n-1}$ (kg). \\\\
                         Đổi đơn vị sang gam: $u_n = %s \\cdot \\left(\\frac{1}{2}\\right)^{n-1} \\cdot 10^3$ (g). \\\\
                         Để chất phóng xạ không độc hại, ta cần $u_n < %s$ g: \\\\
                         $$%s \\cdot \\left(\\frac{1}{2}\\right)^{n-1} \\cdot 10^3 < %s$$
                         $$\\left(\\frac{1}{2}\\right)^{n-1} < \\frac{%s}{%s \\cdot 10^3} = %s$$
                         Lấy logarit cơ số 10 hai vế và giải bất phương trình: \\\\
                         $$n-1 > \\frac{\\log(%s)}{\\log(1/2)} \\approx %s$$
                         $$n > %s$$
                         Vì $n$ là số nguyên (số chu kì), nên cần ít nhất $n=%s$ chu kì. \\\\
                         Số năm cần thiết là $N = n \\cdot T = %s \\cdot %s = %s$ năm.'''

                          %(latex(m0_kg), latex(m0_kg), latex(m_min_g),
                            latex(m0_kg), latex(m_min_g),
                            latex(m_min_g), latex(m0_kg), latex(log_lhs),
                            latex(log_lhs), latex(round(n_min - 1, 2)), # Giá trị logarit gần đúng
                            latex(round(n_min, 2)), # n gần đúng
                            latex(n_min_loigiai),
                            latex(n_min_loigiai), latex(T), latex(so_nam_kq)
                          ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

