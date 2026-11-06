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


def bt_dang6_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            n_khach = 3
            n_toa = 3

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một đoàn tàu nhỏ có %s toa khách đỗ ở sân ga. Có %s hành khách không quen biết cùng bước lên tàu.''' 
                             %(latex(n_toa), latex(n_khach)))

            ########################################################################
            # (a) Số khả năng khách lên tàu tùy ý
            ########################################################################
            tong_so_cach = n_toa**n_khach
            a_sai = 9
            nb_da_1_d = '\\True Số khả năng khách lên tàu tùy ý là %s khả năng' %(latex(tong_so_cach))
            nb_da_1_s = 'Số khả năng khách lên tàu tùy ý là %s khả năng' %(latex(a_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Mỗi hành khách trong số %s người đều có %s cách chọn toa tàu để lên. \\\\ 
                            Theo quy tắc nhân, số khả năng khách lên tàu tùy ý là $%s \\cdot %s \\cdot %s = %s$ khả năng.''' 
                            %(latex(n_khach), latex(n_toa), latex(n_toa), latex(n_toa), latex(n_toa), latex(tong_so_cach)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # (b) Số khả năng 3 hành khách lên cùng một toa
            ########################################################################
            cung_1_toa = n_toa
            b_sai = 1
            th_da_1_d = '\\True Số khả năng %s hành khách lên cùng một toa là %s khả năng' %(latex(n_khach), latex(cung_1_toa))
            th_da_1_s = 'Số khả năng %s hành khách lên cùng một toa là %s khả năng' %(latex(n_khach), latex(b_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Để %s hành khách cùng lên một toa, ta chọn $1$ trong $%s$ toa tàu. \\\\ 
                            Số khả năng là $C_{%s}^1 = %s$ khả năng (cả 3 cùng toa 1, hoặc cùng toa 2, hoặc cùng toa 3).''' 
                            %(latex(n_khach), latex(n_toa), latex(n_toa), latex(cung_1_toa)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # (c) Số khả năng mỗi khách lên một toa
            ########################################################################
            moi_nguoi_1_toa = math.factorial(n_khach)
            c_sai = 3
            vd_da_1_d = '\\True Số khả năng mỗi khách lên một toa là %s khả năng' %(latex(moi_nguoi_1_toa))
            vd_da_1_s = 'Số khả năng mỗi khách lên một toa là %s khả năng' %(latex(c_sai))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Hành khách thứ nhất có %s cách chọn toa. \\\\ 
                            Hành khách thứ hai có %s cách chọn toa (khác toa khách thứ nhất). \\\\ 
                            Hành khách thứ ba có %s cách chọn toa (khác toa của hai khách đầu). \\\\ 
                            Số khả năng là $%s \\cdot %s \\cdot %s = %s$ khả năng.''' 
                            %(latex(n_toa), latex(n_toa-1), latex(n_toa-2), latex(n_toa), latex(n_toa-1), latex(n_toa-2), latex(moi_nguoi_1_toa)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # (d) Số khả năng 2 khách cùng 1 toa, khách thứ 3 toa khác
            ########################################################################
            hai_mot = 18
            d_sai = 12
            vdc_da_1_d = '\\True Số khả năng có 2 hành khách cùng lên một toa, hành khách thứ ba thì lên toa khác là %s' %(latex(hai_mot))
            vdc_da_1_s = 'Số khả năng có 2 hành khách cùng lên một toa, hành khách thứ ba thì lên toa khác là %s' %(latex(d_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Bước 1: Chọn $2$ hành khách trong số $3$ khách để xếp cùng toa có $C_3^2=3$ cách. \\\\ 
                             Bước 2: Chọn toa cho $2$ khách này có $3$ cách. \\\\ 
                             Bước 3: Chọn toa cho hành khách còn lại (phải khác toa trên) có $2$ cách. \\\\ 
                             Vậy số khả năng là $3 \\cdot 3 \\cdot 2 = %s$ khả năng.''' 
                             %(latex(hai_mot)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                answers = [ans_a, ans_b, ans_c, ans_d]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để xuất bản
            shuffled_answers = answers
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

