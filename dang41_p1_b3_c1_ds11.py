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


def bt_dang41_p1_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo danh sách các hàm số lượng giác cơ bản cùng chu kỳ của chúng
                # Mỗi hàm gồm: (chuỗi hiển thị latex, chu kỳ latex, chu kỳ rút gọn latex, giá trị chu kỳ sp để so sánh)
                h_sin2x = ('y = \\sin 2x', '\\frac{2\\pi}{2} = \\pi', '\\pi', pi)
                h_cosx = ('y = \\cos x', '2\\pi', '2\\pi', 2*pi)
                h_tanx = ('y = \\tan x', '\\pi', '\\pi', pi)
                h_cotx = ('y = \\cot x', '\\pi', '\\pi', pi)
                h_sin3x = ('y = \\sin 3x', '\\frac{2\\pi}{3}', '\\frac{2\\pi}{3}', Rational(2,3)*pi)
                h_cos2x = ('y = \\cos 2x', '\\frac{2\\pi}{2} = \\pi', '\\pi', pi)
                h_tan2x = ('y = \\tan 2x', '\\frac{\\pi}{2}', '\\frac{\\pi}{2}', Rational(1,2)*pi)

                # Chọn chu kỳ yêu cầu ngẫu nhiên (ví dụ ở đây chọn chu kỳ là pi)
                chu_ky_yeu_cau_str = '\\pi'
                chu_ky_yeu_cau_val = pi

                # Gom nhóm các hàm số để trích xuất ngẫu nhiên 4 hàm
                pool = [h_sin2x, h_cosx, h_tanx, h_cotx, h_sin3x, h_cos2x, h_tan2x]
                selected_funcs = random.sample(pool, 4)

                # Đếm số hàm số thỏa mãn chu kỳ yêu cầu
                count_correct = 0
                funcs_correct = []
                funcs_incorrect = []

                for f in selected_funcs:
                    if f[3] == chu_ky_yeu_cau_val:
                        count_correct += 1
                        funcs_correct.append(f)
                    else:
                        funcs_incorrect.append(f)

                # Đáp án đúng
                da = count_correct
                du = ['$%s$'%(da)]

                # Tạo các phương án sai (0, 1, 2, 3, 4 loại trừ đáp án đúng)
                s_choices = [0, 1, 2, 3, 4]
                if da in s_choices:
                    s_choices.remove(da)

                s = ['$%s$'%(c) for c in s_choices]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho các hàm số: $%s$, $%s$, $%s$, $%s$. Số hàm số tuần hoàn với chu kỳ $T = %s$ là'''
                                 %(selected_funcs[0][0], selected_funcs[1][0], selected_funcs[2][0], selected_funcs[3][0], chu_ky_yeu_cau_str))

                # Các đáp án
                da_d = ('\\True ' + str(du[0]))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                str_lg = ''
                for f in selected_funcs:
                    if f[3] == chu_ky_yeu_cau_val:
                        str_lg += 'Hàm số $%s$ là hàm số tuần hoàn với chu kỳ $T = %s$. \\\\\n' % (f[0], f[1])
                    else:
                        str_lg += 'Hàm số $%s$ là hàm số tuần hoàn với chu kỳ $T = %s$. \\\\\n' % (f[0], f[1])

                str_lg += 'Vậy có $%s$ hàm số thỏa mãn yêu cầu bài toán.' % (da)

                loigiai = ('''%s''' % (str_lg))

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

