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


def bt_dang40_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập thông số random
            lis_price = [800, 1000, 1200, 1500] # Giá trị xe (triệu đồng)
            car_price = random.choice(lis_price)

            prepaid_options = [300, 400, 500, 600] # Số tiền trả trước (triệu đồng)
            prepaid = random.choice(prepaid_options)
            # Đảm bảo tiền trả trước luôn nhỏ hơn giá xe
            while prepaid >= car_price:
                prepaid = random.choice(prepaid_options)

            debt = car_price - prepaid # Số nợ ban đầu (A)
            interest_year = random.choice([8, 10, 12, 14]) # Lãi suất năm (%)
            r_year_pct = interest_year / 100
            r_month = r_year_pct / 12 # Lãi suất tháng

            years = random.choice([2, 3, 5]) # Số năm trả góp
            n = years * 12 # Số tháng

            # Bước 2: Tính toán kết quả theo công thức trong hình
            # a = (A * (1+r)^n * r) / ((1+r)^n - 1)
            temp_pow = (1 + r_month)**n
            a_val = (debt * temp_pow * r_month) / (temp_pow - 1)

            # Làm tròn đến 3 chữ số thập phân như mẫu (23,537)
            kq_decimal = Decimal(str(a_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
            da_dung = f"${kq_str}$ triệu đồng"
            s = []
            while len(s) < 3:
                # Tạo sai số ngẫu nhiên từ 0.5 đến 3.0
                offset = random.uniform(0.5, 3.0)
                if random.choice([True, False]):
                    wrong_val = kq_decimal + Decimal(str(round(offset, 3)))
                else:
                    wrong_val = kq_decimal - Decimal(str(round(offset, 3)))

                wrong_str = f"${str(wrong_val).replace('.', ',')}$ triệu đồng"
                if wrong_str != da_dung and wrong_str not in s:
                    s.append(wrong_str)

            # Trộn đáp án
            list_ans = [f"\\True {da_dung}", s[0], s[1], s[2]]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = (f"Ông A muốn mua một chiếc ô tô trị giá ${car_price}$ triệu đồng nhưng vì chưa đủ tiền nên chọn mua bằng hình thức trả góp hàng tháng (số tiền trả góp mỗi tháng như nhau) với lãi suất ${interest_year}\\%$/năm và trả trước ${prepaid}$ triệu đồng. Hỏi mỗi tháng ông phải trả số tiền gần nhất với số tiền nào dưới đây để sau đúng ${years}$ năm, kể từ ngày mua xe, ông trả hết nợ, biết kỳ trả nợ đầu tiên sau ngày mua ô tô đúng một tháng và chỉ tính lãi hàng tháng trên số dư nợ thực tế của tháng đó?")

            # Nội dung lời giải (Viết y hệt mẫu trong ảnh nhưng dùng biến)
            r_month_pct = interest_year / 12
            loigiai = (f"Gọi $a$ là số tiền trả hàng tháng. Lãi suất mỗi tháng là $r = {interest_year}\\%/12 = {r_month_pct}\\%$. \\\\\n"
                       f"Số nợ còn lại sau khi trả trước là: ${car_price} - {prepaid} = {debt}$ triệu đồng. \\\\\n"
                       f"Sau tháng thứ 1, số tiền còn lại: $P_1 = {debt}(1+r) - a$. \\\\\n"
                       f"Sau tháng thứ 2, số tiền còn lại: $P_2 = P_1(1+r) - a = {debt}(1+r)^2 - a(1+r) - a$. \\\\\n"
                       f"...\n"
                       f"Sau tháng thứ $n$, số tiền còn lại: $P_n = {debt}(1+r)^n - a(1+r)^{{n-1}} - ... - a(1+r) - a$. \\\\\n"
                       f"Vậy sau ${n}$ tháng: ${debt}(1+r)^{{{n}}} - a\\frac{{(1+r)^{{{n}}} - 1}}{{r}} = 0 \\Leftrightarrow a = \\frac{{{debt}(1+r)^{{{n}}} \\cdot r}}{{(1+r)^{{{n}}} - 1}}$. \\\\\n"
                       f"Thay số: $a = \\frac{{{debt}(1+{r_month_pct}\\%)^{{{n}}} \\cdot {r_month_pct}\\%}}{{(1+{r_month_pct}\\%)^{{{n}}} - 1}} \\approx {kq_str}$ triệu đồng.")

            # Xuất kết quả
            content = (f"\\begin{{minipage}}{{\\textwidth}} \n"
                       f"\\begin{{ex}}\n{noidungcauhoi}\n"
                       f"\\loigiai{{{loigiai}}}\n"
                       f"\\end{{ex}}\n \\end{{minipage}} \n\n")
            return content

