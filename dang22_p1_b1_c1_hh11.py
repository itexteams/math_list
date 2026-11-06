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


def bt_dang22_p1_b1_c1_hh11(self):
    # Khai báo dạng bài
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Hình chóp tứ giác S.ABCD
        p_name = 'S.ABCD'
        vertices = ['A', 'B', 'C', 'D']
        idx = random.randint(0, 3)

        v_common = vertices[idx]
        v_left = vertices[(idx - 1) % 4]
        v_right = vertices[(idx + 1) % 4]
        v_opp = vertices[(idx + 2) % 4]

        p1_str = 'S' + v_left + v_common
        p2_str = 'S' + v_common + v_right

        # Đáp án đúng
        da_correct = 'S' + v_common

        # Tạọ danh sách các phương án sai
        wrong_candidates = [
            'S' + v_left,
            'S' + v_right,
            'S' + v_opp,
            v_left + v_right,
            v_left + v_opp,
            v_common + v_opp,
            v_left + v_common,
            v_common + v_right
        ]

        # Loại bỏ phương án trùng với đáp án đúng
        wrong_candidates = list(set(wrong_candidates))
        if da_correct in wrong_candidates:
            wrong_candidates.remove(da_correct)

        random.shuffle(wrong_candidates)
        das1 = wrong_candidates[0]
        das2 = wrong_candidates[1]
        das3 = wrong_candidates[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $%s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng nào trong các đường thẳng sau?'''
                         %(p_name, p1_str, p2_str))

        # Các đáp án
        da_d = ('\\True $%s$' %(da_correct))
        da_s1 = ('$%s$' %(das1))
        da_s2 = ('$%s$' %(das2))
        da_s3 = ('$%s$' %(das3))

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Hai mặt phẳng $(%s)$ và $(%s)$ có hai điểm chung phân biệt là $S$ và $%s$.\\\\
    Hai mặt phẳng $(%s)$ và $(%s)$ cắt nhau theo giao tuyến là đường thẳng đi qua hai điểm chung đó.\\\\
    Do đó, giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng $%s$.'''
                   %(p1_str, p2_str, v_common, p1_str, p2_str, p1_str, p2_str, da_correct))

    elif dang == '2':
        # Dạng 2: Hình chóp tam giác S.ABC
        p_name = 'S.ABC'
        vertices = ['A', 'B', 'C']
        idx = random.randint(0, 2)

        v_common = vertices[idx]
        v_left = vertices[(idx - 1) % 3]
        v_right = vertices[(idx + 1) % 3]

        p1_str = 'S' + v_left + v_common
        p2_str = 'S' + v_common + v_right

        # Đáp án đúng
        da_correct = 'S' + v_common

        # Tạo danh sách các phương án sai
        wrong_candidates = [
            'S' + v_left,
            'S' + v_right,
            v_left + v_right,
            v_left + v_common,
            v_common + v_right
        ]

        # Loại bỏ phương án trùng với đáp án đúng
        wrong_candidates = list(set(wrong_candidates))
        if da_correct in wrong_candidates:
            wrong_candidates.remove(da_correct)

        random.shuffle(wrong_candidates)
        das1 = wrong_candidates[0]
        das2 = wrong_candidates[1]
        das3 = wrong_candidates[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $%s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng nào trong các đường thẳng sau?'''
                         %(p_name, p1_str, p2_str))

        # Các đáp án
        da_d = ('\\True $%s$' %(da_correct))
        da_s1 = ('$%s$' %(das1))
        da_s2 = ('$%s$' %(das2))
        da_s3 = ('$%s$' %(das3))

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Hai mặt phẳng $(%s)$ và $(%s)$ có hai điểm chung phân biệt là $S$ và $%s$.\\\\
    Hai mặt phẳng $(%s)$ và $(%s)$ cắt nhau theo giao tuyến là đường thẳng đi qua hai điểm chung đó.\\\\
    Do đó, giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng $%s$.'''
                   %(p1_str, p2_str, v_common, p1_str, p2_str, p1_str, p2_str, da_correct))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

