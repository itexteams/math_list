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


def bt_dang35_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số n để tạo bài toán cụ thể từ bài toán tổng quát
                n_val = randint(5, 15)
                m_val = 2 * n_val

                # Kết quả đúng là C(2n, n)
                kq = "C_{%s}^{%s}" % (latex(m_val), latex(n_val))

                # Các đáp án trắc nghiệm
                du = ["$%s$" % (kq)]
                da = random.choice(du)

                # Các phương án sai
                s = [
                    "$C_{%s}^{%s}$" % (latex(m_val), latex(n_val - 1)),
                    "$C_{%s}^{%s}$" % (latex(m_val), latex(n_val + 1)),
                    "$2^{%s}$" % (latex(m_val)),
                    "$2^{%s + 1}$" % (latex(m_val)),
                    "$C_{%s}^{%s}$" % (latex(m_val - 2), latex(n_val)),
                    "$C_{%s}^{%s}$" % (latex(m_val + 2), latex(n_val)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ("Tính tổng $S = \\left(C_{%s}^0\\right)^2 + \\left(C_{%s}^1\\right)^2 + \\left(C_{%s}^2\\right)^2 + \\dots + \\left(C_{%s}^{%s}\\right)^2$."
                                 % (latex(n_val), latex(n_val), latex(n_val), latex(n_val), latex(n_val)))

                # Các đáp án
                da_d = ("\\True " + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu
                loigiai = ("Xét khai triển: $\\left(1 + x\\right)^m \\cdot \\left(1 + x\\right)^n = \\left(1 + x\\right)^{m + n}$ ta có: \\\\"
                           "$C_m^0 \\cdot C_n^k + C_m^1 \\cdot C_n^{k-1} + C_m^2 \\cdot C_n^{k-2} + \\dots + C_m^m \\cdot C_n^{k-m} = C_{m+n}^k$, với $m \\le k \\le n$ (hệ số chứa $x^k$ ở cả hai vế). \\\\"
                           "Áp dụng với khai triển $\\left(1 + x\\right)^{%s} \\cdot \\left(1 + x\\right)^{%s} = \\left(1 + x\\right)^{%s}$ ta có hệ số chứa $x^{%s}$ bằng nhau nên: \\\\"
                           "$C_{%s}^0 \\cdot C_{%s}^{%s} + C_{%s}^1 \\cdot C_{%s}^{%s} + \\dots + C_{%s}^{%s} \\cdot C_{%s}^0 = C_{%s}^{%s}$ \\\\"
                           "Vì $C_{%s}^k = C_{%s}^{%s-k}$ nên: \\\\"
                           "$\\left(C_{%s}^0\\right)^2 + \\left(C_{%s}^1\\right)^2 + \\dots + \\left(C_{%s}^{%s}\\right)^2 = C_{%s}^{%s}$."
                           % (latex(n_val), latex(n_val), latex(m_val), latex(n_val),
                              latex(n_val), latex(n_val), latex(n_val),
                              latex(n_val), latex(n_val), latex(n_val - 1),
                              latex(n_val), latex(n_val),
                              latex(n_val),
                              latex(m_val), latex(n_val),
                              latex(n_val), latex(n_val), latex(n_val),
                              latex(n_val), latex(n_val), latex(n_val), latex(n_val),
                              latex(m_val), latex(n_val)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

