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


def bt_dang53_p4_b1_c4_ds10(self):
            #Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random hệ số a khác 0 và hệ số b
            a = random.choice([i for i in range(-10, 11) if i != 0])
            b = random.randint(-15, 15)

            # Thiết lập hàm số
            f_x = a*x + b
            f_x_latex = latex(f_x)

            # Xác định tính đúng sai để tạo đáp án
            if a > 0:
                ket_luan = "đồng biến"
                loai_nguoc = "nghịch biến"
            else:
                ket_luan = "nghịch biến"
                loai_nguoc = "đồng biến"

            # B4: Điều chỉnh các phương án sai
            da_dung = f"Hàm số {ket_luan} trên $\\mathbb{{R}}$"
            da_sai1 = f"Hàm số {loai_nguoc} trên $\\mathbb{{R}}$"
            da_sai2 = f"Hàm số {ket_luan} trên $(0; +\\infty)$ và {loai_nguoc} trên $(-\\infty; 0)$"
            da_sai3 = f"Hàm số không đổi trên $\\mathbb{{R}}$"

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho hàm số $y = {f_x_latex}$ xác định trên $\\mathbb{{R}}$. "
                             f"Xét tính đồng biến, nghịch biến của hàm số.")

            # Các đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_1)

            # B1 & B2: Viết lại lời giải y hệt mẫu trong ảnh
            # f(x1) - f(x2) = (ax1 + b) - (ax2 + b) = a(x1 - x2)
            loigiai = (f"Với mọi $x_1, x_2 \\in \\mathbb{{R}}$ và $x_1 < x_2$. \\\\\n"
                       f"Ta có $f(x_1) - f(x_2) = ({latex(a)}x_1 + {latex(b)}) - ({latex(a)}x_2 + {latex(b)}) = {latex(a)}(x_1 - x_2)$. \\\\\n"
                       f"Suy ra $\\frac{{f(x_1) - f(x_2)}}{{x_1 - x_2}} = \\frac{{{latex(a)}(x_1 - x_2)}}{{x_1 - x_2}} = {latex(a)} "
                       f"{' < 0' if a < 0 else ' > 0'}$. \\\\\n"
                       f"Vậy hàm số {ket_luan} trên $\\mathbb{{R}}$.")

            # Xuất câu trắc nghiệm theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


