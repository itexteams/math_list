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


def bt_dang12_p2_b1_c4_ds12(self):
            # Khai báo biến
            # m: số quả cầu có thưởng, n: số quả cầu không thưởng
            m = randint(4, 7)
            n = randint(8, 12)
            tong = m + n

            # Tính toán các giá trị xác suất
            p_b = Rational(m, tong)
            p_a_given_b = Rational(m - 1, tong - 1)
            p_ab = p_b * p_a_given_b
            p_not_b = Rational(n, tong)
            p_a_given_not_b = Rational(m, tong - 1)
            p_a = p_b * p_a_given_b + p_not_b * p_a_given_not_b
            p_b_given_a = p_ab / p_a

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong một hộp đựng %s quả cầu chứa phiếu có thưởng và %s quả cầu chứa phiếu không có thưởng (các quả cầu cùng hình dạng, kích thước và khối lượng). Hai bạn Bình, An lần lượt lấy ngẫu nhiên (không hoàn lại) mỗi bạn một quả. Bạn Bình lấy trước, bạn An lấy sau.''' 
                             %(latex(m), latex(n)))

            ########################################################################
            # Nhận biết ############################################################
            # Câu a: Xác suất bạn Bình lấy được quả cầu có thưởng
            nb_da_1_d = '\\True Xác suất bạn Bình lấy được quả cầu chứa thưởng là $%s$' %(latex(p_b))
            nb_da_1_s = 'Xác suất bạn Bình lấy được quả cầu chứa thưởng là $%s$' %(latex(Rational(n, tong)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi B là biến cố: "Bình lấy được quả cầu chứa phiếu có thưởng".\\\\
            Số cách chọn 1 quả cầu từ hộp là $n(\\Omega) = %s$.\\\\
            Số cách Bình chọn được quả có thưởng là $n(B) = %s$.\\\\
            Xác suất là $P(B) = \\frac{n(B)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                            %(latex(tong), latex(m), latex(m), latex(tong), latex(p_b)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu ###########################################################
            # Câu b: Xác suất có điều kiện P(A|B)
            th_da_1_d = '\\True Biết bạn Bình đã lấy được quả cầu chứa phiếu có thưởng, xác suất để bạn An lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_a_given_b))
            th_da_1_s = 'Biết bạn Bình đã lấy được quả cầu chứa phiếu có thưởng, xác suất để bạn An lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi A là biến cố: "An lấy được quả cầu chứa phiếu có thưởng".\\\\
            Khi Bình đã lấy 1 quả cầu có thưởng, trong hộp còn lại %s quả cầu, trong đó có %s quả có thưởng.\\\\
            Xác suất để An lấy được quả có thưởng là $P(A|B) = \\frac{%s}{%s} = %s$.''' 
                            %(latex(tong-1), latex(m-1), latex(m-1), latex(tong-1), latex(p_a_given_b)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng #############################################################
            # Câu c: Xác suất cả hai cùng lấy được thưởng P(AB)
            vd_da_1_d = '\\True Xác suất để cả hai bạn cùng lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_ab))
            vd_da_1_s = 'Xác suất để cả hai bạn cùng lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_b + p_a_given_b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xác suất để cả hai bạn cùng lấy được quả cầu có thưởng (biến cố giao $A \\cap B$) là:\\\\
            $P(A \\cap B) = P(B) \\cdot P(A|B) = %s \\cdot %s = %s$.''' 
                            %(latex(p_b), latex(p_a_given_b), latex(p_ab)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao #########################################################
            # Câu d: Xác suất có điều kiện ngược P(B|A)
            vdc_da_1_d = '\\True Biết bạn An lấy được quả cầu chứa phiếu có thưởng, xác suất để bạn Bình lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_b_given_a))
            vdc_da_1_s = 'Biết bạn An lấy được quả cầu chứa phiếu có thưởng, xác suất để bạn Bình lấy được quả cầu chứa phiếu có thưởng là $%s$' %(latex(p_ab))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để tính $P(B|A)$, ta cần tính xác suất $P(A)$ bằng công thức xác suất đầy đủ:\\\\
            $P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})$\\\\
            $P(A) = %s \\cdot %s + %s \\cdot %s = %s$.\\\\
            Khi đó, theo công thức xác suất có điều kiện:\\\\
            $P(B|A) = \\frac{P(A \\cap B)}{P(A)} = \\frac{%s}{%s} = %s$.''' 
                             %(latex(p_b), latex(p_a_given_b), latex(p_not_b), latex(p_a_given_not_b), latex(p_a), latex(p_ab), latex(p_a), latex(p_b_given_a)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # --- BƯỚC 3: LOGIC CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                current_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Gán lại giá trị đã chọn vào list để xuất nội dung
            shuffled_answers_nb = [nb_sel]
            shuffled_answers_th = [th_sel]
            shuffled_answers_vd = [vd_sel]
            shuffled_answers_vdc = [vdc_sel]

            # Lời giải tương ứng với thứ tự câu hỏi (cố định theo logic a, b, c, d)
            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # --- BƯỚC 4: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

