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


def bt_dang44_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random chỉ số k cho công thức u_k = (u_1 + u_{2k-1})/2
                k = randint(4, 8)
                k2_minus_1 = 2 * k - 1

                # Random chỉ số M cho tổng S_M
                M = randint(10, 20)
                M_minus_1 = M - 1

                # Khẳng định đúng 1
                dung_1 = 'u_{%s} = \\frac{u_1 + u_{%s}}{2}' % (latex(k), latex(k2_minus_1))

                # Khẳng định đúng 2
                dung_2 = 'u_n = u_{n-1} + d, n \\ge 2'

                # Khẳng định đúng 3
                dung_3 = 'u_n = u_1 + (n-1)d, \\forall n \\in \\mathbb{N}^*'

                # Khẳng định sai (đáp án đúng của câu hỏi)
                sai = 'S_{%s} = \\frac{n}{2}(2u_1 + %sd)' % (latex(M), latex(M_minus_1))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho dãy số vô hạn $(u_n)$ là cấp số cộng có công sai $d$, số hạng đầu $u_1$. Hãy chọn khẳng định sai?''')

                # Các đáp án
                da_d = ('\\True $' + str(sai) + '$')
                da_s1 = ('$' + str(dung_1) + '$')
                da_s2 = ('$' + str(dung_2) + '$')
                da_s3 = ('$' + str(dung_3) + '$')

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''+ Theo định nghĩa cấp số cộng, ta có $u_n = u_{n-1} + d$ với mọi $n \\ge 2$. Do đó khẳng định "$%s$" là khẳng định đúng. \\\\
            + Số hạng tổng quát của cấp số cộng là $u_n = u_1 + (n - 1)d$ với mọi $n \\in \\mathbb{N}^*$. Do đó khẳng định "$%s$" là khẳng định đúng. \\\\
            + Ta có $u_1 + u_{%s} = u_1 + u_1 + %sd = 2u_1 + %sd = 2(u_1 + %sd) = 2u_{%s} \\Rightarrow u_{%s} = \\frac{u_1 + u_{%s}}{2}$. Do đó khẳng định "$%s$" là khẳng định đúng. \\\\
            + Công thức tính tổng %s số hạng đầu của cấp số cộng là $S_{%s} = \\frac{%s}{2}(2u_1 + %sd)$. Do đó khẳng định "$%s$" là khẳng định sai. \\\\
            Vậy khẳng định sai là $S_{%s} = \\frac{n}{2}(2u_1 + %sd)$.'''
                           % (dung_2,
                              dung_3,
                              latex(k2_minus_1), latex(k2_minus_1 - 1), latex(k2_minus_1 - 1), latex(k - 1), latex(k), latex(k), latex(k2_minus_1), dung_1,
                              latex(M), latex(M), latex(M), latex(M_minus_1), sai,
                              latex(M), latex(M_minus_1)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

