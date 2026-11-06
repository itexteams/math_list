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


def bt_dang60_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các bộ dữ liệu ngẫu nhiên để thay đổi câu hỏi
                # Mỗi bộ gồm: đáp án đúng chẵn, và 3 đáp án sai (lẻ) kèm theo lời giải chi tiết tương ứng
                cac_bo_du_lieu = [
                    {
                        "da": "y = \\sin^3 x \\cdot \\cos\\left(x - \\frac{\\pi}{2}\\right)",
                        "da_rutgon": "y = f(x) = \\sin^3 x \\cdot \\cos\\left(x - \\frac{\\pi}{2}\\right) = \\sin^3 x \\cdot \\sin x = \\sin^4 x",
                        "da_f_am_x": "f(-x) = (\\sin(-x))^4 = \\sin^4 x = f(x)",
                        "ds_1": "y = \\sin x \\cos 2x",
                        "ds_2": "y = \\frac{\\tan x}{\\tan^2 x + 1}",
                        "ds_3": "y = \\cos x \\sin^3 x",
                        "cum_ds": "y = \\sin x \\cos 2x , y = \\frac{\\tan x}{\\tan^2 x + 1} \\text{ và } y = \\cos x \\sin^3 x"
                    },
                    {
                        "da": "y = \\cos^3 x \\cdot \\sin\\left(x + \\frac{\\pi}{2}\\right)",
                        "da_rutgon": "y = f(x) = \\cos^3 x \\cdot \\sin\\left(x + \\frac{\\pi}{2}\\right) = \\cos^3 x \\cdot \\cos x = \\cos^4 x",
                        "da_f_am_x": "f(-x) = (\\cos(-x))^4 = \\cos^4 x = f(x)",
                        "ds_1": "y = \\sin 2x \\cos x",
                        "ds_2": "y = \\frac{\\sin x}{\\cos^2 x + 2}",
                        "ds_3": "y = \\tan x \\cdot \\cos^2 x",
                        "cum_ds": "y = \\sin 2x \\cos x , y = \\frac{\\sin x}{\\cos^2 x + 2} \\text{ và } y = \\tan x \\cdot \\cos^2 x"
                    },
                    {
                        "da": "y = \\sin x \\cdot \\sin 3x",
                        "da_rutgon": "y = f(x) = \\sin x \\cdot \\sin 3x",
                        "da_f_am_x": "f(-x) = \\sin(-x) \\cdot \\sin(-3x) = (-\\sin x) \\cdot (-\\sin 3x) = \\sin x \\cdot \\sin 3x = f(x)",
                        "ds_1": "y = \\sin^3 x \\cdot \\cos x",
                        "ds_2": "y = \\frac{\\tan 2x}{\\sin^2 x + 3}",
                        "ds_3": "y = \\sin x + \\sin 2x",
                        "cum_ds": "y = \\sin^3 x \\cdot \\cos x , y = \\frac{\\tan 2x}{\\sin^2 x + 3} \\text{ và } y = \\sin x + \\sin 2x"
                    }
                ]

                # Chọn ngẫu nhiên một bộ dữ liệu
                bo = random.choice(cac_bo_du_lieu)

                # Đáp án đúng
                da = bo["da"]
                da_d = ('\\True $' + str(da) + '$')

                # Các đáp án sai
                das1 = '$' + bo["ds_1"] + '$'
                das2 = '$' + bo["ds_2"] + '$'
                das3 = '$' + bo["ds_3"] + '$'

                # Câu hỏi
                noidungcauhoi = ('''Trong các hàm số sau, hàm số nào có đồ thị đối xứng qua trục tung?''')

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết sử dụng %s đúng cấu trúc mẫu
                loigiai = ('''Nhận xét: Hàm số chẵn có đồ thị đối xứng qua trục tung. \\\\
                           Xét các hàm số $%s$ là các hàm số có tính lẻ nên đồ thị không đối xứng qua trục tung. \\\\
                           Xét hàm số $%s$. \\\\
                           Tập xác định $D = \\mathbb{R}$. Do đó $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $%s \\longrightarrow f(x)$ là hàm số chẵn.'''
                           % (str(bo["cum_ds"]), str(bo["da_rutgon"]), str(bo["da_f_am_x"])))

            # Xuất câu trắc nghiệm đúng định dạng mong muốn
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

