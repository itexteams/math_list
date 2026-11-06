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


def bt_dang15_p1_b5_c1_hh11(self):
    # Hàm định dạng số hiển thị dấu phẩy thập phân
    def fmt(val):
        if isinstance(val, (int, Integer)):
            return str(val)
        f_val = float(val)
        if f_val.is_integer():
            return str(int(f_val))
        return str(f_val).replace('.', ',')

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random các thông số độ dài của hình thang và hình chiếu
        bo_so = [
            (3, 7, 4.5, 10.5, 31.5),
            (3, 5, 4.2, 7.0, 21.0),
            (2, 5, 3.2, 8.0, 16.0),
            (3, 4, 4.5, 6.0, 18.0),
            (4, 6, 3.6, 5.4, 21.6),
            (2, 3, 2.6, 3.9, 7.8),
            (4, 5, 3.2, 4.0, 16.0),
            (2, 7, 3.4, 11.9, 23.8)
        ]
        val_AB, val_CD, val_ApBp, val_x, val_tich = random.choice(bo_so)

        s_AB = fmt(val_AB)
        s_CD = fmt(val_CD)
        s_ApBp = fmt(val_ApBp)
        s_x = fmt(val_x)
        s_tich = fmt(val_tich)

        # Các đáp án trắc nghiệm (không có dấu chấm ở cuối các phương án)
        da = '$%s$' % s_x

        # Nhiễu các phương án sai
        sai_1 = fmt(val_x - 1)
        sai_2 = fmt(val_x - 0.5)
        sai_3 = fmt(val_x + 0.5)
        sai_4 = fmt(val_x + 1)
        sai_5 = fmt(val_x + 1.5)

        s = [
            '$%s$' % sai_1,
            '$%s$' % sai_2,
            '$%s$' % sai_3,
            '$%s$' % sai_4,
            '$%s$' % sai_5
        ]
        s = list(set([item for item in s if item != da]))

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi (bỏ hình vẽ)
        noidungcauhoi = ('''Hình thang $ABCD$ có $AB // CD$. Một phép chiếu song song biến nó thành hình thang $A'B'C'D'$. Biết $AB=%s$, $CD=%s$, $A'B'=%s$ và $C'D'=x$. Giá trị của $x$ là'''
                         % (s_AB, s_CD, s_ApBp))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết (viết lại phân số ở dạng \\dfrac{}{})
        loigiai = ('''Vì $AB // CD$, phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng nằm trên hai đường thẳng song song. Do đó\\\\
    $\\dfrac{AB}{CD} = \\dfrac{A'B'}{C'D'} = \\dfrac{%s}{%s}$\\\\
    Suy ra $\\dfrac{%s}{%s} = \\dfrac{%s}{x}$, nên $%sx = %s$ và $x = %s$.'''
                   % (s_AB, s_CD, s_AB, s_CD, s_ApBp, s_AB, s_tich, s_x))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

