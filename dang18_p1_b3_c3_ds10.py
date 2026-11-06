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


def bt_dang18_p1_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Random giá trị dịch chuyển để tạo bộ số liệu mới
                shift = random.randint(-15, 30)

                # Hai bộ base có cùng tổng nhưng độ phân tán khác nhau
                base_1 = [41, 44, 45, 47, 51, 53, 54] # Phân tán hơn (Kém ổn định)
                base_2 = [43, 44, 47, 48, 50, 51, 52] # Tập trung hơn (Ổn định hơn)

                data_1 = [x + shift for x in base_1]
                data_2 = [x + shift for x in base_2]

                # Hoán vị ngẫu nhiên vùng nào kém ổn định hơn
                is_A_spread = random.choice([True, False])

                if is_A_spread:
                    data_A = data_1
                    data_B = data_2
                    region_spread = "A"
                    region_compact = "B"
                else:
                    data_A = data_2
                    data_B = data_1
                    region_spread = "B"
                    region_compact = "A"

                str_A = " ".join(map(str, data_A))
                str_B = " ".join(map(str, data_B))

                # B2: Tính toán các đại lượng chứng minh
                sum_A = sum(data_A)
                sum_B = sum(data_B) # Luôn bằng sum_A do thuật toán base

                iqr_A = data_A[5] - data_A[1] # Q3 - Q1
                iqr_B = data_B[5] - data_B[1] # Q3 - Q1

                range_A = data_A[6] - data_A[0] # Max - Min
                range_B = data_B[6] - data_B[0] # Max - Min

                # Câu hỏi
                noidungcauhoi = (f'''Điều tra năng suất lúa của 7 hec ta trồng lúa của hai vùng A và B ta thu được mẫu số liệu sau:
            \\\\Vùng A: {str_A}
            \\\\Vùng B: {str_B}
            \\\\Khẳng định nào dưới đây là \\textbf{{sai}}?''')

                # Các đáp án trắc nghiệm
                # Đáp án đúng cho câu hỏi là mệnh đề SAI: "Vùng phân tán (kém ổn định) lại ổn định hơn vùng tập trung"
                da_d = ('\\True ' + f'Vùng {region_spread} trồng lúa ổn định hơn vùng {region_compact}')

                # 3 mệnh đề đúng làm đáp án nhiễu
                da_s1 = str('Năng suất trung bình của hai vùng A và B là như nhau')
                da_s2 = str(f'Khoảng tứ phân vị của vùng {region_spread} lớn hơn khoảng tứ phân vị của vùng {region_compact}')
                da_s3 = str(f'Khoảng biến thiên ở vùng {region_spread} lớn hơn khoảng biến thiên của vùng {region_compact}')

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (f'''Phân tích các khẳng định ta có:\\\\
            Năng suất trung bình của vùng A và B đều là $\\frac{{{sum_A}}}{{7}}$ nên khẳng định năng suất trung bình hai vùng như nhau là đúng.\\\\
            Khoảng tứ phân vị của vùng A là ${data_A[5]} - {data_A[1]} = {iqr_A}$ và khoảng tứ phân vị của vùng B là ${data_B[5]} - {data_B[1]} = {iqr_B}$.\\\\
            Khoảng biến thiên ở vùng A là ${data_A[6]} - {data_A[0]} = {range_A}$ và khoảng biến thiên của vùng B là ${data_B[6]} - {data_B[0]} = {range_B}$.\\\\
            Vì khoảng biến thiên và khoảng tứ phân vị của vùng {region_spread} lớn hơn vùng {region_compact} nên vùng {region_compact} trồng lúa ổn định hơn vùng {region_spread}.\\\\
            Do đó, khẳng định "Vùng {region_spread} trồng lúa ổn định hơn vùng {region_compact}" là SAI.''')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

