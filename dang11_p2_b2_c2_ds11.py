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


def bt_dang11_p2_b2_c2_ds11(self):
    # Khai báo biến
    P = randint(80, 110) * 10
    d_val = randint(4, 6) * 10

    u1 = P
    u2 = P - d_val
    u2_sai = u2 + randint(1, 3) * 10

    d_true = -d_val
    d_false = d_val

    k3 = 3
    price_k3 = P - k3 * d_val
    T3 = price_k3 - randint(1, 3) * 10

    half_P = P / 2
    if half_P.is_integer():
        half_P_str = str(int(half_P))
    else:
        half_P_str = str(half_P).replace('.', ',')

    val_n = (P - half_P) / d_val
    if val_n.is_integer():
        val_n_str = str(int(val_n))
    else:
        val_n_str = str(round(val_n, 2)).replace('.', ',')

    N_min = math.floor(val_n) + 1
    N_sai = N_min - randint(1, 2)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Giá của một chiếc xe ô tô lúc mới mua là %s triệu đồng. Cứ sau mỗi năm sử dụng, giá của chiếc xe ô tô giảm %s triệu đồng. Gọi $u_1 = %s$ và $u_{n+1}$ là giá của chiếc ô tô sau $n$ năm sử dụng ($n \\ge 1$).'''
                     % (latex(P), latex(d_val), latex(P)))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Giá của chiếc ô tô sau $1$ năm sử dụng là $%s$ triệu đồng' % (latex(u2))
    nb_da_1_s = 'Giá của chiếc ô tô sau $1$ năm sử dụng là $%s$ triệu đồng' % (latex(u2_sai))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    if '\\True' in nb_da_1:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2)))
    else:
        loigiai_nb_1 = ('''Giá của chiếc ô tô sau $1$ năm sử dụng là $u_2 = u_1 - %s = %s - %s = %s \\ne %s$ (triệu đồng).'''
                        % (latex(d_val), latex(P), latex(d_val), latex(u2), latex(u2_sai)))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Dãy số $(u_n)$ là cấp số cộng với công sai $d = %s$' % (latex(d_true))
    th_da_1_s = 'Dãy số $(u_n)$ là cấp số cộng với công sai $d = %s$' % (latex(d_false))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    if '\\True' in th_da_1:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó dãy số $(u_n)$ là một cấp số cộng với công sai $d = -%s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val)))
    else:
        loigiai_th_1 = ('''Vì giá của chiếc ô tô mỗi năm giảm %s triệu đồng nên $u_{n+1} - u_n = -%s$, do đó công sai của cấp số cộng là $d = -%s \\ne %s$.'''
                        % (latex(d_val), latex(d_val), latex(d_val), latex(d_false)))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giá của chiếc ô tô sau %s năm sử dụng lớn hơn %s triệu đồng' % (latex(k3), latex(T3))
    vd_da_1_s = 'Giá của chiếc ô tô sau %s năm sử dụng nhỏ hơn %s triệu đồng' % (latex(k3), latex(T3))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    if '\\True' in vd_da_1:
        loigiai_vd_1 = ('''Giá của chiếc ô tô sau %s năm sử dụng là $u_{%s} = u_1 - %s \\cdot %s = %s - %s = %s$ (triệu đồng). \\\\
