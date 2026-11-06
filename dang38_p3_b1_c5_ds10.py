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


def bt_dang38_p3_b1_c5_ds10(self):
            # Khai báo biến
            # Random số lượng phần tử của tập A (từ 0 đến n_max)
            n_max = random.choice([5, 6, 7])
            A = list(range(n_max + 1))
            set_A_str = "\\left\\{0, 1, 2, \\dots, %s\\right\\}" % n_max if n_max > 6 else "\\left\\{" + ", ".join(map(str, A)) + "\\right\\}"

            # Tìm các tập con có 4 phần tử có tổng chia hết cho 3
            subsets = list(itertools.combinations(A, 4))
            valid_subsets = [s for s in subsets if sum(s) % 3 == 0]

            # Phân loại tập con có chứa số 0 và không chứa số 0
            has_zero = [list(s) for s in valid_subsets if 0 in s]
            no_zero = [list(s) for s in valid_subsets if 0 not in s]

            count_has_zero = len(has_zero)
            count_no_zero = len(no_zero)

            # Tính toán kết quả
            # Nếu có số 0: 3 cách chọn vị trí hàng nghìn, 3! cách chọn các vị trí còn lại => 3 * 3! = 18 số (hoặc 4! - 3!)
            # Nếu không có số 0: 4! cách chọn => 24 số
            kq_val = count_has_zero * (math.factorial(4) - math.factorial(3)) + count_no_zero * math.factorial(4)

            # Chuẩn bị chuỗi liệt kê các tập con để đưa vào lời giải
            def format_subset(s):
                return "\\left\\{" + ",".join(map(str, sorted(s))) + "\\right\\}"

            all_subsets_str = ", ".join([format_subset(s) for s in valid_subsets])

            # B4: Điều chỉnh các phương án sai
            kq = str(kq_val).replace('.', ',')
            s = set()
            while len(s) < 3:
                sai = kq_val + random.choice([-20, -10, -6, 6, 10, 12, 18, 24])
                if sai > 0 and sai != kq_val:
                    s.add("$%s$" % str(sai).replace('.', ','))

            list_sai = list(s)
            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # B2: Viết nội dung câu hỏi và lời giải theo mẫu
            noidungcauhoi = ('''Cho tập hợp số: $A = %s$. Hỏi có thể thành lập bao nhiêu số có $4$ chữ số khác nhau và chia hết cho $3$?'''
                             % (set_A_str))

            # Nội dung lời giải chi tiết
            loigiai = ('''Ta có một số chia hết cho $3$ khi và chỉ khi tổng các chữ số chia hết cho $3$. \\\\
            Trong tập $A$ có các tập con gồm $4$ chữ số có tổng chia hết cho $3$ là: $%s$. \\\\
            - Với mỗi tập con có chứa chữ số $0$ (có $%s$ tập), số các số tự nhiên có $4$ chữ số khác nhau được lập là: $%s \\cdot \\left(4! - 3!\\right) = %s$ số. \\\\
            - Với mỗi tập con không chứa chữ số $0$ (có $%s$ tập), số các số tự nhiên có $4$ chữ số khác nhau được lập là: $%s \\cdot 4! = %s$ số. \\\\
            Vậy số các số cần lập là: $%s + %s = %s$ số.'''
                       % (all_subsets_str, 
                          latex(count_has_zero), latex(count_has_zero), latex(count_has_zero * 18),
                          latex(count_no_zero), latex(count_no_zero), latex(count_no_zero * 24),
                          latex(count_has_zero * 18), latex(count_no_zero * 24), latex(kq_val)))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))

            # Đáp án đúng
            da_d = ('\\True $%s$' % kq)
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng content
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

