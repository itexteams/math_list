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


def bt_dang23_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            # Random tỷ lệ sản lượng phân xưởng A (pa), phân xưởng B sẽ là 100 - pa
            pa_int = random.choice([60, 70, 50, 80])
            pb_int = 100 - pa_int

            # Random tỷ lệ phế phẩm phân xưởng A (ra) và B (rb) %
            ra_int = random.randint(1, 3)
            rb_int = random.randint(2, 5)

            # Chuyển sang số thập phân để tính toán
            p_a = pa_int / 100
            p_b = pb_int / 100
            p_p_a = ra_int / 100
            p_p_b = rb_int / 100

            # Tính toán các giá trị xác suất
            # b) Xác suất phế phẩm và thuộc A: P(A ∩ P)
            p_a_and_p = round(p_a * p_p_a, 4)

            # c) Xác suất là phế phẩm (Xác suất đầy đủ): P(P)
            p_p = round(p_a * p_p_a + p_b * p_p_b, 4)

            # d) Xác suất thuộc A nếu là phế phẩm (Bayes): P(A|P)
            tu_so = int(p_a_and_p * 10000)
            mau_so = int(p_p * 10000)
            p_a_given_p = Rational(tu_so, mau_so)

            # Hàm hỗ trợ định dạng số thập phân kiểu Việt Nam (thay . thành ,)
            def f_num(value):
                return str(value).replace('.', ',')

            # Nội dung câu hỏi (không dùng raw string r'')
            noidungcauhoi = ('''Một nhà máy có hai phân xưởng A và B tương ứng làm ra %s\\%% và %s\\%% sản phẩm của nhà máy. Tỉ lệ phế phẩm của hai phân xưởng A và B lần lượt là %s\\%% và %s\\%%. Chọn ngẫu nhiên một sản phẩm của nhà máy.''' 
                             %(pa_int, pb_int, ra_int, rb_int))

            ########################################################################
            # Nhận biết ############################################
            p_not_p_a_true = round(1 - p_p_a, 2)
            p_not_p_a_false = round(1 - p_p_b, 2) if ra_int != rb_int else 0.98

            nb_da_1_d = '\\True Nếu sản phẩm chọn ra thuộc phân xưởng A thì xác suất để nó không là phế phẩm là %s' % (f_num(p_not_p_a_true))
            nb_da_1_s = 'Nếu sản phẩm chọn ra thuộc phân xưởng A thì xác suất để nó không là phế phẩm là %s' % (f_num(p_not_p_a_false))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Nếu sản phẩm chọn ra thuộc phân xưởng A thì xác suất để nó không là phế phẩm là $P(\\overline{P}|A)=1-P(P|A)=1-%s=%s$.''' 
                            % (f_num(p_p_a), f_num(p_not_p_a_true)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất để sản phẩm chọn ra là phế phẩm và thuộc phân xưởng A là %s' % (f_num(p_a_and_p))
            th_da_1_s = 'Xác suất để sản phẩm chọn ra là phế phẩm và thuộc phân xưởng A là %s' % (f_num(round(p_a_and_p + 0.002, 4)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Xác suất để sản phẩm chọn ra là phế phẩm và thuộc phân xưởng A là $P(A \\cap P)=P(A).P(P|A)=%s.%s=%s$.''' 
                            % (f_num(p_a), f_num(p_p_a), f_num(p_a_and_p)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất để sản phẩm chọn ra là phế phẩm là %s' % (f_num(p_p))
            vd_da_1_s = 'Xác suất để sản phẩm chọn ra là phế phẩm là %s' % (f_num(round(p_p + 0.005, 4)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xác suất để sản phẩm chọn ra là phế phẩm là tổng xác suất chọn được phế phẩm từ phân xưởng A và từ phân xưởng B \\\\ $P(P)=P(A)P(P|A)+P(B).P(P|B)=%s.%s+%s.%s=%s$.''' 
                            % (f_num(p_a), f_num(p_p_a), f_num(p_b), f_num(p_p_b), f_num(p_p)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Nếu sản phẩm chọn ra là phế phẩm thì xác suất để nó thuộc phân xưởng A là $\\frac{%s}{%s}$' % (p_a_given_p.p, p_a_given_p.q)
            vdc_da_1_s = 'Nếu sản phẩm chọn ra là phế phẩm thì xác suất để nó thuộc phân xưởng A là $\\frac{%s}{%s}$' % (p_a_given_p.p + 1, p_a_given_p.q + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Áp dụng công thức Bayes \\\\ Nếu sản phẩm chọn ra là phế phẩm thì xác suất để nó thuộc phân xưởng A là $P(A|P)=\\frac{P(A \\cap P)}{P(P)}=\\frac{%s}{%s}=%s$.''' 
                             % (f_num(p_a_and_p), f_num(p_p), latex(p_a_given_p)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn bộ đáp án
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung (Đảm bảo cấu trúc minipage/ex/choiceTFn/loigiai)
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

