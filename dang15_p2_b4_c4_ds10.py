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


def bt_dang15_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Bước 1: Tạo bài toán ngẫu nhiên dựa trên cấu trúc Câu 18
            # Phương trình: sqrt(3x^2 - 9x + 1) = 2 - x
            # Để đảm bảo số đẹp, ta giữ nguyên các hệ số hoặc có thể tùy biến nhẹ.
            # Ở đây tôi sẽ giữ nguyên cấu trúc gốc của câu 18 để đảm bảo tính logic của các khẳng định.

            noidungcauhoi = 'Cho phương trình $\\sqrt{3x^2 - 9x + 1} = 2 - x$. (2)'

            ########################################################################
            # a) Bình phương hai vế
            ########################################################################
            # Lời giải chi tiết:
            # Bình phương hai vế: 3x^2 - 9x + 1 = (2 - x)^2
            # <=> 3x^2 - 9x + 1 = 4 - 4x + x^2
            # <=> 2x^2 - 5x - 3 = 0
            nb_da_1_d = '\\True Bình phương hai vế phương trình (2), ta được: $2x^2 - 5x - 3 = 0$'
            nb_da_1_s = 'Bình phương hai vế phương trình (2), ta được: $2x^2 - 5x + 3 = 0$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = 'Bình phương hai vế của phương trình (2), ta được:\\\\ $3x^2 - 9x + 1 = (2-x)^2 \\Leftrightarrow 3x^2 - 9x + 1 = 4 - 4x + x^2 \\Leftrightarrow 2x^2 - 5x - 3 = 0$.'

            ########################################################################
            # b) Tập nghiệm (So sánh với 2x + 1 = 0)
            ########################################################################
            # Giải 2x^2 - 5x - 3 = 0 => x = 3 hoặc x = -1/2
            # Điều kiện 2 - x >= 0 <=> x <= 2. Vậy nghiệm duy nhất là x = -1/2.
            # Phương trình 2x + 1 = 0 có nghiệm x = -1/2.
            th_da_1_d = '\\True Phương trình (2) có chung tập nghiệm với phương trình $2x + 1 = 0$'
            th_da_1_s = 'Phương trình (2) có chung tập nghiệm với phương trình $x - 3 = 0$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = 'Điều kiện của phương trình (2) là $2 - x \\ge 0 \\Leftrightarrow x \\le 2$.\\\\ Giải phương trình hệ quả $2x^2 - 5x - 3 = 0$ ta được $x = 3$ (loại) hoặc $x = -\\frac{1}{2}$ (nhận).\\\\ Vậy tập nghiệm của (2) là $S = \\left\\{ -\\frac{1}{2} \\right\\}$.\\\\ Phương trình $2x + 1 = 0$ cũng có tập nghiệm là $S = \\left\\{ -\\frac{1}{2} \\right\\}$.'

            ########################################################################
            # c) Tổng các nghiệm
            ########################################################################
            # Nghiệm duy nhất là -1/2 nên tổng là -1/2. 
            vd_da_1_d = 'Tổng các nghiệm của phương trình (2) bằng $\\frac{5}{2}$' # Sai vì 5/2 là tổng nghiệm PT hệ quả
            vd_da_1_s = '\\True Tổng các nghiệm của phương trình (2) bằng $-\\frac{1}{2}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = 'Phương trình (2) chỉ có một nghiệm duy nhất là $x = -\\frac{1}{2}$, do đó tổng các nghiệm của phương trình bằng $-\\frac{1}{2}$.'

            ########################################################################
            # d) Nghiệm nhỏ nhất
            ########################################################################
            vdc_da_1_d = '\\True Nghiệm nhỏ nhất của phương trình (2) nhỏ hơn $0$'
            vdc_da_1_s = 'Nghiệm nhỏ nhất của phương trình (2) lớn hơn $0$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = 'Vì phương trình có nghiệm duy nhất $x = -\\frac{1}{2}$ và $-\\frac{1}{2} < 0$, nên nghiệm nhỏ nhất của phương trình nhỏ hơn $0$.'

            # --- Xử lý xáo trộn và chọn số lượng câu đúng ---
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

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
            sh_ans = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            sh_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(sh_ans[0]) + '}\n'
                '{' + str(sh_ans[1]) + '}\n'
                '{' + str(sh_ans[2]) + '}\n'
                '{' + str(sh_ans[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sh_sol[0]) + '\n'
                '\\item ' + str(sh_sol[1]) + '\n'
                '\\item ' + str(sh_sol[2]) + '\n'
                '\\item ' + str(sh_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

