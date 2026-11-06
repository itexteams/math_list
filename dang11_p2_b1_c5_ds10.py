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


def bt_dang11_p2_b1_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến số để có thể mở rộng (ví dụ đổi thành số có 4 chữ số hoặc 5 chữ số)
            k = 5 
            chu_so = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            # Các giá trị tính toán đúng
            val_total = 9 * (10**(k-1))
            val_distinct = 9 * math.perm(9, k-1)
            val_odd_distinct = 5 * 8 * math.perm(8, k-2)
            val_even_distinct = val_distinct - val_odd_distinct

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho số tự nhiên $\\overline{abcde}$ với $a,b,c,d,e$ là các số lấy từ tập $\\{0;1;2;3;4;5;6;7;8;9\\}$.''')

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Có %s số' % (val_total)
            nb_da_1_s = 'Có 100000 số' # Giá trị sai như trong ảnh
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số tự nhiên có %s chữ số $\\overline{abcde}$ ($a \\neq 0$).\\\\
            - Chữ số $a$ có 9 cách chọn ($a \\in \\{1; 2; \\dots; 9\\}$).\\\\
            - Các chữ số $b, c, d, e$ mỗi vị trí có 10 cách chọn.\\\\
            Vậy có $9 \\cdot 10^4 = %s$ số.''' % (k, val_total))

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Có %s số mà các chữ số $a,b,c,d,e$ đôi một khác nhau' % (val_distinct)
            th_da_1_s = 'Có 30240 số mà các chữ số $a,b,c,d,e$ đôi một khác nhau' 
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Các chữ số đôi một khác nhau:\\\\
            - $a$ có 9 cách chọn ($a \\neq 0$).\\\\
            - $b$ có 9 cách chọn ($b \\neq a$).\\\\
            - $c$ có 8 cách chọn.\\\\
            - $d$ có 7 cách chọn.\\\\
            - $e$ có 6 cách chọn.\\\\
            Vậy có $9 \\cdot 9 \\cdot 8 \\cdot 7 \\cdot 6 = %s$ số.''' % (val_distinct))

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = '\\True Có %s số mà các chữ số $a,b,c,d,e$ đôi một khác nhau và số tự nhiên đó là số lẻ' % (val_odd_distinct)
            vd_da_1_s = 'Có 15120 số mà các chữ số $a,b,c,d,e$ đôi một khác nhau và số tự nhiên đó là số lẻ'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số lẻ và các chữ số đôi một khác nhau:\\\\
            - $e \\in \\{1; 3; 5; 7; 9\\} \\Rightarrow$ có 5 cách chọn.\\\\
            - $a \\neq 0$ và $a \\neq e \\Rightarrow$ có 8 cách chọn.\\\\
            - Ba vị trí còn lại $b, c, d$ là chỉnh hợp chập 3 của 8 chữ số còn lại: $A_8^3 = 336$ cách.\\\\
            Vậy có $5 \\cdot 8 \\cdot 336 = %s$ số.''' % (val_odd_distinct))

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = '\\True Có %s số mà các chữ số $a,b,c,d,e$ đôi một khác nhau và số tự nhiên đó chẵn' % (val_even_distinct)
            vdc_da_1_s = 'Có 12000 số mà các chữ số $a,b,c,d,e$ đôi một khác nhau và số tự nhiên đó chẵn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Số chẵn và các chữ số đôi một khác nhau:\\\\
            Ta lấy tổng số các số có 5 chữ số đôi một khác nhau trừ đi các số lẻ có 5 chữ số đôi một khác nhau:\\\\
            $%s - %s = %s$ số.''' % (val_distinct, val_odd_distinct, val_even_distinct))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 đáp án đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

