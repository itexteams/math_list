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


def bt_dang39_p1_b1_c1_ds12(self):
    # Khai báo các loại câu hỏi ngẫu nhiên
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random điểm cực trị x0 trong khoảng [-5, 5]
        x0 = randint(-5, 5)

        # Đáp án đúng duy nhất: chính xác là khoảng (x0; +\infty)
        da = f'({x0};+\\infty)'

        # Các phương án SAI (chứa miền nghịch biến nên hàm số không thể đồng biến trên đó)
        s = [
            f'(-\\infty;{x0})',              # Khoảng nghịch biến hoàn toàn
            f'(-\\infty;{x0 - 2})',          # Khoảng con nằm hoàn toàn bên miền nghịch biến
            f'({x0 - 3};{x0 - 1})',          # Khoảng hữu hạn nằm bên nghịch biến
            f'({x0 - 2};{x0 + 2})',          # Khoảng chứa cả nghịch biến và đồng biến
            '(-\\infty;+\\infty)'            # Toàn miền R (vừa tăng vừa giảm)
        ]

        # Lọc trùng và chọn ngẫu nhiên 3 phương án sai
        s = list(set([item for item in s if item != da]))
        das = random.sample(s, 3)

        # Tạo mã nguồn TikZ cho bảng xét dấu
        tikz_bang_xet_dau = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, line width=1pt]\n'
            '\\tkzTabInit[lgt=1.5,espcl=2.5]\n'
            '{$x$ /1, $f\'(x)$ /1}\n'
            f'{{$-\\infty$, ${x0}$, $+\\infty$}}\n'
            '\\tkzTabLine{ , -, 0, +, }\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        # Câu hỏi
        noidungcauhoi = (
            'Cho hàm số $y = f(x)$ có bảng xét dấu của đạo hàm $f\'(x)$ trên $\\mathbb{R}$ như hình vẽ\n'
            f'{tikz_bang_xet_dau}\n'
            'Hàm số $y = f(x)$ đồng biến trên khoảng'
        )

        # Các đáp án
        da_d = f'\\True ${da}$'
        da_s1 = f'${das[0]}$'
        da_s2 = f'${das[1]}$'
        da_s3 = f'${das[2]}$'

        # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = (
            f'Dựa vào bảng xét dấu của đạo hàm $f\'(x)$, ta thấy $f\'(x) > 0$ với mọi $x \\in {da}$.\\\\\n'
            f'Do đó, hàm số $y = f(x)$ đồng biến trên khoảng ${da}$.'
        )

        # Xuất câu trắc nghiệm
        content = ('\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
            '\\choice \n'
            '{' + str(list_1[1]) + '}\n'
            '{' + str(list_1[2]) + '}\n'
            '{' + str(list_1[3]) + '}\n'
            '{' + str(list_1[0]) + '}\n'
            '\\loigiai{' + str(loigiai) + '}\n'
            '\\end{ex}\n\\end{minipage} \n\n')
        return content

