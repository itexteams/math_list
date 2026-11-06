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


def bt_dang11_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Lấy ngẫu nhiên kích thước mẫu N từ 10 đến 2028 (có thể chẵn hoặc lẻ)
                N = random.randint(10, 2028)

                # Sinh đáp án và lời giải dựa trên tính chẵn/lẻ của N
                distractors = set()

                if N % 2 != 0:
                    correct_pos = (N + 1) // 2
                    da_text = f"Số trung vị trong mẫu số liệu đã cho là số thứ {correct_pos}"
                    loigiai = f"Mẫu số liệu có $N = {N}$ (là số lẻ) nên số trung vị là số thứ $\\frac{{{N}+1}}{{2}} = {correct_pos}$"

                    # Các phương án nhiễu cho trường hợp N lẻ
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {N // 2}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {correct_pos + 1}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {N}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là trung bình cộng của số thứ {N // 2} và số thứ {N // 2 + 1}")
                else:
                    pos1 = N // 2
                    pos2 = N // 2 + 1
                    da_text = f"Số trung vị trong mẫu số liệu đã cho là trung bình cộng của số thứ {pos1} và số thứ {pos2}"
                    loigiai = f"Mẫu số liệu có $N = {N}$ (là số chẵn) nên số trung vị là trung bình cộng của số thứ $\\frac{{{N}}}{{2}} = {pos1}$ và số thứ $\\frac{{{N}}}{{2}}+1 = {pos2}$"

                    # Các phương án nhiễu cho trường hợp N chẵn
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {pos1}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {pos2}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là số thứ {N}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là trung bình cộng của số thứ {pos1 - 1} và số thứ {pos1}")
                    distractors.add(f"Số trung vị trong mẫu số liệu đã cho là trung bình cộng của số thứ {pos2} và số thứ {pos2 + 1}")

                # Đáp án đúng
                da = da_text

                # Lấy ngẫu nhiên 3 phương án nhiễu từ tập hợp
                distractors = list(distractors)
                chosen_distractors = random.sample(distractors, 3)

                das1 = chosen_distractors[0]
                das2 = chosen_distractors[1]
                das3 = chosen_distractors[2]

                # Câu hỏi
                noidungcauhoi = (f"Cho một mẫu số liệu gồm ${N}$ số đã được sắp xếp tăng dần. "
                                 f"Mệnh đề nào sau đây là đúng?")

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

