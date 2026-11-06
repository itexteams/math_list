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


def bt_dang24_p2_b1_c4_ds10(self):
            # Khai báo biến
            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN ---
            start_year = random.choice([1990, 1995, 2000])
            years = [start_year + i for i in range(8)] + [start_year + 9] # Ví dụ: 1995-2004 (bỏ 1 năm ở cuối cho giống đề)
            val = random.randint(150, 250)
            incomes = []
            for i in range(len(years)):
                incomes.append(val)
                val += random.randint(10, 50) # Đảm bảo thu nhập tăng dần

            # Tạo bảng dữ liệu bằng Tabular cho phần nội dung
            table_str = "\\begin{center}\n\\begin{tabular}{|l|" + "c|"*len(years) + "}\n\\hline\n"
            table_str += "Năm & " + " & ".join(map(str, years)) + " \\\\ \\hline\n"
            table_str += "TNBQĐN (USD) & " + " & ".join(map(str, incomes)) + " \\\\ \\hline\n"
            table_str += "\\end{tabular}\n\\end{center}"

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = "Cho bảng mô tả thu nhập bình quân đầu người của nước ta qua các năm:\n" + table_str

            # --- BƯỚC 3: CÁC ĐÁP ÁN (ĐÚNG/SAI) ---

            # Nhận biết (a)
            nb_da_d = '\\True Mỗi năm chỉ tương ứng với đúng một giá trị thu nhập bình quân đầu người nên tương ứng đó xác định một hàm số'
            nb_da_s = 'Mỗi năm tương ứng với nhiều giá trị thu nhập bình quân đầu người nên đây không phải là một hàm số'
            list_nb = [nb_da_d, nb_da_s]
            nb_ans = random.choice(list_nb)
            nb_sol = "Vì với mỗi giá trị của đối số (năm) ta xác định được duy nhất một giá trị tương ứng của hàm số (thu nhập) nên tương ứng này là một hàm số."

            # Thông hiểu (b) - Tập xác định
            years_set = "{" + ",".join(map(str, years)) + "}"
            th_da_d = '\\True Tập hợp các năm (tập xác định) là $\\mathscr{D} = ' + years_set + '$'
            th_da_s = 'Tập hợp các năm (tập xác định) là $\\mathscr{D} = \\mathbb{R}$'
            list_th = [th_da_d, th_da_s]
            th_ans = random.choice(list_th)
            th_sol = "Tập xác định của hàm số là tập hợp tất cả các giá trị của biến số năm, tức là $\\mathscr{D} = " + years_set + "$."

            # Vận dụng (c) - Tra cứu giá trị
            idx = 5 # Lấy năm thứ 6 trong danh sách
            target_year = years[idx]
            target_val = incomes[idx]
            vd_da_d = '\\True Thu nhập bình quân đầu người của nước ta năm ' + str(target_year) + ' là ' + str(target_val) + ' USD'
            vd_da_s = 'Thu nhập bình quân đầu người của nước ta năm ' + str(target_year) + ' là ' + str(target_val + 10) + ' USD'
            list_vd = [vd_da_d, vd_da_s]
            vd_ans = random.choice(list_vd)
            vd_sol = "Dựa vào bảng số liệu, tại cột năm " + str(target_year) + ", giá trị thu nhập tương ứng là " + str(target_val) + " USD."

            # Vận dụng cao (d) - Tính đơn điệu
            vdc_da_d = '\\True Hàm số trên là hàm số tăng (hàm số đồng biến)'
            vdc_da_s = '\\True Hàm số trên là hàm số giảm (hàm số nghịch biến)' # Giả định sai về logic nhưng cấu trúc vẫn để chọn
            # Chỉnh lại logic cho vdc để có đúng/sai rõ ràng
            vdc_list = [
                '\\True Vì giá trị thu nhập tăng dần theo thời gian nên hàm số trên là hàm số tăng.',
                'Hàm số trên không phải là hàm số tăng vì có giá trị thu nhập giảm ở một số năm.'
            ]
            vdc_ans = random.choice(vdc_list)
            vdc_sol = "Quan sát bảng số liệu từ trái sang phải, ta thấy các giá trị của thu nhập bình quân đầu người luôn tăng dần theo các năm, do đó đây là hàm số tăng."

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                noidungcauhoi + '\n' +
                '\\choiceTFn \n'
                '{' + nb_ans + '}\n'
                '{' + th_ans + '}\n'
                '{' + vd_ans + '}\n'
                '{' + vdc_ans + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + nb_sol + '\n'
                '\\item ' + th_sol + '\n'
                '\\item ' + vd_sol + '\n'
                '\\item ' + vdc_sol + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

