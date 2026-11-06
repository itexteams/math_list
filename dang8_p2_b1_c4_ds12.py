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


def bt_dang8_p2_b1_c4_ds12(self):
            # Khai báo biến
            # n21: Không hút & Ung thư, n22: Không hút & Không ung thư

            n11 = random.randint(1100, 1200)
            n12 = random.randint(1100, 1200)
            n21 = random.randint(250, 300)
            n22 = 10000 - n11 - n12 - n21

            total = 10000
            nA = n11 + n12 # Tổng người hút thuốc
            nB = n11 + n21 # Tổng người mắc ung thư
            nNotA = n21 + n22 # Tổng người không hút thuốc

            # Tính toán các xác suất thực tế
            probA_percent = (nA / total) * 100
            probB_percent = (nB / total) * 100
            condAB_percent = (n11 / nB) * 100
            riskA = n11 / nA
            riskNotA = n21 / nNotA
            ratio_risk = round(riskA / riskNotA)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một nhóm nghiên cứu tiến hành khảo sát %s người và nhận thấy những người hút thuốc lá có nguy cơ bị ung thư phổi cao hơn so với người không hút thuốc lá. Kết quả khảo sát của nhóm nghiên cứu được trình bày trong bảng dữ liệu thống kê $2 \\times 2$ sau đây:
            \\begin{center}
            \\begin{tabular}{|l|l|l|}
            \\hline
             & Mắc ung thư phổi & Không mắc ung thư phổi \\\\ \\hline
            Hút thuốc lá & %s người & %s người \\\\ \\hline
            Không hút thuốc lá & %s người & %s người \\\\ \\hline
            \\end{tabular}
            \\end{center}
            Chọn ngẫu nhiên một người trong %s người được khảo sát.''' 
            %(total, n11, n12, n21, n22, total))

            ########################################################################
            # Nhận biết: Xác suất người đó hút thuốc lá P(A)
            ########################################################################
            val_a_true = round(probA_percent, 1)
            val_a_false = round(probA_percent - 5, 1)

            nb_da_1_d = '\\True Xác suất để người đó hút thuốc lá là $%s\\%%$' % (latex(val_a_true)).replace('.', ',')
            nb_da_1_s = 'Xác suất để người đó hút thuốc lá là $%s\\%%$' % (latex(val_a_false)).replace('.', ',')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố người đó có hút thuốc lá. \\\\
            Gọi $B$ là biến cố người đó bị ung thư phổi. \\\\
            Ta có xác suất người đó hút thuốc lá: \\\\
            $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s + %s}{%s} = \\frac{%s}{%s} = %s\\%%$.''' 
            %(n11, n12, total, nA, total, latex(val_a_true).replace('.', ',')))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Xác suất có điều kiện P(A|B)
            ########################################################################
            val_b_limit = 80
            val_b_actual = round(condAB_percent, 2)

            th_da_1_d = '\\True Nếu người đó bị ung thư phổi thì xác suất người đó hút thuốc lá lớn hơn %s\\%%' % (val_b_limit)
            th_da_1_s = 'Nếu người đó bị ung thư phổi thì xác suất người đó hút thuốc lá nhỏ hơn %s\\%%' % (val_b_limit)
            # Đảm bảo tính đúng sai dựa trên kết quả tính toán thực tế
            if val_b_actual > val_b_limit:
                list_th_da_1 = [th_da_1_d, th_da_1_s]
            else:
                list_th_da_1 = [th_da_1_s, th_da_1_d] # Đảo lại nếu ngẫu nhiên rơi vào trường hợp nhỏ hơn

            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Số người bị ung thư phổi là $n(B) = %s + %s = %s$. \\\\
            Ta có $P(A|B) = \\frac{n(A \\cap B)}{n(B)} = \\frac{%s}{%s} \\approx %s\\%%$. \\\\
            Vì $%s\\%% > %s\\%%$ nên khẳng định trên là đúng.''' 
            %(n11, n21, nB, n11, nB, latex(val_b_actual).replace('.', ','), latex(val_b_actual).replace('.', ','), val_b_limit))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Xác suất mắc ung thư phổi P(B)
            ########################################################################
            val_c_true = round(probB_percent, 1)
            val_c_false = round(probB_percent + 2, 1)

            vd_da_1_d = '\\True Xác suất để người đó bị ung thư phổi là $%s\\%%$' % (latex(val_c_true).replace('.', ','))
            vd_da_1_s = 'Xác suất để người đó bị ung thư phổi là $%s\\%%$' % (latex(val_c_false).replace('.', ','))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $P(B) = \\frac{n(B)}{n(\\Omega)} = \\frac{%s + %s}{%s} = \\frac{%s}{%s} = %s\\%%$.''' 
            %(n11, n21, total, nB, total, latex(val_c_true).replace('.', ',')))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tỉ lệ nguy cơ (Relative Risk)
            ########################################################################
            vdc_da_1_d = '\\True Dựa theo kết quả khảo sát trên ta thấy, người hút thuốc lá có nguy cơ mắc bệnh ung thư phổi cao gấp khoảng %s lần so với người không hút thuốc lá' % (ratio_risk)
            vdc_da_1_s = 'Dựa theo kết quả khảo sát trên ta thấy, người hút thuốc lá có nguy cơ mắc bệnh ung thư phổi cao gấp khoảng %s lần so với người không hút thuốc lá' % (ratio_risk + 5)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Ta tính xác suất mắc ung thư khi hút thuốc: $P(B|A) = \\frac{P(BA)}{P(A)} = \\frac{%s}{%s}$. \\\\
            Tính xác suất mắc ung thư khi không hút thuốc: $P(B|\\overline{A}) = \\frac{P(B\\overline{A})}{P(\\overline{A})} = \\frac{%s}{%s}$. \\\\
            Vậy $\\frac{P(B|A)}{P(B|\\overline{A})} = \\frac{%s}{%s} : \\frac{%s}{%s} \\approx %s$.''' 
            %(n11, nA, n21, nNotA, n11, nA, n21, nNotA, ratio_risk))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Lặp và kiểm tra số câu đúng (từ 1 đến 3)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    # Tìm lời giải tương ứng
                    sol1 = loigiai_nb_1
                    sol2 = loigiai_th_1
                    sol3 = loigiai_vd_1
                    sol4 = loigiai_vdc_1
                    break

            # Xuất nội dung
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
                '\\item ' + str(sol1) + '\n'
                '\\item ' + str(sol2) + '\n'
                '\\item ' + str(sol3) + '\n'
                '\\item ' + str(sol4) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

