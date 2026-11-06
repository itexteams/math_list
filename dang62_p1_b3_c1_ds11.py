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


def bt_dang62_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số góc k của hàm tan(k*x) trong đáp án đúng để tạo nhiều câu hỏi khác nhau
                # Ví dụ k = 2 thì là tan 2x, k = 3 là tan 3x, k = 4 là tan 4x,...
                k = random.choice([2, 3, 4, 5])

                # Định nghĩa các chuỗi tương ứng cho phương án đúng (hàm số lẻ)
                ham_dung = 'y = x^2 \\tan %sx - \\cot x' % (latex(k))
                # Tập xác định thay đổi theo hệ số k: x khác pi/(2k) + m*pi/k và x khác m*pi
                txd_dung = 'D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{%s} + \\frac{m\\pi}{%s}, m\\pi; m \\in \\mathbb{Z} \\right\\}' % (latex(2*k), latex(k))
                bien_doi_dung = 'f(-x) = (-x)^2 \\tan(-%sx) - \\cot(-x) = -x^2 \\tan %sx + \\cot x = -f(x)' % (latex(k), latex(k))

                # Các hàm số sai (các hàm số chẵn) giữ nguyên cấu trúc mẫu
                ham_sai1 = 'y = 1 - \\sin^2 x'
                ham_sai2 = 'y = |\\cot x| \\cdot \\sin^2 x'
                ham_sai3 = 'y = 1 + |\\cot x + \\tan x|'

                # Câu hỏi
                noidungcauhoi = ('''Trong các hàm số sau, hàm số nào là hàm số lẻ?''')

                # Các đáp án trắc nghiệm không chứa dấu chấm ở cuối
                da_d = ('\\True $' + str(ham_dung) + '$')
                da_s1 = '$' + str(ham_sai1) + '$'
                da_s2 = '$' + str(ham_sai2) + '$'
                da_s3 = '$' + str(ham_sai3) + '$'

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, đầy đủ từng bước theo mẫu bằng định dạng %s
                loigiai = ('''Xét hàm số $%s = \\cos^2 x$. \\\\
                           Tập xác định $D = \\mathbb{R}$. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = \\cos^2(-x) = \\cos^2 x = f(x) \\longrightarrow f(x)$ là hàm số chẵn. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R} \\setminus \\left\\{ k\\pi, k \\in \\mathbb{Z} \\right\\}$. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = |\\cot(-x)| \\cdot \\sin^2(-x) = |\\cot x| \\cdot \\sin^2 x = f(x) \\longrightarrow f(x)$ là hàm số chẵn. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $%s$ là tập đối xứng. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $%s \\longrightarrow f(x)$ là hàm số lẻ $\\Rightarrow$ Chọn. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{2}, k \\in \\mathbb{Z} \\right\\}$. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $f(-x) = 1 + |\\cot(-x) + \\tan(-x)| = 1 + |-\\cot x - \\tan x| = 1 + |\\cot x + \\tan x| = f(x) \\longrightarrow f(x)$ là hàm số chẵn.'''
                           % (str(ham_sai1), str(ham_sai2), str(ham_dung), str(txd_dung), str(bien_doi_dung), str(ham_sai3)))

            # Xuất câu trắc nghiệm đúng định dạng mẫu của hệ thống
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

