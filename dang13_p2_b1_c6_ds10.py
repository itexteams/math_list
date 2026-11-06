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


def bt_dang13_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo các ký hiệu (nếu cần)
            x = symbols('x')

            # Nội dung câu hỏi gốc
            noidungcauhoi = "Gieo hai con xúc xắc cân đối và đồng chất."

            ########################################################################
            # Nhận biết - Mệnh đề (a): Hiệu số chấm bằng 2
            ########################################################################
            val_a_true = 8
            val_a_false = random.choice([6, 10, 12])

            nb_da_1_d = '\\True "Số chấm xuất hiện trên hai con xúc xắc hơn kém nhau 2 chấm" bằng %s' % (val_a_true)
            nb_da_1_s = '"Số chấm xuất hiện trên hai con xúc xắc hơn kém nhau 2 chấm" bằng %s' % (val_a_false)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = ("""Các cặp kết quả có hiệu số chấm bằng 2 là: $\\left\\{ (1;3), (2;4), (3;5), (4;6), (3;1), (4;2), (5;3), (6;4) \\right\\}$. Có tất cả 8 kết quả.""" )

            ########################################################################
            # Thông hiểu - Mệnh đề (b): Tích số chấm chia hết cho 5
            ########################################################################
            val_b_true = 11
            val_b_false = 12 # Giống trong ảnh đề bài

            th_da_1_d = '\\True "Tích số chấm xuất hiện trên hai con xúc xắc chia hết cho 5" bằng %s' % (val_b_true)
            th_da_1_s = '"Tích số chấm xuất hiện trên hai con xúc xắc chia hết cho 5" bằng %s' % (val_b_false)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ("""Để tích số chấm chia hết cho 5 thì ít nhất một con xúc xắc phải xuất hiện mặt 5 chấm. \\\\
            Các trường hợp gồm: $\\left\\{ (5;1), (5;2), (5;3), (5;4), (5;5), (5;6), (1;5), (2;5), (3;5), (4;5), (6;5) \\right\\}$. \\\\
            Tổng cộng có $6 + 6 - 1 = 11$ kết quả.""" )

            ########################################################################
            # Vận dụng - Mệnh đề (c): Tích số chấm là số lẻ
            ########################################################################
            val_c_true = 9
            val_c_false = random.choice([8, 10, 18])

            vd_da_1_d = '\\True "Tích số chấm xuất hiện trên hai con xúc xắc là một số lẻ" bằng %s' % (val_c_true)
            vd_da_1_s = '"Tích số chấm xuất hiện trên hai con xúc xắc là một số lẻ" bằng %s' % (val_c_false)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = ("""Để tích hai số là số lẻ thì cả hai con xúc xắc đều phải xuất hiện mặt lẻ chấm $\\left\\{ 1, 3, 5 \\right\\}$. \\\\
            Số kết quả là $3 \\times 3 = 9$ kết quả.""" )

            ########################################################################
            # Vận dụng cao - Mệnh đề (d): Tổng số chấm là số chẵn
            ########################################################################
            val_d_true = 18
            val_d_false = 15 # Giống trong ảnh đề bài

            vdc_da_1_d = '\\True "Tổng số chấm xuất hiện trên hai con xúc xắc là số chẵn" bằng %s' % (val_d_true)
            vdc_da_1_s = '"Tổng số chấm xuất hiện trên hai con xúc xắc là số chẵn" bằng %s' % (val_d_false)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = ("""Tổng số chấm là số chẵn khi cả hai con xúc xắc cùng lẻ hoặc cùng chẵn. \\\\
            - Trường hợp cùng lẻ: $3 \\times 3 = 9$ kết quả. \\\\
            - Trường hợp cùng chẵn: $3 \\times 3 = 9$ kết quả. \\\\
            Tổng cộng có $9 + 9 = 18$ kết quả.""" )

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán danh sách kết quả cuối cùng
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

