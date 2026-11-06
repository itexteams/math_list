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


def bt_dang18_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Chọn ngẫu nhiên P(A) từ 0.3 đến 0.7
            p_a_val = random.choice([0.3, 0.4, 0.5, 0.6, 0.7])
            p_b_val = float(Fraction(1) - Fraction(p_a_val))

            # Xác suất phát sinh chi phí khi thuê A và B (P(N|A) và P(N|B))
            p_n_a = random.choice([0.04, 0.05, 0.06, 0.08])
            p_n_b = random.choice([0.02, 0.03, 0.04])

            # Tính xác suất toàn phần P(N)
            p_n = float(Fraction(p_a_val) * Fraction(p_n_a) + Fraction(p_b_val) * Fraction(p_n_b))

            # Tính xác suất Bayes P(A|N), P(B|N) và P(A|not N)
            p_a_given_n = float((Fraction(p_a_val) * Fraction(p_n_a)) / Fraction(p_n))
            p_b_given_n = float((Fraction(p_b_val) * Fraction(p_n_b)) / Fraction(p_n))

            p_not_n = float(Fraction(1) - Fraction(p_n))
            p_not_n_a = float(Fraction(1) - Fraction(p_n_a))
            p_a_given_not_n = float((Fraction(p_a_val) * Fraction(p_not_n_a)) / Fraction(p_not_n))

            # Nội dung đề bài
            noidungcauhoi = ("Xác suất để công ty $X$ thuê một trong hai công ty vệ tinh $A$ và $B$ tư vấn lần lượt là $%s$ và $%s$. Theo kinh nghiệm khả năng $X$ phát sinh thêm chi phí khi sử dụng dịch vụ tư vấn của công ty $A$ và $B$ lần lượt là $%s$ và $%s$." 
                             % (str(p_a_val).replace('.', ','), str(p_b_val).replace('.', ','), str(p_n_a).replace('.', ','), str(p_n_b).replace('.', ',')))

            ########################################################################
            # a) Nhận biết: Tính xác suất toàn phần P(N)
            ########################################################################
            p_n_str = str(round(p_n, 4)).replace('.', ',')
            nb_da_1_d = '\\True Xác suất để $X$ có phát sinh thêm chi phí khi sử dụng dịch vụ tư vấn là %s' % p_n_str
            nb_da_1_s = 'Xác suất để $X$ có phát sinh thêm chi phí khi sử dụng dịch vụ tư vấn là %s' % str(round(p_n + 0.01, 3)).replace('.', ',')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ("Xét các biến cố: $M$: \"Công ty $X$ thuê công ty vệ tinh $A$ tư vấn\"; $N$: \"Công ty $X$ có phát sinh thêm chi phí\".\\\\ "
                            "Ta có $P(M)=%s; P(\\overline{M})=%s; P(N|M)=%s; P(N|\\overline{M})=%s$. \\\\"
                            "Áp dụng công thức xác suất toàn phần: $P(N) = P(M).P(N|M) + P(\\overline{M}).P(N|\\overline{M}) = %s.%s + %s.%s = %s$."
                            % (str(p_a_val).replace('.', ','), str(p_b_val).replace('.', ','), str(p_n_a).replace('.', ','), str(p_n_b).replace('.', ','),
                               str(p_a_val).replace('.', ','), str(p_n_a).replace('.', ','), str(p_b_val).replace('.', ','), str(p_n_b).replace('.', ','), p_n_str))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu: Tính P(A|N)
            ########################################################################
            p_a_n_str = str(round(p_a_given_n, 4)).replace('.', ',')
            th_da_1_d = '\\True Biết $X$ có phát sinh thêm chi phí, xác suất để $X$ thuê công ty $A$ tư vấn là %s' % p_a_n_str
            th_da_1_s = 'Biết $X$ có phát sinh thêm chi phí, xác suất để $X$ thuê công ty $A$ tư vấn là %s' % str(round(p_b_given_n, 4)).replace('.', ',')
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ("Áp dụng công thức Bayes: $P(M|N) = \\frac{P(M).P(N|M)}{P(N)} = \\frac{%s.%s}{%s} \\approx %s$."
                            % (str(p_a_val).replace('.', ','), str(p_n_a).replace('.', ','), p_n_str, p_a_n_str))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng: Tính P(B|N)
            ########################################################################
            p_b_n_str = str(round(p_b_given_n, 4)).replace('.', ',')
            vd_da_1_d = '\\True Biết $X$ có phát sinh thêm chi phí, xác suất để $X$ thuê công ty $B$ tư vấn là %s' % p_b_n_str
            vd_da_1_s = 'Biết $X$ có phát sinh thêm chi phí, xác suất để $X$ thuê công ty $B$ tư vấn là %s' % p_a_n_str
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ("Tương tự câu b, ta có: $P(\\overline{M}|N) = \\frac{P(\\overline{M}).P(N|\\overline{M})}{P(N)} = \\frac{%s.%s}{%s} \\approx %s$."
                            % (str(p_b_val).replace('.', ','), str(p_n_b).replace('.', ','), p_n_str, p_b_n_str))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao: Tính P(A|not N)
            ########################################################################
            p_a_not_n_str = str(round(p_a_given_not_n, 4)).replace('.', ',')
            vdc_da_1_d = '\\True Biết $X$ không phát sinh thêm chi phí, xác suất để $X$ thuê công ty $A$ tư vấn là %s' % p_a_not_n_str
            vdc_da_1_s = 'Biết $X$ không phát sinh thêm chi phí, xác suất để $X$ thuê công ty $A$ tư vấn là %s' % str(round(p_a_given_not_n - 0.05, 3)).replace('.', ',')
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ("Gọi $\\overline{N}$ là biến cố $X$ không phát sinh chi phí. $P(\\overline{N}) = 1 - P(N) = 1 - %s = %s$.\\\\ "
                             "Ta có $P(\\overline{N}|M) = 1 - P(N|M) = 1 - %s = %s$.\\\\ "
                             "Áp dụng công thức Bayes: \\\\ $P(M|\\overline{N}) = \\frac{P(M).P(\\overline{N}|M)}{P(\\overline{N})} = \\frac{%s.%s}{%s} \\approx %s$."
                             % (p_n_str, str(round(p_not_n, 4)).replace('.', ','), str(p_n_a).replace('.', ','), str(round(p_not_n_a, 4)).replace('.', ','),
                                str(p_a_val).replace('.', ','), str(round(p_not_n_a, 4)).replace('.', ','), str(round(p_not_n, 4)).replace('.', ','), p_a_not_n_str))

            list_vdc_2 = [loigiai_vdc_1]

            # Phần logic trộn và xuất nội dung (giữ nguyên cấu trúc mẫu)
            shuffled_answers_nb, shuffled_solutions_nb = [nb_da_1], [loigiai_nb_1]
            shuffled_answers_th, shuffled_solutions_th = [th_da_1], [loigiai_th_1]
            shuffled_answers_vd, shuffled_solutions_vd = [vd_da_1], [loigiai_vd_1]
            shuffled_answers_vdc, shuffled_solutions_vdc = [vdc_da_1], [loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

