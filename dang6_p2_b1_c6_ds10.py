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


def bt_dang6_p2_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo các mặt của đồng xu để random
            mat_1 = random.choice(['\\text{sấp}', '\\text{ngửa}'])
            mat_2 = '\\text{ngửa}' if mat_1 == '\\text{sấp}' else '\\text{sấp}'

            # Nội dung câu hỏi
            noidungcauhoi = ('Xét phép thử là gieo một đồng xu gồm hai mặt $%s$ và $%s$ $3$ lần liên tiếp.' 
                             % (mat_1, mat_2))

            ########################################################################
            # Nhận biết: Số phần tử không gian mẫu
            ########################################################################
            nb_da_1_d = '\\True $n\\left(\\Omega\\right)=8$'
            nb_da_1_s = '$n\\left(\\Omega\\right)=6$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('Mỗi lần gieo đồng xu có $2$ kết quả có thể xảy ra $(%s)$ hoặc $(%s)$. '
                            'Vì gieo $3$ lần liên tiếp nên số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = 2 \\cdot 2 \\cdot 2 = 8$.' 
                            % (mat_1, mat_2))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu: Biến cố đối
            ########################################################################
            # A: "Gieo được ít nhất một mặt sấp" -> Đối A: "Không được mặt sấp nào" (Cả 3 lần ngửa)
            th_da_1_d = '\\True Gọi $A$ là biến cố: "Gieo được mặt %s", khi đó $n\\left(\\overline{A}\\right)=1$' % mat_1
            th_da_1_s = 'Gọi $A$ là biến cố: "Gieo được mặt %s", khi đó $n\\left(\\overline{A}\\right)=7$' % mat_1
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('Giả sử biến cố $A$: "Gieo được ít nhất một mặt %s". '
                            'Khi đó biến cố đối $\\overline{A}$ là: "Không gieo được mặt %s nào", '
                            'tức là cả $3$ lần gieo đều được mặt %s. '
                            'Ta có $\\overline{A} = \\{\\left(%s, %s, %s\\right)\\}$, suy ra $n\\left(\\overline{A}\\right)=1$.' 
                            % (mat_1, mat_1, mat_2, mat_2, mat_2, mat_2))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng: Biến cố đơn giản
            ########################################################################
            # B: "Cả ba lần đều gieo được mặt sấp"
            vd_da_1_d = '\\True Gọi $B$ là biến cố: "Gieo được mặt %s", khi đó $n\\left(B\\right)=1$' % mat_1
            vd_da_1_s = 'Gọi $B$ là biến cố: "Gieo được mặt %s", khi đó $n\\left(B\\right)=3$' % mat_1
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('Giả sử biến cố $B$: "Cả ba lần gieo đều được mặt %s". '
                            'Khi đó $B = \\{\\left(%s, %s, %s\\right)\\}$. '
                            'Vậy số phần tử của biến cố $B$ là $n\\left(B\\right)=1$.' 
                            % (mat_1, mat_1, mat_1, mat_1))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao: Biến cố phức hợp
            ########################################################################
            # C: "Kết quả lần 2 và lần 3 khác nhau"
            vdc_da_1_d = '\\True Gọi $C$ là biến cố: "Kết quả của lần gieo thứ hai và thứ ba khác nhau", khi đó $n\\left(C\\right)=4$'
            vdc_da_1_s = 'Gọi $C$ là biến cố: "Kết quả của lần gieo thứ hai và thứ ba khác nhau", khi đó $n\\left(C\\right)=2$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('Các kết quả của biến cố $C$ có dạng $\\left(x_1, x_2, x_3\\right)$ sao cho $x_2 \\neq x_3$. \\\\ '
                             'Lần gieo thứ nhất $x_1$ có $2$ cách chọn. \\\\ '
                             'Cặp kết quả $\\left(x_2, x_3\\right)$ khác nhau có $2$ cách là: '
                             '$\\left(%s, %s\\right)$ hoặc $\\left(%s, %s\\right)$. \\\\ '
                             'Theo quy tắc nhân, ta có $n\\left(C\\right) = 2 \\cdot 2 = 4$.' 
                             % (mat_1, mat_2, mat_2, mat_1))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            ########################################################################
            # Xử lý Logic và Xuất nội dung
            ########################################################################

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_c = random.choice(list_nb_da_1)
                th_da_c = random.choice(list_th_da_1)
                vd_da_c = random.choice(list_vd_da_1)
                vdc_da_c = random.choice(list_vdc_da_1)

                answers = [nb_da_c, th_da_c, vd_da_c, vdc_da_c]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lại giá trị đã chọn vào list để khớp với lời giải
            shuffled_answers_nb = [nb_da_c]
            shuffled_answers_th = [th_da_c]
            shuffled_answers_vd = [vd_da_c]
            shuffled_answers_vdc = [vdc_da_c]

            # Xuất nội dung theo mẫu yêu cầu
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
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

