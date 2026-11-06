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


def bt_dang36_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng phần tử của mẫu từ 7 đến 20
                n = random.randint(7, 20)

                # Tạo ngẫu nhiên n số nguyên cho mẫu số liệu
                list_num = [random.randint(2, 25) for _ in range(n)]

                # Chuỗi mẫu số liệu ban đầu để in vào đề
                original_str = "; ".join(map(str, list_num))

                # Sắp xếp số liệu
                sorted_num = sorted(list_num)
                sorted_str = "; ".join(map(str, sorted_num))

                # --- TÌM Q2 VÀ LẤY NỬA SAU CỦA MẪU ---
                if n % 2 != 0:
                    # Nếu n lẻ
                    mid_idx = n // 2
                    q2 = sorted_num[mid_idx]
                    q2_str = str(q2)
                    upper_half = sorted_num[mid_idx + 1:]
                    loigiai_q2 = f"Dãy số liệu gồm {n} giá trị (số lẻ), giá trị chính giữa là {q2_str} nên $Q_2 = {q2_str}$."
                else:
                    # Nếu n chẵn
                    mid1 = n // 2 - 1
                    mid2 = n // 2
                    q2 = (sorted_num[mid1] + sorted_num[mid2]) / 2
                    q2_str = str(int(q2)) if q2.is_integer() else str(q2).replace('.', ',')
                    upper_half = sorted_num[mid2:]
                    loigiai_q2 = f"Dãy số liệu gồm {n} giá trị (số chẵn), $Q_2$ là trung bình cộng của hai giá trị chính giữa: $Q_2 = \\frac{{{sorted_num[mid1]} + {sorted_num[mid2]}}}{{2}} = {q2_str}$."

                # --- TÌM Q3 (Trung vị của nửa sau) ---
                m = len(upper_half)
                upper_str = "; ".join(map(str, upper_half))

                if m % 2 != 0:
                    # Nửa sau có số phần tử lẻ
                    m_mid = m // 2
                    q3 = upper_half[m_mid]
                    q3_str = str(int(q3)) if float(q3).is_integer() else str(q3).replace('.', ',')
                    loigiai_q3 = f"Nửa sau của mẫu gồm {m} số liệu: ${upper_str}$. Giá trị chính giữa là ${q3_str}$. Do đó, $Q_3 = {q3_str}$."
                else:
                    # Nửa sau có số phần tử chẵn
                    m_mid1 = m // 2 - 1
                    m_mid2 = m // 2
                    q3 = (upper_half[m_mid1] + upper_half[m_mid2]) / 2
                    q3_str = str(int(q3)) if q3.is_integer() else str(q3).replace('.', ',')
                    loigiai_q3 = f"Nửa sau của mẫu gồm {m} số liệu: ${upper_str}$. $Q_3$ là trung bình cộng của hai giá trị chính giữa: $Q_3 = \\frac{{{upper_half[m_mid1]} + {upper_half[m_mid2]}}}{{2}} = {q3_str}$."

                # --- TẠO ĐÁP ÁN ---
                da = q3_str

                # Tạo đáp án nhiễu
                options = set()
                # Thêm Q2 vào làm nhiễu
                options.add(q2_str)
                # Thêm giá trị lớn nhất, nhỏ nhất
                options.add(str(sorted_num[0]))
                options.add(str(sorted_num[-1]))
                options.discard(da) # Loại bỏ nếu trùng đáp án đúng

                options_list = list(options)

                # Bổ sung nhiễu ngẫu nhiên nếu chưa đủ 3 phương án sai
                while len(options_list) < 3:
                    fake_val = q3 + random.choice([-2, -1, -0.5, 0.5, 1, 2, 3])
                    if fake_val > 0:
                        fake_str = str(int(fake_val)) if float(fake_val).is_integer() else str(fake_val).replace('.', ',')
                        if fake_str != da and fake_str not in options_list:
                            options_list.append(fake_str)

                random.shuffle(options_list)
                das1 = options_list[0]
                das2 = options_list[1]
                das3 = options_list[2]

                # Câu hỏi
                noidungcauhoi = "Tìm tứ phân vị thứ ba của mẫu số liệu $$%s.$$" % original_str

                # Các đáp án
                da_d = '\\True $%s$' % da
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2 
                da_s3 = '$%s$' % das3 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f"Sắp xếp số liệu theo thứ tự không giảm: ${sorted_str}$.\\\\\n"
                           f"{loigiai_q2}\\\\\n"
                           f"Tứ phân vị thứ ba là trung vị của nửa sau mẫu số liệu.\\\\\n"
                           f"{loigiai_q3}")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

