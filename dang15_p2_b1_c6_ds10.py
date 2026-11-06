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


def bt_dang15_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            x = symbols('x')

            # --- NGẪU NHIÊN HÓA THÔNG SỐ BÀI TOÁN ---
            khong_gian_mau = 12

            # 1. Random điều kiện cho câu (b) - Biến cố A
            loai_b = random.choice(['chẵn', 'lẻ'])
            if loai_b == 'chẵn':
                ds_b = ['(S, 2)', '(S, 4)', '(S, 6)']
            else:
                ds_b = ['(S, 1)', '(S, 3)', '(S, 5)']
            str_b = "; ".join(ds_b)

            # 2. Random điều kiện cho câu (c) - Biến cố B
            loai_c = random.choice(['chẵn', 'lẻ'])
            if loai_c == 'chẵn':
                ds_c = ['(N, 2)', '(N, 4)', '(N, 6)']
            else:
                ds_c = ['(N, 1)', '(N, 3)', '(N, 5)']
            str_c = "; ".join(ds_c)

            # 3. Random số chấm cho câu (d) - Biến cố C
            so_cham_d = random.randint(1, 6)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Gieo một đồng xu sau đó gieo một con xúc xắc. Quan sát sự xuất hiện mặt sấp $(S)$, mặt ngửa $(N)$ của đồng xu và số chấm xuất hiện của con xúc xắc.''')

            ########################################################################
            # (a) Nhận biết - Không gian mẫu
            ########################################################################
            sai_a = random.choice([8, 10, 14, 16])
            nb_da_1_d = '\\True Số phần tử không gian mẫu bằng ' + str(khong_gian_mau)
            nb_da_1_s = 'Số phần tử không gian mẫu bằng ' + str(sai_a)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Không gian mẫu của phép thử là \\\\ $\\Omega = \\{(S, 1); (S, 2); (S, 3); (S, 4); (S, 5); (S, 6); (N, 1); (N, 2); (N, 3); (N, 4); (N, 5); (N, 6)\\}$. \\\\ Số phần tử của không gian mẫu là $n(\\Omega) = 2 \\cdot 6 = 12$.''')

            ########################################################################
            # (b) Thông hiểu - Biến cố A
            ########################################################################
            sai_b = random.choice([1, 2, 4, 5])
            cau_hoi_b = 'Số phần tử của biến cố $A$: "Đồng xu xuất hiện mặt sấp và con xúc xắc xuất hiện mặt có số chấm ' + loai_b + '" bằng '
            th_da_1_d = '\\True ' + cau_hoi_b + '3'
            th_da_1_s = cau_hoi_b + str(sai_b)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Biến cố $A = \\{%s\\}$. \\\\ Vậy số phần tử của biến cố $A$ là $n(A) = 3$.''' % str_b)

            ########################################################################
            # (c) Vận dụng - Biến cố B
            ########################################################################
            sai_c = random.choice([1, 2, 4, 5])
            cau_hoi_c = 'Số phần tử của biến cố $B$: "Mặt ngửa của đồng xu và mặt có số chấm ' + loai_c + ' của con xúc xắc xuất hiện" bằng '
            vd_da_1_d = '\\True ' + cau_hoi_c + '3'
            vd_da_1_s = cau_hoi_c + str(sai_c)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Biến cố $B = \\{%s\\}$. \\\\ Vậy số phần tử của biến cố $B$ là $n(B) = 3$.''' % str_c)

            ########################################################################
            # (d) Vận dụng cao - Biến cố C
            ########################################################################
            sai_d = random.choice([1, 3, 4])
            cau_hoi_d = 'Số phần tử của biến cố $C$: "Mặt ' + str(so_cham_d) + ' chấm xuất hiện" bằng '
            vdc_da_1_d = '\\True ' + cau_hoi_d + '2'
            vdc_da_1_s = cau_hoi_d + str(sai_d)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Kết quả thuận lợi cho biến cố $C$ là $\\{(S, %s); (N, %s)\\}$. \\\\ Vậy số phần tử của biến cố $C$ là $n(C) = 2$.''' % (str(so_cham_d), str(so_cham_d)))

            # --- KIỂM TRA SỐ CÂU ĐÚNG (1-3) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # --- XUẤT NỘI DUNG (KHÔNG DÙNG r-string) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

