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


def bt_dang8_p1_b3_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán
                # Random tổng số chấm (S) từ 7 đến 10 để bài toán luôn có lời giải tương tự
                S = random.choice([7, 8, 9, 10])

                # Tính không gian mẫu
                n_omega = 36

                # Tìm các phần tử của biến cố A: Tổng bằng S
                # Tìm các phần tử của biến cố AB: Tổng bằng S và lần gieo thứ hai là số chẵn
                tap_A = []
                tap_AB = []
                for i in range(1, 7):
                    for j in range(1, 7):
                        if i + j == S:
                            tap_A.append((i, j))
                            if j % 2 == 0:
                                tap_AB.append((i, j))

                n_AB = len(tap_AB)
                kq_prob = Rational(n_AB, n_omega)

                # Chuyển tập AB sang định dạng LaTeX để đưa vào lời giải
                # Sử dụng \left( \right) theo yêu cầu
                latex_AB = " \\left\\{ " + "; ".join(["\\left(" + str(i) + "," + str(j) + "\\right)" for i, j in tap_AB]) + " \\right\\} "

                # Bước 4: Điều chỉnh các phương án sai
                # Các đáp án trắc nghiệm phổ biến trong bài toán xúc xắc
                du = ['$%s$' % (latex(kq_prob))]
                da = random.choice(du)

                s_pool = [Rational(1, 6), Rational(1, 12), Rational(1, 18), Rational(1, 9), 
                          Rational(5, 36), Rational(1, 4), Rational(1, 2), Rational(1, 3), Rational(7, 36)]

                # Lọc bỏ đáp án đúng khỏi danh sách phương án sai
                s_filtered = [item for item in s_pool if item != kq_prob]
                random.shuffle(s_filtered)

                das1 = '$%s$' % (latex(s_filtered[0]))
                das2 = '$%s$' % (latex(s_filtered[1]))
                das3 = '$%s$' % (latex(s_filtered[2]))

                # Câu hỏi (Bám sát nội dung ảnh)
                noidungcauhoi = ('''Gieo một con xúc xắc cân đối, đồng chất hai lần liên tiếp. Xét các biến cố:
            \\\\ A: "Tổng số chấm ở hai lần gieo bằng $%s$".
            \\\\ B: "Số chấm xuất hiện ở lần gieo thứ hai là số chẵn".
            \\\\ Xác suất của biến cố $AB$ là''' 
                                 % (latex(S)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Bám sát mẫu ảnh, không viết tắt)
                loigiai = ('''Không gian mẫu của phép thử có số phần tử là $n\\left(\\Omega\\right) = 36$. \\\\
                             Biến cố $AB$ là biến cố: "Tổng số chấm ở hai lần gieo bằng $%s$ và số chấm ở lần gieo thứ hai là số chẵn". \\\\
                             Các kết quả thuận lợi cho biến cố $AB$ là: \\\\
                             $AB = %s$. \\\\
                             Số phần tử của biến cố $AB$ là $n\\left(AB\\right) = %s$. \\\\
                             Xác suất của biến cố $AB$ là: \\\\
                             $P\\left(AB\\right) = \\frac{n\\left(AB\\right)}{n\\left(\\Omega\\right)} = \\frac{%s}{36} = %s$.'''
                           % (latex(S), latex_AB, latex(n_AB), latex(n_AB), latex(kq_prob)))

            # Xuất câu trắc nghiệm theo đúng cấu trúc content
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

