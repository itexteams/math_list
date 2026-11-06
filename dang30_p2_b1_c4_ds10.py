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


def bt_dang30_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Random thông số
            m1 = 8
            m2 = 15
            m3 = 25
            p1, p2, p3, p4 = 6500, 6000, 5500, 5000

            # Nội dung câu hỏi (sử dụng tabular để vẽ bảng)
            noidungcauhoi = r"""Bảng giá cước gọi quốc tế của công ty viễn thông A được cho bởi bảng sau:
            \begin{center}
            \begin{tabular}{|l|c|}
            \hline
            \textbf{Thời gian gọi (phút)} & \textbf{Giá cước điện thoại (đồng/phút)} \\ \hline
            Không quá %s phút & %s \\ \hline
            Từ phút thứ %s đến phút thứ %s & %s \\ \hline
            Từ phút thứ %s đến phút thứ %s & %s \\ \hline
            Từ phút thứ %s trở đi & %s \\ \hline
            \end{tabular}
            \end{center}""" % (m1, p1, m1+1, m2, p2, m2+1, m3, p3, m3+1, p4)

            ########################################################################
            # Nhận biết: Tập xác định
            nb_da_1_d = r'\True Tập xác định của hàm số tính tiền cước là $D = (0; +\infty)$'
            nb_da_1_s = r'Tập xác định của hàm số tính tiền cước là $D = \mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r"Vì thời gian gọi $x$ phải là số dương nên tập xác định là $D = (0; +\infty)$."

            ########################################################################
            # Thông hiểu: Tính mức 1 (VD: 7 phút)
            t1 = 7
            cuoc1 = t1 * p1
            th_da_1_d = r'\True Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t1, cuoc1)
            th_da_1_s = r'Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t1, t1 * p2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r"Vì %s < %s nên số tiền là: $%s \cdot %s = %s$ đồng." % (t1, m1, t1, p1, cuoc1)

            ########################################################################
            # Vận dụng: Tính mức 2 (VD: 9 phút)
            t2 = 9
            # Cách tính: m1 phút đầu giá p1 + (t2 - m1) phút sau giá p2
            cuoc2 = m1 * p1 + (t2 - m1) * p2
            vd_da_1_d = r'\True Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t2, cuoc2)
            vd_da_1_s = r'Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t2, t2 * p2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r"Với cuộc gọi %s phút: %s phút đầu tính giá %s, %s phút sau tính giá %s. Tổng tiền: $%s \cdot %s + %s \cdot %s = %s$ đồng." % (t2, m1, p1, t2-m1, p2, m1, p1, t2-m1, p2, cuoc2)

            ########################################################################
            # Vận dụng cao: Tính mức 2 - trường hợp 12 phút (giống ảnh)
            t3 = 12
            cuoc3 = m1 * p1 + (t3 - m1) * p2
            vdc_da_1_d = r'\True Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t3, cuoc3)
            vdc_da_1_s = r'Số tiền cước phải trả khi gọi %s phút là %s đồng' % (t3, cuoc3 + 1000)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = r"Với cuộc gọi %s phút: %s phút đầu tính giá %s, %s phút tiếp theo tính giá %s. Tổng tiền là: $%s \cdot %s + %s \cdot %s = %s$ đồng." % (t3, m1, p1, t3-m1, p2, m1, p1, t3-m1, p2, cuoc3)

            # Logic chọn đáp án đúng/sai (giữ nguyên cấu trúc mẫu)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_list = [random.choice(list_nb_da_1), random.choice(list_th_da_1), 
                            random.choice(list_vd_da_1), random.choice(list_vdc_da_1)]
                if 1 <= count_true_answers(ans_list) <= 3:
                    shuffled_answers = ans_list
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

