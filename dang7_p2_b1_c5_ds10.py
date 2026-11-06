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


def bt_dang7_p2_b1_c5_ds10(self):
            # Khai báo biến
            # n1 là số lượng chữ số từ 1 đến n1
            n1 = randint(8, 9)
            # n2_max là chữ số lớn nhất trong tập {0, 1, ..., n2_max}
            n2_max = randint(5, 6)
            # k_d là số chữ số cho câu (d)
            k_d = 4

            # Tính toán các kết quả đúng
            res_a = n1**n1
            res_b = math.factorial(n1)
            res_c = n2_max * math.factorial(n2_max)
            res_d = n2_max * math.perm(n2_max, k_d - 1)

            # Tập hợp chữ số
            tap_a_b = ", ".join([str(i) for i in range(1, n1 + 1)])
            tap_c_d = ", ".join([str(i) for i in range(0, n2_max + 1)])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho các chữ số $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$.''')

            ########################################################################
            # Nhận biết (Câu a) ####################################################
            nb_da_1_d = '\\True Có %s số tự nhiên gồm %s chữ số, được tạo thành từ các chữ số %s' % (res_a, n1, tap_a_b)
            nb_da_1_s = 'Có %s số tự nhiên gồm %s chữ số, được tạo thành từ các chữ số %s' % (res_a + randint(10, 100), n1, tap_a_b)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Mỗi chữ số trong số tự nhiên có %s cách chọn (từ tập các chữ số $%s$). \\\\
            Vì số tự nhiên có %s chữ số nên có $%s^{%s} = %s$ số.''' % (n1, tap_a_b, n1, n1, n1, res_a))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b) ###################################################
            th_da_1_d = '\\True Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (res_b, n1, tap_a_b)
            th_da_1_s = 'Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (math.factorial(n1-1), n1, tap_a_b)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Số các số tự nhiên gồm %s chữ số đôi một khác nhau được lập từ tập có %s chữ số là một hoán vị của %s phần tử. \\\\
            Số các số là $P_{%s} = %s! = %s$.''' % (n1, n1, n1, n1, n1, res_b))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c) #####################################################
            vd_da_1_d = '\\True Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (res_c, n2_max + 1, tap_c_d)
            vd_da_1_s = 'Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (math.factorial(n2_max + 1), n2_max + 1, tap_c_d)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Gọi số cần tìm là $\\overline{a_1a_2...a_{%s}}$. \\\\
            Chữ số $a_1$ có %s cách chọn (khác $0$). \\\\
            Các chữ số còn lại là hoán vị của %s chữ số còn lại, nên có $%s!$ cách chọn. \\\\
            Vậy có $%s \\times %s! = %s$ số.''' % (n2_max + 1, n2_max, n2_max, n2_max, n2_max, n2_max, res_c))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d) #################################################
            vdc_da_1_d = '\\True Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (res_d, k_d, tap_c_d)
            vdc_da_1_s = 'Có %s số tự nhiên gồm %s chữ số đôi một khác nhau, được tạo thành từ các chữ số %s' % (math.perm(n2_max + 1, k_d), k_d, tap_c_d)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Gọi số cần tìm là $\\overline{abcd}$. \\\\
            Chữ số $a$ có %s cách chọn (khác $0$). \\\\
            Bộ ba chữ số $(b, c, d)$ được chọn từ %s chữ số còn lại và có sắp xếp nên có $A_{%s}^{3}$ cách chọn. \\\\
            Vậy có $%s \\times A_{%s}^{3} = %s \\times %s = %s$ số.''' % (n2_max, n2_max, n2_max, n2_max, n2_max, n2_max, math.perm(n2_max, 3), res_d))
            list_vdc_2 = [loigiai_vdc_1]

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

            # Gán lại vào list sau khi đã chọn được bộ đáp án thỏa mãn điều kiện
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

