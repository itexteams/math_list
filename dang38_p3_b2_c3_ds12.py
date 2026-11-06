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


def bt_dang38_p3_b2_c3_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng bài tích phân trục căn thức ở mẫu:

        k = randint(1, 5) # Hệ số nhân ở tử số



        a_val = 17 * k
        b_val = -9 * k
        t_val = a_val + b_val # T = a + b = 8*k

        # Chuỗi hiển thị tử số
        if k == 1:
            tu_so = "x"
            tu_so_bien_doi = "x"
        else:
            tu_so = "%d x" % k
            tu_so_bien_doi = "%d x" % k

        # Hiển thị b\sqrt{3} trong đề
        str_b_term = "+ b\\sqrt{3}"

        # Số cần hiển thị đáp án
        kq_str = str(t_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Biết tích phân $\\int\\limits_{0}^{1} \\frac{%s}{\\sqrt{3x + 1} + \\sqrt{2x + 1}} \\,\\mathrm{d}x = \\frac{a + b\\sqrt{3}}{9}$ với $a, b$ là các số nguyên. Tổng $T = a + b$ bằng bao nhiêu?'''
                         % (tu_so))

        # Nội dung lời giải
        if k == 1:
            he_so_k = ""
        else:
            he_so_k = "%d \\cdot " % k

        loigiai = ('''Nhân cả tử và mẫu của biểu thức dưới dấu tích phân với lượng liên hợp $\\sqrt{3x + 1} - \\sqrt{2x + 1}$, ta được: \\\\
                   $\\frac{%s}{\\sqrt{3x + 1} + \\sqrt{2x + 1}} = \\frac{%s\\left(\\sqrt{3x + 1} - \\sqrt{2x + 1}\\right)}{(3x + 1) - (2x + 1)} = %s\\left(\\sqrt{3x + 1} - \\sqrt{2x + 1}\\right)$. \\\\
                   Khi đó: \\\\
                   $I = %s\\int\\limits_{0}^{1} \\left(\\sqrt{3x + 1} - \\sqrt{2x + 1}\\right) \\,\\mathrm{d}x$ \\\\
                   $\\phantom{I} = %s\\left.\\left[\\frac{2}{9}(3x + 1)^{\\frac{3}{2}} - \\frac{1}{3}(2x + 1)^{\\frac{3}{2}}\\right]\\right|_{0}^{1}$ \\\\
                   $\\phantom{I} = %s\\left[\\left(\\frac{2}{9} \\cdot 8 - \\frac{1}{3} \\cdot 3\\sqrt{3}\\right) - \\left(\\frac{2}{9} - \\frac{1}{3}\\right)\\right]$ \\\\
                   $\\phantom{I} = %s\\left(\\frac{14}{9} - \\sqrt{3} + \\frac{1}{9}\\right)$ \\\\
                   $\\phantom{I} = %s\\left(\\frac{17 - 9\\sqrt{3}}{9}\\right) = \\frac{%d - %d\\sqrt{3}}{9}$. \\\\
                   Đối chiếu với giả thiết $\\frac{a + b\\sqrt{3}}{9}$, ta suy ra: \\\\
                   $a = %d$, $b = %d$. \\\\
                   Vậy $T = a + b = %d + (%d) = %d$.'''
                   % (tu_so, tu_so_bien_doi, he_so_k,
                      he_so_k,
                      he_so_k,
                      he_so_k,
                      he_so_k,
                      he_so_k, a_val, abs(b_val),
                      a_val, b_val,
                      a_val, b_val, t_val))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

