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


def bt_dang12_p1_b1_c1_ds11(self):
            # Khai báo biến

            lis=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']
            dang=random.choice(lis)
            if dang=='29':
                # Câu hỏi
                noidungcauhoi=('''Cho $-2\\pi < \\alpha < -\\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True  $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )

            if dang=='30':
                # Câu hỏi
                noidungcauhoi=('''Cho $-2\\pi < \\alpha < -\\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='31':
                # Câu hỏi
                noidungcauhoi=('''Cho $-2\\pi < \\alpha < -\\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='32':
                # Câu hỏi
                noidungcauhoi=('''Cho $-2\\pi < \\alpha < -\\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='25':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{3\\pi}{2} < \\alpha < -\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='26':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{3\\pi}{2} < \\alpha < -\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='27':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{3\\pi}{2} < \\alpha < -\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = ' $\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='28':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{3\\pi}{2} < \\alpha < -\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='21':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\pi < \\alpha < -\\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='22':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\pi < \\alpha < -\\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='23':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\pi < \\alpha < -\\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='24':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\pi < \\alpha < -\\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='17':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{\\pi}{2} < \\alpha < 0$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='18':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{\\pi}{2} < \\alpha < 0$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='19':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{\\pi}{2} < \\alpha < 0$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='20':
                # Câu hỏi
                noidungcauhoi=('''Cho $-\\dfrac{\\pi}{2} < \\alpha < 0$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='16':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{3\\pi}{2} < \\alpha < 2\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='15':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{3\\pi}{2} < \\alpha < 2\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='14':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{3\\pi}{2} < \\alpha < 2\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='13':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{3\\pi}{2} < \\alpha < 2\\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ tư. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='12':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\pi < \\alpha < \\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='11':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\pi < \\alpha < \\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='10':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\pi < \\alpha < \\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha >0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='9':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\pi < \\alpha < \\dfrac{3\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ ba. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha <0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '\\True $\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '\\True $\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = ' $\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )
            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ hai. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha <0$. \\\\ \n'
                        '$\\tan \\alpha <0$. \\\\ \n'
                        '$\\cot \\alpha <0$. '
                        )

            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Cho $0 < \\alpha < \\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '\\True  $\\cot \\alpha >0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )

            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho $0 < \\alpha < \\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '\\True $\\tan \\alpha >0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $0 < \\alpha < \\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin \\alpha <0$'
                da_s1 = '\\True $\\cos \\alpha >0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $0 < \\alpha < \\dfrac{\\pi}{2}$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin \\alpha >0$'
                da_s1 = '$\\cos \\alpha <0$'
                da_s2 = '$\\tan \\alpha <0$'
                da_s3 = '$\\cot \\alpha <0$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\alpha$ có điểm biểu diễn thuộc góc phần tư thứ nhất. \\\\ \n'
                        'Ta có các giá trị \\\\ \n'
                        '$\\sin \\alpha >0$. \\\\ \n'
                        '$\\cos \\alpha >0$. \\\\ \n'
                        '$\\tan \\alpha >0$. \\\\ \n'
                        '$\\cot \\alpha >0$. '
                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

