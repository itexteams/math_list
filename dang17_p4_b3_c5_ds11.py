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


def bt_dang17_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                n = randint(2025, 2050)
                n1 = n      # 2020
                n2 = n - 1  # 2019
                n3 = n - 2  # 2018
                n4 = n - 3  # 2017

                # Đáp án đúng: a = n4^n3
                kq_chuan = '{%s}^{%s}' % (n4, n3)

                # B4: Điều chỉnh các phương án sai
                sai1 = '{%s}^{%s}' % (n3, n2)
                sai2 = '{%s}^{%s}' % (n2, n1)
                sai3 = '0'

                # Các đáp án trắc nghiệm
                da_d = ('\\True $%s$' % kq_chuan)
                da_s1 = ('$%s$' % sai1)
                da_s2 = ('$%s$' % sai2)
                da_s3 = ('$%s$' % sai3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Viết lại y hệt đề bài và lời giải theo mẫu
                # Câu hỏi
                noidungcauhoi = ('''Tập xác định của hàm số $y = \\log_{%s}(\\log_{%s}(\\log_{%s}(\\log_{%s} x)))$ là $D = (a; +\\infty)$. Tính giá trị của $a$.'''
                                 %(latex(n1), latex(n2), latex(n3), latex(n4)))

                # Nội dung lời giải
                loigiai = ('''Điều kiện xác định của hàm số đã cho là:
            \\begin{center}
            $\\begin{cases} x > 0 \\\\ \\log_{%s} x > 0 \\\\ \\log_{%s}(\\log_{%s} x) > 0 \\\\ \\log_{%s}(\\log_{%s}(\\log_{%s} x)) > 0 \\end{cases} 
            \\Leftrightarrow \\begin{cases} x > 0 \\\\ \\log_{%s} x > 0 \\\\ \\log_{%s}(\\log_{%s} x) > 0 \\\\ \\log_{%s}(\\log_{%s} x) > 1 \\end{cases}$
            \\end{center}
            \\begin{center}
            $\\Leftrightarrow \\begin{cases} x > 0 \\\\ \\log_{%s} x > 0 \\\\ \\log_{%s} x > %s^1 \\end{cases} 
            \\Leftrightarrow \\begin{cases} x > 0 \\\\ \\log_{%s} x > %s \\end{cases} 
            \\Leftrightarrow x > %s^{%s}$.
            \\end{center}
            Vậy $a = %s^{%s}$.'''
                           %(latex(n4), latex(n3), latex(n4), latex(n2), latex(n3), latex(n4),
                             latex(n4), latex(n3), latex(n4), latex(n3), latex(n4),
                             latex(n4), latex(n3), latex(n4), latex(n3), 
                             latex(n4), latex(n4), latex(n3),
                             latex(n4), latex(n3)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

