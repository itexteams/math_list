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


def bt_dang74_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ dữ liệu ngẫu nhiên để thay đổi câu hỏi
                cac_bo_du_lieu = [
                    {
                        "khoang": "\\left( -\\frac{\\pi}{3}; \\frac{\\pi}{6} \\right)",
                        "pa_dung": "y = \\sin x",
                        "pa_sai1": "y = \\cos x",
                        "pa_sai2": "y = \\cot 2x",
                        "pa_sai3": "y = \\cos 2x",
                        "tikz_draw": (
                            "\\begin{center} \\begin{tikzpicture}[scale=2, line width=1pt, >=latex]\n"
                            "\\draw[->] (-1.3,0) -- (1.3,0) node[below] {$x$};\n"
                            "\\draw[->] (0,-1.3) -- (0,1.3) node[right] {$y$};\n"
                            "\\node[below left] at (0,0) {$O$};\n"
                            "\\draw (0,0) circle (1);\n"
                            "\\draw[line width=1.5pt] (0, -0.866) -- (0, 0.5);\n"
                            "\\draw[dashed] (0,0.5) node[left, xshift=-2pt] {$\\frac{1}{2}$} -- (0.866,0.5) node[right, xshift=2pt] {$\\frac{\\pi}{6}$};\n"
                            "\\draw[dashed] (0,-0.866) node[left, xshift=-2pt] {$-\\frac{\\sqrt{3}}{2}$} -- (0.5,-0.866) node[right, xshift=2pt] {$-\\frac{\\pi}{3}$};\n"
                            "\\draw[dashed] (0,0) -- (0.866,0.5);\n"
                            "\\draw[dashed] (0,0) -- (0.5,-0.866);\n"
                            "\\end{tikzpicture} \\end{center}"
                        )
                    },
                    {
                        "khoang": "\\left( -\\frac{\\pi}{4}; \\frac{\\pi}{4} \\right)",
                        "pa_dung": "y = \\sin x",
                        "pa_sai1": "y = \\cos x",
                        "pa_sai2": "y = \\tan 2x",
                        "pa_sai3": "y = \\cot x",
                        "tikz_draw": (
                            "\\begin{center} \\begin{tikzpicture}[scale=2, line width=1pt, >=latex]\n"
                            "\\draw[->] (-1.3,0) -- (1.3,0) node[below] {$x$};\n"
                            "\\draw[->] (0,-1.3) -- (0,1.3) node[right] {$y$};\n"
                            "\\node[below left] at (0,0) {$O$};\n"
                            "\\draw (0,0) circle (1);\n"
                            "\\draw[line width=1.5pt] (0, -0.707) -- (0, 0.707);\n"
                            "\\draw[dashed] (0,0.707) node[left, xshift=-2pt] {$\\frac{\\sqrt{2}}{2}$} -- (0.707,0.707) node[right, xshift=2pt] {$\\frac{\\pi}{4}$};\n"
                            "\\draw[dashed] (0,-0.707) node[left, xshift=-2pt] {$-\\frac{\\sqrt{2}}{2}$} -- (0.707,-0.707) node[right, xshift=2pt] {$-\\frac{\\pi}{4}$};\n"
                            "\\draw[dashed] (0,0) -- (0.707,0.707);\n"
                            "\\draw[dashed] (0,0) -- (0.707,-0.707);\n"
                            "\\end{tikzpicture} \\end{center}"
                        )
                    }
                ]

                # Chọn ngẫu nhiên một bộ dữ liệu
                bo = random.choice(cac_bo_du_lieu)

                # Câu hỏi
                noidungcauhoi = ('''Hàm số nào đồng biến trên khoảng $%s$?''' % (str(bo["khoang"])))

                # Định dạng các phương án trả lời trắc nghiệm (không chứa dấu chấm ở cuối)
                da_d = ('\\True $' + str(bo["pa_dung"]) + '$')
                da_s1 = '$' + str(bo["pa_sai1"]) + '$'
                da_s2 = '$' + str(bo["pa_sai2"]) + '$'
                da_s3 = '$' + str(bo["pa_sai3"]) + '$'

                # Trộn thứ tự các phương án ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết bao gồm đồ thị TikZ và phần giải thích chữ sử dụng %s
                loigiai = ('''%s
                           Quan sát trên đường tròn lượng giác, \\\\
                           ta thấy trên khoảng $%s$ hàm $%s$ tăng dần.'''
                           % (str(bo["tikz_draw"]), str(bo["khoang"]), str(bo["pa_dung"])))

            # Xuất câu trắc nghiệm đúng định dạng khung chương trình mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

