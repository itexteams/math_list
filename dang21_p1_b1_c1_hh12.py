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


def bt_dang21_p1_b1_c1_hh12(self):
            # Khai báo biến
            # --- Khai báo biến ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Randomize the side length of the cube
                side_length = random.randint(2, 8)

                # Calculate the correct answer
                correct_magnitude_symbolic = side_length * sqrt(3)
                correct_magnitude_latex = latex(correct_magnitude_symbolic)

                # Generate incorrect answers (distractors)
                wrong_answers = [
                    latex(side_length),                    # Side length
                    latex(side_length * sqrt(2)),          # Face diagonal
                    latex(2 * side_length),                # Double the side
                    latex(side_length * sqrt(2) + 1),      # Off by one on face diagonal
                    latex(side_length * sqrt(3) + 1),      # Off by one on space diagonal
                    latex(side_length / 2 * sqrt(3))       # Half the diagonal
                ]

                # Shuffle the wrong answers to pick randomly
                random.shuffle(wrong_answers)

                # Set the correct answer and a few distractors
                da = f'${correct_magnitude_latex}$'
                das1 = f'${wrong_answers[0]}$'
                das2 = f'${wrong_answers[1]}$'
                das3 = f'${wrong_answers[2]}$'

                # --- Câu hỏi ---
                noidungcauhoi = (
                    f'''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh ${latex(side_length)}$. Đặt $\\vec{{u}} = \\vec{{A'C'}} - \\vec{{A'A}}$. Độ dài của vectơ $\\vec{{u}}$ bằng'''
                )

                # --- Các đáp án ---
                da_d = f'\\True {da}'
                da_s1 = f'{das1}'
                da_s2 = f'{das2}'
                da_s3 = f'{das3}'

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                loigiai = (
                    f'''Ta có $\\vec{{u}} = \\vec{{A'C'}} - \\vec{{A'A}} = \\vec{{AC'}}$. \\\\
                    Đây là vectơ đường chéo của hình lập phương. \\\\
                    Do đó, độ dài của vectơ $\\vec{{u}}$ là \\\\
                    $|\\vec{{u}}| = |\\vec{{AC'}}| = {latex(side_length)}\\sqrt{{3}} = {correct_magnitude_latex}$.'''
                )

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\choice \n'
                f'{{{str(list_1[0])}}}\n'
                f'{{{str(list_1[1])}}}\n'
                f'{{{str(list_1[2])}}}\n'
                f'{{{str(list_1[3])}}}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

