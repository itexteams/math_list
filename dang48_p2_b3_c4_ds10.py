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


def bt_dang48_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Ngẫu nhiên hóa kích thước khuôn bánh ban đầu
            # Để giữ nguyên các giá trị đẹp ở câu c và d (x thuộc (0,5) và [2,3])
            # ta cần hiệu (chiều dài - chiều rộng) = 5
            dai_ban_dau = randint(15, 25)
            rong_ban_dau = dai_ban_dau - 5
            dien_tich_0 = dai_ban_dau * rong_ban_dau

            # Hàm diện tích mới: f(x) = (dai - x)(rong + x) = -x^2 + (dai - rong)x + dai*rong
            # Với dai - rong = 5, ta có f(x) = -x^2 + 5x + dien_tich_0
            f_x = -x**2 + 5*x + dien_tich_0
            f_max = dien_tich_0 + Rational(25, 4) # Giá trị cực đại tại x = 2.5
            target_area = dien_tich_0 + 6 # Giá trị để giải bất phương trình ra nghiệm [2, 3]

            # Nội dung câu hỏi
            noidungcauhoi = ('''Từ một khuôn nhôm làm bánh hình chữ nhật ban đầu có chiều dài $%s \\text{cm}$, chiều rộng $%s \\text{cm}$, người ta muốn thay đổi kích thước khuôn thành $15-x$ và $10+x$ để được một khuôn mới. ''' 
                             %(latex(dai_ban_dau), latex(rong_ban_dau)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Diện tích khuôn mới là $f(x) = -x^2 + 5x + %s$ ($\\text{cm}^2$)' % (latex(dien_tich_0))
            nb_da_1_s = 'Diện tích khuôn mới là $f(x) = -x^2 + 4x + %s$ ($\\text{cm}^2$)' % (latex(dien_tich_0))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Diện tích khuôn mới được tính theo công thức: \\\\
                            $f(x) = (%s - x)(%s + x) = %s + %sx - %sx - x^2 = -x^2 + 5x + %s$.''' 
                            % (latex(dai_ban_dau), latex(rong_ban_dau), latex(dien_tich_0), latex(dai_ban_dau), latex(rong_ban_dau), latex(dien_tich_0)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Diện tích khuôn mới đạt giá trị lớn nhất bằng $%s \\text{cm}^2$' % (latex(float(f_max)).replace('.', ','))
            th_da_1_s = 'Diện tích khuôn mới đạt giá trị lớn nhất bằng $%s \\text{cm}^2$' % (latex(float(dien_tich_0 + 5)).replace('.', ','))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Hàm số $f(x) = -x^2 + 5x + %s$ là một parabol có đỉnh tại $x = -\\frac{b}{2a} = -\\frac{5}{2(-1)} = 2,5$. \\\\
                            Giá trị lớn nhất của diện tích là $f(2,5) = -(2,5)^2 + 5(2,5) + %s = %s$.'''
                            % (latex(dien_tich_0), latex(dien_tich_0), latex(float(f_max)).replace('.', ',')))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Giá trị $x$ nằm trong khoảng $(0; 5)$ thì diện tích khuôn mới sẽ tăng so với diện tích ban đầu'
            vd_da_1_s = 'Giá trị $x$ nằm trong khoảng $(0; %s)$ thì diện tích khuôn mới sẽ tăng so với diện tích ban đầu' % (latex(dai_ban_dau))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Diện tích khuôn mới tăng so với diện tích ban đầu khi: \\\\
                            $f(x) > %s \\Leftrightarrow -x^2 + 5x + %s > %s \\Leftrightarrow -x^2 + 5x > 0$. \\\\
                            Giải bất phương trình ta được $0 < x < 5$. Vậy $x \\in (0; 5)$.'''
                            % (latex(dien_tich_0), latex(dien_tich_0), latex(dien_tich_0)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Để diện tích khuôn mới không nhỏ hơn $%s \\text{cm}^2$ thì $x \\in [2; 3]$' % (latex(target_area))
            vdc_da_1_s = 'Để diện tích khuôn mới không nhỏ hơn $%s \\text{cm}^2$ thì $x \\in [1; 4]$' % (latex(target_area))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Yêu cầu bài toán: $f(x) \\geq %s \\Leftrightarrow -x^2 + 5x + %s \\geq %s$ \\\\
                            $\\Leftrightarrow -x^2 + 5x - 6 \\geq 0 \\Leftrightarrow x^2 - 5x + 6 \\leq 0$. \\\\
                            Xét phương trình $x^2 - 5x + 6 = 0$ có hai nghiệm $x=2, x=3$. \\\\
                            Dựa vào dấu của tam thức bậc hai, ta có tập nghiệm là $x \\in [2; 3]$.'''
                            % (latex(target_area), latex(dien_tich_0), latex(target_area)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Logic chọn ngẫu nhiên số câu đúng (1-3 câu)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    shuffled_answers = current_answers
                    break

            # Gán lời giải tương ứng
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
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

