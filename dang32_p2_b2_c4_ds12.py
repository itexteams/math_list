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


def bt_dang32_p2_b2_c4_ds12(self):
            # Khai báo biến
            # n_total: Tổng số hộp, n1: số hộp loại I, n2: số hộp loại II
            n1 = random.randint(2, 4)
            n2 = random.randint(5, 8)
            n_total = n1 + n2

            # Hộp loại I: w1 bi trắng, r1 bi đỏ. Tổng 10 viên.
            r1 = random.randint(3, 7)
            w1 = 10 - r1

            # Hộp loại II: w2 bi trắng, r2 bi đỏ. Tổng 10 viên.
            r2 = random.randint(1, 4)
            w2 = 10 - r2

            # Tính toán các xác suất
            p_box2 = Rational(n2, n_total)
            p_box1 = Rational(n1, n_total)
            p_red_given_box2 = Rational(r2, 10)
            p_red_given_box1 = Rational(r1, 10)
            p_red_total = p_box2 * p_red_given_box2 + p_box1 * p_red_given_box1
            p_box2_given_red = (p_box2 * p_red_given_box2) / p_red_total

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có %s hộp bi trong đó có %s hộp bi loại I và %s hộp bi loại II, các viên bi có cùng kích thước và khối lượng. Mỗi hộp bi loại I có %s bi trắng và %s bi đỏ, mỗi hộp bi loại II có %s bi trắng và %s bi đỏ. Bạn Nam lấy ngẫu nhiên một hộp bi rồi từ hộp đó lấy ra ngẫu nhiên một viên bi.''' 
                             %(n_total, n1, n2, w1, r1, w2, r2))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất để bạn Nam lấy được hộp bi loại II là $%s$' %(latex(p_box2))
            nb_da_1_s = 'Xác suất để bạn Nam lấy được hộp bi loại II là $%s$' %(latex(p_box1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $A$ là biến cố "Bạn Nam lấy được hộp bi loại II". Ta có $P(A) = \\frac{%s}{%s} = %s$.''' 
                            %(n2, n_total, latex(p_box2)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Biết rằng bạn Nam lấy được hộp bi loại II, xác suất để viên bi lấy ra có màu đỏ bằng $%s$' %(latex(p_red_given_box2))
            th_da_1_s = 'Biết rằng bạn Nam lấy được hộp bi loại II, xác suất để viên bi lấy ra có màu đỏ bằng $%s$' %(latex(p_red_given_box1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Gọi $B$ là biến cố "Bạn Nam lấy được viên bi đỏ". Xác suất để lấy được viên bi đỏ khi biết đã chọn hộp loại II là $P(B|A) = \\frac{%s}{10} = %s$.''' 
                            %(r2, latex(p_red_given_box2)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất để bạn Nam lấy được viên bi màu đỏ bằng $%s$' %(latex(p_red_total))
            vd_da_1_s = 'Xác suất để bạn Nam lấy được viên bi màu đỏ bằng $%s$' %(latex(p_red_total + Rational(1, 20)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có biến cố đối của $A$ là $\\overline{A}$: "Bạn Nam lấy được hộp bi loại I".\\\\
            $P(\\overline{A}) = \\frac{%s}{%s} = %s$; $P(B|\\overline{A}) = \\frac{%s}{10} = %s$.\\\\
            Áp dụng công thức xác suất toàn phần, ta có:\\\\
            $P(B) = P(A)P(B|A) + P(\\overline{A})P(B|\\overline{A}) = %s \\cdot %s + %s \\cdot %s = %s$.''' 
                            %(n1, n_total, latex(p_box1), r1, latex(p_red_given_box1), latex(p_box2), latex(p_red_given_box2), latex(p_box1), latex(p_red_given_box1), latex(p_red_total)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khi bạn Nam lấy được một viên bi màu đỏ thì xác suất để viên bi đó được lấy ra từ hộp II bằng $%s$' %(latex(p_box2_given_red))
            vdc_da_1_s = 'Khi bạn Nam lấy được một viên bi màu đỏ thì xác suất để viên bi đó được lấy ra từ hộp II bằng $%s$' %(latex(p_box2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Áp dụng công thức Bayes, xác suất để viên bi đỏ lấy ra thuộc hộp II là:\\\\
            $P(A|B) = \\frac{P(A).P(B|A)}{P(B)} = \\frac{%s \\cdot %s}{%s} = %s$.''' 
                             %(latex(p_box2), latex(p_red_given_box2), latex(p_red_total), latex(p_box2_given_red)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị đã chọn
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

