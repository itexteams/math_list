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


def bt_dang9_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Tạo các giá trị ngẫu nhiên để bài toán luôn có 2 nghiệm nguyên
            # Giả sử phương trình sau khi bình phương là x^2 - (m+n)x + mn = 0
            while True:
                m = random.randint(-5, -1)
                n = random.randint(1, 5)
                if m != n:
                    break

            # Tạo phương trình: sqrt(2x^2 + B1*x + C1) = sqrt(x^2 + B2*x + C2)
            # Để phương trình tương đương x^2 - (m+n)x + mn = 0
            # Ta chọn g(x) = x^2 - x + 11 (luôn dương) làm nền
            # f(x) = x^2 - (m+n)x + mn
            # VT = sqrt(g(x) + f(x)), VP = sqrt(g(x))

            g_x = x**2 - x + 11
            f_x = x**2 - (m+n)*x + m*n
            bt1 = g_x + f_x
            bt2 = g_x

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = \\sqrt{%s} \\quad (*)$.''' 
                             % (latex(bt1), latex(bt2)))

            ########################################################################
            # Nhận biết (Điều kiện)
            ########################################################################
            # Đúng: x thuộc R vì các biểu thức dưới căn luôn dương
            nb_da_1_d = '\\True Điều kiện xác định của phương trình là $x \\in \\mathbb{R}$'
            nb_da_1_s = 'Điều kiện: $x \\geq 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Xét biểu thức dưới dấu căn: \\\\
                            Ta có $%s > 0, \\forall x \\in \\mathbb{R}$ và $%s > 0, \\forall x \\in \\mathbb{R}$. \\\\
                            Do đó điều kiện xác định của phương trình là $x \\in \\mathbb{R}$.''' 
                            % (latex(bt1), latex(bt2)))

            ########################################################################
            # Thông hiểu (Bình phương)
            ########################################################################
            # Phương trình hệ quả: f_x = 0 <=> x^2 - (m+n)x + mn = 0
            pt_he_qua = sp.expand(bt1 - bt2)
            pt_sai = sp.expand(bt1 - bt2 + 2*x) # Tạo một pt sai

            th_da_1_d = '\\True Bình phương hai vế phương trình $(*)$ ta được $%s = 0$' % (latex(pt_he_qua))
            th_da_1_s = 'Bình phương hai vế phương trình $(*)$ ta được $%s = 0$' % (latex(pt_sai))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Bình phương hai vế phương trình $(*)$ ta được: \\\\
                            $%s = %s \\Leftrightarrow %s = 0$.''' 
                            % (latex(bt1), latex(bt2), latex(pt_he_qua)))

            ########################################################################
            # Vận dụng (Số nghiệm)
            ########################################################################
            vd_da_1_d = '\\True Phương trình $(*)$ có $2$ nghiệm phân biệt'
            vd_da_1_s = 'Phương trình $(*)$ có $1$ nghiệm duy nhất'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Giải phương trình $%s = 0$, ta tìm được các nghiệm là $x = %s$ và $x = %s$. \\\\
                            Cả hai nghiệm này đều thỏa mãn điều kiện xác định. \\\\
                            Vậy phương trình $(*)$ có $2$ nghiệm phân biệt.''' 
                            % (latex(pt_he_qua), latex(m), latex(n)))

            ########################################################################
            # Vận dụng cao (Biểu thức nghiệm)
            ########################################################################
            x1, x2 = sorted([m, n]) # x1 < x2
            gia_tri_dung = x1 - 2*x2
            gia_tri_sai = x1 + x2

            vdc_da_1_d = '\\True Giả sử $x_1, x_2 \\, (x_1 < x_2)$ là nghiệm của phương trình $(*)$ khi đó: $x_1 - 2x_2 = %s$' % (latex(gia_tri_dung))
            vdc_da_1_s = 'Giả sử $x_1, x_2 \\, (x_1 < x_2)$ là nghiệm của phương trình $(*)$ khi đó: $x_1 - 2x_2 = %s$' % (latex(gia_tri_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Từ kết quả câu trên, ta có hai nghiệm là $x = %s$ và $x = %s$. \\\\
                            Vì $x_1 < x_2$ nên $x_1 = %s$ và $x_2 = %s$. \\\\
                            Khi đó: $x_1 - 2x_2 = %s - 2(%s) = %s$.''' 
                            % (latex(m), latex(n), latex(x1), latex(x2), latex(x1), latex(x2), latex(gia_tri_dung)))

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

            # Gán vào list để đồng bộ với lời giải
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Do mỗi phần chỉ có 1 câu hỏi tương ứng, ta lấy luôn kết quả đã chọn ở trên
            shuffled_answers_nb = [nb_da_1]
            shuffled_solutions_nb = [loigiai_nb_1]
            shuffled_answers_th = [th_da_1]
            shuffled_solutions_th = [loigiai_th_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_solutions_vd = [loigiai_vd_1]
            shuffled_answers_vdc = [vdc_da_1]
            shuffled_solutions_vdc = [loigiai_vdc_1]

            # Xuất câu hỏi
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

