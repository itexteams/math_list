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


def bt_dang17_p1_b1_c1_hh12(self):
        # Khai báo biến
        lisdang = ['1']
        dang = random.choice(lisdang)

        if dang == '1':
            # Cố định tứ diện ABCD
            A, B, C, D = 'A', 'B', 'C', 'D'

            # Đáp án đúng:
            da = f'$\\vec{{I{A}}} + \\vec{{I{B}}} + \\vec{{I{C}}} + \\vec{{I{D}}} = \\vec{{0}}$'

            # Bộ 3 phương án sai cố định, phân biệt và bám sát dạng đề bài
            # Phủ định mệnh đề đúng hoặc các hệ thức sai thường gặp
            das1 = f'$\\vec{{I{A}}} + \\vec{{I{B}}} + \\vec{{I{C}}} + \\vec{{I{D}}} \\ne \\vec{{0}}$'
            das2 = f'$\\vec{{I{A}}} + \\vec{{I{B}}} = \\vec{{0}}$'
            das3 = f'$\\vec{{I{C}}} + \\vec{{I{D}}} = \\vec{{0}}$'

            # Nội dung câu hỏi
            noidungcauhoi = (f'Cho tứ diện ${A}{B}{C}{D}$. Gọi $M, N$ lần lượt là trung điểm của ${A}{B}, {C}{D}$ và $I$ là trung điểm của $MN$. '
                             f'Trong các khẳng định sau, khẳng định nào đúng?')

            # Các phương án
            da_d = '\\True ' + str(da)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Xáo trộn vị trí các phương án A, B, C, D
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = (f'$M, N, I$ lần lượt là trung điểm của ${A}{B}, {C}{D}, MN$ nên theo quy tắc trung điểm ta có:\n'
                       f'$$\\vec{{I{A}}} + \\vec{{I{B}}} = 2\\vec{{IM}}; \\quad \\vec{{I{C}}} + \\vec{{I{D}}} = 2\\vec{{IN}}; \\quad \\vec{{IM}} + \\vec{{IN}} = \\vec{{0}}.$$\n'
                       f'Suy ra:\n'
                       f'$$\\vec{{I{A}}} + \\vec{{I{B}}} + \\vec{{I{C}}} + \\vec{{I{D}}} = 2\\vec{{IM}} + 2\\vec{{IN}} = 2(\\vec{{IM}} + \\vec{{IN}}) = 2\\vec{{0}} = \\vec{{0}}.$$')

        # Xuất câu trắc nghiệm định dạng minipage TeX
        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                   '\\choice \n'
                   '{' + str(list_1[0]) + '}\n'
                   '{' + str(list_1[1]) + '}\n'
                   '{' + str(list_1[2]) + '}\n'
                   '{' + str(list_1[3]) + '}\n'
                   '\\loigiai{' + str(loigiai) + '}\n'
                   '\\end{ex}\n\\end{minipage}\n\n')
        return content

