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


def bt_dang16_p4_b2_c1_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Các tham số của bài toán, có thể thay đổi để tạo bài mới
                a1 = 3
                b1 = 6
                c1 = 4
                a2 = -2
                b2 = 1

                # Điều kiện để P, Q là tập hợp khác rỗng
                # 3m - 6 < 4  => 3m < 10 => m < 10/3
                # m + 1 > -2 => m > -3
                dk_rong_1 = f'{a1}m - {b1} < {c1}'
                dk_rong_2 = f'm + {b2} > {a2}'

                # Điều kiện P con Q
                # 3m - 6 > -2  => 3m > 4 => m > 4/3
                # 4 <= m + 1 => m >= 3
                dk_con_1 = f'{a1}m - {b1} > {a2}'
                dk_con_2 = f'{c1} <= m + {b2}'

                # Giải các điều kiện
                m1_rong_so = sp.sympify(f'({c1} + {b1}) / {a1}')
                m2_rong_so = sp.sympify(f'{a2} - {b2}')
                m1_con_so = sp.sympify(f'({a2} + {b1}) / {a1}')
                m2_con_so = sp.sympify(f'{c1} - {b2}')

                # Lấy giá trị lớn nhất trong các điều kiện
                kq_cuoi_so = max(m1_con_so, m2_con_so)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hai tập hợp $P = [%s m - %s; %s)$ và $Q = (%s; m + %s)$ khác rỗng, $m \\in \\mathbb{R}$. Tìm $m$ để $P \\setminus Q = \\emptyset$.'''
                                 %(latex(a1), latex(b1), latex(c1), latex(a2), latex(b2)))

                # Lời giải
                loigiai = ('''Vì $P, Q$ là hai tập hợp khác rỗng, nên ta có điều kiện: \\\\
                $\\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow  \\begin{cases} m < %s \\\\ m > %s \\end{cases} \\Leftrightarrow  %s < m < %s$. \\\\
                Để $P \\setminus Q = \\emptyset \\Leftrightarrow  P \\subset Q$ $\\Leftrightarrow  \\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow  \\begin{cases} m > %s \\\\ m \\ge %s \\end{cases} \\Leftrightarrow  m \\ge %s$. \\\\
                Kết hợp với điều kiện ta có $%s \\le m < %s$.'''
                           %(dk_rong_1, dk_rong_2, latex(m1_rong_so), latex(m2_rong_so), latex(m2_rong_so), latex(m1_rong_so),
                             dk_con_1, dk_con_2, latex(m1_con_so), latex(m2_con_so), latex(kq_cuoi_so),
                             latex(kq_cuoi_so), latex(m1_rong_so)))


                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) +
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n').replace('<=','\\le')
            return content 

