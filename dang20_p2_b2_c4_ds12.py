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


def bt_dang20_p2_b2_c4_ds12(self):
            # Khai báo biến
            # p_a_b_bar_val: Tỉ lệ thực sự mua trong nhóm trả lời "không mua" P(A|B_bar)

            n_total = random.choice([100, 200, 300, 400, 500])
            n_buy_yes = random.randint(int(0.45 * n_total), int(0.55 * n_total))
            n_buy_no = n_total - n_buy_yes

            p_a_b_val = random.choice([0.7, 0.8, 0.6])
            p_a_b_bar_val = random.choice([0.2, 0.3, 0.4])

            # Các giá trị tính toán
            prob_B = Rational(n_buy_yes, n_total)
            prob_B_bar = 1 - prob_B
            prob_A = p_a_b_val * prob_B + p_a_b_bar_val * prob_B_bar
            prob_B_A = (p_a_b_val * prob_B) / prob_A
            percent_B_A = round(float(prob_B_A) * 100)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trước khi đưa một loại sản phẩm ra thị trường, người ta đã phỏng vấn ngẫu nhiên %s khách hàng về sản phẩm đó. Kết quả thống kê như sau: có %s người trả lời "sẽ mua"; có %s người trả lời "không mua". Kinh nghiệm cho thấy tỉ lệ khách hàng thực sự sẽ mua sản phẩm tương ứng với những cách trả lời "sẽ mua" và "không mua" lần lượt là %s\\%% và %s\\%%. Gọi $A$ là biến cố "Người được phỏng vấn thực sự sẽ mua sản phẩm". Gọi $B$ là biến cố "Người được phỏng vấn trả lời sẽ mua sản phẩm".''' 
                             %(n_total, n_buy_yes, n_buy_no, int(p_a_b_val*100), int(p_a_b_bar_val*100)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất $P(B)=%s$ và $P(\\overline{B})=%s$' %(latex(prob_B), latex(prob_B_bar))
            nb_da_1_s = 'Xác suất $P(B)=%s$ và $P(\\overline{B})=%s$' %(latex(prob_B_bar), latex(prob_B))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = ('''Xác suất $P(B)=\\frac{n_B}{n_{\\Omega}} = \\frac{%s}{%s} = %s$; $P(\\overline{B})=1-P(B)=%s$.''' 
                            %(n_buy_yes, n_total, latex(prob_B), latex(prob_B_bar)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất có điều kiện $P(A|B)=%s$' %(latex(p_a_b_val))
            th_da_1_s = 'Xác suất có điều kiện $P(A|B)=%s$' %(latex(p_a_b_bar_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ('''Theo đề bài: Kinh nghiệm cho thấy tỉ lệ khách hàng thực sự sẽ mua sản phẩm tương ứng với những cách trả lời "sẽ mua" là %s\\%%. Do đó xác suất có điều kiện $P(A|B)=%s$.''' 
                            %(int(p_a_b_val*100), latex(p_a_b_val)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Xác suất $P(A)=%s$' %(latex(prob_A))
            vd_da_1_s = 'Xác suất $P(A)=%s$' %(latex(round(float(prob_A) + 0.05, 2)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = ('''Xác suất $P(A)=P(A|B).P(B)+P(A|\\overline{B}).P(\\overline{B}) = %s.%s + %s.%s = %s$.''' 
                            %(latex(p_a_b_val), latex(prob_B), latex(p_a_b_bar_val), latex(prob_B_bar), latex(prob_A)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Trong số những người được phỏng vấn thực sự sẽ mua sản phẩm có %s\\%% người đã trả lời "sẽ mua" khi được phỏng vấn (kết quả làm tròn đến hàng đơn vị)' %(percent_B_A)
            vdc_da_1_s = 'Trong số những người được phỏng vấn thực sự sẽ mua sản phẩm có %s\\%% người đã trả lời "sẽ mua" khi được phỏng vấn' %(percent_B_A - 5)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = ('''Ta cần tính xác suất có điều kiện $P(B|A)$. Theo công thức Bayes: \\\\ $P(B|A) = \\frac{P(A|B).P(B)}{P(A)} = \\frac{%s.%s}{%s} \\approx %s\\%%$.''' 
                             %(latex(p_a_b_val), latex(prob_B), latex(prob_A), percent_B_A))

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

            # Gán lời giải tương ứng với lựa chọn đúng/sai (để giải thích đúng vấn đề)
            # Lưu ý: Trong cấu trúc của bạn, shuffled_solutions thường đi kèm với đáp án.
            # Ở đây tôi chuẩn bị sẵn nội dung lời giải chuẩn.

            solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(solutions[0])+'\n'
                '\\item '+str(solutions[1])+'\n'
                '\\item '+str(solutions[2])+'\n'
                '\\item '+str(solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

