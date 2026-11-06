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


def bt_dang24_p2_b2_c4_ds12(self):
            # Khai báo biến
            # n_d: số lượng đồng xu double-headed (hai mặt ngửa)
            n_f = random.randint(2, 5)
            n_d = random.randint(1, 2)
            tong_xu = n_f + n_d

            # Các giá trị tính toán theo biến random
            p_fair = Rational(n_f, tong_xu)
            p_double = Rational(n_d, tong_xu)

            # a) Xác suất fair coin và mặt sấp: P(F và S) = P(F) * P(S|F) = p_fair * 1/2
            pa_dung = p_fair * Rational(1, 2)
            pa_sai = Rational(1, 2) if pa_dung != Rational(1, 2) else Rational(1, 3)

            # b) Xác suất xuất hiện mặt ngửa (toàn phần): P(N) = P(F)*1/2 + P(D)*1
            pb_dung = p_fair * Rational(1, 2) + p_double * 1
            pb_sai = Rational(1, 2) if pb_dung != Rational(1, 2) else Rational(3, 4)

            # c) Xác suất double-headed nếu biết đã ngửa (Bayes): P(D|N) = P(D)/P(N)
            pc_dung = p_double / pb_dung
            pc_sai = Rational(3, 5) if pc_dung != Rational(3, 5) else Rational(2, 5)

            # d) Xác suất lần 2 ngửa nếu lần 1 ngửa: P(N2|N1) = P(N1 và N2) / P(N1)
            # P(N1 và N2) = P(F)*(1/2)^2 + P(D)*(1)^2
            p_n1n2 = p_fair * Rational(1, 4) + p_double * 1
            pd_dung = p_n1n2 / pb_dung
            pd_sai = Rational(7, 10) if pd_dung != Rational(7, 10) else Rational(1, 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một túi chứa %s đồng xu công bằng (fair coin - tức đồng xu có đủ hai mặt sấp ngửa) và %s đồng xu có hai mặt ngửa (double-headed coin). Một đồng xu được chọn ngẫu nhiên từ túi và được gieo để xem mặt hiện ra là ngửa hay sấp.''' 
                             % (latex(n_f), latex(n_d)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Xác suất để đồng xu fair coin được chọn và mặt sấp xuất hiện bằng $%s$' % latex(pa_dung)
            nb_da_1_s = 'Xác suất để đồng xu fair coin được chọn và mặt sấp xuất hiện bằng $%s$' % latex(pa_sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Gọi biến cố $A$: "Chọn được một đồng xu fair coin" $\\Rightarrow P(A)=\\frac{%s}{%s}$. \\\\ Gọi biến cố $B$: "Gieo đồng xu xuất hiện mặt sấp" $\\Rightarrow P(B|A)=\\frac{1}{2}$. \\\\ Xác suất để đồng xu fair coin được chọn và mặt sấp xuất hiện là $P(AB) = P(A) \\cdot P(B|A) = \\frac{%s}{%s} \\cdot \\frac{1}{2} = %s$.''' 
                            % (latex(n_f), latex(tong_xu), latex(n_f), latex(tong_xu), latex(pa_dung)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Xác suất xuất hiện mặt ngửa bằng $%s$' % latex(pb_dung)
            th_da_1_s = 'Xác suất xuất hiện mặt ngửa bằng $%s$' % latex(pb_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gọi $\\bar{B}$ là biến cố: "Gieo đồng xu xuất hiện mặt ngửa". \\\\ Ta có $P(\\bar{B}|A)=\\frac{1}{2}$ và $P(\\bar{B}|\\bar{A})=1$ (với $\\bar{A}$ là biến cố chọn đồng xu hai mặt ngửa). \\\\ Theo công thức xác suất toàn phần: $P(\\bar{B}) = P(A) \\cdot P(\\bar{B}|A) + P(\\bar{A}) \\cdot P(\\bar{B}|\\bar{A}) = \\frac{%s}{%s} \\cdot \\frac{1}{2} + \\frac{%s}{%s} \\cdot 1 = %s$.''' 
                            % (latex(n_f), latex(tong_xu), latex(n_d), latex(tong_xu), latex(pb_dung)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Nếu biết mặt ngửa đã xuất hiện, xác suất đồng xu có hai mặt ngửa đã được chọn bằng $%s$' % latex(pc_dung)
            vd_da_1_s = 'Nếu biết mặt ngửa đã xuất hiện, xác suất đồng xu có hai mặt ngửa đã được chọn bằng $%s$' % latex(pc_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Nếu biết mặt ngửa đã xuất hiện, xác suất đồng xu hai mặt ngửa đã được chọn là xác suất có điều kiện $P(\\bar{A}|\\bar{B})$. \\\\ Theo công thức Bayes: $P(\\bar{A}|\\bar{B}) = \\frac{P(\\bar{A}) \\cdot P(\\bar{B}|\\bar{A})}{P(\\bar{B})} = \\frac{\\frac{%s}{%s} \\cdot 1}{%s} = %s$.''' 
                            % (latex(n_d), latex(tong_xu), latex(pb_dung), latex(pc_dung)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Nếu gieo đồng xu lần đầu xuất hiện mặt ngửa, xác suất để khi gieo đồng xu đó lần thứ hai vẫn xuất hiện mặt ngửa bằng $%s$' % latex(pd_dung)
            vdc_da_1_s = 'Nếu gieo đồng xu lần đầu xuất hiện mặt ngửa, xác suất để khi gieo đồng xu đó lần thứ hai vẫn xuất hiện mặt ngửa bằng $%s$' % latex(pd_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Gọi biến cố $E$: "Lần gieo đầu xuất hiện mặt ngửa" và $F$: "Lần gieo thứ hai xuất hiện mặt ngửa". \\\\ Ta đã tính $P(E) = %s$. \\\\ Tính $P(E \\cap F)$: \\\\ TH1: Chọn được fair coin và cả hai lần đều ngửa: $P(A) \\cdot (\\frac{1}{2})^2 = \\frac{%s}{%s} \\cdot \\frac{1}{4} = \\frac{%s}{%s}$. \\\\ TH2: Chọn được đồng xu hai mặt ngửa: $P(\\bar{A}) \\cdot 1^2 = \\frac{%s}{%s}$. \\\\ $\\Rightarrow P(E \\cap F) = \\frac{%s}{%s} + \\frac{%s}{%s} = %s$. \\\\ Vậy $P(F|E) = \\frac{P(E \\cap F)}{P(E)} = \\frac{%s}{%s} = %s$.''' 
                             % (latex(pb_dung), latex(n_f), latex(tong_xu), latex(n_f), latex(4*tong_xu), latex(n_d), latex(tong_xu), latex(n_f), latex(4*tong_xu), latex(n_d), latex(tong_xu), latex(p_n1n2), latex(p_n1n2), latex(pb_dung), latex(pd_dung)))

            # Lặp để chọn bộ đáp án có 1-3 câu đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da, th_da, vd_da, vdc_da]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

