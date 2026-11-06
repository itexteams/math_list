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


def bt_dang28_p3_b1_c5_ds10(self):
            # Khai báo biến
            # B3: Suy nghĩ tìm cách random bài toán
            # Ta có thể random giữa việc tìm các chữ số đều 'chẵn' hoặc đều 'lẻ'
            lisdang = ['chẵn', 'lẻ']
            dang = random.choice(lisdang)

            if dang == 'chẵn':
                tập_A = '{0, 2, 4, 6, 8}'
                tập_a_chọn = '{2, 4, 6, 8}'
                n1 = 4  # Số cách chọn a (loại số 0)
                n2 = 5  # Số cách chọn b
                kq_num = n1 * n2
                điều_kiện_a = 'a \\neq 0'
            else:
                tập_A = '{1, 3, 5, 7, 9}'
                tập_a_chọn = '{1, 3, 5, 7, 9}'
                n1 = 5  # Số cách chọn a
                n2 = 5  # Số cách chọn b
                kq_num = n1 * n2
                điều_kiện_a = 'a \\in A' # Vì tập A lẻ không chứa số 0

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            kq = str(kq_num).replace('.', ',')

            # Tạo danh sách các phương án nhiễu
            s_pool = [10, 16, 20, 25, 45, 50, 90, 99]
            if kq_num in s_pool:
                s_pool.remove(kq_num)

            random.shuffle(s_pool)
            das1 = s_pool[0]
            das2 = s_pool[1]
            das3 = s_pool[2]

            # Câu hỏi (B2: Viết lại y hệt nội dung nhưng theo biến số)
            noidungcauhoi = ('''Có bao nhiêu số tự nhiên có hai chữ số mà hai chữ số đều %s?'''
                             % (dang))

            # Các đáp án
            da_d = ('\\True $%s$' % (kq))
            da_s1 = '$%s$' % (str(das1).replace('.', ','))
            da_s2 = '$%s$' % (str(das2).replace('.', ','))
            da_s3 = '$%s$' % (str(das3).replace('.', ','))

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết (B2: Không viết tắt, dùng \left( \right))
            loigiai = ('''Gọi số cần tìm có dạng $\\overline{ab}$ với $\\left( a, b \\right) \\in A = %s$ và $%s$. \\\\
                         Trong đó: \\\\
                         $a$ được chọn từ tập $%s$ nên có $%s$ cách chọn. \\\\
                         $b$ được chọn từ tập $A$ nên có $%s$ cách chọn. \\\\
                         Như vậy, ta có $%s \\times %s = %s$ số cần tìm.'''
                       % (tập_A, điều_kiện_a, tập_a_chọn, latex(n1), latex(n2), latex(n1), latex(n2), kq))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm (Phần content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

