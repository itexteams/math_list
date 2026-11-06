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


def bt_dang58_p1_b3_c5_ds11(self):
            # Khai báo biến
            # b: hằng số trong trị tuyệt đối
            a = random.randint(2, 9)
            b = random.randint(-5, 5)

            # Xây dựng hàm số và đáp án dựa trên b
            # Hàm: y = log_a |x + b|
            # Điều kiện: x + b != 0 => x != -b
            # Tập xác định: D = R \ {-b}

            if b == 0:
                func_latex = "\\log_{%s} |x|" % a
                ket_qua = "\\mathbb{R} \\setminus \\{0\\}"
                b_val = 0
            elif b > 0:
                func_latex = "\\log_{%s} |x + %s|" % (a, b)
                ket_qua = "\\mathbb{R} \\setminus \\{-%s\\}" % b
                b_val = -b
            else: # b < 0, ví dụ x - 2
                func_latex = "\\log_{%s} |x - %s|" % (a, abs(b))
                ket_qua = "\\mathbb{R} \\setminus \\{%s\\}" % abs(b)
                b_val = abs(b)

            # Các đáp án sai
            s_wrong = [
                "\\mathbb{R}",
                "(0; +\\infty)",
                "(-\\infty; 0)",
                "\\mathbb{R} \\setminus \\{%s\\}" % (b_val + 1),
                "\\mathbb{R} \\setminus \\{%s\\}" % (b_val - 1),
                "(%s; +\\infty)" % b_val
            ]

            # Đảm bảo không trùng đáp án đúng (loại bỏ nếu có trong list sai)
            wrong_answers = random.sample([item for item in s_wrong if item != ket_qua], 3)

            # Câu hỏi
            noidungcauhoi = ("Tập xác định của hàm số $y = %s$ là" % func_latex)

            # Đáp án
            da_d = '\\True $' + str(ket_qua)+'$'
            da_s1 = '$'+str(wrong_answers[0])+'$'
            da_s2 = '$'+str(wrong_answers[1])+'$'
            da_s3 = '$'+str(wrong_answers[2])+'$'

            # Danh sách đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = (("Điều kiện xác định của hàm số là $|x %s %s| > 0$ \\\\" if b != 0 else "Điều kiện xác định của hàm số là $|x| > 0$ \\\\") +
                       ("$\\Leftrightarrow  x %s %s \\neq 0 \\\\" if b != 0 else "\\Leftrightarrow  x \\neq 0 \\\\") +
                       ("\\Leftrightarrow  x \\neq %s$. \\\\" if b != 0 else "") +
                       "Vậy tập xác định của hàm số là $D = %s$." )

            if b == 0:
                loigiai = loigiai % (ket_qua)
            elif b > 0:
                loigiai = loigiai % ("+", b, "+", b, -b, ket_qua)
            else:
                loigiai = loigiai % ("-", abs(b), "-", abs(b), -b, ket_qua)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

