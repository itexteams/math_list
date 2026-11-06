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


def bt_dang14_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Để nghiệm nguyên đẹp, ta chọn 2 nghiệm x1, x2 trước
            # Sau đó tính S = x1 + x2, P = x1 * x2
            # Phương trình: sqrt(x^2 - Sx + P + k^2) = k
            x1 = random.randint(1, 4)
            x2 = x1 + random.randint(2, 4) # Đảm bảo x2 > x1 để có 2 nghiệm phân biệt
            k = random.randint(2, 5)
            S = x1 + x2
            P = x1 * x2
            m = P + k**2
            mid = S / 2 # Giá trị trung gian để xét câu c

            # Nội dung câu hỏi
            # Phương trình dạng: \sqrt{x^2 - Sx + m} = k
            bieuthuc_trong_can = x**2 - S*x + m
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = %s$. (1)''' 
                             %(latex(bieuthuc_trong_can), latex(k)))

            ########################################################################
            # Nhận biết ############################################
            # a) Bình phương hai vế
            nb_da_1_d = '\\True Bình phương hai vế phương trình (1), ta được: $%s = 0$' %(latex(x**2 - S*x + P))
            nb_da_1_s = 'Bình phương hai vế phương trình (1), ta được: $%s = %s$' %(latex(x**2 - S*x + m), latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Bình phương hai vế phương trình (1), ta có: \\\\
                            $x^2 - %sx + %s = %s^2 \\Leftrightarrow x^2 - %sx + %s = 0$.''' 
                            %(S, m, k, S, P))

            ########################################################################
            # Thông hiểu ############################################
            # b) Số lượng nghiệm
            th_da_1_d = '\\True Phương trình (1) có hai nghiệm phân biệt'
            th_da_1_s = 'Phương trình (1) có một nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Giải phương trình $x^2 - %sx + %s = 0$, ta tìm được hai nghiệm $x = %s$ và $x = %s$.''' 
                            %(S, P, x1, x2))

            ########################################################################
            # Vận dụng ############################################
            # c) So sánh nghiệm với một giá trị (ở đây lấy điểm giữa mid)
            vd_da_1_d = '\\True Phương trình (1) có một nghiệm nhỏ hơn $%s$' %(latex(Rational(S, 2)))
            vd_da_1_s = 'Phương trình (1) có hai nghiệm đều lớn hơn $%s$' %(latex(Rational(S, 2)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì hai nghiệm là $x = %s$ và $x = %s$, mà $%s < %s$ nên phương trình có một nghiệm nhỏ hơn $%s$.''' 
                            %(x1, x2, x1, latex(Rational(S, 2)), latex(Rational(S, 2))))

            ########################################################################
            # Vận dụng cao ############################################
            # d) Tổng các nghiệm
            vdc_da_1_d = '\\True Tổng các nghiệm của phương trình (1) bằng %s' %(S)
            vdc_da_1_s = 'Tổng các nghiệm của phương trình (1) bằng %s' %(P)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Tổng các nghiệm là $x_1 + x_2 = %s + %s = %s$.''' 
                             %(x1, x2, S))

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

            # Gán lại vào danh sách để xuất bản
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi theo mẫu latex yêu cầu
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
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

