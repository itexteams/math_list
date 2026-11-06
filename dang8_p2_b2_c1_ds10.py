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


def bt_dang8_p2_b2_c1_ds10(self):
            # Khai báo biến
            # --- BƯỚC 3: THIẾT KẾ RANDOM ---
            k = random.randint(3, 8)  # Số chia
            buoc_nhay = random.randint(200, 500)
            limit = k * buoc_nhay + random.randint(1, k-1) # Giới hạn n < limit

            # Tính toán thông số toán học
            first_el = 0
            last_el = ((limit - 1) // k) * k
            n_elements = (last_el - first_el) // k + 1
            s_sum = (first_el + last_el) * n_elements // 2

            # --- BƯỚC 2: VIẾT LẠI THEO MẪU CODE PYTHON ---

            # Khai báo biến (nếu cần dùng sympy)
            n = symbols('n')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tập hợp $A = \\{n \\in \\mathbb{N} \\mid n \\vdots %s, n < %s\\}$.''' 
                             %(latex(k), latex(limit)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Tập $A$ gồm các số tự nhiên chia hết cho %s và nhỏ hơn %s' % (latex(k), latex(limit))
            nb_da_1_s = 'Tập $A$ gồm các số tự nhiên chia hết cho %s và nhỏ hơn hoặc bằng %s' % (latex(k), latex(last_el - 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Tập hợp $A$ được viết dưới dạng liệt kê là $A = \\{0; %s; %s; \\dots; %s\\}$.''' 
                            % (latex(k), latex(2*k), latex(last_el)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hiệu của hai phần tử liên tiếp bất kỳ trong tập hợp $A$ luôn bằng %s' % (latex(k))
            th_da_1_s = 'Hiệu của hai phần tử liên tiếp bất kỳ trong tập hợp $A$ luôn bằng %s' % (latex(k+1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Vì các phần tử là bội của %s nên hai số liên tiếp cách nhau %s đơn vị.''' 
                            % (latex(k), latex(k)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Tập hợp $A$ có tất cả %s phần tử' % (latex(n_elements))
            vd_da_1_s = 'Tập hợp $A$ có tất cả %s phần tử' % (latex(n_elements + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số phần tử của tập hợp $A$ là $\\frac{%s - 0}{%s} + 1 = %s$.''' 
                            % (latex(last_el), latex(k), latex(n_elements)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng các phần tử của tập hợp $A$ bằng %s' % (latex(s_sum))
            vdc_da_1_s = 'Tổng các phần tử của tập hợp $A$ bằng %s' % (latex(s_sum - k))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tổng các phần tử là $S = \\frac{(0 + %s) \\cdot %s}{2} = %s$.''' 
                             % (latex(last_el), latex(n_elements), latex(s_sum)))

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

            # Gán vào list để đồng bộ với phần xuất (giữ cấu trúc mẫu)
            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi (Không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
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

