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


def bt_dang9_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = sp.symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random giá trị x - a (với a là số nguyên dương từ 1 đến 5)
                a = random.randint(1, 100)

                # Random số mũ (có thể là pi, e, hoặc một số vô tỉ/không nguyên bất kỳ)
                mu_list = [sp.pi, sp.exp(1), sp.Rational(1, 3), sp.sqrt(2)]
                mu = random.choice(mu_list)
                mu_latex = latex(mu)

                # Điều kiện để ln(x-a) > 0 => x-a > 1 => x > a+1
                can_duoi = a + 1

                # Các đáp án
                da_dung = '$(%s; +\\infty)$' % latex(can_duoi)

                # Tạo các đáp án nhiễu
                s = [
                    '$(%s; +\\infty)$' % latex(a),        # Quên điều kiện ln > 0
                    '$(0; +\\infty)$',                    # Đáp án mặc định sai
                    '$\\mathbb{R}$',                      # Đáp án mặc định sai
                    '$(%s; +\\infty)$' % latex(can_duoi + 1),
                    '$(%s; %s)$' % (latex(a), latex(can_duoi))
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Nội dung câu hỏi
                noidungcauhoi = (r'Tìm tập xác định của hàm số $y = [\ln(x - %s)]^{%s}$.'
                                 % (latex(a), mu_latex))

                # Các đáp án trắc nghiệm
                da_d = '\\True ' + da_dung
                da_s1 = das1
                da_s2 = das2
                da_s3 = das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = (r'''Vì số mũ $%s$ không nguyên nên điều kiện xác định là: \\
                           $\begin{cases} \ln(x - %s) > 0 \\ x - %s > 0 \end{cases} \Leftrightarrow \begin{cases} x - %s > 1 \\ x > %s \end{cases} \Leftrightarrow x > %s$. \\
                           Vậy tập xác định là $D = (%s; +\infty)$.'''
                           % (mu_latex, latex(a), latex(a), latex(a), latex(a), latex(can_duoi), latex(can_duoi)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

