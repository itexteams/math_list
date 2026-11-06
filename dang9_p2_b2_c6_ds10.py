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


def bt_dang9_p2_b2_c6_ds10(self):
            # Khai báo biến
            # ================= B3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN =================
            # Ta sẽ random số lượng nam (m) và nữ (w). 
            m = random.randint(5, 10) # Số nam
            w = random.randint(3, 6)  # Số nữ
            tong = m + w

            # Sử dụng math.comb để tính toán giá trị số (nhanh và chính xác cho số nguyên)
            omega = math.comb(tong, 2)
            chon_2_nam = math.comb(m, 2)
            chon_2_nu = math.comb(w, 2)

            # Dùng Rational của sympy để giữ phân số tối giản cho kết quả
            p_khong_nu = Rational(chon_2_nam, omega)
            p_ca_2_nu = Rational(chon_2_nu, omega)
            p_it_nhat_1_nu = 1 - p_khong_nu

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một tổ có $%s$ nam và $%s$ nữ. Chọn ngẫu nhiên $2$ người.''' 
                             %(latex(m), latex(w)))

            ########################################################################
            # Nhận biết: Số phần tử không gian mẫu #################################
            nb_da_1_d = '\\True Số phần tử của không gian mẫu là $%s$' %(latex(omega))
            nb_da_1_s = 'Số phần tử của không gian mẫu là $%s$' %(latex(omega + random.choice([-5, 5, 2])))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^2 = %s$.''' 
                            %(latex(tong), latex(omega)))

            ########################################################################
            # Thông hiểu: Xác suất không có nữ nào #################################
            th_da_1_d = '\\True Xác suất để không có nữ nào cả bằng $%s$' %(latex(p_khong_nu))
            th_da_1_s = 'Xác suất để không có nữ nào cả bằng $%s$' %(latex(Rational(p_khong_nu.p + 2, p_khong_nu.q)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Để không có nữ nào cả, ta chọn $2$ nam từ $%s$ nam. \\\\
                            Số cách chọn là $n\\left(A\\right) = C_{%s}^2 = %s$. \\\\
                            Xác suất là $P\\left(A\\right) = \\frac{%s}{%s} = %s$.''' 
                            %(latex(m), latex(m), latex(chon_2_nam), latex(chon_2_nam), latex(omega), latex(p_khong_nu)))

            ########################################################################
            # Vận dụng: Xác suất đều là nữ #########################################
            vd_da_1_d = '\\True Xác suất để đều là nữ bằng $%s$' %(latex(p_ca_2_nu))
            vd_da_1_s = 'Xác suất để đều là nữ bằng $%s$' %(latex(Rational(1, omega)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Để cả $2$ người đều là nữ, ta chọn $2$ nữ từ $%s$ nữ. \\\\
                            Số cách chọn là $n\\left(B\\right) = C_{%s}^2 = %s$. \\\\
                            Xác suất là $P\\left(B\\right) = \\frac{%s}{%s} = %s$.''' 
                            %(latex(w), latex(w), latex(chon_2_nu), latex(chon_2_nu), latex(omega), latex(p_ca_2_nu)))

            ########################################################################
            # Vận dụng cao: Ít nhất một nữ #########################################
            vdc_da_1_d = '\\True Xác suất để có ít nhất một nữ bằng $%s$' %(latex(p_it_nhat_1_nu))
            vdc_da_1_s = 'Xác suất để có ít nhất một nữ bằng $%s$' %(latex(Rational(p_it_nhat_1_nu.p - 1, p_it_nhat_1_nu.q)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Biến cố "Có ít nhất một nữ" là biến cố đối của biến cố "Không có nữ nào". \\\\
                             Ta có $P\\left(C\\right) = 1 - P\\left(A\\right) = 1 - %s = %s$.''' 
                             %(latex(p_khong_nu), latex(p_it_nhat_1_nu)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp để đảm bảo số đáp án đúng từ 1 đến 3
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_sel) + '}\n'
                '{' + str(th_sel) + '}\n'
                '{' + str(vd_sel) + '}\n'
                '{' + str(vdc_sel) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

