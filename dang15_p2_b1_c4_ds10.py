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


def bt_dang15_p2_b1_c4_ds10(self):
            # Khai báo biến
            # --- BƯỚC 1: KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            ten_thanh_pho = random.choice(["Hà Nội", "TP. Hồ Chí Minh", "Đà Nẵng", "Cần Thơ"])
            nam = 2019

            chi_so = [round(random.uniform(30, 75), 1) for _ in range(12)]
            trung_binh_nam = round(sum(chi_so) / 12, 1)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI (BẢNG TABULAR) ---
            hang_chi_so = " & ".join([str(val).replace('.', ',') for val in chi_so])

            noidungcauhoi = (
                "Bảng dưới đây cho biết chỉ số $PM_{2,5}$ ở thành phố %s từ tháng 1 đến tháng 12 của năm %d.\n"
                "\\begin{center}\n"
                "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}\n"
                "\\hline\n"
                " & Trung bình & \\multicolumn{12}{c|}{Tháng} \\\\ \\cline{3-14}\n"
                " & năm %d & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\\\ \\hline\n"
                "$PM_{2,5}$ ($\\mu g/m^3$) & %s & %s \\\\ \\hline\n"
                "\\end{tabular}\n"
                "\\end{center}"
            ) % (ten_thanh_pho, nam, nam, str(trung_binh_nam).replace('.', ','), hang_chi_so)

            ########################################################################
            # Nhận biết
            ########################################################################
            val_t1 = str(chi_so[0]).replace('.', ',')
            nb_da_1_d = "\\True Từ bảng thống kê, chỉ số $PM_{2,5}$ của tháng 1 là %s ($\\mu g/m^3$)" % val_t1
            nb_da_1_s = "Từ bảng thống kê, chỉ số $PM_{2,5}$ của tháng 1 là %s ($\\mu g/m^3$)" % str(chi_so[1]).replace('.', ',')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = "Dựa vào bảng dữ liệu, tại cột tháng 1, ta dóng xuống hàng chỉ số $PM_{2,5}$ thu được giá trị là %s ($\\mu g/m^3$)." % val_t1

            ########################################################################
            # Thông hiểu
            ########################################################################
            val_t2 = chi_so[1]
            val_t6 = chi_so[5]
            so_sanh = "nhỏ hơn" if val_t2 < val_t6 else "lớn hơn"
            so_sanh_sai = "lớn hơn" if val_t2 < val_t6 else "nhỏ hơn"

            th_da_1_d = "\\True Chỉ số $PM_{2,5}$ trong tháng 2 %s chỉ số $PM_{2,5}$ trong tháng 6" % so_sanh
            th_da_1_s = "Chỉ số $PM_{2,5}$ trong tháng 2 %s chỉ số $PM_{2,5}$ trong tháng 6" % so_sanh_sai
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = "Chỉ số $PM_{2,5}$ tháng 2 là %s và tháng 6 là %s. Vì %s %s %s nên chỉ số tháng 2 %s chỉ số tháng 6." % (
                str(val_t2).replace('.', ','), str(val_t6).replace('.', ','), 
                str(val_t2).replace('.', ','), "<" if val_t2 < val_t6 else ">", str(val_t6).replace('.', ','), so_sanh)

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = "\\True Mỗi tháng chỉ tương ứng với đúng một chỉ số $PM_{2,5}$ nên chỉ số này là hàm số của tháng"
            vd_da_1_s = "Chỉ số $PM_{2,5}$ không phải là hàm số của tháng vì các giá trị có thể trùng nhau"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = "Vì với mỗi giá trị của tháng (từ 1 đến 12), ta luôn xác định được duy nhất một giá trị chỉ số $PM_{2,5}$ tương ứng, nên theo định nghĩa, chỉ số $PM_{2,5}$ là một hàm số của biến số tháng."

            ########################################################################
            # Vận dụng cao
            ########################################################################
            tap_gia_tri = "{" + "; ".join([str(val).replace('.', ',') for val in chi_so]) + "}"
            so_phan_tu = len(set(chi_so))

            vdc_da_1_d = "\\True Tập giá trị của hàm số này có %d phần tử" % so_phan_tu
            vdc_da_1_s = "Tập giá trị của hàm số này có 12 phần tử" if so_phan_tu != 12 else "Tập giá trị của hàm số này có 10 phần tử"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = "Tập giá trị $T$ gồm các giá trị khác nhau xuất hiện trong bảng: \\ $T = %s$. \\ Sau khi loại bỏ các giá trị trùng lặp, ta đếm được tập hợp có %d phần tử." % (tap_gia_tri, so_phan_tu)

            # --- BƯỚC 3: KIỂM TRA ĐIỀU KIỆN ĐÁP ÁN ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG (KHÔNG DÙNG r'...') ---
            content = (
                "\\begin{minipage}{\\textwidth}\n"
                "\\begin{ex}\n" +
                str(noidungcauhoi) + "\n"
                "\\choiceTFn\n"
                "{" + str(d1) + "}\n"
                "{" + str(d2) + "}\n"
                "{" + str(d3) + "}\n"
                "{" + str(d4) + "}\n"
                "\\loigiai{\n"
                "\\begin{enumEX}[a)]{1}\n"
                "\\item " + str(loigiai_nb_1) + "\n"
                "\\item " + str(loigiai_th_1) + "\n"
                "\\item " + str(loigiai_vd_1) + "\n"
                "\\item " + str(loigiai_vdc_1) + "\n"
                "\\end{enumEX}}\n"
                "\\end{ex}\n"
                "\\end{minipage}\n\n")
            return content

