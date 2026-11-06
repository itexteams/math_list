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


def bt_dang41_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random góc A sao cho công sai d là số nguyên (6d = 360 - 4a -> 360 - 4a chia hết cho 6 -> a chia hết cho 3)
                # Ta chọn góc A hợp lý (từ 15 đến 60 độ)
                a = random.choice([15, 30, 45, 60])

                # Tính công sai d
                d = (360 - 4 * a) // 6

                # Tính các góc còn lại
                b = a + d
                c = a + 2 * d
                e = a + 3 * d

                # Các đáp án trắc nghiệm
                da = '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (b, c, e)

                # Tạo các phương án sai (thay đổi công sai d)
                d1 = d + 5
                d2 = d - 2
                d3 = d + 10
                d4 = d - 5
                d5 = d + 3

                s = [
                    '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (a + d1, a + 2 * d1, a + 3 * d1),
                    '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (a + d2, a + 2 * d2, a + 3 * d2),
                    '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (a + d3, a + 2 * d3, a + 3 * d3),
                    '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (a + d4, a + 2 * d4, a + 3 * d4),
                    '$%s^\\circ ; %s^\\circ ; %s^\\circ$' % (a + d5, a + 2 * d5, a + 3 * d5)
                ]

                random.shuffle(s)
                das1 = s.pop()
                das2 = s.pop()
                das3 = s.pop()

                # Câu hỏi
                noidungcauhoi = ('Cho tứ giác $ABCD$ biết các góc của tứ giác lập thành một cấp số cộng và góc A bằng $%s^\\circ$. Tìm các góc còn lại?'
                                 % (a))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('Gọi số đo các góc $A, B, C, D$ của tứ giác lần lượt là $u_1, u_2, u_3, u_4$ lập thành một cấp số cộng với công sai $d$.\\\\ '
                         'Ta có tổng $4$ góc của tứ giác bằng $360^\\circ$ nên:\\\\ '
                         '$u_1 + u_2 + u_3 + u_4 = 360^\\circ \\Leftrightarrow u_1 + (u_1 + d) + (u_1 + 2d) + (u_1 + 3d) = 360^\\circ \\Leftrightarrow 4u_1 + 6d = 360^\\circ$.\\\\ '
                         'Thay $u_1 = %s^\\circ$ vào phương trình trên ta được:\\\\ '
                         '$4 \\cdot %s + 6d = 360 \\Leftrightarrow 6d = %s \\Leftrightarrow d = %s$.\\\\ '
                         'Vậy các góc còn lại của tứ giác là:\\\\ '
                         '$B = u_1 + d = %s^\\circ + %s^\\circ = %s^\\circ$\\\\ '
                         '$C = u_1 + 2d = %s^\\circ + 2 \\cdot %s^\\circ = %s^\\circ$\\\\ '
                         '$D = u_1 + 3d = %s^\\circ + 3 \\cdot %s^\\circ = %s^\\circ$.'
                         % (a, a, 360 - 4*a, d, a, d, b, a, d, c, a, d, e))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

