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


def bt_dang27_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển đổi dấu . thành , cho số thập phân
            def v(val):
                # Sử dụng định dạng 'g' để loại bỏ các số 0 thừa ở cuối và thay dấu chấm bằng dấu phẩy
                s = format(float(val), 'g')
                return s.replace('.', ',')

            # --- BƯỚC 1: KHỞI TẠO CÁC GIÁ TRỊ NGẪU NHIÊN ---
            p_nu_val = random.randint(40, 55) 
            p_dh_nu_val = random.randint(25, 40) 
            p_dh_nam_val = random.randint(20, 35) 

            p_nu = Rational(p_nu_val, 100)
            p_nam = 1 - p_nu
            p_dh_tren_nu = Rational(p_dh_nu_val, 100)
            p_dh_tren_nam = Rational(p_dh_nam_val, 100)

            p_nu_dh = p_nu * p_dh_tren_nu
            p_nu_khong_dh = p_nu * (1 - p_dh_tren_nu)
            p_nam_dh = p_nam * p_dh_tren_nam
            p_nam_khong_dh = p_nam * (1 - p_dh_tren_nam)

            p_dh_chung = p_nu_dh + p_nam_dh
            p_khong_dh_chung = 1 - p_dh_chung
            p_khac_gioi = 2 * p_nu * p_nam
            p_dung_1_dh = 2 * p_dh_chung * p_khong_dh_chung

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một doanh nghiệp có $%s\\%%$ nhân viên là nữ. Trong các nhân viên nữ có $%s\\%%$ nhân viên có bằng đại học, tỉ lệ này trong các nhân viên nam là $%s\\%%$.''' 
                             %(p_nu_val, p_dh_nu_val, p_dh_nam_val))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Tỉ lệ nhân viên nam trong tổng số nhân viên là %s\\%%' %(v(p_nam*100))
            nb_da_1_s = 'Tỉ lệ nhân viên nam trong tổng số nhân viên là %s\\%%' %(v(p_nu*100))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố "Nhân viên được chọn là nữ".\\\\ Theo giả thiết, ta có $P(A) = %s\\%% = %s$.\\\\ Khi đó, tỉ lệ nhân viên nam trong tổng số nhân viên là $100\\%% - %s\\%% = %s\\%%$ hay $P(\\overline{A}) = %s$.''' 
                            %(p_nu_val, v(p_nu), p_nu_val, v(p_nam*100), v(p_nam)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Tỉ lệ nhân viên nữ không có bằng đại học trong tổng số nhân viên là %s\\%%' %(v(p_nu_khong_dh*100))
            th_da_1_s = 'Tỉ lệ nhân viên nữ không có bằng đại học trong tổng số nhân viên là %s\\%%' %(v(p_nu_dh*100))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $B$ là biến cố "Nhân viên được chọn có bằng đại học".\\\\ Vì trong các nhân viên nữ có $%s\\%%$ nhân viên có bằng đại học nên $P(B|A) = %s$.\\\\ Tỉ lệ này trong các nhân viên nam là $%s\\%%$, tức là $P(B|\\overline{A}) = %s$.\\\\ Mặt khác $P(AB) = P(B|A) \\cdot P(A) = %s \\cdot %s = %s = %s\\%%$.\\\\ Mà $AB$ là biến cố "Nhân viên nữ có bằng đại học" nên tỉ lệ nhân viên nữ không có bằng đại học trong tổng số nhân viên là $%s\\%% - %s\\%% = %s\\%%$.''' 
                            %(p_dh_nu_val, v(p_dh_tren_nu), p_dh_nam_val, v(p_dh_tren_nam), v(p_dh_tren_nu), v(p_nu), v(p_nu_dh), v(p_nu_dh*100), p_nu_val, v(p_nu_dh*100), v(p_nu_khong_dh*100)))

            ########################################################################
            # Vận dụng ############################################
            nguong_c = round(float(p_khac_gioi*100) - 5, 1)
            vd_da_1_d = '\\True Chọn ngẫu nhiên hai nhân viên, xác suất chọn được hai người khác giới lớn hơn %s\\%%' %(v(nguong_c))
            vd_da_1_s = 'Chọn ngẫu nhiên hai nhân viên, xác suất chọn được hai người khác giới nhỏ hơn %s\\%%' %(v(nguong_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất chọn người thứ nhất là nữ và người thứ hai là nam là $%s \\cdot %s = %s$.\\\\ Xác suất chọn người thứ nhất là nam và người thứ hai là nữ là $%s \\cdot %s = %s$.\\\\ Xác suất để chọn được hai người khác giới là $%s + %s = %s = %s\\%%$.\\\\ Vậy tỉ lệ này lớn hơn %s\\%%.''' 
                            %(v(p_nu), v(p_nam), v(p_nu*p_nam), v(p_nam), v(p_nu), v(p_nu*p_nam), v(p_nu*p_nam), v(p_nu*p_nam), v(p_khac_gioi), v(p_khac_gioi*100), v(nguong_c)))

            ########################################################################
            # Vận dụng cao ############################################
            nguong_d = round(float(p_dung_1_dh*100) / 2, 1)
            vdc_da_1_d = '\\True Chọn ngẫu nhiên hai nhân viên, xác suất để trong hai người có đúng một người có bằng đại học lớn hơn %s\\%%' %(v(nguong_d))
            vdc_da_1_s = 'Chọn ngẫu nhiên hai nhân viên, xác suất để trong hai người có đúng một người có bằng đại học nhỏ hơn %s\\%%' %(v(nguong_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xác suất chọn một người có bằng đại học là \\\\ $P(B) = P(A)P(B|A) + P(\\overline{A})P(B|\\overline{A}) = %s + %s = %s$.\\\\ Xác suất chọn một người không có bằng đại học là $1 - %s = %s$.\\\\ Xét các trường hợp chọn 2 người có đúng 1 người có bằng đại học:\\\\ TH1: Người thứ nhất có bằng ĐH, người thứ hai không: $%s \\cdot %s = %s$.\\\\ TH2: Người thứ nhất không có bằng ĐH, người thứ hai có: $%s \\cdot %s = %s$.\\\\ Tổng xác suất là $%s + %s = %s = %s\\%% > %s\\%%$.''' 
                             %(v(p_nu_dh), v(p_nam_dh), v(p_dh_chung), v(p_dh_chung), v(p_khong_dh_chung), v(p_dh_chung), v(p_khong_dh_chung), v(p_dh_chung*p_khong_dh_chung), v(p_khong_dh_chung), v(p_dh_chung), v(p_dh_chung*p_khong_dh_chung), v(p_dh_chung*p_khong_dh_chung), v(p_dh_chung*p_khong_dh_chung), v(p_dung_1_dh), v(p_dung_1_dh*100), v(nguong_d)))

            # --- BƯỚC XỬ LÝ ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # --- XUẤT NỘI DUNG THEO MẪU ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

