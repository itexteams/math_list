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


def bt_dang36_p1_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Khởi tạo ngẫu nhiên các đối tượng cho bài toán liên quan đến định lý P => Q
        # Danh sách các bộ định lý tương tự để random đề bài
        cac_dinh_ly = [
            {
                "p": "một tam giác có một góc bằng $90^\\circ$",
                "q": "tam giác đó là tam giác vuông",
                "p_viet_hoa": "Một tam giác có một góc bằng $90^\\circ$",
                "q_viet_hoa": "Tam giác đó là tam giác vuông"
            },
            {
                "p": "một tứ giác có bốn cạnh bằng nhau",
                "q": "tứ giác đó là hình thoi",
                "p_viet_hoa": "Một tứ giác có bốn cạnh bằng nhau",
                "q_viet_hoa": "Tứ giác đó là hình thoi"
            },
            {
                "p": "một tam giác có ba cạnh bằng nhau",
                "q": "tam giác đó là tam giác đều",
                "p_viet_hoa": "Một tam giác có ba cạnh bằng nhau",
                "q_viet_hoa": "Tam giác đó là tam giác đều"
            }
        ]

        # Chọn ngẫu nhiên một định lý làm đề bài
        dt = random.choice(cac_dinh_ly)
        str_p = dt["p"]
        str_q = dt["q"]
        str_p_vh = dt["p_viet_hoa"]
        str_q_vh = dt["q_viet_hoa"]

        # Đáp án đúng: Q là điều kiện đủ để có P (hoặc phát biểu tương đương của định lý đảo)
        # Định lý gốc: Nếu P thì Q. Định lý đảo: Nếu Q thì P (tức là Q là điều kiện đủ để có P)
        da = "%s là điều kiện đủ để %s" % (str_q_vh, str_p)
        da_d = ('\\True ' + str(da))

        # Các phương án sai
        s = [
            "%s là điều kiện cần và đủ để %s" % (str_q_vh, str_p),
            "%s khi và chỉ khi %s" % (str_p_vh, str_q),
            "%s là điều kiện đủ để %s" % (str_p_vh, str_q),
            "%s là điều kiện cần để %s" % (str_q_vh, str_p)
        ]

        # Lấy ngẫu nhiên các phương án sai và đảm bảo không trùng với đáp án đúng
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Phát biểu định lý đảo của định lý \"Nếu %s thì %s\" là'''
                            % (str_p, str_q))

        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Định lý gốc có dạng $P \\Rightarrow Q$ với: \\\\
                    $P$: \"%s\" \\\\
                    $Q$: \"%s\". \\\\
                    Định lý đảo của định lý trên là $Q \\Rightarrow P$: \"Nếu %s thì %s\". \\\\
                    Phát biểu dưới dạng điều kiện cần và đủ: %s là điều kiện đủ để %s.'''
                    % (str_p, str_q, str_q, str_p, str_q_vh, str_p))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

