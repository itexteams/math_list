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


def bt_dang66_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo ngẫu nhiên các hệ số cho 2 parabol: y = ax^2 + bx + c và y = dx^2 + ex + f
                # Để đảm bảo có nghiệm, ta chọn nghiệm trước rồi suy ngược ra phương trình
                x1 = random.randint(-3, 2)
                x2 = random.randint(3, 6)

                # Giả sử phương trình hoành độ: (a-d)x^2 + (b-e)x + (c-f) = k(x - x1)(x - x2)
                k = random.choice([-2, -1, 1, 2, 3])

                # Parabol 1: y = a1*x^2 + b1*x + c1
                a1 = random.randint(1, 3)
                b1 = random.randint(-2, 4)
                c1 = random.randint(-5, 5)

                # Parabol 2: y = a2*x^2 + b2*x + c2
                # Ta có a1 - a2 = k => a2 = a1 - k
                a2 = a1 - k
                # Ta có b1 - b2 = -k(x1 + x2) => b2 = b1 + k(x1 + x2)
                b2 = b1 + k * (x1 + x2)
                # Ta có c1 - c2 = k*x1*x2 => c2 = c1 - k*x1*x2
                c2 = c1 - k * x1 * x2

                # Tính tọa độ giao điểm thực tế
                y1 = a1 * x1**2 + b1 * x1 + c1
                y2 = a1 * x2**2 + b1 * x2 + c1

                p1 = (x1, y1)
                p2 = (x2, y2)

                # Đáp án đúng
                da_dung = f"$({latex(x1)}; {latex(y1)})$ và $({latex(x2)}; {latex(y2)})$"

                # Tạo các phương án sai (nhiễu tọa độ)
                s = [
                    f"$({latex(x1)}; {latex(-y1)})$ và $({latex(x2)}; {latex(-y2)})$",
                    f"$({latex(-x1)}; {latex(y1)})$ và $({latex(-x2)}; {latex(y2)})$",
                    f"$({latex(y1)}; {latex(x1)})$ và $({latex(y2)}; {latex(x2)})$",
                    f"$({latex(x1+1)}; {latex(y1-1)})$ và $({latex(x2-1)}; {latex(y2+1)})$",
                    f"$({latex(x1)}; {latex(y1)})$",
                    f"$({latex(x2)}; {latex(y2)})$"
                ]

                # Loại bỏ nếu trùng đáp án đúng (đề phòng xui rủi)
                if da_dung in s: s.remove(da_dung)

                wrong_answers = random.sample(s, 3)

                # Nội dung câu hỏi
                noidungcauhoi = (f"Giao điểm của các cặp đồ thị của các hàm số $y = {latex(a1*x**2 + b1*x + c1)}$ "
                                 f"và $y = {latex(a2*x**2 + b2*x + c2)}$ là")

                # Xử lý đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d] + wrong_answers
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo ảnh
                # Phương trình hoành độ: (a1-a2)x^2 + (b1-b2)x + (c1-c2) = 0
                A_hieu = a1 - a2
                B_hieu = b1 - b2
                C_hieu = c1 - c2
                pt_hoanh_do = f"{latex(simplify(A_hieu*x**2 + B_hieu*x + C_hieu))} = 0"

                loigiai = (f"Tọa độ giao điểm của $y = {latex(a1*x**2 + b1*x + c1)}$ và "
                           f"$y = {latex(a2*x**2 + b2*x + c2)}$ là nghiệm của hệ sau:\\\\"
                           f"$\\begin{{cases}} y = {latex(a1*x**2 + b1*x + c1)} \\\\ y = {latex(a2*x**2 + b2*x + c2)} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} y = {latex(a1*x**2 + b1*x + c1)} \\\\ {pt_hoanh_do} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} x = {latex(x1)} \\\\ y = {latex(y1)} \\end{{cases}}$ hoặc "
                           f"$\\begin{{cases}} x = {latex(x2)} \\\\ y = {latex(y2)} \\end{{cases}}$.\\\\"
                           f"Vậy hai giao điểm có tọa độ là $({latex(x1)}; {latex(y1)})$ và $({latex(x2)}; {latex(y2)})$.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

