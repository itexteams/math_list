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


def bt_dang9_p2_b3_c5_ds10(self):
            # Khai báo biến
            # B1-Nghiên cứu đề bài và lời giải:
            # Random số mũ n trong khoảng từ 6 đến 10 để đảm bảo các số mũ 2, 3, 5 luôn tồn tại
            n = random.randint(6, 10)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Khai triển $\\left( 1-x \\right)^{%s}$.''' % (latex(n)))

            ########################################################################
            # Nhận biết ############################################
            # Hệ số của x^2: (-1)^2 * C_n^2 = C_n^2
            nb_da_1_d = '\\True Hệ số của $x^2$ trong khai triển là $C_{%s}^2$' % (latex(n))
            nb_da_1_s = 'Hệ số của $x^2$ trong khai triển là $-C_{%s}^2$' % (latex(n))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Số hạng tổng quát trong khai triển $\\left( 1-x \\right)^{%s}$ là $T_{k+1} = C_{%s}^k \\cdot 1^{%s-k} \\cdot \\left( -x \\right)^k = (-1)^k C_{%s}^k x^k$.\\\\
            Để tìm hệ số của $x^2$, ta cho $k=2$.\\\\
            Hệ số là $(-1)^2 C_{%s}^2 = C_{%s}^2$.'''
                           % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Hệ số của x^3: (-1)^3 * C_n^3 = -C_n^3
            th_da_1_d = '\\True Hệ số của $x^3$ trong khai triển là $-C_{%s}^3$' % (latex(n))
            th_da_1_s = 'Hệ số của $x^3$ trong khai triển là $C_{%s}^3$' % (latex(n))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Với $k=3$, hệ số của $x^3$ là $(-1)^3 C_{%s}^3 = -C_{%s}^3$.'''
                           % (latex(n), latex(n)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Hệ số của x^5: (-1)^5 * C_n^5 = -C_n^5
            vd_da_1_d = '\\True Hệ số của $x^5$ trong khai triển là $-C_{%s}^5$' % (latex(n))
            vd_da_1_s = 'Hệ số của $x^5$ trong khai triển là $C_{%s}^5$' % (latex(n))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Với $k=5$, hệ số của $x^5$ là $(-1)^5 C_{%s}^5 = -C_{%s}^5$.'''
                           % (latex(n), latex(n)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Biểu thức tổng: C_n^0 - C_n^1 + ... = (1-1)^n = 0
            tong_tex = ""
            for i in range(n + 1):
                sign = " - " if i % 2 != 0 else " + "
                if i == 0: sign = ""
                tong_tex += "%s C_{%s}^{%s}" % (sign, latex(n), latex(i))

            vdc_da_1_d = '\\True $%s = 0$' % (tong_tex)
            vdc_da_1_s = '$%s = 1$' % (tong_tex)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Xét khai triển: $\\left( 1-x \\right)^{%s} = C_{%s}^0 - C_{%s}^1 x + C_{%s}^2 x^2 - \\dots + (-1)^{%s} C_{%s}^{%s} x^{%s}$.\\\\
            Thay $x=1$ vào hai vế của đẳng thức trên, ta được:\\\\
            $\\left( 1-1 \\right)^{%s} = C_{%s}^0 - C_{%s}^1 + C_{%s}^2 - \\dots + (-1)^{%s} C_{%s}^{%s} \\Leftrightarrow %s = 0$.'''
                            % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n),
                               latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), latex(n), tong_tex))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Gán lại vào list để xuất
            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

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
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

