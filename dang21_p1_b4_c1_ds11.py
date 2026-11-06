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


def bt_dang21_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo tính ngẫu nhiên cho bài toán
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng gốc từ hình ảnh: tan^2(x) = 3
                m_val = 3
                m_sqrt_latex = '\\sqrt{3}'
                goc_latex = '\\frac{\\pi}{3}'

                da_text = 'x = \\pm\\frac{\\pi}{3} + k\\pi'
                das1 = 'x = \\frac{\\pi}{3} + k\\pi'          # Bẫy thiếu dấu +-
                das2 = 'x = -\\frac{\\pi}{3} + k\\pi'         # Bẫy thiếu dấu +- nhánh âm
                das3 = 'vô nghiệm'                           # Bẫy vô nghiệm giống mẫu

            elif dang == '2':
                # Dạng biến đổi 2: tan^2(x) = 1
                m_val = 1
                m_sqrt_latex = '1'
                goc_latex = '\\frac{\\pi}{4}'

                da_text = 'x = \\pm\\frac{\\pi}{4} + k\\pi'
                das1 = 'x = \\frac{\\pi}{4} + k\\pi'
                das2 = 'x = \\pm\\frac{\\pi}{4} + k2\\pi'        # Bẫy sai chu kỳ
                das3 = 'vô nghiệm'

            else:
                # Dạng biến đổi 3: tan^2(x) = 1/3
                m_val = Rational(1, 3)
                m_sqrt_latex = '\\frac{\\sqrt{3}}{3}'
                goc_latex = '\\frac{\\pi}{6}'

                da_text = 'x = \\pm\\frac{\\pi}{6} + k\\pi'
                das1 = 'x = \\frac{\\pi}{6} + k\\pi'
                das2 = 'x = \\pm\\frac{\\pi}{3} + k\\pi'        # Bẫy nhầm góc
                das3 = 'vô nghiệm'

            # Câu hỏi sử dụng định dạng %s theo đúng mẫu
            noidungcauhoi = ('''Giải phương trình: $\\tan^2 x = %s$ có nghiệm là''' 
                             % (latex(m_val)))

            # Nội dung lời giải chi tiết từng bước, không viết tắt, tuân thủ quy tắc xuống dòng
            loigiai = ('''$\\tan^2 x = %s \\Leftrightarrow \\tan x = \\pm %s \\Leftrightarrow x = \\pm %s + k\\pi, k \\in \\mathbb{Z}$.''' 
                       % (latex(m_val), m_sqrt_latex, goc_latex))

            # Thiết lập đáp án đúng và đáp án sai (Tuyệt đối không chứa dấu chấm ở cuối các phương án)
            da_d = ('\\True $' + str(da_text) + '$' if da_text != 'vô nghiệm' else '\\True vô nghiệm')
            da_s1 = '$' + str(das1) + '$' if das1 != 'vô nghiệm' else 'vô nghiệm'
            da_s2 = '$' + str(das2) + '$' if das2 != 'vô nghiệm' else 'vô nghiệm'
            da_s3 = '$' + str(das3) + '$' if das3 != 'vô nghiệm' else 'vô nghiệm'

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên thứ tự hiển thị
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm định dạng mẫu minipage hoàn chỉnh
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

