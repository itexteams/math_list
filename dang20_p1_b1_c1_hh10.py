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


def bt_dang20_p1_b1_c1_hh10(self):
            # Khai báo biến
            lis=['1','2','3','4','5','6','7','8']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $'
                da_s1 = '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha \\cot \\alpha = -1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha - \\cos^{2} \\alpha =1 $'
                da_s1 = '\\True $1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '$1 + \\cot^{2} \\alpha = -\\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha \\cot \\alpha = 2 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =-1 $'
                da_s1 = '$1 - \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '\\True $1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha \\cot \\alpha = -1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây là đúng? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha - \\cos^{2} \\alpha =1 $'
                da_s1 = '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s2 = '$1 - \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '\\True $\\tan \\alpha \\cot \\alpha = 1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây \\textbf{sai}? \n'''
                            )
                # Các đáp án
                da_d = '\\True $\\sin^{2} \\alpha - \\cos^{2} \\alpha =1 $'
                da_s1 = '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha \\cot \\alpha = 1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây \\textbf{sai}? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $'
                da_s1 = '\\True $1 - \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha \\cot \\alpha = 1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='7':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây \\textbf{sai}? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $'
                da_s1 = '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '\\True $2 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '$\\tan \\alpha  \\cot \\alpha = 1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
                        )
            if dang=='8':
                # Câu hỏi
                noidungcauhoi=('''Cho góc $0^\\circ < \\alpha < 90^\\circ$. Khẳng định nào sau đây \\textbf{sai}? \n'''
                            )
                # Các đáp án
                da_d = '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $'
                da_s1 = '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $'
                da_s2 = '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $'
                da_s3 = '\\True $\\tan \\alpha + \\cot \\alpha = 1 $'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\sin^{2} \\alpha + \\cos^{2} \\alpha =1 $. \\\\ \n'
                        '$1 + \\tan^{2} \\alpha = \\dfrac{1}{\\cos^{2} \\alpha} $. \\\\ \n'
                        '$1 + \\cot^{2} \\alpha = \\dfrac{1}{\\sin^{2} \\alpha} $. \\\\ \n'
                        '$\\tan \\alpha \\cot \\alpha = 1 $. '
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-')
            return content

