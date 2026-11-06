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


def bt_dang7_p1_b2_c4_ds11(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')
            # =============================================================================


            # RANDOM ĐỐI SỐ
            # Khởi tạo ngẫu nhiên
            a, b, c = random.randint(-20,40), random.randint(-10,20), random.randint(-9,9)
            while a*b == 0:
                a, b, c = random.randint(-20,40), random.randint(-10,20), random.randint(-9,9)

            de_bai=f"Cho $\\lim\\limits_{{x\\to {c}}}f(x)={a}$ và $\\lim\\limits_{{x\\to {c}}}g(x)={b}$. "
            ds_abcd=[
                (f"Giá trị của $\\lim\\limits_{{x\\to {c}}}\\left[f(x)\\cdot g(x)\\right]$ bằng "
                    ,f"Dựa vào lý thuyết"
                    ,f"${latex(a*b)}$", f"${latex(a+b)}$",f"${latex(a-b)}$",f"${latex(S(a)/b)}$"
                    )
                ,(f"Giá trị của $\\lim\\limits_{{x\\to {c}}}\\left[f(x)+ g(x)\\right]$ bằng "
                    ,f"Dựa vào lý thuyết"
                    ,f"${latex(a+b)}$",f"${latex(a*b)}$", f"${latex(a-b)}$",f"${latex(S(a)/b)}$",
                    )
                ,(f"Giá trị của $\\lim\\limits_{{x\\to {c}}}\\left[f(x)- g(x)\\right]$ bằng "
                    ,f"Dựa vào lý thuyết"
                    ,f"${latex(a-b)}$",f"${latex(a*b)}$", f"${latex(a+b)}$",f"${latex(S(a)/b)}$",
                    )
                ,(f"Giá trị của $\\lim\\limits_{{x\\to {c}}}\\dfrac{{f(x)}}{{g(x)}}$ bằng "
                    ,f"Dựa vào lý thuyết"
                    ,f"${latex(S(a)/b)}$", f"${latex(a+b)}$",f"${latex(a*b)}$", f"${latex(a-b)}$"
                    )
            ]

            # PHẦN XỬ LÝ XUẤT LATEX NÊN KHÔNG THAY ĐỔI TỪ ĐÂY TRỞ XUỐNG
            de_TN = random.choice(ds_abcd)
            da_dung = f"\\True {de_TN[2]}" 
            da_nhieu = de_TN[3:]
            da_nhieu = [nhieu for nhieu in da_nhieu if nhieu != da_dung]

            while len(set(da_nhieu)) < 3:
                da_nhieu.append(random.choice(["$10$", "$20$", "$30$", "$40$", "$50$", "$60$"]))

            # print("Không đủ 3 đáp án nhiễu khác nhau. Cần viết thêm.")
            nhieu1, nhieu2, nhieu3 = random.sample(da_nhieu, 3)
            dap_an = [da_dung, nhieu1, nhieu2, nhieu3]
            random.shuffle(dap_an)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n' 
                '\\begin{ex}\n'+ de_bai + de_TN[0] + '\n'
                '\\choice \n'
                '{'+ dap_an[0] +'}\n'
                '{'+ dap_an[1] +'}\n'
                '{'+ dap_an[2] +'}\n'
                '{'+ dap_an[3] +'}\n'
                '\\loigiai{\n'+ de_TN[1] +'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

