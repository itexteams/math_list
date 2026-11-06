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


def bt_dang10_p2_b2_c6_ds10(self):
            # Khai báo biến
            # Random số lượng quả cầu để bài toán phong phú
            n_x = random.randint(4, 5)  # Số quả cầu xanh
            n_t = random.randint(6, 7)  # Số quả cầu trắng
            n_chon = 3                  # Số quả cầu chọn ra
            tong = n_x + n_t

            # Tính toán các giá trị xác suất
            omega = binomial(tong, n_chon)

            # Xác suất 3 quả xanh
            n_A = binomial(n_x, 3)
            p_A = Rational(n_A, omega)

            # Xác suất 2 xanh, 1 trắng
            n_B = binomial(n_x, 2) * binomial(n_t, 1)
            p_B = Rational(n_B, omega)

            # Xác suất 3 quả cùng màu
            n_C = binomial(n_x, 3) + binomial(n_t, 3)
            p_C = Rational(n_C, omega)

            # Xác suất ít nhất 1 quả xanh
            n_D = omega - binomial(n_t, 3)
            p_D = Rational(n_D, omega)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một bình đựng %s quả cầu xanh và %s quả cầu trắng. Chọn ngẫu nhiên %s quả cầu.''' 
                             %(latex(n_x), latex(n_t), latex(n_chon)))

            ########################################################################
            # Nhận biết
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để được %s quả cầu toàn màu xanh bằng $%s$' %(latex(n_chon), latex(p_A))
            nb_da_1_s = 'Xác suất để được %s quả cầu toàn màu xanh bằng $%s$' %(latex(n_chon), latex(p_B))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số cách chọn ngẫu nhiên %s quả cầu từ %s quả cầu là $n(\\Omega) = C_{%s}^{%s} = %s$. \\\\
            Gọi $A$ là biến cố "Chọn được %s quả cầu màu xanh". \\\\
            Số cách chọn %s quả xanh từ %s quả xanh là $n(A) = C_{%s}^{%s} = %s$. \\\\
            Xác suất của biến cố $A$ là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.'''
                            %(latex(n_chon), latex(tong), latex(tong), latex(n_chon), latex(omega),
                              latex(n_chon), latex(n_chon), latex(n_x), latex(n_x), latex(n_chon), latex(n_A),
                              latex(n_A), latex(omega), latex(p_A)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Xác suất để được 2 quả cầu xanh và 1 quả cầu trắng bằng $%s$' %(latex(p_B))
            th_da_1_s = 'Xác suất để được 2 quả cầu xanh và 1 quả cầu trắng bằng $%s$' %(latex(p_A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $B$ là biến cố "Chọn được 2 quả cầu xanh và 1 quả cầu trắng". \\\\
            Số cách chọn 2 quả xanh từ %s quả xanh là $C_{%s}^2 = %s$. \\\\
            Số cách chọn 1 quả trắng từ %s quả trắng là $C_{%s}^1 = %s$. \\\\
            Số phần tử của biến cố $B$ là $n(B) = C_{%s}^2 \\cdot C_{%s}^1 = %s \\cdot %s = %s$. \\\\
            Xác suất của biến cố $B$ là $P(B) = \\frac{%s}{%s} = %s$.'''
                            %(latex(n_x), latex(n_x), latex(binomial(n_x, 2)), 
                              latex(n_t), latex(n_t), latex(n_t),
                              latex(n_x), latex(n_t), latex(binomial(n_x, 2)), latex(n_t), latex(n_B),
                              latex(n_B), latex(omega), latex(p_B)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để được %s quả cầu cùng màu bằng $%s$' %(latex(n_chon), latex(p_C))
            vd_da_1_s = 'Xác suất để được %s quả cầu cùng màu bằng $%s$' %(latex(n_chon), latex(Rational(1, 6)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $C$ là biến cố "Chọn được %s quả cầu cùng màu". \\\\
            Trường hợp 1: Chọn được %s quả cầu màu xanh, có $C_{%s}^{%s} = %s$ cách. \\\\
            Trường hợp 2: Chọn được %s quả cầu màu trắng, có $C_{%s}^{%s} = %s$ cách. \\\\
            Số phần tử của biến cố $C$ là $n(C) = %s + %s = %s$. \\\\
            Xác suất của biến cố $C$ là $P(C) = \\frac{%s}{%s} = %s$.'''
                            %(latex(n_chon), latex(n_chon), latex(n_x), latex(n_chon), latex(binomial(n_x, 3)),
                              latex(n_chon), latex(n_t), latex(n_chon), latex(binomial(n_t, 3)),
                              latex(binomial(n_x, 3)), latex(binomial(n_t, 3)), latex(n_C),
                              latex(n_C), latex(omega), latex(p_C)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để chọn được ít nhất một quả cầu xanh bằng $%s$' %(latex(p_D))
            vdc_da_1_s = 'Xác suất để chọn được ít nhất một quả cầu xanh bằng $%s$' %(latex(1-p_D))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Gọi $D$ là biến cố "Chọn được ít nhất một quả cầu xanh". \\\\
            Biến cố đối của $D$ là $\\overline{D}$: "Không chọn được quả cầu xanh nào" (tức là chọn %s quả trắng). \\\\
            Số cách chọn %s quả trắng từ %s quả trắng là $n(\\overline{D}) = C_{%s}^{%s} = %s$. \\\\
            Xác suất của biến cố đối là $P(\\overline{D}) = \\frac{%s}{%s} = %s$. \\\\
            Vậy xác suất cần tìm là $P(D) = 1 - P(\\overline{D}) = 1 - %s = %s$.'''
                             %(latex(n_chon), latex(n_chon), latex(n_t), latex(n_t), latex(n_chon), latex(binomial(n_t, 3)),
                               latex(binomial(n_t, 3)), latex(omega), latex(Rational(binomial(n_t, 3), omega)),
                               latex(Rational(binomial(n_t, 3), omega)), latex(p_D)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán và xáo trộn như mẫu
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

