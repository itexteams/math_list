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


def bt_dang8_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Nội dung câu hỏi gốc
            noidungcauhoi = r'''Gọi $S$ là tập hợp các số tự nhiên có ba chữ số. Chọn ngẫu nhiên một số từ tập $S$.'''

            # Giải thuật tính toán các giá trị đúng
            # Tổng các số có 3 chữ số: 100 đến 999 -> 900 số
            n_Omega_dung = 900
            # Số có 3 chữ số đôi một khác nhau: 9 * 9 * 8 = 648
            n_A_dung = 648
            # Số có 3 chữ số chia hết cho 5: tận cùng là 0 hoặc 5 -> 9 * 10 * 2 = 180
            n_B_dung = 180
            # Số có 3 chữ số là số chẵn: tận cùng 0, 2, 4, 6, 8 -> 9 * 10 * 5 = 450
            n_C_dung = 450

            ########################################################################
            # Nhận biết: Về không gian mẫu n(Omega)
            ########################################################################
            nb_da_1_d = '\\True $n\\left(\\Omega\\right) = %s$' % (n_Omega_dung)
            nb_da_1_s = '$n\\left(\\Omega\\right) = 1000$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số các số tự nhiên có ba chữ số là các số từ $100$ đến $999$. \\\\
                            Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = 999 - 100 + 1 = %s$.''' % (n_Omega_dung))

            ########################################################################
            # Thông hiểu: Biến cố A (chữ số đôi một khác nhau)
            ########################################################################
            th_da_1_d = '\\True Gọi $A$ là biến cố: "Chọn được số tự nhiên có các chữ số đôi một khác nhau", khi đó $n\\left(A\\right) = %s$' % (n_A_dung)
            th_da_1_s = 'Gọi $A$ là biến cố: "Chọn được số tự nhiên có các chữ số đôi một khác nhau", khi đó $n\\left(A\\right) = 729$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Gọi số cần chọn có dạng $\\overline{abc}$ với $a, b, c \\in \\left\\{ 0; 1; \\dots; 9 \\right\\}, a \\neq 0$. \\\\
                            Để các chữ số đôi một khác nhau: \\\\
                            - Chữ số $a$ có $9$ cách chọn $\\left( a \\neq 0 \\right)$. \\\\
                            - Chữ số $b$ có $9$ cách chọn $\\left( b \\neq a \\right)$. \\\\
                            - Chữ số $c$ có $8$ cách chọn $\\left( c \\neq a, c \\neq b \\right)$. \\\\
                            Vậy $n\\left(A\\right) = 9 \\cdot 9 \\cdot 8 = %s$.''' % (n_A_dung))

            ########################################################################
            # Vận dụng: Biến cố B (chia hết cho 5)
            ########################################################################
            vd_da_1_d = '\\True Gọi $B$ là biến cố: "Chọn được số tự nhiên chia hết cho $5$", khi đó $n\\left(B\\right) = %s$' % (n_B_dung)
            vd_da_1_s = 'Gọi $B$ là biến cố: "Chọn được số tự nhiên chia hết cho $5$", khi đó $n\\left(B\\right) = 200$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số tự nhiên có ba chữ số chia hết cho $5$ có dạng $\\overline{abc}$ với $c \\in \\left\\{ 0; 5 \\right\\}$. \\\\
                            - Chữ số $c$ có $2$ cách chọn. \\\\
                            - Chữ số $a$ có $9$ cách chọn $\\left( a \\neq 0 \\right)$. \\\\
                            - Chữ số $b$ có $10$ cách chọn. \\\\
                            Vậy $n\\left(B\\right) = 9 \\cdot 10 \\cdot 2 = %s$.''' % (n_B_dung))

            ########################################################################
            # Vận dụng cao: Biến cố C (số chẵn)
            ########################################################################
            vdc_da_1_d = '\\True Gọi $C$ là biến cố: "Chọn được số tự nhiên chẵn", khi đó $n\\left(C\\right) = %s$' % (n_C_dung)
            vdc_da_1_s = 'Gọi $C$ là biến cố: "Chọn được số tự nhiên chẵn", khi đó $n\\left(C\\right) = 500$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Số tự nhiên chẵn có ba chữ số có dạng $\\overline{abc}$ với $c \\in \\left\\{ 0; 2; 4; 6; 8 \\right\\}$. \\\\
                            - Chữ số $c$ có $5$ cách chọn. \\\\
                            - Chữ số $a$ có $9$ cách chọn $\\left( a \\neq 0 \\right)$. \\\\
                            - Chữ số $b$ có $10$ cách chọn. \\\\
                            Vậy $n\\left(C\\right) = 9 \\cdot 10 \\cdot 5 = %s$.''' % (n_C_dung))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng để đảm bảo tính khách quan của đề thi
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            loigiai_list = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_list[0]) + '\n'
                '\\item ' + str(loigiai_list[1]) + '\n'
                '\\item ' + str(loigiai_list[2]) + '\n'
                '\\item ' + str(loigiai_list[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

