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


def bt_dang63_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên số lượng học sinh ở các vùng độc lập trong biểu đồ Venn
                x_abc = randint(1, 2)     # Số học sinh làm được cả 3 câu
                x_ab = randint(1, 3)      # Số học sinh chỉ làm được câu 1 và câu 2
                x_ac = randint(1, 3)      # Số học sinh chỉ làm được câu 1 và câu 3
                x_bc = randint(0, 2)      # Số học sinh chỉ làm được câu 2 và câu 3
                x_a = randint(2, 5)       # Số học sinh chỉ làm được duy nhất câu 1
                x_b = randint(2, 5)       # Số học sinh chỉ làm được duy nhất câu 2
                x_c = randint(2, 5)       # Số học sinh chỉ làm được duy nhất câu 3

                # Tính toán các dữ kiện tổng hợp cho đề bài
                nA = x_a + x_ab + x_ac + x_abc   # Tổng số học sinh làm được câu 1
                nB = x_b + x_ab + x_bc + x_abc   # Tổng số học sinh làm được câu 2
                nC = x_c + x_ac + x_bc + x_abc   # Tổng số học sinh làm được câu 3

                nAB = x_ab + x_abc               # Số học sinh làm được câu 1 và câu 2
                nAC = x_ac + x_abc               # Số học sinh làm được câu 1 và câu 3
                nBC = x_bc + x_abc               # Số học sinh làm được câu 2 và câu 3

                # Đáp án đúng: Số học sinh chỉ làm được 1 câu
                kq = x_a + x_b + x_c

                # Tạo các phương án trắc nghiệm
                da = '$%s$' % (latex(kq))

                # Tạo danh sách các đáp án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    val = kq + randint(-4, 4)
                    if val != kq and val > 0:
                        s.add('$%s$' % (latex(val)))

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Các em học sinh lớp 10A làm bài thi khảo sát học sinh giỏi môn Toán. Đề thi có 3 câu. Sau khi chấm bài giáo viên tổng kết được như sau: Có $%s$ học sinh làm được câu 1, có $%s$ học sinh làm được câu 2, có $%s$ học sinh làm được câu 3. Có $%s$ học sinh làm được câu 1 và câu 2, có $%s$ học sinh làm được câu 1 và câu 3, có $%s$ học sinh làm được câu 2 và câu 3 và chỉ có $%s$ học sinh làm được cả 3 câu. Hỏi có bao nhiêu học sinh chỉ làm được 1 câu?'''
                                 % (latex(nA), latex(nB), latex(nC), latex(nAB), latex(nAC), latex(nBC), latex(x_abc)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Gọi $A, B, C$ lần lượt là tập hợp các học sinh làm được câu 1, câu 2, câu 3. \\\\
            Số học sinh chỉ làm được câu 1 và câu 2 là: $%s - %s = %s$ học sinh. \\\\
            Số học sinh chỉ làm được câu 1 và câu 3 là: $%s - %s = %s$ học sinh. \\\\
            Số học sinh chỉ làm được câu 2 và câu 3 là: $%s - %s = %s$ học sinh. \\\\
            Số học sinh chỉ làm được đúng câu 1 là: $%s - %s - %s - %s = %s$ học sinh. \\\\
            Số học sinh chỉ làm được đúng câu 2 là: $%s - %s - %s - %s = %s$ học sinh. \\\\
            Số học sinh chỉ làm được đúng câu 3 là: $%s - %s - %s - %s = %s$ học sinh. \\\\
            Vậy số học sinh chỉ làm được đúng 1 câu là: $%s + %s + %s = %s$ học sinh.'''
                           % (latex(nAB), latex(x_abc), latex(x_ab),
                              latex(nAC), latex(x_abc), latex(x_ac),
                              latex(nBC), latex(x_abc), latex(x_bc),
                              latex(nA), latex(x_ab), latex(x_ac), latex(x_abc), latex(x_a),
                              latex(nB), latex(x_ab), latex(x_bc), latex(x_abc), latex(x_b),
                              latex(nC), latex(x_ac), latex(x_bc), latex(x_abc), latex(x_c),
                              latex(x_a), latex(x_b), latex(x_c), latex(kq)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

