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


def bt_dang28_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def fmt(val):
                return str(round(float(val), 2)).replace('.', ',')

            # --- BƯỚC 1: KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            # p1: % người bị tiểu đường (30% - 50%)
            p1_int = random.choice([30, 35, 40, 45, 50])
            p1 = p1_int / 100

            # p2: % người bị tiểu đường kèm cao huyết áp (60% - 80%)
            p2_int = random.choice([60, 65, 70, 75, 80])
            p2 = p2_int / 100

            # p3: % người không bị tiểu đường nhưng bị cao huyết áp (15% - 30%)
            p3_int = random.choice([15, 20, 25, 30])
            p3 = p3_int / 100

            # Tính toán các giá trị liên quan
            pa = p1
            pa_not = 1 - pa
            pb_given_a = p2
            pb_given_a_not = p3
            pb = pa * pb_given_a + pa_not * pb_given_a_not
            pa_given_b = (pa * pb_given_a) / pb
            pa_not_given_b = 1 - pa_given_b

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khi điều tra sức khỏe nhiều người cao tuổi ở một địa phương, người ta thấy rằng có %d\\%% người cao tuổi bị bệnh tiểu đường. Có %d\\%% người bị bệnh tiểu đường bị bệnh cao huyết áp và %d\\%% người không bị bệnh tiểu đường bị bệnh cao huyết áp. Chọn ngẫu nhiên 1 người cao tuổi để kiểm tra sức khỏe.''' 
                             % (p1_int, p2_int, p3_int))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất chọn được người bị bệnh tiểu đường là %s' % fmt(pa)
            nb_da_1_s = 'Xác suất chọn được người bị bệnh tiểu đường là %s' % fmt(pa + 0.1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Gọi $A$: "chọn được người bị bệnh tiểu đường" $\\Rightarrow P(A)=%s$.''' % fmt(pa))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là %s' % fmt(pb_given_a)
            th_da_1_s = 'Xác suất chọn được người bị bệnh huyết áp cao, biết người đó bị bệnh tiểu đường là %s' % fmt(pb_given_a_not)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gọi $B$: "chọn được người bị bệnh huyết áp cao". Ta có xác suất có điều kiện $P(B|A)=%s$ và $P(B|\\overline{A})=%s$.''' 
                            % (fmt(pb_given_a), fmt(pb_given_a_not)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất chọn được người bị bệnh huyết áp cao là %s' % fmt(pb)
            vd_da_1_s = 'Xác suất chọn được người bị bệnh huyết áp cao là %s' % fmt(pb - 0.05)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xác suất chọn được người bị bệnh huyết áp cao là: \\\\
            $P(B) = P(A).P(B|A) + P(\\overline{A}).P(B|\\overline{A}) = %s.%s + %s.%s = %s$.''' 
                            % (fmt(pa), fmt(pb_given_a), fmt(pa_not), fmt(pb_given_a_not), fmt(pb)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Xác suất chọn được người không bị bệnh tiểu đường, biết người đó bị bệnh huyết áp cao là %s' % fmt(pa_not_given_b)
            vdc_da_1_s = 'Xác suất chọn được người không bị bệnh tiểu đường, biết người đó bị bệnh huyết áp cao là %s' % fmt(pa_given_b)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Xác suất chọn được người không bị bệnh tiểu đường, biết người đó bị bệnh huyết áp cao là: \\\\
            $P(\\overline{A}|B) = 1 - P(A|B) = 1 - \\frac{P(A).P(B|A)}{P(B)} = 1 - \\frac{%s.%s}{%s} \\approx %s$.''' 
                             % (fmt(pa), fmt(pb_given_a), fmt(pb), fmt(pa_not_given_b)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Sử dụng list_nb_2, list_th_2... để chứa lời giải cố định)
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp và xáo trộn (Dù ở đây mỗi list chỉ có 1 lời giải tương ứng)
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi (Không dùng raw string r, dùng double backslash cho LaTeX)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
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

