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


def bt_dang38_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thập phân
            def format_decimal(value):
                return str(value).replace('.', ',')

            # --- BƯỚC 1: NGHIÊN CỨU VÀ RANDOM THÔNG SỐ ---
            # p_trang: % bóng màu trắng, p_xanh: % bóng màu xanh
            p_trang = random.choice([60, 65, 70, 75])
            p_xanh = 100 - p_trang

            # ti_le_hong_trang: % hỏng của bóng trắng, ti_le_hong_xanh: % hỏng của bóng xanh
            tl_hong_trang = random.choice([2, 3, 4])
            tl_hong_xanh = random.choice([3, 5, 6])

            # Tính toán các giá trị xác suất
            pa = p_trang / 100
            pa_ngang = p_xanh / 100
            pb_a_ngang = tl_hong_trang / 100 # P(B_|A)
            pb_a = 1 - pb_a_ngang # P(B|A)
            pb_not_a_ngang = tl_hong_xanh / 100 # P(B_|\bar{A})
            pb_not_a = 1 - pb_not_a_ngang # P(B|\bar{A})

            # Xác suất toàn phần P(B)
            p_b = pa * pb_a + pa_ngang * pb_not_a

            # Chuyển sang định dạng chuỗi có dấu phẩy
            str_pa = format_decimal(pa)
            str_pa_ngang = format_decimal(pa_ngang)
            str_pb_a_ngang = format_decimal(pb_a_ngang)
            str_pb_a = format_decimal(round(pb_a, 4))
            str_pb_not_a_ngang = format_decimal(pb_not_a_ngang)
            str_pb_not_a = format_decimal(round(pb_not_a, 4))
            str_pb = format_decimal(round(p_b, 4))

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Một cửa hàng bán hai loại bóng đèn, trong đó có %s\\%% bóng đèn là màu trắng và %s\\%% bóng đèn là màu xanh, "
                "các bóng đèn có kích thước như nhau. Các bóng đèn màu trắng có tỉ lệ hỏng là %s\\%% và các bóng đèn màu xanh "
                "có tỉ lệ hỏng là %s\\%%. Một khách hàng chọn mua ngẫu nhiên 1 bóng đèn từ cửa hàng đó. Xét các biến cố:\\\\"
                "$A$: “Khách hàng chọn được bóng màu trắng”;\\\\"
                "$B$: “Khách hàng chọn được bóng không hỏng”."
                % (p_trang, p_xanh, tl_hong_trang, tl_hong_xanh)
            )

            # --- BƯỚC 3: CÁC PHẦN NHẬN BIẾT, THÔNG HIỂU, VẬN DỤNG, VDC ---

            # --- Nhận biết: P(A ngang) ---
            nb_da_1_d = "\\True $P(\\overline{A}) = %s$" % str_pa_ngang
            nb_da_1_s = "$P(\\overline{A}) = %s$" % str_pa
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = "Ta có $P(A) = %s$ nên $P(\\overline{A}) = 1 - %s = %s$." % (str_pa, str_pa, str_pa_ngang)

            # --- Thông hiểu: P(B|A) ---
            th_da_1_d = "\\True $P(B|A) = %s$" % str_pb_a
            th_da_1_s = "$P(B|A) = %s$" % str_pb_a_ngang
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (
                "Vì các bóng đèn màu trắng có tỉ lệ hỏng là %s\\%% nên $P(\\overline{B}|A) = %s$.\\\\ "
                "Suy ra $P(B|A) = 1 - P(\\overline{B}|A) = 1 - %s = %s$." 
                % (tl_hong_trang, str_pb_a_ngang, str_pb_a_ngang, str_pb_a)
            )

            # --- Vận dụng: P(B|A ngang) ---
            vd_da_1_d = "\\True $P(B|\\overline{A}) = %s$" % str_pb_not_a
            vd_da_1_s = "$P(B|\\overline{A}) = 0,3$" # Giữ giá trị sai như trong ảnh hoặc random
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (
                "Vì các bóng đèn màu xanh có tỉ lệ hỏng là %s\\%% nên $P(\\overline{B}|\\overline{A}) = %s$\\\\ "
                "Suy ra $P(B|\\overline{A}) = 1 - P(\\overline{B}|\\overline{A}) = 1 - %s = %s$." 
                % (tl_hong_xanh, str_pb_not_a_ngang, str_pb_not_a_ngang, str_pb_not_a)
            )

            # --- Vận dụng cao: P(B) ---
            vdc_da_1_d = "\\True $P(B) = %s$" % str_pb
            vdc_da_1_s = "$P(B) = 0,95$" 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (
                "Theo công thức xác suất toàn phần ta có:\\\\"
                "$P(B) = P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A}) = %s.%s + %s.%s = %s$."
                % (str_pa, str_pb_a, str_pa_ngang, str_pb_not_a, str_pb)
            )

            # --- LẶP CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán vào list cuối cùng
            shuffled_answers = answers
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT NỘI DUNG (Content) ---
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

