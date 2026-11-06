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


def bt_dang37_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến ngẫu nhiên cho tọa độ điểm M(xm; ym)
            xm = randint(-10, 10)
            ym = randint(-10, 10)

            # Đảm bảo điểm M không nằm trên gốc tọa độ để bài toán hay hơn
            while xm == 0 and ym == 0:
                xm = randint(-10, 10)
                ym = randint(-10, 10)

            # Phân tích bài toán:
            # Đường phân giác góc phần tư (I) là y = x <=> x - y = 0
            # VTCP của đường phân giác là u = (1; 1)
            # Vì d song song với đường phân giác nên VTCP của d là ud = (1; 1)
            # Phương trình tham số: x = xm + t, y = ym + t

            # Tạo các thành phần chuỗi cho phương trình đúng
            dau_xm = "" if xm < 0 else ""
            phts_dung = "\\begin{cases} x = %s + t \\\\ y = %s + t \\end{cases}" % (latex(xm), latex(ym))

            # Tạo các phương án nhiễu (đảm bảo không trùng với đáp án đúng)
            # Nhiễu 1: Đổi dấu t ở y (giống câu A trong ảnh)
            pa_sai1 = "\\begin{cases} x = %s + t \\\\ y = %s - t \\end{cases}" % (latex(xm), latex(ym))

            # Nhiễu 2: Đổi dấu tọa độ điểm M (giống câu C trong ảnh)
            pa_sai2 = "\\begin{cases} x = %s + t \\\\ y = %s + t \\end{cases}" % (latex(-xm), latex(-ym))

            # Nhiễu 3: Đổi chỗ x, y và đổi dấu t (giống câu D trong ảnh)
            pa_sai3 = "\\begin{cases} x = %s - t \\\\ y = %s + t \\end{cases}" % (latex(ym), latex(xm))

            # Kiểm tra trùng lặp (phòng trường hợp xm, ym đặc biệt)
            danh_sach_phuong_an = [phts_dung, pa_sai1, pa_sai2, pa_sai3]
            # Nếu có phần tử trùng nhau, ta gán thủ công để đảm bảo tính trắc nghiệm
            if len(set(danh_sach_phuong_an)) < 4:
                pa_sai1 = "\\begin{cases} x = %s - t \\\\ y = %s + t \\end{cases}" % (latex(xm), latex(ym))
                pa_sai2 = "\\begin{cases} x = %s + t \\\\ y = %s - 2t \\end{cases}" % (latex(xm), latex(ym))
                pa_sai3 = "\\begin{cases} x = %s + 2t \\\\ y = %s + t \\end{cases}" % (latex(xm), latex(ym))

            # Gán đáp án đúng
            da_d = '\\True $' + phts_dung + '$'
            da_s1 = '$' + pa_sai1 + '$'
            da_s2 = '$' + pa_sai2 + '$'
            da_s3 = '$' + pa_sai3 + '$'

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Phương trình tham số của đường thẳng $d$ đi qua điểm $M(%s;%s)$ và song song với đường phân giác của góc phần tư thứ nhất là"
                % (latex(xm), latex(ym))
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                "Đường phân giác của góc phần tư thứ nhất có phương trình là $y = x$ hay $x - y = 0$. \\\\ "
                "Suy ra một vectơ chỉ phương của đường phân giác này là $\\vec{u} = (1;1)$. \\\\ "
                "Vì đường thẳng $d$ song song với đường phân giác của góc phần tư thứ nhất nên $d$ nhận $\\vec{u}_d = \\vec{u} = (1;1)$ làm vectơ chỉ phương. \\\\ "
                "Mặt khác, $d$ đi qua điểm $M(%s;%s)$. \\\\ "
                "Vậy phương trình tham số của đường thẳng $d$ là: "
                "$\\begin{cases} x = %s + t \\\\ y = %s + t \\end{cases} (t \\in \\mathbb{R})$."
                % (latex(xm), latex(ym), latex(xm), latex(ym))
            )

            # Xuất nội dung theo mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

