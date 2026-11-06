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


def bt_dang22_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm bổ trợ để chuyển dấu . thành dấu , cho số thập phân
            def format_v(n):
                # Chuyển về float, loại bỏ .0 nếu là số nguyên, sau đó replace . thành ,
                val = float(n)
                if val.is_integer():
                    return str(int(val))
                return str(val).replace('.', ',')

            # ========================================================================
            # B1 & B3: NGHIÊN CỨU ĐỀ BÀI VÀ THIẾT LẬP RANDOM
            # ========================================================================

            pW_pt = random.choice([55, 60, 65, 70, 75, 80])
            dW_pt = random.randint(2, 5)
            dY_pt = random.randint(1, 4)

            pW = Rational(pW_pt, 100)           
            pY = 1 - pW                         
            pY_pt = int(pY * 100)

            dW = Rational(dW_pt, 100)           
            dY = Rational(dY_pt, 100)           

            pB_given_W = 1 - dW                 
            pB_given_Y = 1 - dY                 

            pB = pW * pB_given_W + pY * pB_given_Y

            # ========================================================================
            # B2: VIẾT LẠI THEO MẪU CODE PYTHON (Đã đổi dấu thập phân)
            # ========================================================================

            noidungcauhoi = ('''Bạn Hoàng Huy chọn ngẫu nhiên một bóng đèn led trên quầy. Trên quầy có hai loại đèn màu trắng và màu vàng có hình thức và kích thước như nhau. Trong đó màu trắng chiếm %s\\%%. Bóng đèn màu trắng có tỉ lệ hỏng là %s\\%%, bóng đèn màu vàng có tỉ lệ hỏng là %s\\%%. Xác suất để Huy chọn được''' 
                             % (pW_pt, dW_pt, dY_pt))

            # ------------------------------------------------------------------------
            # Nhận biết
            # ------------------------------------------------------------------------
            nb_da_1_d = '\\True Một bóng đèn màu vàng là %s' % (format_v(pY))
            nb_da_1_s = 'Một bóng đèn màu vàng là %s' % (format_v(pW)) 
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Bóng màu trắng chiếm %s\\%% nên bóng đèn màu vàng chiếm %s\\%%. Vậy xác suất để lấy được bóng đèn vàng là %s.''' 
                            % (pW_pt, pY_pt, format_v(pY)))

            # ------------------------------------------------------------------------
            # Thông hiểu
            # ------------------------------------------------------------------------
            th_da_1_d = '\\True Một bóng đèn không hỏng, biết nó màu trắng là %s' % (format_v(pB_given_W))
            th_da_1_s = 'Một bóng đèn không hỏng, biết nó màu trắng là %s' % (format_v(dW)) 
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Xét hai biến cố\\\\
            A: "lấy được bóng đèn màu trắng".\\\\
            B: "lấy được bóng đèn không hỏng".\\\\
            Khi đó $P(B | A) = 1 - %s\\%% = %s$.''' 
                            % (dW_pt, format_v(pB_given_W)))

            # ------------------------------------------------------------------------
            # Vận dụng
            # ------------------------------------------------------------------------
            vd_da_1_d = '\\True Một bóng đèn không hỏng, biết nó màu vàng là %s' % (format_v(pB_given_Y))
            vd_da_1_s = 'Một bóng đèn không hỏng, biết nó màu vàng là %s' % (format_v(1 - pB_given_Y + Rational(1, 100)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ta có $P(B | \\overline{A}) = 1 - %s\\%% = %s$.''' 
                            % (dY_pt, format_v(pB_given_Y)))

            # ------------------------------------------------------------------------
            # Vận dụng cao
            # ------------------------------------------------------------------------
            vdc_da_1_d = '\\True Một bóng đèn không hỏng là %s' % (format_v(pB))
            vdc_da_1_s = 'Một bóng đèn không hỏng là %s' % (format_v(pB - Rational(5, 1000)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $P(B) = P(A).P(B | A) + P(\\overline{A}).P(B | \\overline{A}) = %s.%s + %s.%s = %s$.''' 
                             % (format_v(pW), format_v(pB_given_W), format_v(pY), format_v(pB_given_Y), format_v(pB)))

            # ========================================================================
            # LẶP ĐỂ ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3
            # ========================================================================

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất nội dung (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_nb_2[0]) + '\n'
                '\\item ' + str(list_th_2[0]) + '\n'
                '\\item ' + str(list_vd_2[0]) + '\n'
                '\\item ' + str(list_vdc_2[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

