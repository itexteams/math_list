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


def bt_dang15_p1_b2_c4_ds12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Random các giá trị xác suất (thường là các số thập phân đẹp)
                # p_b_bar: P(B ngang)
                # p_a_cond_b: P(A|B)
                # p_a_cond_b_bar: P(A|B ngang)

                p_b_bar_val = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
                p_a_cond_b_val = random.choice([0.5, 0.6, 0.7, 0.8])
                p_a_cond_b_bar_val = random.choice([0.1, 0.2, 0.3, 0.4])

                # Chuyển sang Decimal để tính toán chính xác số thập phân
                p_b_bar = Decimal(str(p_b_bar_val))
                p_a_cond_b = Decimal(str(p_a_cond_b_val))
                p_a_cond_b_bar = Decimal(str(p_a_cond_b_bar_val))

                p_b = 1 - p_b_bar

                # Tính P(A)
                res_pa = p_a_cond_b * p_b + p_a_cond_b_bar * p_b_bar

                # Định dạng hiển thị (thay dấu chấm bằng dấu phẩy theo chuẩn VN trong một số trường hợp)
                def fmt(val):
                    return str(val).replace('.', ',')

                kq_dung = '$%s$' % fmt(res_pa)

                # --- B4: Điều chỉnh các phương án sai không trùng đáp án đúng ---
                s = set()
                while len(s) < 3:
                    # Tạo các phương án sai quanh quẩn đáp án đúng
                    sai = res_pa + Decimal(random.choice(['0.1', '-0.1', '0.05', '-0.05', '0.12', '-0.08']))
                    if sai > 0 and sai < 1 and sai != res_pa:
                        s.add('$%s$' % fmt(sai))

                list_sai = list(s)

                # Câu hỏi
                noidungcauhoi = (
                    'Cho hai biến cố $A, B$ thỏa mãn $P(\\overline{B}) = %s; P(A|B) = %s; P(A|\\overline{B}) = %s$. Khi đó, $P(A)$ bằng'
                    % (fmt(p_b_bar), fmt(p_a_cond_b), fmt(p_a_cond_b_bar))
                )

                # Các đáp án
                da_d = '\\True ' + kq_dung
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Ta có $P(B) = 1 - P(\\overline{B}) = 1 - %s = %s$. \\\\ '
                    'Áp dụng công thức xác suất toàn phần, ta có: \\\\ '
                    '$P(A) = P(A|B) \\cdot P(B) + P(A|\\overline{B}) \\cdot P(\\overline{B})$ \\\\ '
                    '$P(A) = %s \\cdot %s + %s \\cdot %s = %s$.'
                    % (fmt(p_b_bar), fmt(p_b), fmt(p_a_cond_b), fmt(p_b), fmt(p_a_cond_b_bar), fmt(p_b_bar), fmt(res_pa))
                )

            # Xuất câu trắc nghiệm (Không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

