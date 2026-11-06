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


def bt_dang18_p1_b2_c2_ds11(self):
            # Khai báo biến
            # RANDOM ĐỐI SỐ
            n = random.randint(5, 30)
            d = random.choice(list(range(-9, -2)) + list(range(2, 9)))
            U1 = random.choice([j for j in range(-9, 9) if j != 0])
            Un = U1 + (n - 1) * d

            # NỘI DUNG BÀI TOÁN
            de_bai_chung = f"Cho cấp số cộng $(u_n)$ có "
            hoi_giai_dapan = [
                (f" số hạng đầu $u_1 = {U1}$ và công sai $d = {d}$. Số hạng thứ ${n}$ bằng ", # Phần riêng của đề bài là phần tử thứ 1
                    f""" Áp dụng công thức tính số hạng tổng quát $u_n = u_1 + (n - 1)d \\Leftrightarrow u_{{{n}}} = {U1} + {n-1}\\cdot {d} = {Un}$.""", # Lời giải là phần tử thứ 2
                    f"${Un}$",   # Đáp án đúng là phần tử thứ 3
                    f"${Un - d}$",   # Đáp án nhiễu thứ 1
                    f"${Un + d}$",   # Đáp án nhiễu thứ 2
                    f"${Un + 2 * d}$",   # Đáp án nhiễu thứ 3, ... có thể nhiều hơn, miễn sao có từ 3 đáp án nhiễu khác nhau trở lên
                    ),

                (f" $u_{{{n}}} = {Un}$ và công sai $d = {d}$. Số hạng đầu bằng ", 
                    f""" Áp dụng công thức tính số hạng tổng quát 
                    \\allowdisplaybreaks
                    \\begin{{eqnarray*}}
                        &u_n &= u_1 + (n - 1)d \\\\
                        \\Leftrightarrow &{Un} &= u_1 + {n-1}\\cdot {d}\\\\
                        \\Leftrightarrow &u_1 &= {U1}
                    \\end{{eqnarray*}} """, 
                    f"${U1}$",   
                    f"${U1 - d}$",   
                    f"${U1 + d}$",   
                    f"${U1 - 2 * d}$",    
                    ),

                (f" số hạng đầu $u_1 = {U1}$ và $u_{{{n}}} = {Un}$. Công sai của cấp số cộng bằng ", 
                    f""" Áp dụng công thức tính số hạng tổng quát 
                    \\allowdisplaybreaks
                    \\begin{{eqnarray*}}
                        &u_n &= u_1 + (n - 1)d \\\\
                        \\Leftrightarrow &{Un} &= {U1} + {n-1}d\\\\
                        \\Leftrightarrow &d &= {d}
                    \\end{{eqnarray*}} """, 
                    f"${d}$",   
                    f"${d + random.choice([-1, 1])}$",   
                    f"${d + random.choice([-2, 2])}$",   
                    f"${d + random.choice([-3, 3])}$",   
                    f"${latex(S(Un - U1) /n)}$"         # Đáp án nhiễu thứ 4
                    ),

                (f" số hạng đầu $u_1 = {U1}$, công sai $d = {d}$. Hỏi số ${Un}$ là số hạng thứ mấy? ", 
                    f""" Áp dụng công thức tính số hạng tổng quát 
                    \\allowdisplaybreaks
                    \\begin{{eqnarray*}}
                        &u_n &= u_1 + (n - 1)d \\\\
                        \\Leftrightarrow &{Un} &= {U1} + (n - 1) \\cdot {d} \\\\
                        \\Leftrightarrow &n &= {n}
                    \\end{{eqnarray*}} """, 
                    f"${n}$",   
                    f"${n + random.choice([-1, 1])}$",   
                    f"${n + random.choice([-2, 2])}$",   
                    f"${n + random.choice([-3, 3])}$",   
                    ),
            ]

            # PHẦN XỬ LÝ XUẤT LATEX NÊN KHÔNG THAY ĐỔI TỪ ĐÂY TRỞ XUỐNG
            de_TN = random.choice(hoi_giai_dapan)
            da_dung = f"\\True {de_TN[2]}" 
            da_nhieu = de_TN[3:]
            da_nhieu = [nhieu for nhieu in da_nhieu if nhieu != da_dung]
            if len(set(da_nhieu)) < 3:
                print("Không đủ 3 đáp án nhiễu khác nhau. Cần viết thêm.")

            nhieu1, nhieu2, nhieu3 = random.sample(da_nhieu, 3)
            dap_an = [da_dung, nhieu1, nhieu2, nhieu3]
            random.shuffle(dap_an)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n' 
                '\\begin{ex}\n'+ de_bai_chung + de_TN[0] + '\n'
                '\\choice \n'
                '{'+ dap_an[0] +'}\n'
                '{'+ dap_an[1] +'}\n'
                '{'+ dap_an[2] +'}\n'
                '{'+ dap_an[3] +'}\n'
                '\\loigiai{'+ de_TN[1] +'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

