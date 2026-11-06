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


def bt_dang25_p1_b1_c3_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Lặp để đảm bảo sai số tương đối của 2 người không bằng nhau
        while True:
            L_A = random.choice([200, 250, 300, 400, 500])
            e_A = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])

            L_B = random.choice([10, 12, 15, 18, 20, 25, 30])
            e_B = random.choice([0.1, 0.2])

            # Tính sai số tương đối (dạng số thập phân)
            r_A_val = e_A / L_A
            r_B_val = e_B / L_B

            # Chuyển sang phần trăm và làm tròn 2-4 chữ số
            r_A_pct = round(r_A_val * 100, 4)
            r_B_pct = round(r_B_val * 100, 4)

            if r_A_pct != r_B_pct:
                break

        # Xác định người đo chính xác hơn
        if r_A_pct < r_B_pct:
            winner = "A"
            loser = "B"
            win_err_pct = r_A_pct
        else:
            winner = "B"
            loser = "A"
            win_err_pct = r_B_pct

        # Hàm định dạng số, đổi dấu phẩy
        def fmt(num):
            if num == int(num):
                return str(int(num))
            # Làm tròn tối đa 4 chữ số thập phân để tránh chuỗi quá dài
            return str(round(num, 4)).rstrip('0').rstrip('.').replace('.', ',')

        str_L_A = fmt(L_A)
        str_e_A = fmt(e_A)
        str_L_B = fmt(L_B)
        str_e_B = fmt(e_B)
        str_win_err_pct = fmt(win_err_pct)

        # Tính sai số cho đáp án nhiễu
        wrong_err_pct = round(win_err_pct + random.choice([0.02, 0.03, -0.01, 0.05]), 4)
        if wrong_err_pct <= 0:
            wrong_err_pct = win_err_pct + 0.04
        str_wrong_err_pct = fmt(wrong_err_pct)

        # Câu hỏi
        noidungcauhoi = ('Bạn A đo chiều dài của một sân bóng ghi được $%s \\pm %sm$. Bạn B đo chiều cao của một cột cờ được $%s \\pm %sm$. Trong 2 bạn A và B, bạn nào có phép đo chính xác hơn và sai số tương đối trong phép đo của bạn đó là bao nhiêu?' 
                         % (str_L_A, str_e_A, str_L_B, str_e_B))

        # Các đáp án trắc nghiệm
        da = 'Bạn %s đo chính xác hơn bạn %s với sai số tương đối là $%s\\%%$' % (winner, loser, str_win_err_pct)
        das1 = 'Bạn %s đo chính xác hơn bạn %s với sai số tương đối là $%s\\%%$' % (loser, winner, str_win_err_pct)
        das2 = 'Hai bạn đo chính xác như nhau với sai số tương đối bằng nhau là $%s\\%%$' % (str_win_err_pct)
        das3 = 'Bạn %s đo chính xác hơn bạn %s với sai số tương đối là $%s\\%%$' % (winner, loser, str_wrong_err_pct)

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        dau_ss = "<" if r_A_pct < r_B_pct else ">"
        loigiai = ('Phép đo của bạn A có sai số tương đối $\\delta_1 \\le \\frac{%s}{%s} = %s = %s\\%%$\\\\ \n'
                   'Phép đo của bạn B có sai số tương đối $\\delta_2 \\le \\frac{%s}{%s} = %s = %s\\%%$\\\\ \n'
                   'Vì $%s\\%% %s %s\\%%$ nên phép đo của bạn %s có độ chính xác cao hơn.'
                   % (str_e_A, str_L_A, fmt(round(r_A_val, 6)), fmt(r_A_pct),
                      str_e_B, str_L_B, fmt(round(r_B_val, 6)), fmt(r_B_pct),
                      fmt(r_A_pct), dau_ss, fmt(r_B_pct), winner))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

