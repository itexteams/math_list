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


def bt_dang70_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo danh sách dạng (ở đây chỉ có 1 dạng)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Bước 3: Suy nghĩ tìm cách random bài toán ---
                # f(x) = (m*sqrt(x - a) - n) / (x - k) khi x >= a
                # f(x) = x^2 + b khi x < a

                a = random.randint(2, 5)        # Điểm biên (trong hình là 2)
                m = random.randint(1, 4)        # Hệ số trước căn (trong hình là 2)
                n = random.randint(1, 5)        # Số trừ ở tử (trong hình là 3)
                k = a - 1                       # Mẫu số x - k (trong hình là x - 1)
                b = random.randint(1, 5)        # Số cộng ở nhánh dưới (trong hình là 2)

                # Tính f(a) - Nhánh trên
                # f(a) = (m*sqrt(a-a) - n) / (a-k) = -n / (a-k)
                f_a = Rational(-n, a - k)

                # Tính f(-a) - Nhánh dưới (vì -a luôn < a)
                # f(-a) = (-a)^2 + b
                f_neg_a = a**2 + b

                # Kết quả P = f(a) + f(-a)
                kq_val = f_a + f_neg_a
                kq = latex(kq_val)

                # --- Bước 4: Điều chỉnh các phương án sai ---
                # Tạo các đáp án nhiễu không trùng với đáp án đúng
                s_vals = {kq_val + 1, kq_val - 1, kq_val + 2, kq_val - 2, 0, kq_val + 5}
                if kq_val in s_vals:
                    s_vals.remove(kq_val)

                s = [f'${latex(v)}$' for v in list(s_vals)]
                random.shuffle(s)

                da_d = '\\True $' + kq + '$'
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Bước 2: Viết nội dung đề bài ---
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{%s\sqrt{x-%s}-%s}{x-%s} & \text{khi } x \ge %s \\ x^2+%s & \text{khi } x < %s \end{cases}$. Tính giá trị $P = f(%s) + f(-%s)$.'''
                                 %(latex(m), latex(a), latex(n), latex(k), latex(a), latex(b), latex(a), latex(a), latex(a)))

                # --- Bước 2: Viết nội dung lời giải giống ảnh mẫu ---
                # f(a) biểu diễn chi tiết tử và mẫu
                tu_fa = r'%s\sqrt{%s-%s}-%s' % (latex(m), latex(a), latex(a), latex(n))
                mau_fa = r'%s-%s' % (latex(a), latex(k))

                loigiai = (r'''Ta có: $f(%s) + f(-%s) = \dfrac{%s}{%s} + \left[(-%s)^2 + %s \right] \Rightarrow P = %s$.'''
                           %(latex(a), latex(a), tu_fa, mau_fa, latex(a), latex(b), kq))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

