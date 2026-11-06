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


def bt_dang18_p3_b2_c5_ds10(self):
            while True:
                # Giới hạn n1, n2 và k nhỏ lại để kq < 999
                # k nên từ 3 đến 5
                k = randint(3, 5)
                # n1, n2 nên từ k đến k + 5
                n1 = randint(k, k + 5)
                n2 = randint(k, k + 5)

                n = n1 + n2

                # Tính toán
                c = math.comb(n, k)
                c1 = math.comb(n1, k)
                c2 = math.comb(n2, k)
                kq_val = c - c1 - c2

                # Kiểm tra điều kiện kq < 999
                if kq_val < 999:
                    kq = kq_val
                    break

            # Câu hỏi
            noidungcauhoi = '''Một hộp đựng $%s$ viên bi trong đó có $%s$ bi đỏ và $%s$ bi xanh. Số cách lấy ra $%s$ viên bi có đủ hai màu bằng bao nhiêu?''' % (latex(n), latex(n1), latex(n2), latex(k))

            # Các đáp án
            da_d = '\\True $%s$' % (latex(kq))

            # Tạo đáp án nhiễu (tránh trùng và không âm)
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([10, -10, 5, -5, 2, -2])
                nhieu = kq + offset
                if nhieu > 0 and nhieu != kq:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_1 = [da_d] + list(s_set)
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ( 'Lấy ra $%s$ viên bi bất kỳ trong tổng số $%s$ viên có $\\mathrm{C}_{%s}^{%s}$ cách.\\\\ \n'
                       'Số cách lấy ra $%s$ viên bi chỉ toàn màu đỏ là $\\mathrm{C}_{%s}^{%s}$ cách.\\\\ \n'
                       'Số cách lấy ra $%s$ viên bi chỉ toàn màu xanh là $\\mathrm{C}_{%s}^{%s}$ cách.\\\\ \n'
                       'Vậy số cách lấy ra $%s$ bi có đủ hai màu là $\\mathrm{C}_{%s}^{%s} - \\mathrm{C}_{%s}^{%s} - \\mathrm{C}_{%s}^{%s} = %s$ (cách).'
                       % (latex(k), latex(n), latex(n), latex(k),
                          latex(k), latex(n1), latex(k),
                          latex(k), latex(n2), latex(k),
                          latex(k), latex(n), latex(k),
                          latex(n1), latex(k), latex(n2), latex(k), latex(kq))
                     )

            # Đáp án ngắn
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')

            return content

