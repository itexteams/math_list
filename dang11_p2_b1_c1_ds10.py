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


def bt_dang11_p2_b1_c1_ds10(self):
    # Khai báo biến
    # Danh sách các số để random
    n = random.choice([7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    # Xác định tính chất để đưa vào lời giải
    is_prime_n = isprime(n)

    # Nội dung câu hỏi
    noidungcauhoi = ('Cho mệnh đề $P$: "$%d$ là số nguyên tố". Các câu sau là đúng hay sai?' % n)

    ########################################################################
    # Nhận biết - Câu a: Phát biểu hợp số
    if is_prime_n:
        nb_da_1_d = '\\True Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ là hợp số"' % n
        nb_da_1_s = 'Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ không là hợp số"' % n
        loigiai_nb_1 = ('Mệnh đề $P$: "$%d$ là số nguyên tố". Phủ định của "là số nguyên tố" trong tập số tự nhiên là "là hợp số" (trừ trường hợp số $1$ và $0$ nhưng với $n=%d$ thì đúng).' % (n, n))
    else:
        nb_da_1_s = '\\True Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ là hợp số"' % n
        nb_da_1_d = 'Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ không là hợp số"' % n
        loigiai_nb_1 = ('Vì $%d$ không là số nguyên tố nên mệnh đề phủ định hợp lý là "$%d$ là hợp số" là sai.' % (n, n))

    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    ########################################################################
    # Thông hiểu - Câu b: Phát biểu "không là..."
    th_da_1_d = '\\True Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ không là số nguyên tố"' % n
    th_da_1_s = 'Mệnh đề phủ định của mệnh đề $P$ là $\\bar{P}$: "$%d$ là số nguyên tố"' % n
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    loigiai_th_1 = ('Mệnh đề phủ định của mệnh đề "$n$ là số nguyên tố" luôn là "$n$ không là số nguyên tố". Vậy khẳng định này là đúng.')

    ########################################################################
    # Vận dụng - Câu c: Xét tính đúng của mệnh đề phủ định
    # Nếu P đúng -> Not P sai. Nếu P sai -> Not P đúng.
    if is_prime_n:
        vd_da_1_s = '\\True Mệnh đề phủ định của mệnh đề $P$ là mệnh đề sai'
        vd_da_1_d = 'Mệnh đề phủ định của mệnh đề $P$ là mệnh đề đúng'
        trang_thai = "đúng"
        ket_luan = "sai"
    else:
        vd_da_1_d = '\\True Mệnh đề phủ định của mệnh đề $P$ là mệnh đề đúng'
        vd_da_1_s = 'Mệnh đề phủ định của mệnh đề $P$ là mệnh đề sai'
        trang_thai = "sai"
        ket_luan = "đúng"

    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    loigiai_vd_1 = ('Mệnh đề $P$: "$%d$ là số nguyên tố" là mệnh đề %s, do đó mệnh đề phủ định của $P$ là mệnh đề %s.' % (n, trang_thai, ket_luan))

    ########################################################################
    # Vận dụng cao - Câu d: Ngược lại với câu c
    if is_prime_n:
        vdc_da_1_s = '\\True Mệnh đề phủ định của mệnh đề $P$ là mệnh đề đúng'
        vdc_da_1_d = 'Mệnh đề phủ định của mệnh đề $P$ là mệnh đề sai'
        trang_thai_vdc = "đúng"
        ket_luan_vdc = "sai"
    else:
        vdc_da_1_d = '\\True Mệnh đề phủ định của mệnh đề $P$ là mệnh đề sai'
        vdc_da_1_s = 'Mệnh đề phủ định của mệnh đề $P$ là mệnh đề đúng'
        trang_thai_vdc = "sai"
        ket_luan_vdc = "đúng"

    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    loigiai_vdc_1 = ('Mệnh đề $P$: "$%d$ là số nguyên tố" là mệnh đề %s, do đó mệnh đề phủ định của $P$ là mệnh đề %s.' % (n, trang_thai_vdc, ket_luan_vdc))

    ########################################################################
    # Logic xử lý
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list để shuffle
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    # Kết hợp
    combined_nb = list(zip(list_nb_1, [loigiai_nb_1]))
    combined_th = list(zip(list_th_1, [loigiai_th_1]))
    combined_vd = list(zip(list_vd_1, [loigiai_vd_1]))
    combined_vdc = list(zip(list_vdc_1, [loigiai_vdc_1]))

    # Xáo trộn
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

