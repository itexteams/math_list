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


def bt_dang48_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random vị trí k và giá trị số hạng đầu u1
                k = randint(3, 7)
                u1 = randint(2, 6)

                # Từ đẳng thức 4S_n = S_{2n} ta luôn suy ra d = 2*u1
                d = 2 * u1

                # Tính u_k theo công thức u_k = u1 + (k - 1)*d
                uk = u1 * (2 * k - 1)

                # Biến tính toán phục vụ lời giải
                k_minus_1 = k - 1
                two_k_minus_1 = 2 * k - 1

                # Đáp án đúng
                da_str = 'u_1 = %s; d = %s' % (latex(u1), latex(d))

                # Tạo danh sách phương án sai không trùng với đáp án đúng
                s = set()
                s.add('u_1 = %s; d = %s' % (latex(u1), latex(u1)))
                s.add('u_1 = %s; d = %s' % (latex(u1), latex(d - 1)))
                s.add('u_1 = %s; d = %s' % (latex(u1), latex(d + 1)))
                s.add('u_1 = %s; d = %s' % (latex(u1 + 1), latex(d)))
                s.add('u_1 = %s; d = %s' % (latex(u1 + 1), latex(u1)))
                s.add('u_1 = %s; d = %s' % (latex(d), latex(u1)))

                s.discard(da_str)

                s_list = list(s)
                random.shuffle(s_list)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho cấp số cộng $(u_n)$ biết $u_{%s} = %s$ và $4S_n = S_{2n}$. Số hạng đầu tiên $u_1$ và công sai $d$ của cấp số cộng là'''
                                 % (latex(k), latex(uk)))

                # Định dạng các phương án trả lời
                da_d = ('\\True $%s$' % (da_str))
                da_s1 = ('$%s$' % (das1))
                da_s2 = ('$%s$' % (das2))
                da_s3 = ('$%s$' % (das3))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Ta có $S_n = \\frac{n}{2}[2u_1 + (n-1)d]$ và $S_{2n} = \\frac{2n}{2}[2u_1 + (2n-1)d] = n[2u_1 + (2n-1)d]$. \\\\
            Theo đề bài, ta có: \\\\
            $4S_n = S_{2n} \\Leftrightarrow 4 \\cdot \\frac{n}{2}[2u_1 + (n-1)d] = n[2u_1 + (2n-1)d]$ \\\\
            $\\Leftrightarrow 2[2u_1 + (n-1)d] = 2u_1 + (2n-1)d$ \\\\
            $\\Leftrightarrow 4u_1 + 2nd - 2d = 2u_1 + 2nd - d$ \\\\
            $\\Leftrightarrow 2u_1 = d \\Leftrightarrow d = 2u_1$. \\\\
            Mặt khác, $u_{%s} = u_1 + %sd = %s$. Thay $d = 2u_1$ vào, ta được: \\\\
            $u_1 + %s \\cdot (2u_1) = %s \\Leftrightarrow %su_1 = %s \\Leftrightarrow u_1 = %s$. \\\\
            Suy ra $d = 2 \\cdot %s = %s$. \\\\
            Vậy $u_1 = %s; d = %s$.'''
                           % (latex(k), latex(k_minus_1), latex(uk),
                              latex(k_minus_1), latex(uk), latex(two_k_minus_1), latex(uk), latex(u1),
                              latex(u1), latex(d),
                              latex(u1), latex(d)))

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

