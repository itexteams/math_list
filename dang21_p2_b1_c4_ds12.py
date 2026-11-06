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


def bt_dang21_p2_b1_c4_ds12(self):
            # Khai báo biến
            # ================= Khai báo biến số ngẫu nhiên =================
            n_milk = random.randint(10, 15) * 10  
            n_tpcn = random.randint(5, 9) * 10    
            total = n_milk + n_tpcn

            std_milk = random.randint(n_milk // 2 + 10, n_milk - 10)
            std_tpcn = random.randint(n_tpcn // 2 + 5, n_tpcn - 5)

            # Các giá trị tính toán
            p_milk_rational = Rational(n_milk, total)
            p_as_val = round(float(std_milk / total), 2)
            p_cond_rational = Rational(std_milk, n_milk)
            p_cond_float = round(float(std_milk / n_milk), 4)

            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thập phân
            def format_decimal(value):
                return str(value).replace('.', ',')

            # Chuyển đổi các giá trị thập phân sang định dạng VN
            p_as_str = format_decimal(p_as_val)
            p_cond_str = format_decimal(p_cond_float)
            p_wrong_str = format_decimal(round(std_tpcn/total, 2))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gần đây, cơ quan chức năng đã phát hiện một lượng lớn sản phẩm sữa và thực phẩm chức năng giả trên thị trường. Một siêu thị đã kiểm tra chất lượng của %s sản phẩm gồm %s hộp sữa và %s hộp thực phẩm chức năng. Qua kiểm tra có %s hộp sữa đạt chuẩn an toàn thực phẩm và %s hộp thực phẩm chức năng đạt an toàn thực phẩm. Một người chọn ngẫu nhiên một sản phẩm trong %s sản phẩm kiểm tra.''' 
                             %(latex(total), latex(n_milk), latex(n_tpcn), latex(std_milk), latex(std_tpcn), latex(total)))

            ########################################################################
            # a) Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Xác suất chọn được sản phẩm là sữa bằng $%s$' % (latex(p_milk_rational))
            nb_da_1_s = 'Xác suất chọn được sản phẩm là sữa bằng $%s$' % (latex(Rational(n_tpcn, total)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $S$ là biến cố chọn được sản phẩm là hộp sữa. \\\\ Xác suất chọn được sản phẩm là sữa: $P(S) = \\frac{%s}{%s} = %s$.''' 
                            % (latex(n_milk), latex(total), latex(p_milk_rational)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Số sản phẩm sữa đạt chuẩn an toàn là %s sản phẩm' % (latex(std_milk))
            th_da_1_s = 'Số sản phẩm sữa đạt chuẩn an toàn là %s sản phẩm' % (latex(std_tpcn))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Dựa vào dữ kiện đề bài, số sản phẩm sữa đạt chuẩn an toàn là %s sản phẩm.''' % (latex(std_milk)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Xác suất chọn được sản phẩm là sữa và đạt an toàn thực phẩm bằng %s' % (p_as_str)
            vd_da_1_s = 'Xác suất chọn được sản phẩm là sữa và đạt an toàn thực phẩm bằng %s' % (p_wrong_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Gọi $A$ là biến cố chọn được sữa và đạt an toàn thực phẩm. \\\\ Ta có $P(A) = \\frac{%s}{%s} = %s$ và $P(S) = \\frac{%s}{%s} = %s$. \\\\ $A \\cap S$ là biến cố chọn được sản phẩm là sữa và đạt an toàn thực phẩm. \\\\ $P(AS) = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$.''' 
                            % (latex(std_milk), latex(n_milk), latex(p_cond_rational), 
                               latex(n_milk), latex(total), latex(p_milk_rational),
                               latex(n_milk), latex(total), latex(std_milk), latex(n_milk), p_as_str))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True Biết sản phẩm được chọn là sữa, xác suất sản phẩm đó an toàn thực phẩm bằng $%s$' % (latex(p_cond_rational))
            vdc_da_1_s = 'Biết sản phẩm được chọn là sữa, xác suất sản phẩm đó an toàn thực phẩm bằng 0,7' 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gọi $S$ là biến cố sản phẩm được chọn là sữa. $A$ là biến cố sản phẩm được chọn đạt an toàn. \\\\ $P(A|S) = \\frac{P(AS)}{P(S)} = \\frac{%s}{%s} = %s \\approx %s$.''' 
                             % (p_as_str, latex(p_milk_rational), latex(p_cond_rational), p_cond_str))
            list_vdc_2 = [loigiai_vdc_1]

            # ================= Logic trộn =================

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Đóng gói kết quả (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_nb_2[0]) + '\n'
                '\\item ' + str(list_th_2[0]) + '\n'
                '\\item ' + str(list_vd_2[0]) + '\n'
                '\\item ' + str(list_vdc_2[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

