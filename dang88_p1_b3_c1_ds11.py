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


def bt_dang88_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số góc của hàm lượng giác (bài gốc là 3)
                he_so_goc = randint(2, 5)

                # Random bội số k để tạo giá trị lớn nhất mong muốn bằng k * sqrt(2)
                # Bài gốc k = 1 -> giá trị lớn nhất bằng \sqrt{2}
                k = randint(1, 4)

                # Biểu thức giá trị lớn nhất đề bài cho trước
                if k == 1:
                    gtln_de_bai = '\\sqrt{2}'
                else:
                    gtln_de_bai = '%s\\sqrt{2}' % (latex(k))

                # Tính toán giá trị đúng của m: sqrt(2) + m = k*sqrt(2) => m = (k-1)*sqrt(2)
                m_val_numeric = k - 1
                if m_val_numeric == 0:
                    da_chuoi = 'm = 0'
                elif m_val_numeric == 1:
                    da_chuoi = 'm = \\sqrt{2}'
                else:
                    da_chuoi = 'm = %s\\sqrt{2}' % (latex(m_val_numeric))

                du = ['$%s$' % (da_chuoi)]
                da_choice = random.choice(du)

                # Tạo các phương án nhiễu sinh động theo mẫu bài gốc (bảo đảm không trùng đáp án đúng)
                s_nhieu = [
                    'm = \\sqrt{2}',
                    'm = 1',
                    'm = \\frac{1}{\\sqrt{2}}',
                    'm = 0',
                    'm = -\\sqrt{2}',
                    'm = 2\\sqrt{2}',
                    'm = %s' % (latex(k))
                ]

                s = []
                for phuong_an in s_nhieu:
                    chuoi_pa = '$%s$' % (phuong_an)
                    if chuoi_pa != '$%s$' % (da_chuoi) and chuoi_pa not in s:
                        s.append(chuoi_pa)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Giá trị của $m$ để hàm số $y = \\sin %sx - \\cos %sx + m$ có giá trị lớn nhất bằng $%s$ là''' 
                                 % (latex(he_so_goc), latex(he_so_goc), gtln_de_bai))

                # Các đáp án (Đã đưa vào bên trong khối điều kiện logic if)
                da_d = ('\\True ' + str(da_choice))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết trình bày rõ ràng từng bước như nội dung gốc
                loigiai = ('''Ta có $y = \\sin %sx - \\cos %sx + m = \\sqrt{2}\\sin\\left(%sx - \\frac{\\pi}{4}\\right) + m \\le \\sqrt{2} + m$.\\\\
                           Để hàm số có giá trị lớn nhất bằng $%s$ thì $\\sqrt{2} + m = %s \\Leftrightarrow %s$.'''
                           % (latex(he_so_goc), latex(he_so_goc), latex(he_so_goc), gtln_de_bai, gtln_de_bai, da_chuoi))

            # Xuất câu trắc nghiệm đúng định dạng mẫu khung chương trình
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

