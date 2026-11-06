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


def bt_dang16_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Khởi tạo các giá trị ngẫu nhiên cho số lượng sách
            # t: toán, l: lý, h: hóa
            t = random.randint(4, 6)
            l = random.randint(3, 5)
            h = random.randint(2, 4)
            tong_sach = t + l + h

            # Tính toán các giá trị tổ hợp
            omega = math.comb(tong_sach, 3)
            bien_co_A = t * l * h
            bien_co_B = math.comb(t, 3)
            bien_co_C = omega - math.comb(l + h, 3)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trên giá sách có %s quyển sách toán, %s quyển sách lý, %s quyển sách hóa. Lấy ngẫu nhiên 3 quyển sách.''' 
                             % (latex(t), latex(l), latex(h)))

            ########################################################################
            # Nhận biết - Câu (a)
            nb_da_1_d = '\\True $n(\\Omega) = %s$' % (latex(omega))
            nb_da_1_s = '$n(\\Omega) = %s$' % (latex(omega + random.choice([-2, 2, 5])))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số phần tử của không gian mẫu là $n(\\Omega) = C_{%s}^3 = %s$.''' 
                            % (latex(tong_sach), latex(omega)))

            ########################################################################
            # Thông hiểu - Câu (b)
            th_da_1_d = '\\True Số phần tử của biến cố $A$: "Thuộc 3 môn khác nhau" bằng %s' % (latex(bien_co_A))
            th_da_1_s = 'Số phần tử của biến cố $A$: "Thuộc 3 môn khác nhau" bằng %s' % (latex(bien_co_A - 4))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Để chọn 3 quyển thuộc 3 môn khác nhau, ta chọn mỗi môn 1 quyển. \\\\
                            Số cách chọn là $n(A) = C_{%s}^1 \\cdot C_{%s}^1 \\cdot C_{%s}^1 = %s \\cdot %s \\cdot %s = %s$.''' 
                            % (latex(t), latex(l), latex(h), latex(t), latex(l), latex(h), latex(bien_co_A)))

            ########################################################################
            # Vận dụng - Câu (c)
            vd_da_1_d = '\\True Số phần tử của biến cố $B$: "Đều là môn toán" bằng %s' % (latex(bien_co_B))
            vd_da_1_s = 'Số phần tử của biến cố $B$: "Đều là môn toán" bằng %s' % (latex(bien_co_B + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Để chọn 3 quyển đều là môn toán, ta chọn 3 quyển từ %s quyển toán. \\\\
                            Số cách chọn là $n(B) = C_{%s}^3 = %s$.''' 
                            % (latex(t), latex(t), latex(bien_co_B)))

            ########################################################################
            # Vận dụng cao - Câu (d)
            vdc_da_1_d = '\\True Số phần tử của biến cố $C$: "Có ít nhất một quyển sách toán" bằng %s' % (latex(bien_co_C))
            vdc_da_1_s = 'Số phần tử của biến cố $C$: "Có ít nhất một quyển sách toán" bằng %s' % (latex(bien_co_C - 4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Sử dụng biến cố đối $\\overline{C}$: "Không có quyển sách toán nào". \\\\
                             Khi đó 3 quyển sách được chọn từ %s quyển lý và hóa. \\\\
                             Ta có $n(\\overline{C}) = C_{%s + %s}^3 = C_{%s}^3 = %s$. \\\\
                             Số phần tử của biến cố $C$ là $n(C) = n(\\Omega) - n(\\overline{C}) = %s - %s = %s$.''' 
                             % (latex(l+h), latex(l), latex(h), latex(l+h), latex(math.comb(l+h, 3)), latex(omega), latex(math.comb(l+h, 3)), latex(bien_co_C)))

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

            # Gán lại vào list để giữ cấu trúc
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi với đáp án và lời giải
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

