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


def bt_dang7_p3_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và thực hiện ngẫu nhiên bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Biên độ và hằng số tịnh tiến giữ nguyên cấu trúc
                a = 3
                b = 13

                # Biến đổi số ngày tịnh tiến c (Gốc là 60)
                c = random.choice([40, 50, 55, 60, 65, 70, 75, 80])

                # Tính toán giá trị ngày x để hàm sin đạt giá trị bằng 1
                # \pi/180 * (x + c) = \pi/2 + k*2\pi => (x + c)/180 = 1/2 + 2k => x + c = 90 + 360k => x = 90 - c + 360k
                x_val = 90 - c

                # Hàm chuyển đổi số ngày trong năm thành định dạng ngày/tháng (Năm không nhuận 2018)
                def single_date_calc(day_num):
                    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    current_day = day_num
                    for i in range(12):
                        if current_day <= months[i]:
                            return '%02d/%02d' % (current_day, i + 1)
                        current_day -= months[i]
                    return '30/12'

                # Kết quả đúng của bài toán
                da_date = single_date_calc(x_val)

                # Tạo danh sách các phương án nhiễu (không trùng phương án đúng)
                s_dates = []
                fake_days = [x_val - 1, x_val + 1, x_val + 2, x_val - 2, 30, 31, 60, 90]
                for fd in fake_days:
                    if fd > 0 and fd != x_val:
                        d_str = single_date_calc(fd)
                        if d_str not in s_dates and d_str != da_date:
                            s_dates.append(d_str)

                random.shuffle(s_dates)
                das1 = s_dates[0]
                das2 = s_dates[1]
                das3 = s_dates[2]

                # Tính toán các giá trị số thập phân phục vụ phần lời giải chi tiết
                k1 = Decimal(float(1 - x_val)) / Decimal('360')
                k1_str = str(k1.quantize(Decimal('0.02'), rounding=ROUND_HALF_UP)).replace('.', ',')

                k2 = Decimal(float(365 - x_val)) / Decimal('360')
                k2_str = str(k2.quantize(Decimal('0.02'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Định dạng các tham số bằng LaTeX %s theo yêu cầu mẫu
                noidungcauhoi = ('''Số giờ có ánh sáng mặt trời của Thủ đô Hà Nội năm 2018 được cho bởi công thức $y = %s \\sin \\left( \\frac{\\pi}{180} (x + %s) \\right) + %s$ với $1 \\le x \\le 365$ là số ngày trong năm. Ngày nào sau đây của năm 2018 thì số giờ có ánh sáng mặt trời của Hà Nội lớn nhất?'''
                                 % (latex(a), latex(c), latex(b)))

                loigiai = ('''Để số giờ có ánh sáng mặt trời lớn nhất thì hàm số $y = %s \\sin \\left( \\frac{\\pi}{180} (x + %s) \\right) + %s$ đạt giá trị lớn nhất. Khi đó $\\sin \\left( \\frac{\\pi}{180} (x + %s) \\right) = 1 \\Leftrightarrow \\frac{\\pi}{180} (x + %s) = \\frac{\\pi}{2} + k2\\pi \\Leftrightarrow x = %s + k360, k \\in \\mathbb{Z}$.\\\\
            Vì $1 \\le x \\le 365$ nên ta có $1 \\le %s + k360 \\le 365 \\Leftrightarrow %s \\le k \\le %s \\Rightarrow k = 0$.\\\\
            Do đó $x = %s$.\\\\
            Ngày thứ %s của năm.'''
                           % (latex(a), latex(c), latex(b), latex(c), latex(c), latex(x_val), latex(x_val), k1_str, k2_str, latex(x_val), latex(x_val)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_val))
            # Gán phương án trả lời đúng và các phương án sai (không có dấu chấm ở cuối)
            da_d = ('\\True ' + str(da_date))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên thứ tự
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm định dạng mẫu minipage hoàn chỉnh
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

