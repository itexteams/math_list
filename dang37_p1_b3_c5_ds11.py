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


def bt_dang37_p1_b3_c5_ds11(self):
            # Khai báo biến
            # 3. Thời gian gửi (n): từ 3 đến 24 tháng

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo giá trị ngẫu nhiên
                A0_val = random.choice([50, 100, 150, 200, 300, 500]) # triệu đồng
                r_val = random.choice([0.3, 0.4, 0.5, 0.6, 0.7, 0.8]) # % mỗi tháng
                n_val = random.randint(4, 12) # số tháng

                # Tính toán kết quả đúng
                # Công thức: A = A0 * (1 + r)^n
                A0_full = A0_val * 1000000
                r_decimal = r_val / 100
                kq_float = A0_full * (1 + r_decimal)**n_val

                # Làm tròn đến hàng đơn vị (theo mẫu lời giải trong ảnh)
                kq_final = int(Decimal(str(kq_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Định dạng hiển thị số tiền có dấu chấm phân cách hàng nghìn
                def format_money(n):
                    return "{:,}".format(n).replace(',', '.')

                da_dung = format_money(kq_final)

                # --- B4: Điều chỉnh các phương án sai không trùng đáp án đúng ---
                s = set()
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi ngẫu nhiên một chút kết quả hoặc tính sai công thức
                    offset = random.choice([-200000, -150000, 150000, 200000, 350000, -350000])
                    fake_val = kq_final + offset
                    fake_str = format_money(fake_val)
                    if fake_str != da_dung:
                        s.add(fake_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Một người gửi $%s$ triệu đồng vào ngân hàng với lãi suất $%s\\%%$/ tháng. Biết rằng nếu không rút tiền ra khỏi ngân hàng thì cứ sau mỗi tháng, số tiền lãi sẽ được lập vào vốn ban đầu để tính lãi cho tháng tiếp theo. Hỏi sau $%s$ tháng, người đó được lĩnh số tiền (cả vốn ban đầu và lãi) gần nhất với số tiền nào dưới đây, nếu trong khoảng thời gian này người đó không rút tiền ra và lãi suất không thay đổi.'''
                                 %(latex(A0_val), latex(r_val), latex(n_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung) + ' đồng')
                da_s1 = str(das1) + ' đồng'
                da_s2 = str(das2) + ' đồng'
                da_s3 = str(das3) + ' đồng'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta có $A_n = A_0 (1+r)^n = %s \\left(1 + \\frac{%s}{100}\\right)^{%s} = %s$.'''
                           %(format_money(A0_full), latex(r_val), latex(n_val), format_money(kq_final)))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
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

