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


def bt_dang10_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Yêu cầu tính S = a + b

            x0 = random.randint(-10, 10)
            y0 = random.randint(-10, 10)

            # Để a, b thuộc N* (số nguyên dương) theo yêu cầu đề bài
            a_val = random.randint(1, 15)
            b_val = random.randint(1, 15)

            # Đáp án đúng
            ket_qua = a_val + b_val

            # ==========================================================
            # B4: Tạo các phương án sai (không trùng đáp án đúng)
            # ==========================================================
            s = set()
            while len(s) < 3:
                sai = ket_qua + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                if sai != ket_qua and sai > 0:
                    s.add(sai)

            wrong_list = list(s)

            # ==========================================================
            # B2: Viết nội dung câu hỏi và lời giải (theo mẫu)
            # ==========================================================

            # Câu hỏi
            noidungcauhoi = (
                'Đường thẳng $d$ đi qua điểm $M(' + str(x0) + ';' + str(y0) + ')$ và có vectơ chỉ phương '
                '$\\vec{u} = (' + str(a_val) + ';' + str(b_val) + ')$ có phương trình tham số là: '
                '$d: \\begin{cases} x = ' + str(x0) + ' + at \\\\ y = ' + str(y0) + ' + bt \\end{cases}; a, b \\in \\mathbb{N}^*$. '
                'Tính $a + b$.'
            )

            # Các đáp án
            da_d = ('\\True $' + str(ket_qua) + '$')
            da_s1 = ('$' + str(wrong_list[0]) + '$')
            da_s2 = ('$' + str(wrong_list[1]) + '$')
            da_s3 = ('$' + str(wrong_list[2]) + '$')

            # Trộn đáp án
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            loigiai = (
                'Đường thẳng $d$ đi qua điểm $M(' + str(x0) + ';' + str(y0) + ')$ và có vectơ chỉ phương '
                '$\\vec{u} = (' + str(a_val) + ';' + str(b_val) + ')$ nên phương trình tham số của đường thẳng $d$ có dạng: '
                '\\begin{center} '
                '$d: \\begin{cases} x = ' + str(x0) + ' + ' + str(a_val) + 't \\\\ y = ' + str(y0) + ' + ' + str(b_val) + 't \\end{cases}$ '
                '\\end{center} '
                'Đối chiếu với phương trình đề bài cho: $d: \\begin{cases} x = ' + str(x0) + ' + at \\\\ y = ' + str(y0) + ' + bt \\end{cases}$, '
                'ta xác định được $a = ' + str(a_val) + '$ và $b = ' + str(b_val) + '$. '
                'Vì $a, b \\in \\mathbb{N}^*$ nên các giá trị này thỏa mãn điều kiện đề bài. \\\\ '
                'Vậy $a + b = ' + str(a_val) + ' + ' + str(b_val) + ' = ' + str(ket_qua) + '$.'
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(ket_qua))

            # ==========================================================
            # Xuất nội dung theo cấu trúc yêu cầu (không dùng tiền tố r)
            # ==========================================================
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content 

