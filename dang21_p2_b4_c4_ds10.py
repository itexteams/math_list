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


def bt_dang21_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Để phương trình 2(x-a)^2 + 2(x+b) - 5(x-a)sqrt(x+b) = 0 có nghiệm nguyên đẹp
            # Ta chọn các cặp (a, b) sao cho a + b + 1 là số chính phương và 16(a+b) + 1 là số chính phương
            # Các cặp (a, b) thỏa mãn: (2, 1), (1, 2), (0, 3)
            list_ab = [(2, 1), (1, 2)]
            a_val, b_val = random.choice(list_ab)

            # Tính toán các hệ số cho phương trình: 2x^2 + Bx + C - 5(x-a)sqrt(x+b) = 0
            # 2(x-a)^2 + 2(x+b) = 2x^2 - 4ax + 2a^2 + 2x + 2b = 2x^2 - (4a-2)x + (2a^2+2b)
            hso_b = -(4 * a_val - 2)
            hso_c = 2 * a_val**2 + 2 * b_val

            # Tính toán các nghiệm thực tế để đưa vào lời giải
            # TH1: x-a = 2*sqrt(x+b) => x^2 - (2a+4)x + a^2-4b = 0
            x1 = int(((2 * a_val + 4) + sqrt((2 * a_val + 4)**2 - 4 * (a_val**2 - 4 * b_val))) / 2)
            # TH2: 2(x-a) = sqrt(x+b) => 4x^2 - (8a+1)x + 4a^2-b = 0
            # Nghiệm lớn hơn a của pt bậc 2 này
            delta2 = (8 * a_val + 1)**2 - 16 * (4 * a_val**2 - b_val)
            x2 = int(((8 * a_val + 1) + sqrt(delta2)) / 8)

            tong_nghiem = x1 + x2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $2x^2 %s x + %s - 5(x - %s)\\sqrt{x + %s} = 0$.''' 
                             % (('+' + str(hso_b) if hso_b > 0 else str(hso_b)), 
                                hso_c, a_val, b_val))

            ########################################################################
            # Nhận biết (Câu a) ############################################
            nb_da_1_d = '\\True Điều kiện xác định của phương trình là $x \\ge %s$' % (latex(-b_val))
            nb_da_1_s = 'Điều kiện xác định của phương trình là $x \\ge %s$' % (latex(a_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Điều kiện xác định: $x + %s \\ge 0 \\Leftrightarrow x \\ge %s$.''' % (b_val, -b_val))
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            th_da_1_d = '\\True Phương trình tương đương với $2(x-%s)^2 + 2(x+%s) - 5(x-%s)\\sqrt{x+%s} = 0$' % (a_val, b_val, a_val, b_val)
            th_da_1_s = 'Phương trình tương đương với $2(x-%s)^2 + (x+%s) - 5(x-%s)\\sqrt{x+%s} = 0$' % (a_val, b_val, a_val, b_val)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $2x^2 %s x + %s = 2(x^2 - %sx + %s) + 2x + %s = 2(x-%s)^2 + 2(x+%s)$. \\\\
            Nên phương trình trở thành $2(x-%s)^2 + 2(x+%s) - 5(x-%s)\\sqrt{x+%s} = 0$.''' 
                            % (('+' + str(hso_b) if hso_b > 0 else str(hso_b)), hso_c, 2*a_val, a_val**2, 2*b_val, a_val, b_val, a_val, b_val, a_val, b_val))
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Câu c) ############################################
            # Kiểm tra xem x=0 có là nghiệm không (thường là không với bộ số này)
            ve_trai_0 = 2*(0)**2 + hso_b*(0) + hso_c - 5*(0 - a_val)*sqrt(0 + b_val)
            if ve_trai_0 == 0:
                vd_da_1_d = '\\True $x = 0$ là nghiệm của phương trình'
                vd_da_1_s = '$x = 0$ không là nghiệm của phương trình'
            else:
                vd_da_1_d = '\\True $x = 0$ không là nghiệm của phương trình'
                vd_da_1_s = '$x = 0$ là nghiệm của phương trình'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Thay $x=0$ vào vế trái phương trình ta được: $2(0)^2 %s(0) + %s - 5(0-%s)\\sqrt{0+%s} = %s$. \\\\
            Vì giá trị này %s nên $x=0$ %s là nghiệm của phương trình.''' 
                            % (hso_b, hso_c, a_val, b_val, latex(ve_trai_0), 
                               ' bằng 0 ' if ve_trai_0 == 0 else ' khác 0 ',
                               '' if ve_trai_0 == 0 else 'không'))
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            vdc_da_1_d = '\\True Tổng các nghiệm của phương trình bằng $%s$' % (tong_nghiem)
            vdc_da_1_s = 'Tổng các nghiệm của phương trình bằng $%s$' % (tong_nghiem + random.randint(1, 5))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Đặt $u = x-%s$ và $v = \\sqrt{x+%s} \\ge 0$. Phương trình trở thành: \\\\
            $2u^2 + 2v^2 - 5uv = 0 \\Leftrightarrow (u-2v)(2u-v) = 0 \\Leftrightarrow \\left[\\begin{aligned} &u = 2v \\\\ &v = 2u \\end{aligned}\\right.$. \\\\
            + Với $u=2v$: $x-%s = 2\\sqrt{x+%s} \\Leftrightarrow \\begin{cases} x \\ge %s \\\\ x^2-%sx+%s=0 \\end{cases} \\Leftrightarrow x=%s$ (nhận). \\\\
            + Với $v=2u$: $\\sqrt{x+%s} = 2(x-%s) \\Leftrightarrow \\begin{cases} x \\ge %s \\\\ 4x^2-%sx+%s=0 \\end{cases} \\Leftrightarrow x=%s$ (nhận). \\\\
            Tổng các nghiệm là $%s + %s = %s$.''' 
                             % (a_val, b_val, a_val, b_val, a_val, 2*a_val+4, a_val**2-4*b_val, x1, 
                                b_val, a_val, a_val, 8*a_val+1, 4*a_val**2-b_val, x2, x1, x2, tong_nghiem))
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_s = random.choice(list_nb_da_1)
                th_s = random.choice(list_th_da_1)
                vd_s = random.choice(list_vd_da_1)
                vdc_s = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_s, th_s, vd_s, vdc_s]) <= 3:
                    shuffled_answers_nb = [nb_s]; shuffled_answers_th = [th_s]
                    shuffled_answers_vd = [vd_s]; shuffled_answers_vdc = [vdc_s]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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

