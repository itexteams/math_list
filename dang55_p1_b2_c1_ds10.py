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


def bt_dang55_p1_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các giá trị ngẫu nhiên hợp lý cho sơ đồ Venn 3 tập hợp
                nABC = random.randint(2, 6)
                nA_only_B = random.randint(3, 7)
                nB_only_C = random.randint(3, 7)
                nC_only_A = random.randint(3, 7)

                nAB = nA_only_B + nABC
                nBC = nB_only_C + nABC
                nCA = nC_only_A + nABC

                nA_only = random.randint(2, 7)
                nB_only = random.randint(2, 7)
                nC_only = random.randint(2, 7)

                nA = nA_only + nAB + nCA - nABC
                nB = nB_only + nAB + nBC - nABC
                nC = nC_only + nBC + nCA - nABC

                union_abc = nA_only + nB_only + nC_only + nA_only_B + nB_only_C + nC_only_A + nABC
                no_opinion = random.randint(5, 12)
                total = union_abc + no_opinion

                sum_part = nA + nB + nC - nAB - nBC - nCA

                # Đáp án đúng
                du = ['$%s$'%(latex(nABC))]
                da = random.choice(du)

                # Tạo các phương án nhiễu không trùng với đáp án đúng
                s_options = [nABC + 1, nABC + 2, nABC + 3, nABC - 1, nABC - 2]
                s_options = [x for x in s_options if x > 0 and x != nABC]
                random.shuffle(s_options)

                s = []
                for val in s_options[:3]:
                    s.append('$%s$'%(latex(val)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trước kì bầu cử bí thư lớp 10A, cô giáo chủ nhiệm có cuộc thăm dò tín nhiệm của $%s$ bạn đối với ba ứng cử viên $A, B, C$ và có kết quả như sau: số bạn có tín nhiệm với ứng cử viên: $A$ là $%s$, $B$ là $%s$, $C$ là $%s$, $A$ và $B$ là $%s$, $B$ và $C$ là $%s$, $C$ và $A$ là $%s$, số học sinh không có ý kiến là $%s$. Hỏi số bạn tín nhiệm cả ba bạn $A, B, C$ là bao nhiêu?'''
                                %(latex(total), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nBC), latex(nCA), latex(no_opinion)))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $A, B, C$ lần lượt là tập hợp các học sinh tín nhiệm ứng cử viên $A, B, C$. \\\\
            Số học sinh tín nhiệm ít nhất một trong ba ứng cử viên là: \\\\
            $%s - %s = %s$ (học sinh). \\\\
            Theo nguyên lí bao hàm - loại trừ, ta có: \\\\
            $|A \\cup B \\cup C| = |A| + |B| + |C| - |A \\cap B| - |B \\cap C| - |C \\cap A| + |A \\cap B \\cap C|$ \\\\
            Thay các số liệu đã biết vào công thức trên, ta được: \\\\
            $%s = %s + %s + %s - %s - %s - %s + |A \\cap B \\cap C|$ \\\\
            $\\Leftrightarrow %s = %s + |A \\cap B \\cap C|$ \\\\
            $\\Leftrightarrow |A \\cap B \\cap C| = %s - %s = %s$ (học sinh). \\\\
            Vậy số bạn tín nhiệm cả ba bạn $A, B, C$ là $%s$ bạn.'''
                %(latex(total), latex(no_opinion), latex(union_abc),
                  latex(union_abc), latex(nA), latex(nB), latex(nC), latex(nAB), latex(nBC), latex(nCA),
                  latex(union_abc), latex(sum_part),
                  latex(union_abc), latex(sum_part), latex(nABC), latex(nABC)))

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

