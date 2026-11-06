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


def bt_dang29_p4_b2_c1_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Vòng lặp đảm bảo sinh số hợp lý về mặt toán học
                while True:
                    X = randint(4, 12)          # Số HS giỏi cả Văn và Toán (Đáp án đúng)
                    N_none = randint(8, 15)     # Số HS không đạt HSG
                    N = randint(38, 48)         # Tổng số học sinh cả lớp
                    N_good = N - N_none         # Số HS giỏi ít nhất một môn
                    # Điều kiện để tồn tại bộ số tập hợp hợp lệ
                    if N_good > X + 2:
                        V = randint(X + 1, N_good - 1)  # Số HS giỏi Văn
                        T = N_good + X - V              # Số HS giỏi Toán
                        if T > X and T < N_good:
                            break

                da = '$%s$' % (latex(X))

                # Khởi tạo các phương án sai (không trùng với đáp án đúng)
                s = [
                    '$%s$' % (latex(X + 2)),
                    '$%s$' % (latex(X + 3)),
                    '$%s$' % (latex(X + 5)),
                    '$%s$' % (latex(X + 7)),
                ]
                if X - 2 > 0:
                    s.append('$%s$' % (latex(X - 2)))
                if X - 3 > 0:
                    s.append('$%s$' % (latex(X - 3)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong kì thi học sinh giỏi cấp trường lớp 11B1 có $%s$ học sinh giỏi Văn, $%s$ học sinh giỏi Toán. Tìm số học sinh giỏi cả Văn và Toán biết lớp 11B1 có $%s$ học sinh, và có $%s$ học sinh không đạt học sinh giỏi.'''
                                 % (latex(V), latex(T), latex(N), latex(N_none)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Số học sinh đạt danh hiệu học sinh giỏi (giỏi ít nhất một trong hai môn Văn hoặc Toán) của lớp 11B1 là:\\\\
            $%s - %s = %s$ (học sinh).\\\\
            Gọi $X$ là tập hợp các học sinh giỏi Văn, $Y$ là tập hợp các học sinh giỏi Toán.\\\\
            Khi đó, số học sinh giỏi cả Văn và Toán là số phần tử của tập hợp giao $X \\cap Y$.\\\\
            Theo nguyên lý bao hàm - loại trừ, ta có công thức:\\\\
            $n(X \\cup Y) = n(X) + n(Y) - n(X \\cap Y)$\\\\
            $\\Rightarrow %s = %s + %s - n(X \\cap Y)$\\\\
            $\\Rightarrow n(X \\cap Y) = %s + %s - %s = %s$ (học sinh).\\\\
            Vậy có $%s$ học sinh giỏi cả Văn và Toán.'''
                           % (latex(N), latex(N_none), latex(N_good),
                              latex(N_good), latex(V), latex(T),
                              latex(V), latex(T), latex(N_good), latex(X), latex(X)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')   
            return content 

